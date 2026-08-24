# Original Owner Prompt and Immediate Context — Verbatim

> The following text is preserved exactly as supplied by the owner on 2026-08-24. Do not treat earlier exploratory statements as newer than later explicit decisions in the same text.

It boots (I don't see why it wouldn't), but the shell is completely broken. I don't see the features I've specified either: no visual buttons displayed at all on the dock bar. I can't open even the app menu so I cannot inspect what's changed. The desktop shell became unusable so I have to use \`ujust hearth-recovery-kde\`.



I have no clue what happened to our Q&A and the plan that we previously made from the prompt I gave:
```vbnet
We need to dedicate time on starlight-hearth-shell, then separate [$deliver-vertical-slices](/Users/akippnn/.codex/skills/deliver-vertical-slices/SKILL.md)concerns from starlight-hearth and starlight-hearth-shell (note that previous assumptions may be documented, see docs), determine what vertical slices the following QOL should be prioritised in):

- You need to ask me how the controller layout works.
- The shell NEEDS to be aware a controller is connected, and the buttons should not convert into keyboard buttons. It should also not block actual keyboard button presses.
- DMS apps and widgets should have dedicated controller support (which can then nicely become keyboard support at some point). For example, navigating process widget All/User/System (on Processes panel) or All/Apps/Files/Plugins (on App menu panel) should be doable with RB/LB. Opening panels should focus on the best first item to focus on and allow navigation (first app on app menu, first control button I assume is Ethernet on default on the merged control settings+notifications -- do not hard code).  Pressing X focuses on search in all apps/panels/widgets rather than just opening the keyboard (but should not trigger both, should trigger selecting the search bar, the search bar on focus should open the keyboard). That means the search must also not be on focus the moment any panel or widget opens on controller mode. Pressing Y on supported areas (usually a space bar I suppose) changes mode: on app menu, changes mode from list/grid/etc.). On merged control setting and notifications, focuses on the lock/power/settings/edit button. Sliders like the sound and brightness should receive a controller treatment as well.
- Apps/panels/widgets with native controller support must display the controller button similar to mentioned in the below points.
- Remove the enlarged panels (app menu, power, and also add other widget panels here too) we used earlier, even the app menu. Rely on the later trick I mention instead, dark overlay by darkening the rest except the dank bar and the selected widget/app.
- A dedicated section in the settings for controller layout "Controller Layout" with displayed Controller layout visual for each button (does not matter what visual the controller uses, just make the ABXY face buttons correctly display PS4/XBOX/NS layout). Maybe use a standardized existing vector found online and then determine where to place lines to lead to the text displaying what action the button does (with modifier support, like LS and RS modifier that we currently use). It should have the exact same "New Keybind" window that allows assigning all types of buttons. It should also support modifier buttons.
- In later vertical slices, place Controller in the System section for Controller settings.
- Remove the power widget from the dank bar unless we know it's installed on a laptop.
- Create a new widget where notifications and control center are merged, then use that as the default dankbar widget at the rightmost part of the dank bar. Replacing the separate notifications and control center widgets. The notification icon should be the rightmost icon of this new merged widget. I haven't seen what it looks like when there's a notification. Steam notifications don't pop up here either, it acts as a window instead of a notification. We tried fixing this? It didn't work. Are there any fixes that could be done?
- The dank bar widgets should display the buttons on what triggers an action. For example, app launcher in settings has a set controller button (start button, the three lines in a circle). For those that use modifiers, show only the modifier (with an indicator that it is a modifier) until the modifier is held, then show the button. For workspace for example while the modifier is being held, LB is shown at the leftmost of the workspace widget, and RB is shown at the rightmost of the workspace widget).
- The select button (double square button) focus on the dank bar (a new action) and can focus at the left-most or right-most. I recommend the right-most since that's where the new merged control center+notifications will be located in. Pressing A will use the same expressive animation I mentioned earlier.
- Make sure the expressive animations are on theme and can be customised in the settings as well.
- Animate dank bar when a button is pressed (use material design 3 expressive, and make it very visible -- specific to our fork only), and those with their panels open should display if they are still open. Also for those overlays (like the app menu overlay or the control center overlay), gray out the rest except for the dank bar.
- Window controls shortcuts (X close, Y fullscreen) and window focus (RB+LB) using the RS stick modifier by default.
- I am missing a lot of control that I normally have with other shell. You should ask me what actions get a default controller bind and what controller interaction we're currently not using (so far I don't see anything to add).
- RS up and down controls page scroll by default.
- Keyboard has to be smaller, in the bottom, and should not disturb opened menus (especially starlight-hearth-shell's menu). Find a way to have it get automatically triggered when a text bar is on focus on any app currently supported.
- Settings should be replaced with Hearth information, while attributing to DMS, niri, Bazzite, Steam, etc.
- I might have missed anything so feel free to ask me questions.
- Make sure that downstream from DMS is simple and that upstreaming certain features like better controller and keyboard support is a separate concern nicely. No hardcoding and avoid collisions where possible. Might be preferably done on different branches too and update branches back and forth normally where possible.



Many apps currently don't work nicely with the controller, prompting the use for LB/RB more often. It's quite erratic and hard to predict what would happen. Is it fixable? We can fix Niri shell apps to behave more nicely, like the Settings app for example, graying out parts that are not selected.



On starlight-hearth:

- Perceived controller latency seems higher on Steam gaming mode than it used to. I'm not sure if this is an issue from our side.
- starlight-hearth will still document features and the controller layout from starlight-hearth-shell and should be maintained regularly.
- On starlight-hearth, documentation has to be updated as well. It seems that there are still statements that are outdated (such as DMS being noted as the initial shell, which was an older decision regarding whether to write an entirely new shell from scratch or use DMS).



That being said, it's still undecided: is it better to use the more mature DMS shell, or is it better to create a shell from scratch using Quickshell and Rust on our own? That would take a lot of time but that is something to consider: separately on org.starlight.HearthShell
```



This is completely disregarded in HS-003. I hope you also don't forget the Hearth Portal we've worked on:



\`\`\`



GM-001 is fine but we need to revert that and have Hearth Portal (please look into [@Fix Bazzite app roadmap]\(thread://01a02cf2-005a-75d3-84b6-58db5451402c) for more information) and other potential Hearth apps be the GM-001. Without making multiple app instances, add them as a "Non-Steam Game" but our hearth apps should be aware if it's in Gaming mode or otherwise. I think tweaking should be part of gaming mode as well, not just Steam.



- Hearth Portal should also look into restarting Steam (and Steam in Gaming mode) if the tweaks require to do so.
- Again, as customary, hearthPortal should be aligned with Bazzite Portal and should be easily maintainable. Instead, we can replace/overwrite existing entries instead if needed, create entries, or remove entries if incompatible with hearthOS.
- Hearth portal can also be the management interface for games. That includes replacing Decky-Framegen UI and maybe render ProtonPlus app unnecessary as well(?). We probably can't replace ProtonTricks though.
- Try adding more controller-adjacent apps into Steam



Anyways since we've come this far I think it's better to repurpose our existing work and go fully custom shell with Quickshell, QML. Then focus on improving Gaming Mode entirely if possible, and a custom working starlight-hearth-shell that works decently with a controller. We should trim down on the amount of features I proposed and build a very solid foundation first. Use MD3E styled interface and icons. Make sure the iconography is high quality, the font is high quality. Use the high-variety style of MD3E.



We need to make this clear from the get go. The desktop is not too necessary for now, it's more or less a gaming OS. But it also needs to be usable enough so a laptop to SSH is not overly necessary (although a nice bonus, since we can tweak via SSH without needing to go to Desktop mode for example, much cleaner). It needs to be usable enough for mouse+keyboard controls and controller use.



Also I want gaming mode controls to be similar to gaming mode. Right stick still controls the mouse (same thing anyway). We need the guide menu as well. But also, guide and vertical right stick controls volume. I assume horizontal controls brightness? Check Steam if it does that.



Then instead of the trigger sticks, use the shoulder buttons for clicking. LT and RT is useful for navigating panels and workspaces instead. Since our new shell won't have that much panels yet.



Our new shell needs:

- high-quality iconography for button hints.
- customizable keyboard shortcuts or controller layout in settings.
- customizable hearth bar, invisible. starts blurring background (MD3E-style blur) when an item is selected (or when mouse hovers on it). drag and drop philosophy (or right click menu, can also show this menu by pressing start, ctrl+i/shift+i on keyboard), on controller: pressing the select button should select this bar (starts at leftmost item, can be set on settings).
- a simple app menu at the right-most of hearth bar with keyboard/controller navigation (dpad+left-stick or wasd/hjkl/arrow-keys), categorization (LT/RT or q/e or shift+h/shift+l or shift+left/shift+right), search (Y on Xbox or Triangle on PS or X on Nintendo, ctrl+f/`/` on keyboard), app options/right-click menu (press start, ctrl+i/shift+i on keyboard). the default category, how the apps are categorized (can be done with drag and drop on mouse, or the app right click menu and then navigating categories can be done on keyboard and controller too), and how many items on the grid column of the app menu can have depends on what's set in the settings app (
- workspaces button next to the app menu button. opens niri's workspace. a keyboard shortcut can be assigned, by default: meta+f3.
- a window/workspace switcher with nicely blurred MD3E-style overlay (I assume shells handle this, not niri) too. by default, meta+tab switches window. meta+` switches workspaces.
- time and clock at the center of the bar (does nothing except show time for now).
- system tray at the left. opens a simple customizable control center
- both the control center (shows the icon) and hearth bar support placing widgets anywhere. for now we don't really need that much in the control center. how many items on the grid column the control center can have depends on what's set in the settings app (by default 3).
- settings app should exist with all of this in mind. do not overpopulate the settings app for now, some system settings can be changed via the gaming mode in early stages for now (like Wi-Fi or Time for example). we can dedicate this to modifying the shell for now. all non-default settings are placed in the config file. all shell settings are applied by the settings app automatically (and also when config file changes are detected).
- a config file standard needs to be determined.
- hearth shell apps are also completely navigateable using controller and keyboard. hearth portal and hearth settings are the two first apps. UI for MPV will be added later.
- some apps from the hearth shell can be uniquely opened in gaming mode. hearth portal (our own take on bazzite portal -- if you remember my specifications about this) is one of them. it still retains MD3E but be careful with window scaling here.
- a few set of starlight color tones on the settings app to color the rest of the environment, and option for custom tones.
- a secure but powerful plugin system.
- a background wallpaper

It's funny that using a controller on desktop has parallels with making it actually usable for keyboard users like us that love vim shortcuts as well. Desktop UIs seem to have lost that and have gotten overly complicated over time. I hope that starlight-hearth and starlight-hearth-shell grow to be much more than just a controller-first OS. Though not that uniquely as I've seen a lot of vibecoded shells too, but we can take initiative by actually attacking the foundation where it's so important.

Yes Gaming Mode is a good part of the focus, but making the shell good enough as an alternative to gaming mode is important too before paying attention to the smaller details.

To find inspiration, we will keep DMS installed for inspiration and features to be added.
