exec(open('build_all.py').read())
d1=make('es.pdf',0,('en_part1.pdf' if not LANGC else f'{LANGC}_part1.pdf')); d2=make('es2.pdf',36,('en_part2.pdf' if not LANGC else f'{LANGC}_part2.pdf'))
OUT='final'+('_'+LANGC if LANGC else '');os.makedirs(OUT,exist_ok=True)
from PIL import Image
for off,d in ((0,d1),(36,d2)):
    for i,p in enumerate(d):
        n=off+i+1
        pix=p.get_pixmap(matrix=fitz.Matrix(960/1920,960/1920))
        Image.frombytes('RGB',[pix.width,pix.height],pix.samples).save(f'{OUT}/s{n:02d}.jpg',quality=72,optimize=True,progressive=True)
json.dump([list(map(str,r)) for r in report],open('report.json','w'),ensure_ascii=False)
from collections import Counter
print(Counter(r[1] for r in report))
for r in report:
    if r[1] in ('OVERFLOW',): print(r)
