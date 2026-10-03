#!/usr/bin/env python3
"""Render share cards from existing SVG design plates. Requires ImageMagick."""
from pathlib import Path
import subprocess
import os

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'assets/images/collaborations'
OUT = ROOT / 'assets/images/social'
OUT.mkdir(parents=True, exist_ok=True)
# Override on other systems with a local monospace font path or ImageMagick font name.
FONT = os.environ.get('VERUM_SHARE_FONT', '/System/Library/Fonts/Menlo.ttc')
for slug in ['registro', 'persistencia', 'testigo', 'cota', 'trazo', 'escuadra']:
    subprocess.run([
        'magick', '-font', FONT, '(', str(ART / f'{slug}.svg'), '-resize', '504x630', ')',
        '(', str(ART / f'{slug}-back.svg'), '-resize', '504x630', ')',
        '+append', '-background', '#e4e3d9', '-gravity', 'center',
        '-extent', '1200x630', str(OUT / f'{slug}.png'),
    ], check=True)
print('Rendered six garment share cards from front/back SVG plates.')
