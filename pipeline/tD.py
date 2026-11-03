import fitz,os
FD='/tmp/claude-0/pdfw/fnt/texgyreadventor-bold.otf'
def fixD(p):
    hits=[]
    for b in p.get_text('dict')['blocks']:
        if b['type']!=0: continue
        for l in b['lines']:
            for s in l['spans']:
                if s['text'].strip()=='C' and 765<s['bbox'][1]<780: hits.append(s)
    for s in hits:
        x0,y0,x1,y1=s['bbox']
        pm=p.get_pixmap(clip=fitz.Rect(x0-8,y0+12,x0-4,y1-12),alpha=False)
        n=pm.width*pm.height
        px=[pm.pixel(i%pm.width,i//pm.width) for i in range(n)]
        col=tuple(sorted(c[k] for c in px)[len(px)//2] for k in range(3)) if False else tuple(sorted(c[k] for c in px)[len(px)//2]/255 for k in range(3))
        r=fitz.Rect(x0-1,y0,x1+1,y1)
        p.add_redact_annot(r,fill=col)
        p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
        f=fitz.Font(fontfile=FD)
        p.insert_font(fontname='advB',fontfile=FD)
        w=f.text_length('D',fontsize=s['size'])
        cx=(x0+x1)/2
        p.insert_text(fitz.Point(cx-w/2,s['origin'][1]),'D',fontname='advB',fontsize=s['size'],color=(0,0,0))
