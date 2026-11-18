#!/bin/sh
# Build the pinned checkout directly; never restore sources by PO timestamps.
set -eu

destination=${1:-book-pages}
case "$destination" in
  /*) ;;
  *) destination="$PWD/$destination" ;;
esac
git diff --exit-code -- src third_party
if [ -e "$destination/site" ]; then
  printf '%s\n' "Choose a fresh build destination: $destination/site already exists" >&2
  exit 2
fi
mkdir -p "$destination/site"
for language in en id; do
  MDBOOK_BOOK__LANGUAGE="$language" \
    MDBOOK_OUTPUT__HTML__SITE_URL="/comprehensive-rust/$language/" \
    MDBOOK_OUTPUT__PANDOC__DISABLED=true \
    mdbook build -d "$destination/$language"
  cp -R "$destination/$language/html" "$destination/site/$language"
  (cd "$destination/$language/exerciser" &&
    zip -q -r "$destination/site/$language/comprehensive-rust-exercises.zip" comprehensive-rust-exercises)
done

# PDF generation is deliberately outside this HTML release. Keep the original
# download usable and identify its language instead of publishing a broken link.
python3 - "$destination/site" <<'PY'
from pathlib import Path
import sys
root = Path(sys.argv[1])
for p in root.rglob('*.html'):
    content = p.read_text()
    content = content.replace('href="comprehensive-rust.pdf"',
        'href="https://google.github.io/comprehensive-rust/comprehensive-rust.pdf" hreflang="en"')
    p.write_text(content)
(root / 'index.html').write_text('''<!doctype html>
<html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0;url=id/">
<title>Comprehensive Rust — Indonesia</title></head>
<body><a href="id/">Baca Comprehensive Rust dalam bahasa Indonesia</a></body></html>
''')
PY
git diff --exit-code -- src third_party
