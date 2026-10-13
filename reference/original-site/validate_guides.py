"""Check released guide structure, numbering, metadata and language-specific links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import xml.etree.ElementTree as ET
from site_config import ORIGIN, DIST

ROOT = Path(__file__).parent
DATA = json.loads((ROOT / 'episode_content.json').read_text())
PREFIX = '/dramas/mehmed-fetihler-sultani/episodes/'
EXPECTED = ['identity', 'quick-answer', 'release-details', 'where-to-watch', 'overview',
            'story-details', 'context', 'availability-history', 'questions', 'sources']
DATES = {'84': '2026-09-15', '85': '2026-09-22', '86': '2026-09-29', '87': '2026-10-06'}


class Guide(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.sections, self.links, self.canonicals, self.titles, self.schema = [], [], [], [], []
        self.title = self.script = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'section' and a.get('id'):
            self.sections.append(a['id'])
        if a.get('href'):
            self.links.append(a['href'])
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonicals.append(a['href'])
        if tag == 'title':
            self.title = ''
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.script = ''

    def handle_data(self, text):
        if self.title is not None:
            self.title += text
        if self.script is not None:
            self.script += text

    def handle_endtag(self, tag):
        if tag == 'title':
            self.titles.append(self.title)
            self.title = None
        if tag == 'script' and self.script is not None:
            self.schema.extend(json.loads(self.script))
            self.script = None


titles = set()
for n, data in DATA.items():
    for lang in ['Urdu', 'English']:
        route = PREFIX + n + '/' + lang.lower() + '-subtitles/'
        text = (DIST / route.strip('/') / 'index.html').read_text()
        page = Guide(text)
        assert page.sections == EXPECTED, (route, page.sections)
        assert page.canonicals == [ORIGIN + route], route
        assert len(page.titles) == 1 and page.titles[0] not in titles, route
        titles.add(page.titles[0])
        watch = text[text.index('<section id="where-to-watch"'):text.index('<section id="overview"')]
        names = ['Great Nation', 'Makki TV', 'Niazi TV', 'Historical Point']
        positions = [watch.index('>'+name+'</h3>') for name in names]
        assert positions == sorted(positions), route
        assert 'Free · Notifications' in watch and 'publisher-supplied information' in watch
        wanted = 'https://play.niazitv.pk/drama/82/single-serie?watch=1&episode=' + data['niazi'][lang]
        assert wanted in page.links, route
        other = 'English' if lang == 'Urdu' else 'Urdu'
        wrong = 'https://play.niazitv.pk/drama/82/single-serie?watch=1&episode=' + data['niazi'][other]
        assert wrong not in page.links, route
        assert PREFIX+n+'/'+other.lower()+'-subtitles/' in page.links, route
        webpage = next(x for x in page.schema if x.get('@type') == 'WebPage')
        article = next(x for x in page.schema if x.get('@type') == 'Article')
        episode = webpage['about']
        assert episode['episodeNumber'] == int(n)-83
        assert episode['datePublished'] == DATES[n]
        assert webpage['inLanguage'] == article['inLanguage'] == 'en'
        assert 'hreflang' not in text and 'VideoObject' not in text
        assert 'not a complete watched recap' in text
        assert 'The publisher verified' in text
        assert 'Unverified' not in text and 'Playback has not been tested' not in text
        assert '/season-4/broadcast-dates/' in text
        assert 'episodate' not in text.lower()
        assert 'TRT 1 — official episode synopses' in text

sitemap = ET.parse(DIST / 'sitemap.xml')
locs = [x.text for x in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(locs) == len(set(locs))
assert all(ORIGIN+PREFIX+n+'/'+lang.lower()+'-subtitles/' in locs for n in DATA for lang in ['Urdu', 'English'])
print(json.dumps({'released_guides': 8, 'common_section_order': 'passed', 'provider_order': 'passed',
                  'language_specific_links': 'passed', 'canonical_and_numbering': 'passed',
                  'source_transparency': 'passed', 'sitemap': 'passed'}))
