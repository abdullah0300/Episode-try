"""One origin for preview and self-hosted builds; never derive it from a request."""
import os
from pathlib import Path
from urllib.parse import urlsplit

ROOT=Path(__file__).parent
PREVIEW_ORIGIN='https://fatih-episode-journal.abdullah898898.chatgpt.site'
BUILD_TARGET=os.environ.get('BUILD_TARGET','preview')
if BUILD_TARGET not in ['preview','self-hosted']:
    raise ValueError('BUILD_TARGET must be preview or self-hosted.')
provided=os.environ.get('SITE_ORIGIN')
if BUILD_TARGET=='self-hosted' and not provided:
    raise ValueError('Set SITE_ORIGIN to your final HTTPS domain before a self-hosted build.')
ORIGIN=(provided or PREVIEW_ORIGIN).rstrip('/')
parts=urlsplit(ORIGIN)
if parts.scheme!='https' or not parts.hostname or any(c.isspace() for c in ORIGIN) or parts.path or parts.query or parts.fragment or parts.username or parts.password:
    raise ValueError('SITE_ORIGIN must be an HTTPS origin, without a path, query, credentials or fragment.')
if BUILD_TARGET=='self-hosted' and ORIGIN==PREVIEW_ORIGIN:
    raise ValueError('A self-hosted build must use your own final domain rather than the preview origin.')
DIST=Path(os.environ.get('SITE_OUTPUT_DIR',str(ROOT/'dist'))).resolve()
# Actual editorial modification date; deliberately not the current build date.
UPDATED='2026-10-13'
