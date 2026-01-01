#!/usr/bin/env python3
"""Compile SCSS -> CSS for the DVWA mockup.

Usage:
  python build_scss.py

Requires: `pip install -r requirements.txt` (package `sass`)
"""
from pathlib import Path
import sys

try:
    import sass
except Exception as e:
    print("Missing 'sass' package. Install with: python -m pip install -r requirements.txt")
    raise

ROOT = Path(__file__).resolve().parent
SCSS = ROOT / 'app' / 'static' / 'dvwa.scss'
CSS = ROOT / 'app' / 'static' / 'dvwa.css'

if not SCSS.exists():
    print(f"SCSS source not found: {SCSS}")
    sys.exit(1)

css_text = sass.compile(filename=str(SCSS), output_style='expanded')

CSS.write_text(css_text, encoding='utf-8')
print(f"Compiled {SCSS} -> {CSS}")
