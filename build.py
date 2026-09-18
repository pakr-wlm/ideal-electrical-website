"""Inline styles.css and assets (base64) into a single self-contained index.html."""
import base64, re
MIME = {'jpg': 'image/jpeg', 'png': 'image/png'}
def data(path):
    return 'data:' + MIME[path.rsplit('.', 1)[1]] + ';base64,' + base64.b64encode(open(path, 'rb').read()).decode()

html = open('index.src.html', encoding='utf8').read()
css = open('styles.css', encoding='utf8').read()
css = re.sub(r'url\("(assets/[^"]+)"\)', lambda m: 'url("' + data(m.group(1)) + '")', css)
html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + css + '\n</style>')
html = re.sub(r'src="(assets/[^"]+\.(?:jpg|png))"', lambda m: 'src="' + data(m.group(1)) + '"', html)
open('index.html', 'w', encoding='utf8').write(html)
print(len(html) // 1024, 'KB')
