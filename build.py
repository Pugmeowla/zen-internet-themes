#!/usr/bin/env python3
"""Build styles.json for Zen Internet: official themes + my overrides.

Each folder in styles/ is one site key (e.g. styles/classroom.google.com/).
Each .css file inside is one toggleable feature; the filename (minus .css)
is the feature name shown in the Zen Internet popup. A local site folder
replaces the official theme for that site entirely.
"""
import json
import pathlib
import urllib.request

UPSTREAM = "https://sameerasw.github.io/my-internet/styles.json"
ROOT = pathlib.Path(__file__).parent

with urllib.request.urlopen(UPSTREAM, timeout=30) as r:
    styles = json.load(r)

websites = styles["website"]
for site_dir in sorted((ROOT / "styles").iterdir()):
    if not site_dir.is_dir():
        continue
    features = {f.stem: f.read_text() for f in sorted(site_dir.glob("*.css"))}
    assert features, f"{site_dir} has no .css files"
    websites[f"{site_dir.name}.css"] = features
    print(f"override {site_dir.name}: {len(features)} features")

assert len(websites) > 100, "upstream looks broken, refusing to write"
(ROOT / "styles.json").write_text(json.dumps(styles, indent=1) + "\n")
print(f"wrote styles.json with {len(websites)} sites")
