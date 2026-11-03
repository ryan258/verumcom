#!/usr/bin/env python3
"""Focused review regressions; run after a fresh Hugo build. No third-party packages."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tomllib
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('destination', type=Path)
parser.add_argument('--base-url', help='Effective Hugo base URL, including any deployment subpath')
parser.add_argument('--contact-url', help='Expected primary link when using a config/env override')
args = parser.parse_args()
dest = args.destination.resolve()
base_url = (args.base_url or tomllib.loads((ROOT / 'hugo.toml').read_text())['baseURL']).rstrip('/') + '/'
base = urlsplit(base_url)
if base.scheme not in ('http', 'https') or not base.netloc or base.query or base.fragment:
    parser.error('--base-url must be an absolute HTTP(S) URL without query or fragment')
base_path = unquote(base.path)

def site_route(route):
    return base_path.rstrip('/') + route

def output_path(path):
    decoded = unquote(path)
    assert decoded.startswith(base_path), f'Local URL escapes deployment base path: {path}'
    relative = decoded[len(base_path):]
    assert '..' not in Path(relative).parts, f'Unsafe local URL: {path}'
    return dest / relative

subprocess.run([sys.executable, str(ROOT / 'scripts/verify_concepts.py'), str(dest), '--base-url', base_url], check=True)
params = tomllib.loads((ROOT / 'hugo.toml').read_text())['params']
expected_contact = args.contact_url
if expected_contact is None and params.get('contact_verified'):
    expected_contact = {
        'instagram': params.get('instagram'),
        'email': 'mailto:' + params.get('contact_email', ''),
        'whatsapp': params.get('whatsapp'),
    }.get(params.get('primary_contact'))
    assert expected_contact, 'Confirmed primary channel has no configured destination'


class Page(HTMLParser):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.links, self.images, self.ids, self.headings = [], [], [], []
        self.meta, self.classes, self.text = {}, [], []
        self.feed((dest / route.strip('/') / 'index.html').read_text())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.classes.extend(a.get('class', '').split())
        if a.get('id'):
            self.ids.append(a['id'])
        if tag == 'a':
            self.links.append(a.get('href', ''))
        if tag == 'img':
            self.images.append(a.get('src', ''))
        if tag == 'meta':
            self.meta[a.get('property', a.get('name', ''))] = a.get('content', '')
        if tag in ('h1', 'h2', 'h3'):
            self.headings.append(tag)

    def handle_data(self, data):
        self.text.append(data)


slugs = ('registro', 'persistencia', 'testigo', 'cota', 'trazo', 'escuadra')
for lang, prefix, manifesto, contact in [('es', '', 'manifiesto', 'contacto'), ('en', '/en', 'manifesto', 'contact')]:
    home = Page(prefix + '/')
    lookbook = Page(prefix + '/lookbook/')
    drops = Page(prefix + '/drops/')
    about = Page(prefix + '/' + manifesto + '/')
    contact_page = Page(prefix + '/' + contact + '/')
    for page in (home, lookbook):
        assert page.classes.count('concept-piece-card') == 6, f'{page.route}: expected six garment cards'
        for slug in slugs:
            assert site_route(prefix + '/lookbook/' + slug + '/') in page.links, f'{page.route}: missing garment {slug}'
    assert 'artist-card' not in lookbook.classes, 'Lookbook should present garments directly'
    assert drops.classes.count('artist-card') == 2, 'Drops should retain both collections'
    assert not any('hero-model' in src or 'hero-bg' in src for src in home.images), 'Retired campaign in homepage'
    assert 'equipo' in about.ids and site_route(prefix + '/' + manifesto + '/#equipo') in home.links, 'Missing founder-section route'
    assert 'h3' not in lookbook.headings, 'Lookbook garment cards should follow h1 with h2'
    assert not any('10:00' in t or '19:00' in t for t in contact_page.text), 'Unconfirmed workshop hours remain'
    pages = [home, lookbook, about, contact_page, drops]
    social_urls = set()
    for slug in slugs:
        page = Page(prefix + '/lookbook/' + slug + '/')
        pages.append(page)
        url = page.meta.get('og:image', '')
        assert f'/images/social/{slug}' in url and url.endswith('.jpg'), f'{slug}: incorrect social image'
        assert output_path(urlsplit(url).path).is_file(), f'{slug}: share image not emitted'
        assert page.meta.get('og:image:alt') and page.meta.get('twitter:image') == url, f'{slug}: missing share metadata'
        social_urls.add(url)
    assert len(social_urls) == 6, 'Garments must have distinct share images'
    for slug in ('sobreimpreso', 'en-obra'):
        page = Page(prefix + '/drops/' + slug + '/')
        assert site_route(prefix + '/drops/') in page.links, 'Collection must return to Drops'
        pages.append(page)
    for page in pages:
        if expected_contact:
            assert expected_contact in page.links, f'{page.route}: primary channel missing'
            if page not in (about, contact_page, drops):
                assert 'follow-project' in page.classes, f'{page.route}: follow action missing'
        else:
            assert not any(url.startswith(('mailto:', 'https://instagram.com/', 'https://wa.me/')) for url in page.links), f'{page.route}: unconfirmed destination exposed'
            assert 'follow-project' not in page.classes, f'{page.route}: inactive follow action exposed'
print('PASS: garment-first home/lookbook, collection navigation, founder route, six share images, and contact state in both languages.')
