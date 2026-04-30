#!/usr/bin/env python3
"""
Generate slides.html from slides.template.html + content files.

Usage:
    python3 generate.py

Content files:
    content/speaker-csg.json   <- diisi pemateri CSG
    content/speaker-ajaib.json <- diisi pemateri Ajaib
"""

import json
import re
import sys
from pathlib import Path

TEMPLATE = Path("slides.template.html")
OUTPUT   = Path("slides.html")
CONTENT  = [
    Path("content/speaker-csg.json"),
    Path("content/speaker-ajaib.json"),
]

# ── Load & merge content files ────────────────────────────────────────────────

data = {}
for path in CONTENT:
    if not path.exists():
        print(f"ERROR: {path} tidak ditemukan.")
        sys.exit(1)
    try:
        with open(path) as f:
            chunk = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: {path} JSON tidak valid — {e}")
        sys.exit(1)
    # skip meta/instruksi keys
    chunk = {k: v for k, v in chunk.items() if not k.startswith("_")}
    data.update(chunk)

# ── Load template ─────────────────────────────────────────────────────────────

if not TEMPLATE.exists():
    print(f"ERROR: {TEMPLATE} tidak ditemukan.")
    sys.exit(1)

template = TEMPLATE.read_text()

# ── Replace {{PLACEHOLDER}} tokens ───────────────────────────────────────────

missing = []

def replace_token(match):
    key = match.group(1)
    if key in data:
        return data[key]
    missing.append(key)
    return match.group(0)  # keep original if missing

result = re.sub(r"\{\{([A-Z0-9_]+)\}\}", replace_token, template)

# ── Report ────────────────────────────────────────────────────────────────────

filled  = len(data)
total   = len(re.findall(r"\{\{[A-Z0-9_]+\}\}", template))
unique  = len(set(re.findall(r"\{\{([A-Z0-9_]+)\}\}", template)))

print(f"Template  : {TEMPLATE}")
print(f"Placeholder: {unique} unique / {total} total")
print(f"Content   : {filled} keys loaded")

if missing:
    print(f"\nWARNING: {len(set(missing))} placeholder belum diisi:")
    for key in sorted(set(missing)):
        print(f"  {{{{ {key} }}}}")
    print("\nSlides tetap di-generate dengan placeholder yang ada.")
else:
    print("Status    : semua placeholder terisi")

# ── Write output ──────────────────────────────────────────────────────────────

OUTPUT.write_text(result)
print(f"\nOutput    : {OUTPUT} ({OUTPUT.stat().st_size // 1024} KB)")
print("Buka slides.html di browser untuk preview.")
