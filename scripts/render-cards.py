"""Render authored profile cards; STATIC=1 produces the still-image fallback."""
from html import escape
from pathlib import Path
import os
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
STATIC = os.getenv('STATIC') == '1'
OUT = ROOT / 'cards' / ('static' if STATIC else '')
OUT.mkdir(parents=True, exist_ok=True)
MOTION = '' if STATIC else '''<style>
.entry { animation: arrive 450ms cubic-bezier(.16,1,.3,1); }
@keyframes arrive { from { opacity: .45; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
@media (prefers-reduced-motion: reduce) { .entry { animation: none; } }
</style>'''

def render(name, title, lines, icon='', banner=False):
    height = 260 if banner else 200
    label = escape(' · '.join([title, *lines]))
    x = 40 if banner else 110
    body = f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{label}</desc>
{MOTION}
<rect x="1" y="1" width="958" height="{height-2}" rx="18" fill="#101115" stroke="#333641" stroke-width="2"/>
<g class="entry" font-family="Arial, Helvetica, sans-serif">
{icon}
<text x="{x}" y="{'83' if banner else '70'}" font-size="{'56' if banner else '36'}" font-weight="700" fill="#F4F4F6">{escape(title)}</text>
'''
    for i,line in enumerate(lines):
        body += f'<text x="{x}" y="{132 + i*43 if banner else 118 + i*36}" font-size="{30 if banner else 28}" fill="{ "#A78BFA" if i == 0 else "#B5B6C2"}">{escape(line)}</text>\n'
    body += '</g></svg>\n'
    ET.fromstring(body)
    assert '<script' not in body and 'href=' not in body and 'infinite' not in body
    assert STATIC or 'prefers-reduced-motion' in body
    (OUT / f'{name}.svg').write_text(body)

icons = {
    'film': '<g fill="none" stroke="#A78BFA" stroke-width="3" stroke-linejoin="round"><rect x="35" y="52" width="48" height="40" rx="5"/><path d="m35 65 48-10M42 54l8 8m8-12 8 8m8-12 7 8M53 74l14 7-14 7z"/></g>',
    'code': '<path d="m49 56-17 17 17 17m21-34 17 17-17 17m-7-40-9 47" fill="none" stroke="#A78BFA" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    'repair': '<g fill="none" stroke="#A78BFA" stroke-width="3"><rect x="44" y="43" width="31" height="56" rx="6"/><path d="M54 91h10M54 51h10"/></g>'
}
copy = {
'en': [('Filmmaking & video editing', ['Stories shaped through cuts, pacing and sound.', 'Cuts · Pacing · Captions · Sound'], 'film'), ('Software development', ['Interfaces and tools grounded in everyday work.', 'React · TypeScript · Supabase · PostgreSQL'], 'code'), ('Phone repair', ['3 years at Oliveira Imports · 1,300+ phones repaired', 'Diagnostics · Repair · Time at the workbench'], 'repair')],

}
for lang,items in copy.items():
    render(f'banner-{lang}', 'kuky', ['André Ribeiro', 'Curiosity turned into creation.'], banner=True)
    for title,lines,key in items:
        render(f'{key}-{lang}',title,lines,icons[key])
assert len(list(OUT.glob('*.svg'))) == 4
print(f'Rendered and checked 4 {"static" if STATIC else "animated"} cards in {OUT}')
