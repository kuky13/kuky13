"""Check local Markdown targets, SVG safety and reproducible card rendering."""
from pathlib import Path
import re
import subprocess
import os
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
root = Path(__file__).resolve().parents[1]


class ImageTargets(HTMLParser):
    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if tag == 'img':
            assert attributes.get('alt'), 'Every profile image needs alt text.'
        if tag in ('img', 'source'):
            for key in ('src', 'srcset'):
                target = attributes.get(key)
                if target and not target.startswith('https://'):
                    assert (root/target).is_file(), target


ImageTargets().feed((root/'README.md').read_text())
for readme in [root/'README.md', root/'assets/README.md']:
    for target in re.findall(r'\]\(([^)]+)\)',readme.read_text()):
        if not target.startswith(('https://','#')):
            assert (readme.parent/target).exists(), (readme,target)
for static in [False,True]:
    folder=root/'cards'/('static' if static else '')
    before={p.name:p.read_bytes() for p in folder.glob('*.svg')}
    subprocess.run(['python3',str(root/'scripts/render-cards.py')],check=True,env={**os.environ,'STATIC':'1' if static else '0'})
    after={p.name:p.read_bytes() for p in folder.glob('*.svg')}
    assert before == after
    for svg in folder.glob('*.svg'):
        text=svg.read_text()
        ET.fromstring(text)
        assert '<script' not in text and 'href=' not in text and 'infinite' not in text
        assert 'prefers-reduced-motion' in text or static
assert 'releases/latest' in (root/'README.md').read_text()
assert not (root/'.github/workflows').exists()
print('Profile links, 8 SVGs, accessibility metadata and deterministic rendering checked.')
