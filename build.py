#!/usr/bin/env python3
"""Stamp the production domain into index.html, robots.txt and sitemap.xml.
Usage: python3 build.py midominio.com   (no https://, no trailing slash)"""
import sys, re, pathlib
if len(sys.argv) != 2: sys.exit(__doc__)
d = sys.argv[1].strip().lower().replace("https://","").replace("http://","").strip("/")
root = pathlib.Path(__file__).parent
for name in ("index.html","robots.txt","sitemap.xml","404.html"):
    p = root/name
    if p.exists():
        t = p.read_text(encoding="utf-8")
        t = t.replace("__DOMAIN__", d)
        p.write_text(t, encoding="utf-8")
print("Dominio aplicado:", d)
