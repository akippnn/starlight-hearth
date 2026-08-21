from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PublicWarningContracts(unittest.TestCase):
    def test_readme_warns_before_product_description(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        first = "\n".join(readme.splitlines()[:24])
        rendered = "\n".join(
            line.removeprefix("> ").removeprefix(">")
            for line in first.splitlines()
        )
        normalized = " ".join(rendered.split())
        self.assertIn("Pre-alpha — owner testing only", normalized)
        self.assertIn("not ready for general installation", normalized)
        self.assertIn("download counts do not imply a supported release", normalized)

    def test_recipe_publishes_owner_test_warning(self):
        recipe = (ROOT / "recipes" / "recipe.yml").read_text(encoding="utf-8")
        self.assertIn(
            "description: PRE-ALPHA / OWNER TESTING ONLY - DO NOT INSTALL FOR GENERAL USE.",
            recipe,
        )
        self.assertIn("VS-002 is audit-ready and awaits owner hardware acceptance.", recipe)
        self.assertIn(
            "org.opencontainers.image.source: https://github.com/akippnn/starlight-hearth",
            recipe,
        )



if __name__ == "__main__":
    unittest.main()

