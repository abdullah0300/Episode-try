"""Whole-site SEO contracts: canonicals, schema, navigation and number mappings."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import re
import xml.etree.ElementTree as ET
from site_config import ORIGIN, DIST

ROOT=DIST

class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.meta={};self.canonical=[];self.links=[];self.graph=[];self.title='';self.capture=None;self.schema=None;self.h1=0;self.ids=[];self.aria=[];self.html_lang=None
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.html_lang=a.get('lang')
        if tag=='title':self.capture='title'
        if tag=='h1':self.h1+=1
        if a.get('id'):self.ids.append(a['id'])
        if a.get('aria-labelledby'):self.aria+=a['aria-labelledby'].split()
        if tag=='meta':self.meta[a.get('name') or a.get('property')]=a.get('content')
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
        if tag=='a' and a.get('href'):self.links.append(a['href'])
        if tag=='script' and a.get('type')=='application/ld+json':self.schema=''
    def handle_data(self,data):
        if self.capture=='title':self.title+=data
        if self.schema is not None:self.schema+=data
    def handle_endtag(self,tag):
        if tag=='title':self.capture=None
        if tag=='script' and self.schema is not None:self.graph+=json.loads(self.schema);self.schema=None

pages={p:Page(p.read_text()) for p in ROOT.rglob('*.html')}
locs=[e.text for e in ET.parse(ROOT/'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(locs)==len(set(locs))
canonical_titles={}
canonical_descriptions={}
for path,p in pages.items():
    assert p.h1==1 and len(p.canonical)==1,path
    assert len(p.ids)==len(set(p.ids)),path
    assert all(v in p.ids for v in p.aria),path
    assert p.html_lang=='en',path
    assert p.meta.get('og:title')==p.title,path
    assert p.meta.get('og:description')==p.meta.get('description'),path
    assert p.meta.get('og:url')==p.canonical[0],path
    assert p.meta.get('twitter:card')=='summary_large_image',path
    assert p.meta.get('robots'),path
    assert any(x.get('@type')=='Organization' and x.get('@id')==ORIGIN+'/#publisher' for x in p.graph),path
    assert any(x.get('@type')=='WebSite' and x.get('publisher',{}).get('@id')==ORIGIN+'/#publisher' for x in p.graph),path
    if path.name=='404.html':
        assert p.meta['robots'].startswith('noindex') and p.canonical[0] not in locs
        continue
    canonical=p.canonical[0]
    if canonical in canonical_titles:
        # Homepage is an intentional alias of the season landing page.
        assert p.title==canonical_titles[canonical] and path in [ROOT/'index.html',ROOT/'dramas/mehmed-fetihler-sultani/season-4/index.html'],path
    else:
        assert p.title not in canonical_titles.values(),path
        assert p.meta['description'] not in canonical_descriptions.values(),path
        canonical_titles[canonical]=p.title
        canonical_descriptions[canonical]=p.meta['description']
    assert canonical in locs,path
    for link in p.links:
        if not link.startswith('/'):continue
        parts=urlsplit(link);target=ROOT/parts.path.strip('/')
        if not target.suffix:target=target/'index.html'
        assert target.is_file(),(path,link)
for n in range(84,89):
    s=n-83
    for lang in ['urdu','english']:
        path=ROOT/f'dramas/mehmed-fetihler-sultani/episodes/{n}/{lang}-subtitles/index.html'
        text=path.read_text();p=pages[path]
        assert f'Episode {s}<span class="episode-original-number">Original Turkish episode {n}</span>' in text
        assert f'Episode {n}' in p.title and f'S4 Ep {s}' in p.title
        assert '/guides/mehmed-season-4-episode-numbers/' in p.links
        assert 'edition-reading-notes' in text
        if lang=='urdu':assert 'lang="ur" dir="rtl"' in text and 'Urdu reading summary' in text
        else:assert 'English viewer context' in text
        assert 'hreflang' not in text  # These are subtitle-intent guides, not full page translations.
        episode=next(x['about'] for x in p.graph if x.get('@type')=='WebPage')
        assert episode['episodeNumber']==s and str(n) in episode['identifier']
        webpage=next(x for x in p.graph if x.get('@type')=='WebPage')
        assert webpage['primaryImageOfPage']['@type']=='ImageObject'
assert set(locs)==set(canonical_titles)
assert all(any('/'+str(path.parent.relative_to(ROOT)).strip('/')+'/' in p.links for p in pages.values()) for path in pages if path.name=='index.html' and path!=ROOT/'index.html')
print(json.dumps({'html_pages':len(pages),'canonical_indexable_pages':len(locs),'unique_metadata':'passed',
                  'publisher_schema':'passed','internal_links':'passed','dual_numbering':'passed',
                  'edition_content':'passed','sitemap_and_404':'passed'}))
