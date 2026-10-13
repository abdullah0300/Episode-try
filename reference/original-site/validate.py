from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import xml.etree.ElementTree as ET
from site_config import DIST

class Page(HTMLParser):
 def __init__(self,text):
  super().__init__(); self.h1=0;self.ids=set();self.links=[];self.assets=[];self.meta=False;self.canonical=False;self.has_title=False;self.json_text=None;self.jsons=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='title':self.has_title=True
  if a.get('id'):self.ids.add(a['id'])
  if tag=='meta' and a.get('name')=='description':self.meta=True
  if tag=='link' and a.get('rel')=='canonical':self.canonical=True
  if a.get('href'):self.links.append(a['href'])
  if a.get('src'):self.assets.append(a['src'])
  if tag=='img' and 'alt' not in a:raise ValueError('Missing alt')
  if tag=='script' and a.get('type')=='application/ld+json':self.json_text=''
 def handle_data(self,data):
  if self.json_text is not None:self.json_text+=data
 def handle_endtag(self,tag):
  if tag=='script' and self.json_text is not None:self.jsons.append(json.loads(self.json_text));self.json_text=None

root=DIST;parsed={p:Page(p.read_text()) for p in root.rglob('*.html')};errors=[]
for path,page in parsed.items():
 if page.h1!=1 or not(page.meta and page.canonical and page.has_title):errors.append(f'{path}: heading/metadata')
 for u in page.links+page.assets:
  if not u.startswith('/'):continue
  parts=urlsplit(u);target=root/parts.path.strip('/')
  if not target.suffix:target=target/'index.html'
  if not target.is_file():errors.append(f'{path}: missing {u}')
  elif parts.fragment and target.suffix=='.html' and parts.fragment not in parsed[target].ids:errors.append(f'{path}: missing fragment {u}')
ET.parse(root/'sitemap.xml')
fonts=root/'assets/fonts.css'
if not fonts.is_file():errors.append('Missing local font stylesheet')
print(json.dumps({'html_pages':len(parsed),'local_links_and_fragments':'checked','metadata_and_jsonld':'checked','sitemap':'valid','errors':errors}))
if errors:raise SystemExit(1)
