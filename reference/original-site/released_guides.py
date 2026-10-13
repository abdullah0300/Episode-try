"""Readable episode pages with one shared editorial and SEO structure."""
import html
import json
from pathlib import Path

CONTENT = json.loads(Path(__file__).with_name('episode_content.json').read_text())
GREAT = 'https://greatnation.webcraftio.com/'
MAKKI = 'https://makkitv.com/'
NIAZI = 'https://play.niazitv.pk/'
HISTORICAL = 'https://historicalpoint.com/'
TRT = 'https://www.trt1.com.tr/diziler/mehmed-fetihler-sultani'
CHECKED = '13 October 2026'
BROADCAST_GUIDE = '/dramas/mehmed-fetihler-sultani/season-4/broadcast-dates/'


def esc(value):
    return html.escape(str(value), quote=True)


def external(url, label, cls='episode-button secondary'):
    return f'<a class="{cls}" href="{esc(url)}" target="_blank" rel="noopener">{esc(label)}</a>'


def internal(url, label, cls='episode-button secondary'):
    return f'<a class="{cls}" href="{esc(url)}">{esc(label)}</a>'


def display_date(value):
    from datetime import date
    d = date.fromisoformat(value)
    return f'{d.day} {d.strftime("%B %Y")}'


def viewing_options(ep, lang, upcoming=False):
    """Release badges follow the publisher verification record."""
    n, s = ep['n'], ep['s']
    data = CONTENT.get(str(n), {})
    great_episode = GREAT + f'drama/mehmed-fetihler-sultani/season-4/episode-{s}'
    niazi_episode = NIAZI + 'drama/82/single-serie?watch=1&episode=' + data.get('niazi', {}).get(lang, '')
    providers = [
        ('Great Nation', GREAT, 'Free · Notifications',
         'Free viewing with notifications. Select your subtitle language on the episode page.',
         great_episode if not upcoming else None),
        ('Makki TV', MAKKI, 'Includes ads',
         'Ad-supported viewing. Check the subtitle language before opening the player.',
         data.get('makki', {}).get(lang)),
        ('Niazi TV', NIAZI, 'Ads · Frequent pop-ups reported',
         'Includes ads. Frequent, intrusive pop-ups have been reported by the publisher.',
         niazi_episode if not upcoming else None),
        ('Historical Point', HISTORICAL, 'Ads · Fewer pop-ups reported',
         'Includes ads, with fewer intrusive pop-ups than Niazi TV according to the publisher.',
         data.get('historical', {}).get(lang)),
    ]
    cards = []
    for rank, (name, home, offer, note, deep) in enumerate(providers, 1):
        verified = data.get('verification', {}).get('status') == 'verified' and lang in data.get('verification', {}).get('languages', []) and name in data.get('verification', {}).get('providers', [])
        state = 'Awaiting episode release' if upcoming else (f'Verified · {lang} subtitles' if verified else 'Awaiting publisher verification')
        preferred = '<span class="provider-preference">Recommended platform</span>' if rank == 1 else ''
        actions = external(deep, f'Open Episode {s} (Original {n})', 'episode-button '+('light' if rank == 1 else 'primary')) if deep else ''
        actions += external(home, 'Visit '+name, 'episode-button '+('light-outline' if rank == 1 else 'secondary'))
        cards.append(f'''<article class="platform-card {'platform-featured' if rank == 1 else ''}" aria-labelledby="platform-{rank}">
          <div class="platform-description">{preferred}<h3 id="platform-{rank}">{esc(name)}</h3>
          <span class="platform-offer">{esc(offer)}</span><p>{esc(note)}</p>
          <p class="platform-availability"><span class="availability-dot" aria-hidden="true"></span>{state}</p></div>
          <div class="platform-actions">{actions}</div>
        </article>''')
    return f'''<div class="platform-list">{''.join(cards)}</div>
      <p class="page-note platform-disclosure">Great Nation is the publisher’s preferred platform. Free access, notifications and ad/popup notes are publisher-supplied information. {('This episode is awaiting release.' if upcoming else f'The publisher verified these {lang} viewing options on {CHECKED}.')}</p>
      <div class="official-option"><div><h3>Watch the Turkish original on TRT 1</h3><p>TRT is the official broadcaster for the original Turkish episode. Choose one of the platforms above for {lang} subtitles.</p></div>{external(TRT+(f'/ozet/{n}-bolum-ozet' if upcoming else f'/bolum/{n}-bolum'), 'Open official preview' if upcoming else 'Open TRT episode')}</div>'''


def render(ep, lang, origin, season, series, route):
    from edition_notes import render_notes
    n, s = ep['n'], ep['s']
    upcoming = ep['upcoming']
    data = CONTENT.get(str(n), {})
    other = 'English' if lang == 'Urdu' else 'Urdu'
    name = 'Sultan Muhammad Fateh' if lang == 'Urdu' else 'Mehmed Fetihler Sultani'
    title = f'{name} Episode {n} {lang} Subtitles | S4 Ep {s}'
    date = display_date(ep['date'])
    date_kind = 'scheduled broadcast date' if upcoming else 'original broadcast date'
    description = f'Season 4 Episode {s} (original Episode {n}): {lang} subtitle viewing options, {date} {date_kind}, '+('release updates and the official preview.' if upcoming else 'verified providers and sourced story details.')
    url = route(n, lang)
    official = TRT + (f'/ozet/{n}-bolum-ozet' if upcoming else f'/bolum/{n}-bolum')
    great_source = GREAT + f'drama/mehmed-fetihler-sultani/season-4/episode-{s}'
    niazi_source = None if upcoming else NIAZI + f'drama/82/single-serie?watch=1&episode={data["niazi"][lang]}'
    status = f'Scheduled for {date}' if upcoming else f'Released on TRT 1 · {date}'
    availability = 'Awaiting subtitle release' if upcoming else f'Verified · {lang} subtitles'
    answer = f'Episode {n} is scheduled for {date} on TRT 1. It is Season 4 Episode {s}.' if upcoming else f'Episode {n} aired on {date} on TRT 1. It is Season 4 Episode {s}.'
    answer_note = f'The {lang}-subtitled version is awaiting release. The Turkish broadcast and subtitle upload are separate events.' if upcoming else f'{lang} subtitle viewing options have been verified by the publisher. Great Nation is our first choice for free viewing and notifications.'
    primary_cta = internal('#where-to-watch', 'View watching options', 'episode-button primary')
    secondary_cta = internal(route(n, other), f'{other} subtitle guide')
    source_synopsis = ep['summary'] if upcoming else data['overviews'][lang]
    reading_notes = render_notes(ep,lang,data)
    developments = [('What the official preview says', ep['summary'])] if upcoming else data['developments']
    story_items = ''.join(f'<li><h3>{esc(h)}</h3><p>{esc(p)}</p></li>' for h, p in developments)
    story_note = 'This is an official preview, not a released-episode recap. Outcomes will be added only when supported by episode evidence.' if upcoming else 'These details come from published synopses, not a complete watched recap. The sources do not establish every scene or the ending.'
    context = 'Episode 87 introduces financial pressure and danger in Karaman. The next official preview focuses on diplomacy and Mustafa’s future.' if upcoming else data['context']
    people = [('Mehmed', 'Faces diplomatic pressure and decisions at court.'), ('Mustafa', 'His future is central to the official preview.')] if upcoming else data['people']
    people_list = ''.join(f'<div><dt>{esc(person)}</dt><dd>{esc(role)}</dd></div>' for person, role in people)
    first_observation = f'{lang} subtitle release is upcoming.' if upcoming else f'The publisher verified the {lang}-subtitled release and viewing options for Episode {n}.'
    free_answer = f'Great Nation is our first choice for free viewing and notifications. Episode {n} with {lang} subtitles is awaiting release.' if upcoming else f'Great Nation is our first choice for free viewing with notifications. Open Episode {s} / Bolum {n} and select {lang} Subtitles. The publisher has verified this release.'
    date_answer = f'The original Turkish broadcast is scheduled for {date}. The {lang} subtitle upload time is not confirmed.' if upcoming else f'The original Turkish broadcast date is {date}. That date does not establish when the {lang}-subtitled edition was uploaded.'
    tip = f'Use overall Episode {n} or Season 4 Episode {s}, and check for {lang} subtitles. A title alone does not confirm a playable subtitled release.' if upcoming else data['watch_tip'][lang]
    faqs = [
        (f'Is Season 4 Episode {s} the same as Episode {n}?', f'Yes. Season 4 Episode {s} maps to overall Turkish Episode {n}, also written Bölüm {n}. A dubbed release can use a different cut or numbering.'),
        (f'What is the release date for Episode {n}?', date_answer),
        (f'Where can I watch Episode {n} with {lang} subtitles for free?', free_answer),
        (f'How do I choose the correct {lang} version?', tip),
    ]
    if not upcoming:
        faqs.append((data['question'], data['answer']))
    questions = ''.join(f'<details><summary>{esc(q)}<span class="faq-symbol" aria-hidden="true">+</span></summary><p>{esc(a)}</p></details>' for q, a in faqs)
    sources = [
        (official, f'TRT 1 — official Episode {n} '+('preview' if upcoming else 'page'), 'Primary broadcaster source for episode identity and artwork.', 'Open TRT source'),
        (TRT+'/bolum', 'TRT 1 — official episode synopses', 'Primary story source for the episode overview and plot details.', 'Read TRT synopses'),
    ]
    if niazi_source:
        sources.append((niazi_source, f'Niazi TV — Episode {n}, {lang} edition', 'Language-specific listing and secondary story cross-check.', 'Open Niazi source'))
    sources.append((BROADCAST_GUIDE, 'Episode Journal — Season 4 broadcast dates', 'Our episode calendar, with the official TRT broadcast slot and primary source links.', 'View broadcast calendar'))
    sources.append((TRT, 'TRT 1 — official broadcast schedule', 'Tuesday at 20:00 Turkey time, as displayed on TRT’s series page.', 'Open TRT schedule'))
    if not upcoming:
        sources.append((great_source, f'Great Nation — Season 4 Episode {s}', f'{lang} release verified by the publisher on {CHECKED}.', 'Open Great Nation listing'))
    source_list = ''.join(f'<li><div><h3>{esc(label)}</h3><p>{esc(note)}</p></div>{(internal(link, action) if link.startswith("/") else external(link, action))}</li>' for link, label, note, action in sources)
    prev = internal(route(n-1, lang), f'Previous: Episode {s-1} (Original {n-1})') if n > 84 else internal(season, 'Season 4 overview')
    next_link = internal(route(n+1, lang), f'Next: Episode {s+1} (Original {n+1})'+(' · Upcoming' if n == 87 else '')) if n < 88 else internal(season+'#alerts', 'Follow upcoming releases')
    content = f'''
    <article class="episode-page">
      <nav class="episode-breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="{series}">Sultan Fatih</a></li><li><a href="{season}">Season 4</a></li><li aria-current="page">Episode {s} (Original {n}) · {lang}</li></ol></nav>
      <section id="identity" class="episode-hero" aria-labelledby="episode-title">
        <div class="episode-hero-copy"><p class="episode-kicker">Season 4 · Episode {s}</p>
          <h1 id="episode-title"><span class="episode-series-name">{name}</span> Episode {s}<span class="episode-original-number">Original Turkish episode {n}</span><span class="episode-title-edition">{lang} subtitles</span></h1>
          <p class="episode-status"><span class="status-dot" aria-hidden="true"></span>{status}</p>
          <p class="episode-intro">Release date, subtitle viewing options and a sourced story guide for original Turkish Episode {n}.</p>
          <div class="episode-hero-actions">{primary_cta}{secondary_cta}</div>
        </div>
        <figure class="episode-artwork"><img src="/assets/ep{n}.webp" alt="Official TRT artwork for Mehmed Fetihler Sultani Episode {n}" width="1000" height="562" fetchpriority="high"><figcaption>Official TRT artwork · Episode {n} / Bölüm {n}</figcaption></figure>
      </section>
      <section id="quick-answer" class="episode-answer" aria-labelledby="answer-title"><h2 id="answer-title">Episode {s} (Original {n}): release date and subtitles</h2><p class="direct-answer">{esc(answer)}</p><p>{esc(answer_note)}</p></section>
      <section id="release-details" class="episode-release" aria-label="Episode release details"><dl><div><dt>{'Scheduled broadcast' if upcoming else 'Original broadcast date'}</dt><dd><time datetime="{ep['date']}">{date}</time></dd></div><div><dt>Episode numbering</dt><dd>Season 4, Episode {s}<span>Original episode {n} / Bölüm {n}</span></dd></div><div><dt>{lang} subtitles</dt><dd>{availability}<span>{('Awaiting release' if upcoming else 'Verified '+CHECKED)}</span></dd></div></dl><p class="page-note">Reviewed {CHECKED}. Official TRT broadcast slot: Tuesday at 20:00 Turkey time. <a href="{BROADCAST_GUIDE}">View our Season 4 broadcast calendar.</a></p></section>
      <nav class="episode-jump-nav" aria-label="Jump to episode information">{internal('#where-to-watch','Where to watch')}{internal('#overview','Episode story')}{internal('#questions','Episode FAQs')}{internal('#sources','Sources')}</nav>
      <section id="where-to-watch" class="episode-section" aria-labelledby="watch-title"><div class="episode-section-heading"><h2 id="watch-title">Where to watch Episode {s} (Original {n}) with {lang} subtitles</h2><p>Choose a platform below. Great Nation is our first choice.</p></div>{viewing_options(ep, lang, upcoming)}</section>
      <section id="overview" class="episode-section reading-section" aria-labelledby="overview-title"><h2 id="overview-title">Episode {s} (Original {n}) story overview</h2><span class="content-label">Spoiler-free overview</span><p class="story-overview">{esc(source_synopsis)}</p>{reading_notes}</section>
      <section id="story-details" class="episode-section reading-section" aria-labelledby="story-title"><h2 id="story-title">{'Official episode preview' if upcoming else f'What happens in Episode {s} (Original {n})?'}</h2><p class="story-warning">{'Upcoming episode · Preview only' if upcoming else 'Spoiler notice: plot details from published synopses.'}</p><ol class="episode-story-list">{story_items}</ol><p class="page-note">{esc(story_note)}</p></section>
      <section id="context" class="episode-section reading-section" aria-labelledby="context-title"><h2 id="context-title">{'Before Episode '+str(n) if upcoming else ('Season context and key characters' if s==1 else 'Previous episode context and key characters')}</h2><p>{esc(context)}</p><dl class="episode-characters">{people_list}</dl><p class="page-note">Character roles describe the drama. Turkish names and translated spellings may differ between subtitle editions.</p></section>
      <section id="availability-history" class="episode-section" aria-labelledby="history-title"><h2 id="history-title">Subtitle availability updates</h2><div class="episode-update"><time datetime="2026-10-13">{CHECKED}</time><p>{esc(first_observation)}</p></div><p class="page-note">Verification date records the publisher’s check. It does not represent the subtitle upload time.</p></section>
      <section id="questions" class="episode-section" aria-labelledby="faq-title"><h2 id="faq-title">Episode {s} (Original {n}): frequently asked questions</h2><div class="episode-faq-list">{questions}</div></section>
      <section id="sources" class="episode-section" aria-labelledby="sources-title"><h2 id="sources-title">Sources and episode updates</h2><p class="sources-intro">Story and release details are based on the sources below. Guide reviewed {CHECKED} by Episode Journal.</p><ul class="episode-source-list">{source_list}</ul>
        <div class="episode-notify"><div><h3>Get notifications on Great Nation</h3><p>Great Nation is our free platform choice with publisher-reported notifications. Visit the platform for its current notification options.</p><p class="page-note">Episode Journal email alerts are not connected yet.</p></div>{external(GREAT,'Visit Great Nation','episode-button primary')}</div>
        <nav class="episode-bottom-nav" aria-label="More episode guides">{prev}{next_link}{internal(route(n,other),f'Episode {s} (Original {n}): {other} subtitles')}{internal(season,'All Season 4 episodes')}</nav>
      </section>
    </article>
    '''
    episode_id = origin + series + f'#episode-{n}'
    tv = {'@type': 'TVEpisode', '@id': episode_id, 'name': f'Mehmed: Fetihler Sultanı {n}. Bölüm',
          'episodeNumber': s, 'identifier': f'Original Turkish broadcast episode {n}',
          'partOfSeason': {'@type': 'TVSeason', 'seasonNumber': 4, 'url': origin+season},
          'partOfSeries': {'@type': 'TVSeries', '@id': origin+series+'#series', 'name': 'Mehmed: Fetihler Sultanı', 'url': origin+series}, 'sameAs': official}
    if not upcoming:
        tv['datePublished'] = ep['date']
    schema = [
        {'@context': 'https://schema.org', '@type': 'WebPage', '@id': origin+url+'#webpage',
         'name': title, 'description': description, 'url': origin+url, 'inLanguage': 'en',
         'datePublished': '2026-10-13', 'dateModified': '2026-10-13', 'about': tv,
         'primaryImageOfPage': {'@type':'ImageObject','url':origin+f'/assets/ep{n}.webp','contentUrl':origin+f'/assets/ep{n}.webp'}},
        {'@context': 'https://schema.org', '@type': 'Article', 'headline': title,
         'description': description, 'inLanguage': 'en', 'datePublished': '2026-10-13', 'dateModified': '2026-10-13',
         'author': {'@id': origin+'/#publisher'},
         'publisher': {'@id': origin+'/#publisher'},
         'image': origin+f'/assets/ep{n}.webp', 'mainEntityOfPage': {'@id': origin+url+'#webpage'},
         'about': {'@id': episode_id}, 'citation': [origin+item[0] if item[0].startswith('/') else item[0] for item in sources]},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Episode Journal', 'item': origin+'/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Sultan Fatih', 'item': origin+series},
            {'@type': 'ListItem', 'position': 3, 'name': 'Season 4', 'item': origin+season},
            {'@type': 'ListItem', 'position': 4, 'name': f'Episode {s} (Original {n}) · {lang} subtitles', 'item': origin+url}]}]
    return title, description, content, schema
