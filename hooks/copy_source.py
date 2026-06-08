"""
MkDocs post-build hook: kopíruje docs/ strom do site/_source/

Po každém buildu (včetně --strict) jsou raw Markdown soubory dostupné přes HTTP
na /_source/<cesta>.md — užitečné pro AI parsery, které preferují čistý MD
před renderovaným HTML.
"""

import shutil
from pathlib import Path


def on_post_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    site_dir = Path(config["site_dir"])
    source_dir = site_dir / "_source"

    if source_dir.exists():
        shutil.rmtree(source_dir)

    shutil.copytree(docs_dir, source_dir)
