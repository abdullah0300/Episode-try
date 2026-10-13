"""Shared metadata and consistent publisher/site entities."""
import html
import json
from site_config import ORIGIN, UPDATED

SERIES = '/dramas/mehmed-fetihler-sultani/'
SEASON = SERIES + 'season-4/'


def breadcrumbs(items):
    return {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[
        {'@type':'ListItem','position':i+1,'name':name,'item':ORIGIN+url} for i,(name,url) in enumerate(items)]}


def page_schema(title, description, url, kind='WebPage', about=None):
    result={'@context':'https://schema.org','@type':kind,'@id':ORIGIN+url+'#webpage','name':title,
            'description':description,'url':ORIGIN+url,'inLanguage':'en','dateModified':UPDATED,
            'isPartOf':{'@id':ORIGIN+'/#website'},'publisher':{'@id':ORIGIN+'/#publisher'}}
    if about:result['about']=about
    return result


def head(title, description, url, schema=None):
    esc=lambda v:html.escape(str(v),quote=True)
    nodes=list(schema or [])
    if not any(x.get('@type') in ['WebPage','CollectionPage','AboutPage','ContactPage'] for x in nodes):
        nodes.insert(0,page_schema(title,description,url))
    for node in nodes:
        if node.get('@type') in ['WebPage','CollectionPage','AboutPage','ContactPage']:
            node.setdefault('@id',ORIGIN+url+'#webpage')
            node.setdefault('isPartOf',{'@id':ORIGIN+'/#website'})
            node.setdefault('publisher',{'@id':ORIGIN+'/#publisher'})
            node.setdefault('inLanguage','en')
            node.setdefault('dateModified',UPDATED)
    image=next((x['image'] for x in nodes if x.get('image')),ORIGIN+'/assets/frame-1.webp')
    graph=[
        {'@context':'https://schema.org','@type':'Organization','@id':ORIGIN+'/#publisher','name':'Episode Journal',
         'url':ORIGIN+'/about/','logo':{'@type':'ImageObject','url':ORIGIN+'/assets/episode-journal-logo.png','width':2172,'height':724},
         'parentOrganization':{'@type':'Organization','name':'Webcraftio','url':'https://webcraftio.com/'}},
        {'@context':'https://schema.org','@type':'WebSite','@id':ORIGIN+'/#website','name':'Episode Journal',
         'url':ORIGIN+'/','inLanguage':'en','publisher':{'@id':ORIGIN+'/#publisher'}},*nodes]
    robots='noindex,follow' if url=='/404.html' else 'index,follow,max-image-preview:large'
    og_type='article' if any(x.get('@type')=='Article' for x in nodes) else 'website'
    article=next((x for x in nodes if x.get('@type')=='Article'),{})
    dates=''.join(f'<meta property="article:{key}" content="{value}">' for key,value in [
        ('published_time',article.get('datePublished')),('modified_time',article.get('dateModified'))] if value)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="robots" content="{robots}"><link rel="canonical" href="{ORIGIN+url}"><meta name="theme-color" content="#20362d"><meta property="og:site_name" content="Episode Journal"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="{og_type}"><meta property="og:url" content="{ORIGIN+url}"><meta property="og:image" content="{image}"><meta property="og:image:alt" content="{esc(title)}"><meta property="og:locale" content="en_US"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{image}">{dates}<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/fonts.css"><link rel="stylesheet" href="/assets/style.css"><link rel="stylesheet" href="/assets/episode.css"><script type="application/ld+json">{json.dumps(graph,ensure_ascii=False)}</script><script src="/assets/app.js" defer></script></head><body>'''
