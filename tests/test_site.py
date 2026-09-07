"""Checks the newsletter landing page is complete enough to publish."""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "devtoolpirate.com"
HANDLE = "cepstrum9"


class SiteContractTests(unittest.TestCase):
    def test_cname_is_apex_domain(self) -> None:
        self.assertEqual(ROOT.joinpath("CNAME").read_text(encoding="utf-8").strip(), DOMAIN)

    def test_index_states_the_three_beats(self) -> None:
        html = ROOT.joinpath("index.html").read_text(encoding="utf-8")
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("Devtool Pirate", html)
        self.assertIn("open-source", html.lower())
        self.assertIn("paper", html.lower())
        self.assertIn("engineering", html.lower())
        self.assertIn(f"https://x.com/{HANDLE}", html)
        self.assertIn('id="subscribe-form"', html)
        self.assertIn('type="email"', html)
        self.assertIn('name="viewport"', html)
        self.assertIn('rel="canonical"', html)

    def test_index_is_not_a_for_sale_page(self) -> None:
        html = ROOT.joinpath("index.html").read_text(encoding="utf-8")
        for token in ("for sale", "Inquire on X", "Price on request", "TODO", "TBD"):
            self.assertNotIn(token, html)

    def test_supporting_files_exist(self) -> None:
        for name in ("404.html", "favicon.svg", "robots.txt", "sitemap.xml"):
            path = ROOT.joinpath(name)
            self.assertTrue(path.is_file(), f"missing {name}")
            self.assertGreater(path.stat().st_size, 0)

    def test_robots_and_sitemap_point_at_domain(self) -> None:
        robots = ROOT.joinpath("robots.txt").read_text(encoding="utf-8")
        sitemap = ROOT.joinpath("sitemap.xml").read_text(encoding="utf-8")
        self.assertIn("Allow: /", robots)
        self.assertIn(f"https://{DOMAIN}/sitemap.xml", robots)
        self.assertIn(f"https://{DOMAIN}/", sitemap)


if __name__ == "__main__":
    unittest.main()
