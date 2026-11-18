#!/usr/bin/env python3
"""Compare rendered English/Indonesian code and audit reviewed locale links."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('english', type=Path)
parser.add_argument('indonesian', type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
report = json.loads((root / 'TRANSLATION_QA.json').read_text())


class Page(HTMLParser):

    def __init__(self, text):
        super().__init__()
        self.pre = False
        self.current = []
        self.code = []
        self.ids = set()
        self.urls = []
        self.lang = None
        self.feed(text)

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'pre':
            self.pre = True
            self.current = []
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.urls.append(attrs['href'])

    def handle_data(self, data):
        if self.pre:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == 'pre' and self.pre:
            self.code.append(''.join(self.current))
            self.pre = False


cache = {}


def load(path):
    path = path.resolve()
    if path not in cache:
        cache[path] = Page(path.read_text())
    return cache[path]


pages = 0
blocks = 0
for source in args.english.rglob('*.html'):
    target = args.indonesian / source.relative_to(args.english)
    assert target.is_file(), target
    assert load(source).code == load(target).code, ('Rendered code changed',
                                                    source)
    pages += 1
    blocks += len(load(source).code)
links = 0
unbuilt = set()
for page in report['pages']:
    if not page['reviewed_in_this_batch']:
        continue
    relative = Path(page['path']).relative_to('src').with_suffix('.html')
    path = args.indonesian / relative
    current = load(path)
    assert current.lang == 'id', path
    assert 'Status terjemahan' in path.read_text(), path
    for url in current.urls:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc:
            continue
        resolved = urlsplit(
            urljoin('https://preview.invalid/' + relative.as_posix(), url))
        dest = args.indonesian / unquote(resolved.path).lstrip('/')
        if dest.is_dir():
            dest = dest / 'index.html'
        if not dest.exists() and dest.name in (
                'comprehensive-rust.pdf', 'comprehensive-rust-exercises.zip'):
            unbuilt.add(dest.name)
            continue
        assert dest.is_file(), (relative, url, dest)
        if resolved.fragment:
            assert unquote(resolved.fragment) in load(dest).ids, (relative,
                                                                  url)
        links += 1
print(
    f'PASS: {pages} HTML pages, {blocks} pre blocks identical; {links} local links in reviewed pages'
)
print('Optional downloads not built:', ', '.join(sorted(unbuilt)) or 'none')
