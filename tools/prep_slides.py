import re, json, base64, io
from PIL import Image
md = open('/tmp/claude-0/x/d.md', encoding='utf-8').read()
parts = re.split(r'(!\[[^\]]*\]\(media/(image\d+)\.png\)(?:\{[^}]*\})?)', md)
# parts: [pre, full, name, text, full, name, text...]
slides = []
i = 1
while i < len(parts):
    name = parts[i+1]; text = parts[i+2] if i+2 < len(parts) else ''
    i += 3
    t = text.strip()
    t = re.sub(r'^\*\*Subtitle:\*\*\s*', '', t)
    t = re.sub(r'^Subtitle:\s*', '', t)
    t = t.replace('\\\n', '\n').replace("\\'", "'").replace('\\"','"')
    t = re.sub(r'^\*+|\*+$', '', t.strip()).strip()
    t = re.sub(r'\s*\n\s*(?=[A-Z])', '\n', t) if False else t
    t = re.sub(r'[ \t]*\n[ \t]*', '\n', t)
    slides.append({'file': name, 'en': t})
print(len(slides))
out = []
for n, s in enumerate(slides, 1):
    im = Image.open(f"/tmp/claude-0/x/d/word/media/{s['file']}.png").convert('RGB')
    w = 960; h = round(im.height * w / im.width)
    im = im.resize((w, h), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=68, optimize=True, progressive=True)
    out.append({'n': n, 'img': 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode(), 'en': s['en'], 'w': w, 'h': h})
json.dump(out, open('/home/claude/build/slides.json', 'w'), ensure_ascii=False)
print(sum(len(o['img']) for o in out)/1e6, 'MB')
print(set((o['w'],o['h']) for o in out))
for o in out[:5]+out[-3:]: print(o['n'], repr(o['en'][:90]))
