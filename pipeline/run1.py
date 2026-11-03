import sys; sys.argv=[sys.argv[0]]+sys.argv[1:]
exec(open('build_all.py').read())
d=make('es.pdf',0,'en_part1.pdf')
os.makedirs('out',exist_ok=True)
for i,p in enumerate(d):
    n=i+1
    if only and n not in only: continue
    p.get_pixmap(matrix=fitz.Matrix(0.5,0.5)).save(f'out/e{n:02d}.png')
for r in report: print(r)
