"""Internal episode calendar; TRT is the external broadcast source."""
import json
from pathlib import Path
from released_guides import esc, external, internal, display_date, BROADCAST_GUIDE

CALENDAR = json.loads(Path(__file__).with_name('broadcast_calendar.json').read_text())


def render_calendar(origin, season, series, route):
    records = []
    for ep in CALENDAR['episodes']:
        n, s, date = ep['overall_episode'], ep['season_episode'], ep['broadcast_date']
        state = 'Upcoming' if ep['status'] == 'upcoming' else 'Released'
        source_label = 'Official TRT preview' if ep['status'] == 'upcoming' else 'Official TRT episode'
        records.append(f'''<li class="broadcast-record" id="episode-{n}">
          <div class="broadcast-identity"><h2>Episode {s}</h2><p>Original Turkish episode {n}<br>Season 4</p><span class="content-label">{state}</span></div>
          <div class="broadcast-date"><span>Original broadcast date</span><time datetime="{date}">{display_date(date)}</time><p>TRT weekly slot: Tuesday · 20:00 Turkey</p></div>
          <div class="broadcast-actions">{external(ep['trt_source'],source_label)}{internal(route(n,'Urdu'),'Urdu subtitle guide')}{internal(route(n,'English'),'English subtitle guide')}</div>
        </li>''')
    content = f'''<article class="episode-page broadcast-page">
      <nav class="episode-breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="{series}">Sultan Fatih</a></li><li><a href="{season}">Season 4</a></li><li aria-current="page">Broadcast dates</li></ol></nav>
      <header class="broadcast-intro"><p class="episode-kicker">Sultan Muhammad Fateh / Mehmed Fetihler Sultani</p><h1>Season 4<br>broadcast dates.</h1><p>Original Turkish release dates, correct episode numbers and the official TRT broadcast schedule in one place.</p><div class="episode-hero-actions">{external(CALENDAR['schedule_source'],'Open TRT broadcast schedule','episode-button primary')}{internal(season,'All Season 4 episodes')}</div></header>
      <section class="episode-answer"><h2>When does Sultan Fatih air on TRT 1?</h2><p class="direct-answer">TRT lists Mehmed: Fetihler Sultanı for Tuesdays at 20:00 Turkey time.</p><p>Turkey uses UTC+3. The slot corresponds to 17:00 UTC. Episode Journal maintains the episode dates below and links each record to the official TRT episode or preview.</p></section>
      <section class="episode-section"><h2>Season 4 episode release calendar</h2><p class="sources-intro">Season 4 Episodes 1–5 correspond to original Turkish Episodes 84–88. Dates refer to the original broadcast; each subtitle edition has its own viewing guide.</p><ol class="broadcast-records">{''.join(records)}</ol></section>
      <section class="episode-section reading-section"><h2>How we record dates and times</h2><p>The calendar uses Episode Journal’s editorial episode records. TRT is the primary source for the weekly broadcast slot, episode identity, official episode pages and previews.</p><p>TRT’s <span lang="tr">Giriş</span> and <span lang="tr">Güncelleme</span> timestamps describe when a webpage was posted or updated. They are separate from the television broadcast date and from subtitle upload times.</p><p>For example, TRT’s Episode 87 webpage displays 7 October 2026, while our episode calendar records the original broadcast on 6 October 2026.</p><div class="episode-hero-actions">{external(CALENDAR['schedule_source'],'TRT official series schedule')}{external(CALENDAR['schedule_source']+'/bolum/87-bolum','TRT Episode 87 page')}</div><p class="page-note">Calendar reviewed 13 October 2026. Released Urdu and English viewing options were verified by the publisher. Upcoming episodes remain scheduled until released.</p></section>
      <nav class="episode-bottom-nav" aria-label="Related guides">{internal(season,'Return to Season 4')}{internal('/how-we-check/','How we verify episodes')}</nav>
    </article>'''
    title = 'Sultan Muhammad Fateh Season 4 Release Dates & TRT Schedule'
    description = 'Sultan Fatih Season 4 broadcast dates for Episodes 84–88, the official Tuesday 20:00 TRT schedule, and separate Urdu and English subtitle guides.'
    schema = [
        {'@context':'https://schema.org','@type':'CollectionPage','name':title,'description':description,'url':origin+BROADCAST_GUIDE,'inLanguage':'en','dateModified':'2026-10-13','about':{'@type':'TVSeason','seasonNumber':4,'partOfSeries':{'@type':'TVSeries','name':'Mehmed: Fetihler Sultanı','url':origin+series}},'citation':CALENDAR['schedule_source']},
        {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[
            {'@type':'ListItem','position':1,'name':'Episode Journal','item':origin+'/'},
            {'@type':'ListItem','position':2,'name':'Sultan Fatih','item':origin+series},
            {'@type':'ListItem','position':3,'name':'Season 4','item':origin+season},
            {'@type':'ListItem','position':4,'name':'Broadcast dates','item':origin+BROADCAST_GUIDE}]}]
    return title, description, content, schema
