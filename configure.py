"""Configure only public contact information and GitHub Pages URLs."""
import argparse
import html
import json
from pathlib import Path
import plistlib
import re

parser = argparse.ArgumentParser()
parser.add_argument('--owner', required=True)
parser.add_argument('--repo', required=True)
parser.add_argument('--email', required=True)
parser.add_argument('--operator', required=True)
args = parser.parse_args()
if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,38}', args.owner):
    parser.error('Geçerli bir GitHub kullanıcı/organizasyon adı girin.')
if not re.fullmatch(r'[A-Za-z0-9_.-]+', args.repo) or args.repo in ('.', '..'):
    parser.error('Geçerli bir depo adı girin.')
if not re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', args.email):
    parser.error('Geçerli bir destek e-postası girin.')
if not args.operator.strip():
    parser.error('Uygulama sahibi/veri sorumlusu adı gerekiyor.')
root = Path(__file__).resolve().parent
for template in (root / '.templates').glob('*.html'):
    text = template.read_text()
    for key, value in {'OPERATOR_NAME': args.operator, 'SUPPORT_EMAIL': args.email}.items():
        text = text.replace('{{' + key + '}}', html.escape(value, quote=True))
    (root / template.name).write_text(text)
base = f'https://{args.owner.lower()}.github.io/'
if args.repo.lower() != args.owner.lower() + '.github.io':
    base += args.repo + '/'
links = {'support_url': base + 'support.html', 'privacy_url': base + 'privacy.html', 'marketing_url': base}
(root / 'app-store-links.json').write_text(json.dumps(links, ensure_ascii=False, indent=2) + '\n')
plist = root.parent / 'HemenHemen' / 'Info.plist'
if plist.exists():
    with plist.open('rb') as file:
        info = plistlib.load(file)
    info['SUPPORT_URL'] = links['support_url']
    info['PRIVACY_POLICY_URL'] = links['privacy_url']
    with plist.open('wb') as file:
        plistlib.dump(info, file, sort_keys=False)
print(json.dumps(links, ensure_ascii=False, indent=2))
