render:
    #!/usr/bin/env bash
    set -euxo pipefail
    quarto render
    python scripts/clean_up.py
    python scripts/sitemap_strip_index.py _book/sitemap.xml
