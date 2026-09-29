import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

parser = argparse.ArgumentParser()
parser.add_argument('--allow-draft', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parent
errors = []
class Links(HTMLParser):
    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        for key in ('href', 'src'):
            value = attributes.get(key)
            if not value or value.startswith('#'):
                continue
            url = urlsplit(value)
            if not url.scheme and url.path and not (root / unquote(url.path)).is_file():
                errors.append(f'Kırık dosya bağlantısı: {value}')
for name in ('index.html', 'support.html', 'privacy.html'):
    content = (root / name).read_text()
    if not args.allow_draft and ('{{' in content or '}}' in content):
        errors.append(f'{name}: iletişim ve uygulama sahibi bilgileri yapılandırılmamış; configure.py çalıştırın.')
    if '<html lang="tr">' not in content or 'name="viewport"' not in content:
        errors.append(f'{name}: dil veya mobil görünüm bilgisi eksik.')
    Links().feed(content)
if errors:
    raise SystemExit('\n'.join(errors))
print('Üç sayfanın yerel bağlantıları, dil ve mobil görünüm bilgileri doğrulandı.' + (' Taslak modunda.' if args.allow_draft else ' Yayına hazır yapılandırma.'))
