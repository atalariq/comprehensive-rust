#!/usr/bin/env python3
"""Audit the completed Indonesian batch using GNU Gettext and Python stdlib.

Run with msgfmt on PATH: python3 scripts/check-id-translation.py
"""
import gettext
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
REPORT = json.loads((ROOT / 'TRANSLATION_QA.json').read_text())
sha = lambda text: hashlib.sha256(text.encode()).hexdigest()

with tempfile.TemporaryDirectory(prefix='rust-id-audit-') as temporary:
    mo = Path(temporary) / 'id.mo'
    subprocess.run(
        ['msgfmt', '--check', '-o',
         str(mo), str(ROOT / 'po/id.po')],
        check=True)
    with mo.open('rb') as stream:
        catalogue = gettext.GNUTranslations(stream)._catalog

messages = {
    sha(key): (key, value)
    for key, value in catalogue.items() if isinstance(key, str) and key
}
reviewed = REPORT['reviewed_message_sha256']
assert set(reviewed) <= messages.keys(
), 'Reviewed messages are missing, empty or fuzzy'
assert {str(f.relative_to(ROOT))
        for f in (ROOT / 'src').rglob('*.md')
        } == {p['path']
              for p in REPORT['pages']}, 'Source page inventory changed'
for page in REPORT['pages']:
    assert hashlib.sha256((ROOT / page['path']).read_bytes()).hexdigest(
    ) == page['sha256'], page['path'] + ': source changed; review required'
for digest in reviewed:
    source, target = messages[digest]
    for pattern in (r'(?<!`)`[^`\n]+`(?!`)', r'\]\(([^)]+)\)',
                    r'<(https?://[^>]+)>', r'</?(?:kbd|sub|sup)[^>]*>'):
        assert re.findall(pattern, source) == re.findall(
            pattern, target), ('Protected source content changed', source)
for digest in REPORT['identity_message_sha256']:
    source, target = messages[digest]
    assert source == target, ('Protected literal changed', source)
if 'fundamentals' in REPORT:
    summary = (ROOT / 'src/SUMMARY.md').read_text()
    course = summary.split('# Day 1: Morning',
                           1)[1].split('# Macros: Morning', 1)[0]
    expected = {
        'src/' + path
        for _, path in re.findall(r'\[([^]]+)\]\(([^)]+)\)', course)
    }
    assert expected == set(
        REPORT['fundamentals']
        ['pages']), 'Fundamentals coverage differs from navigation'
    pages = {page['path']: page for page in REPORT['pages']}
    assert all(
        pages[path]['reviewed_in_this_batch']
        and pages[path]['all_entries_present']
        for path in expected), 'Fundamentals contains an unfinished page'
    print(
        f'PASS: all {len(expected)} Fundamentals pages are included in the reviewed batch'
    )
print(
    f'PASS: {len(reviewed)} reviewed messages; protected literals/links/markup and all source hashes'
)
print(
    'Catalogue is partial. AI review is not human review; see TRANSLATION_STATUS.md.'
)
