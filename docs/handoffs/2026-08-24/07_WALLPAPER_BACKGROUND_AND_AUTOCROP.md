# Wallpaper, Background Plugin, Waifu.im, and Deterministic Artistic Auto-Crop

## Product surface

The background/wallpaper feature should be a real first-class Hearth Shell feature and also an early exercise of the plugin/settings/config architecture.

Requirements:

- Implement the background system as a **shell plugin installed by default**.
- Add a dedicated **Wallpaper** section in Hearth Settings.
- Support at least local/static wallpapers and an online-provider abstraction.
- Use **Waifu.im** as the first online provider.
- Keep provider fetching/configuration separate enough from the QML Settings page that future Gaming Mode/Decky work can reuse the provider and crop logic.
- Cache responsibly and handle offline/API failures without destabilizing the shell.

The exact plugin ABI, process boundary, cache path, rotation scheduler, and provider interface should be planned by Codex rather than decided by this file.

## Waifu.im provider

Use the API endpoint (`https://api.waifu.im`), not webpage scraping. Current Waifu.im documentation states that basic random-image requests do not require authentication.

Current API version at this handoff is `v7`; the docs recommend pinning production requests with:

`Accept-Version: v7`

Codex should verify the current version when implementing and decide how version upgrades are managed.

### Shipped/default wallpaper-oriented parameters

The owner wants the Settings UI to **show the default parameters being passed**, not hide them behind opaque behavior. Starting defaults discussed in this thread:

- `IncludedTags=waifu`
- `ExcludedTags=oppai`
- `ExcludedTags=selfies`
- `IsNsfw=False`
- `Orientation=LANDSCAPE`
- minimum width around `>=1920`
- minimum height around `>=1080`
- `IsAnimated=False`

The exact minimum-resolution default may be revisited during planning for 1440p/4K televisions; the goal is to avoid making the eligible image pool unnecessarily tiny while still getting wallpaper-suitable sources.

### Important tag/query semantics

Current docs:

- repeated `IncludedTags` use AND logic;
- repeated `ExcludedTags` use OR logic;
- `IsNsfw` accepts `False`, `True`, or `All` and defaults to `False`;
- available tags can be fetched from `/tags`.

The query builder must serialize repeated query parameters correctly. A previous manually constructed link accidentally percent-encoded the `&` separators as `%26`, causing the API to interpret the rest of the query as part of `IncludedTags[0]` and return a 400 validation error. Do **not** construct provider URLs through string concatenation that can reproduce this bug; use a proper query encoder/HTTP client representation that preserves repeated parameter keys.

### Customization and NSFW handling

Default Hearth behavior should be conservative/SFW, but do **not** add a prominent dedicated `Enable NSFW` UI toggle as a product feature.

Instead:

- expose generic advanced provider parameters/tags in a way that knowledgeable users can deliberately edit;
- show the shipped defaults;
- allow valid tags/parameters supported by the provider;
- if a user intentionally changes generic `IsNsfw`/tags to other provider-supported values, the system need not artificially prevent it;
- do not make NSFW discovery/recommendation a default or featured workflow.

Codex should plan validation/error UX so a malformed tag/parameter does not silently break wallpaper rotation.

## Image metadata

Waifu.im responses include useful metadata such as image ID, source URL, artist data, width, height, animation/NSFW status, tags, dominant color, and CDN image URL. Consider preserving enough metadata in the cache/model to support debugging, attribution/source viewing, duplicate avoidance, crop caching, and future settings UX. This is a planning consideration rather than a requirement to show every field in the UI.

## Why auto-crop exists

Even when Waifu.im is filtered to `LANDSCAPE`, landscape does not guarantee the target display aspect ratio (for example 16:9). A good wallpaper system should avoid blindly center-cropping artwork and cutting off the subject or destroying deliberate negative space.

The owner wants a lightweight ML-assisted crop that is **artistic but deterministic** for a given source image and target resolution/geometry.

## Model

Use the previously discussed **U²-NetP** salient-object model as the lightweight subject/saliency detector. The official U²-Net project describes U²-NetP as the small ~4.7 MB model and its reference inference pipeline resizes to roughly 320 px for saliency inference.

For Hearth, plan a practical ONNX-based/native inference route suitable for the immutable Fedora/Bazzite environment. The exact ONNX Runtime/package integration, model artifact source, checksum/version pinning, CPU execution provider, and packaging location must be investigated and documented rather than improvised in QML.

The ML model's job is to estimate **important/salient image regions**. It should **not** directly choose the final crop.

## Deterministic composition engine

After generating a reduced-resolution saliency/subject mask:

1. determine the exact target aspect ratio/geometry;
2. generate valid candidate crop rectangles with deterministic ordering;
3. score candidates using deterministic composition rules;
4. select the best score with an explicit deterministic tie-breaker;
5. apply the selected crop coordinates to the original-resolution image;
6. cache the crop decision keyed by source image identity/hash plus target geometry/aspect context;
7. if ML analysis fails, use a deterministic safe fallback such as a sensible center crop rather than failing the wallpaper subsystem.

Candidate scoring should account for the previously discussed artistic goals:

- retain as much important subject/saliency as practical;
- heavily penalize awkward cuts through important subject regions;
- provide reasonable edge clearance;
- preserve useful negative space rather than always centering the subject;
- respect composition already present in the original artwork;
- prefer sensible rule-of-thirds placement where it improves the composition;
- account for an off-center subject's apparent orientation/available space when deciding which side of the frame to preserve;
- avoid randomness.

Do not blindly encode the illustrative weights from earlier brainstorming as final constants. Codex should design/tune the scoring model and document why it is stable and deterministic.

## Subject orientation

U²-NetP provides saliency/shape, not semantic gaze direction. The first implementation can infer useful composition from the mask's centroid, bounding geometry, spatial distribution, and original negative space without pretending it knows where a character is looking.

Possible later enhancement: evaluate a lightweight anime character/face/orientation detector if real samples prove mask-only composition insufficient. Do not add a second model merely because it sounds clever; keep the first implementation lightweight and measurable.

## Performance and lifecycle

Planning should consider:

- run ML only when needed, not every frame;
- inference on a reduced-resolution copy;
- crop/render from original source resolution;
- CPU-first behavior so wallpaper selection does not unnecessarily wake/occupy the gaming GPU;
- cache saliency/crop results;
- avoid blocking the Quickshell render thread;
- network and ML failures must not crash/freeze the shell;
- model/plugin failure should leave the last known-good wallpaper or a safe local fallback;
- multiple monitor resolutions/aspect ratios may need separate cached crop geometry;
- rotation interval/manual-next/cache-retention behavior should be planned in Settings rather than silently hardcoded.

## Gaming Mode reuse

The future Hearth Decky/GM implementation should be able to reuse:

- provider configuration/query building;
- network fetch/download/cache metadata;
- deterministic crop logic and cached results;
- wallpaper selection state where appropriate.

Do not bury all of this inside a QML `WallpaperPage.qml` implementation that Gaming Mode would have to reimplement.
