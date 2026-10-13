"""Practical edition-specific guidance, without inventing subtitle-file observations."""
from released_guides import esc, internal


def render_notes(ep, lang, data):
    n,s=ep['n'],ep['s']
    notes=data.get('reading_notes',{})
    if lang=='Urdu':
        summary=notes.get('urdu_summary','پانچویں قسط کا سرکاری پیش منظر سفارت کاری، دربار کے دباؤ اور شہزادہ مصطفیٰ کے مستقبل پر توجہ دیتا ہے۔ مکمل قسط کا انجام جاری ہونے کے بعد معتبر شواہد کی بنیاد پر شامل کیا جائے گا۔')
        text=f'<h3>Urdu reading summary</h3><p class="urdu-reading" lang="ur" dir="rtl">{esc(summary)}</p><h3>Choose Urdu subtitles, not a dubbed cut</h3><p>Open Season 4 Episode {s}, original Episode {n}, then select <strong>Urdu Subtitles</strong> on Great Nation. The original dialogue is Turkish; the Urdu text is the translation. <strong>Urdu Dubbed</strong> is a separate spoken-audio version, so its episode cuts can differ.</p><p>For released episodes, the Niazi source in the guide is the Urdu edition. If you arrive through a search for Sultan Muhammad Fateh, compare both the season episode and original broadcast number before choosing the player.</p>'
        term_rows=''.join(f'<tr><th scope="row">{esc(term)}</th><td lang="ur" dir="rtl">{esc(urdu)}</td></tr>' for term,urdu,_ in notes.get('terms',[]))
        heading='Terms you may see while following the Urdu edition'
        columns='<th scope="col">Turkish term</th><th scope="col">Urdu reading aid</th>'
    else:
        paragraph=notes.get('english_notes','The upcoming preview centres on diplomacy and Mustafa’s future. It introduces the next conflict rather than documenting the released episode or its ending. Continue from Season 4 Episode 4 / original 87 before moving to Episode 5 / original 88.')
        text=f'<h3>English viewer context</h3><p>{esc(paragraph)}</p><h3>Find the original episode with English captions</h3><p>Look for <strong>Mehmed Fetihler Sultani</strong> or the Turkish spelling <strong>Mehmed: Fetihler Sultanı</strong>. Match Season 4 Episode {s} with original Episode {n}, then choose <strong>English Subtitles</strong> on Great Nation. A page labelled Urdu Subtitles or Urdu Dubbed is another edition.</p><p>For released episodes, the Niazi link in the guide opens the English entry. Keep that subtitle edition as you use the previous and next episode buttons.</p>'
        term_rows=''.join(f'<tr><th scope="row">{esc(term)}</th><td>{esc(meaning)}</td></tr>' for term,_,meaning in notes.get('terms',[]))
        heading='English reading aid for names and terms'
        columns='<th scope="col">Turkish term</th><th scope="col">English context</th>'
    glossary=f'<h3>{heading}</h3><div class="table-wrap"><table class="edition-glossary"><thead><tr>{columns}</tr></thead><tbody>{term_rows}</tbody></table></div><p class="page-note">Editorial reading aids, not quotations from a specific subtitle file. Provider spelling and translation choices can differ.</p>' if term_rows else ''
    return f'<div class="edition-reading-notes">{text}{glossary}{internal("/guides/mehmed-season-4-episode-numbers/","Episode numbering help")}</div>'
