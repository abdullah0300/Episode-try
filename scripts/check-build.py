"""Check snapshot fidelity, allowing approved subtitle timers and release FAQ edits."""
from pathlib import Path
from html.parser import HTMLParser
import json, re, xml.etree.ElementTree as ET

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.meta = {}; self.canonical = []; self.h1 = 0; self.main = False
        self.skip_subtitle_timer = False
        self.subtitle_timers = []
        self.main_text = []; self.main_links = []; self.links = []; self.assets = []; self.graph = []
        self.script = None; self.title = ''; self.in_title = False; self.ids = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'data-subtitle-countdown' in a:
            self.subtitle_timers.append((a['data-subtitle-countdown'], a.get('data-edition')))
        if tag == 'section' and 'subtitle-countdown' in a.get('class', '').split(): self.skip_subtitle_timer = True
        if tag == 'main': self.main = True
        if tag == 'h1': self.h1 += 1
        if tag == 'title': self.in_title = True
        if tag == 'meta': self.meta[a.get('name') or a.get('property')] = a.get('content')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical.append(a['href'])
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
            if self.main: self.main_links.append(a['href'])
        if tag == 'img' and a.get('src'): self.assets.append(a['src'])
        if tag == 'script' and a.get('type') == 'application/ld+json': self.script = ''
        if a.get('id'): self.ids.append(a['id'])
    def handle_data(self, text):
        if self.main and not self.skip_subtitle_timer: self.main_text.append(text)
        if self.in_title: self.title += text
        if self.script is not None: self.script += text
    def handle_endtag(self, tag):
        if tag == 'section' and self.skip_subtitle_timer: self.skip_subtitle_timer = False
        if tag == 'main': self.main = False
        if tag == 'title': self.in_title = False
        if tag == 'script' and self.script is not None:
            self.graph.extend(json.loads(self.script)); self.script = None

def normalized(parts):
    text = re.sub(r'\s+', ' ', ''.join(parts)).strip()
    for edition in ('Urdu', 'English'):
        text = text.replace('The '+edition+' subtitle upload time is not confirmed.', edition+' subtitles are expected by Wednesday, 14 October 2026 at 12:00 noon Pakistan time (PKT). Uploads may arrive earlier; availability is checked separately.')
    return text

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root/'data/route-manifest.json').read_text(encoding="utf-8"))
metadata = json.loads((root/'data/page-metadata.json').read_text(encoding="utf-8"))
revisions = json.loads((root/'data/page-revisions.json').read_text(encoding="utf-8"))
build = root/'.next/server/app'
origin = None; canonical = set()
for item in manifest:
    path = item['path']
    rendered = build/('index.html' if path == '/' else '_not-found.html' if path == '/404/' else path.strip('/')+'.html')
    assert rendered.is_file(), rendered
    text = rendered.read_text(encoding="utf-8")
    assert 'chatgpt.site' not in text and '__SITE_ORIGIN__' not in text, path
    p = Page(text)
    timer_editions = {
        '/': ['Urdu', 'English', 'Urdu', 'English'],
        '/dramas/mehmed-fetihler-sultani/season-4/': ['Urdu', 'English', 'Urdu', 'English'],
        '/dramas/mehmed-fetihler-sultani/season-4/urdu-subtitles/': ['Urdu'],
        '/dramas/mehmed-fetihler-sultani/season-4/english-subtitles/': ['English'],
        '/dramas/mehmed-fetihler-sultani/episodes/88/urdu-subtitles/': ['Urdu'],
        '/dramas/mehmed-fetihler-sultani/episodes/88/english-subtitles/': ['English'],
        '/dramas/mehmed-fetihler-sultani/episodes/89/urdu-subtitles/': ['Urdu'],
        '/dramas/mehmed-fetihler-sultani/episodes/89/english-subtitles/': ['English'],
    }.get(path, [])
    deadline = '2026-10-14T12:00:00+05:00' if '/episodes/88/' in path else '2026-10-21T12:00:00+05:00'
    assert p.subtitle_timers == [(deadline, edition) for edition in timer_editions], path
    if timer_editions:
        assert ('Wednesday, 14 October 2026' if '/episodes/88/' in path else 'Wednesday, 21 October 2026') in text and '12:00 noon Pakistan time (UTC+5)' in text, path
    original = Page((root/'reference/original-site'/item['source']).read_text(encoding="utf-8")) if item.get('source') else None
    assert p.h1 == 1, path
    assert len(p.ids) == len(set(p.ids)), path
    changed = path == '/' or '/season-4/' in path or '/episodes/' in path or '/mehmed-season-4-episode-numbers/' in path
    if original and not changed:
        assert normalized(p.main_text) == normalized(original.main_text), f'main text changed: {path}'
        assert p.main_links == original.main_links, f'main links changed: {path}'
        assert [a.replace('episode-journal-logo-480.webp', 'episode-journal-logo.png') for a in p.assets] == original.assets, f'images changed: {path}'
    for link in p.links:
        if link.startswith('/') and not link.startswith('//'):
            target = link.split('#')[0].split('?')[0] or path
            assert target in metadata or target.startswith('/assets/') or target in ('/sitemap.xml', '/robots.txt'), f'broken internal link: {path} -> {link}'
    if '/episodes/89/' in path:
        assert 'Expected on 20 October 2026' in text, path
        assert 'episode-specific synopsis has not been verified' in text, path
        assert 'episodes/88/' in text and 'frame-1.webp' in text, path
        assert '/ozet/89-bolum-ozet' not in text, path
    assert p.title == metadata[path]['title'], path
    assert p.meta['description'] == metadata[path]['description'], path
    assert len(p.canonical) == 1, path
    actual_origin = p.canonical[0].split('/', 3)[:3]
    actual_origin = '/'.join(actual_origin)
    origin = origin or actual_origin
    assert actual_origin == origin, path
    expected = json.loads(json.dumps(metadata[path]).replace('__SITE_ORIGIN__', origin))
    assert p.canonical[0] == expected['canonical'], path
    assert p.graph == expected['graph'], f'schema changed: {path}'
    for node in p.graph:
        if 'dateModified' in node: assert node['dateModified'] == revisions[path], path
    assert not any('makkitv.com/mehmed-' in link for link in p.links), path
    assert p.meta['og:url'] == expected['canonical'], path
    if path == '/404/': assert 'noindex' in p.meta['robots'], path
    else:
        assert 'noindex' not in p.meta['robots'], path
        canonical.add(p.canonical[0])

locs = [e.text for e in ET.parse(build/'sitemap.xml.body').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(locs) == len(set(locs)) == 21
assert set(locs) == canonical
assert origin+'/sitemap.xml' in (build/'robots.txt.body').read_text(encoding="utf-8")
assert 'chatgpt.site' not in (build/'sitemap.xml.body').read_text(encoding="utf-8")
print(json.dumps({'rendered_pages': len(manifest), 'canonical_pages': len(canonical),
                  'unchanged_page_fidelity': 'passed', 'internal_links_and_new_guides': 'passed',
                  'metadata_and_schema': 'passed', 'sitemap_and_robots': 'passed', 'build_origin': origin}))
