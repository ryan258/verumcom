#!/usr/bin/env python3
"""Focused, dependency-free verification of the two artist collections."""
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import tomllib
from urllib.parse import unquote, urljoin, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DEST = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else None
if DEST is None or not DEST.is_dir():
    raise SystemExit('Usage: python3 scripts/verify_concepts.py <clean Hugo output directory>')


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def metadata(path):
    # Interviews use TOML (+++) for their nested chapters; other content is one JSON value per line.
    text = path.read_text()
    if text.startswith('+++'):
        return tomllib.loads(text.split('+++', 2)[1])
    front = text.split('---', 2)[1]
    return {key: json.loads(value) for key, value in
            (line.split(': ', 1) for line in front.strip().splitlines())}


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.h1 = 0
        self.text = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'h1':
            self.h1 += 1

    def handle_data(self, data):
        self.text.append(data)


all_routes = []
translations = {}
for lang, prefix in [('es', ''), ('en', '/en')]:
    sections = {}
    for section, count in [('lookbook', 6), ('drops', 2), ('veritas', 2)]:
        files = sorted((ROOT / 'content' / lang / section).glob('*/index.md'))
        check(len(files) == count, f'{lang}/{section}: expected {count} items')
        sections[section] = {p.parent.name: metadata(p) for p in files}
        for slug, data in sections[section].items():
            translations.setdefault(data['translationKey'], []).append((lang, data))
            check(data['concept'] is True, f'{lang}/{section}/{slug}: missing concept flag')
            all_routes.append(f'{prefix}/{section}/{slug}/')
        all_routes.append(f'{prefix}/{section}/')
    all_routes.append(f'{prefix}/')
    counts = Counter(p['artist_id'] for p in sections['lookbook'].values())
    check(sorted(counts.values()) == [3, 3], f'{lang}: each artist needs three pieces')
    for slug, piece in sections['lookbook'].items():
        for ref, section in [('drop_ref', 'drops'), ('story_ref', 'veritas')]:
            target = piece[ref].removeprefix(section + '/')
            check(target in sections[section], f'{slug}: missing {ref}')
            check(sections[section][target]['artist_id'] == piece['artist_id'], f'{slug}: wrong artist in {ref}')
        for field in ['art', 'art_back']:
            check((ROOT / 'assets' / piece[field]).is_file(), f'{slug}: missing {field}')
    for slug, story in sections['veritas'].items():
        check(len(story['chapters']) == 3, f'{slug}: needs three chapters')
        linked = []
        for chapter in story['chapters']:
            piece = sections['lookbook'][chapter['piece']]
            check(piece['artist_id'] == story['artist_id'], f'{slug}: unrelated garment insert')
            check(len(chapter['questions']) == 2, f'{slug}: needs two questions per chapter')
            check(all(len(pair) == 2 and all(pair) for pair in chapter['questions']), f'{slug}: incomplete interview')
            linked.append(chapter['piece'])
        check(len(set(linked)) == 3, f'{slug}: repeated garment insert')
    for slug, drop in sections['drops'].items():
        kinds = {p['kind'] for p in sections['lookbook'].values() if p['artist_id'] == drop['artist_id']}
        check(kinds == {'tee', 'hoodie', 'cap'}, f'{slug}: expected tee, hoodie and cap')
        check(drop['status'] == 'concept', f'{slug}: incorrect release claim')

for key, pairs in translations.items():
    check({lang for lang, _ in pairs} == {'es', 'en'} and len(pairs) == 2, f'{key}: translation pair missing')
    a, b = pairs[0][1], pairs[1][1]
    for field in ['artist_id', 'drop_ref', 'story_ref', 'art', 'art_back', 'hero']:
        check(a.get(field) == b.get(field), f'{key}: {field} differs across languages')

cache = {}


def rendered(path):
    if path not in cache:
        check(path.is_file(), f'Missing output: {path}')
        cache[path] = Page(path)
    return cache[path]


links_checked = 0
for route in all_routes:
    page = rendered(DEST / route.lstrip('/') / 'index.html')
    check(page.h1 == 1, f'{route}: expected one h1')
    check(len(page.ids) == len(set(page.ids)), f'{route}: duplicate IDs')
    text = ' '.join(page.text)
    check(('Fictional concept' if route.startswith('/en/') else 'Concepto de ficción') in text, f'{route}: missing disclosure')
    for image in page.images:
        check('alt' in image and 'width' in image and 'height' in image, f'{route}: incomplete image attributes')
        target = urlsplit(urljoin('https://verum.com' + route, image['src']))
        if target.netloc == 'verum.com':
            check((DEST / unquote(target.path).lstrip('/')).is_file(), f'{route}: missing image {target.path}')
    for link in page.links:
        target = urlsplit(urljoin('https://verum.com' + route, link))
        if target.scheme not in ['http', 'https'] or target.netloc != 'verum.com':
            continue
        path = DEST / unquote(target.path).lstrip('/')
        if target.path.endswith('/') or path.is_dir():
            path /= 'index.html'
        check(path.is_file(), f'{route}: broken link {link}')
        if target.fragment and path.suffix == '.html':
            check(unquote(target.fragment) in rendered(path).ids, f'{route}: missing anchor {link}')
        links_checked += 1

for lang, prefix in [('es', ''), ('en', 'en')]:
    for section in ['lookbook', 'drops', 'veritas']:
        source_slugs = {p.parent.name for p in (ROOT / 'content' / lang / section).glob('*/index.md')}
        output_slugs = {p.parent.name for p in (DEST / prefix / section).glob('*/index.html')}
        check(source_slugs == output_slugs, f'{lang}/{section}: stale or missing output routes')

print(f'PASS: {len(all_routes)} rendered pages; 20 localized content items; '
      f'{links_checked} local links; bilingual relationships, interview anchors, '
      'images, disclosures and retired-route cleanup verified.')
