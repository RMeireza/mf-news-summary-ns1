#!/usr/bin/env python3
"""News-summary-01 entry: writes the bundled summary of Wednesday 11 November 2026 world news to /output/entry.txt.
The summary is shipped in the repository; this program copies it, byte-identical on every run (no network)."""
import os, shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "summary.txt")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.txt"))
