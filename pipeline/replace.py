import fitz, sys, json, re
import os
FD='/tmp/claude-0/pdfw/'+('fnt_gr' if os.environ.get('LANGC') in ('el','bg') else 'fnt_pl' if os.environ.get('LANGC') in ('pl','lt','lv') else 'fnt')
ARC=fitz.Archive(FD)
CSS_FACES='''
@font-face{font-family:Adv;src:url(texgyreadventor-regular.otf);}
@font-face{font-family:Adv;font-weight:bold;src:url(texgyreadventor-bold.otf);}
@font-face{font-family:Adv;font-style:italic;src:url(texgyreadventor-italic.otf);}
@font-face{font-family:Jost;font-weight:bold;font-style:italic;src:url(Jost-700-Italic.ttf);}
'''
def hexc(c): return '#%06x'%c

def spans_of(page):
    out=[]
    for b in page.get_text('dict')['blocks']:
        if b['type']!=0: continue
        for l in b['lines']:
            for s in l['spans']:
                out.append(s)
    return out

def run(src, dst, pages):
    d=fitz.open(src)
    for pno, items in pages.items():
        page=d[pno-1]
        sp=[s for s in spans_of(page) if s['text'].strip() and 'consectetuer' not in s['text'] and not s['text'].strip().startswith(('Lorem','euismod','ipsum'))]
        plan=[]
        for it in items:
            keys=[k.strip() for k in it['es']]
            found=[s for s in sp if s['text'].strip() in keys]
            if len(set(s['text'].strip() for s in found))!=len(set(keys)):
                miss=set(keys)-set(s['text'].strip() for s in found)
                print(f'  p{pno}: NOT FOUND {miss}')
            if not found: continue
            r=fitz.Rect(found[0]['bbox'])
            for s in found[1:]: r|=fitz.Rect(s['bbox'])
            s0=found[0]
            raw=sorted(s['bbox'][1] for s in found); ys=[]
            for y in raw:
                if not ys or y-ys[-1]>8: ys.append(y)
            pitch=(ys[-1]-ys[0])/(len(ys)-1) if len(ys)>1 else s0['size']*1.25
            plan.append((it,found,r,s0,pitch))
            for s in found: page.add_redact_annot(fitz.Rect(s['bbox'])+(-1,-1,1,1))
        for s in sp:
            if s['text'].strip()=='a' and 1620<s['bbox'][0]<1632 and 520<s['bbox'][1]<530: page.add_redact_annot(fitz.Rect(s['bbox'])+(-1,-1,1,1))
        page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE, graphics=fitz.PDF_REDACT_LINE_ART_NONE)
        for it,found,r,s0,pitch in plan:
            padx=it.get('padx',0.08)*r.width
            if 'x0' in it: r.x0=it['x0']
            box=fitz.Rect(r.x0-padx, r.y0-2, r.x1+padx, r.y1+2)
            title='Jost' if 'Futura' in s0['font'] and 'Bold' in s0['font'] else 'Adv'
            size=it.get('size', s0['size'])
            col=it.get('color', hexc(s0['color']))
            css=CSS_FACES+f"body{{font-family:{title};font-size:{size}pt;color:{col};text-align:{it.get('align','center')};line-height:{it.get('lh', pitch)}pt;margin:0;padding:0}} b{{font-weight:bold}}"
            if title=='Jost': css+=" body{font-weight:bold;font-style:italic}"
            html=it['en']
            # measure to vertically center within the original block
            tmp=fitz.open(); tp=tmp.new_page(width=page.rect.width,height=page.rect.height)
            spare,scale=tp.insert_htmlbox(box,html,css=css,archive=ARC,scale_low=0.5)
            tmp.close()
            dy=0
            if spare>0 and it.get('vcenter',True): dy=spare/2 if scale==1 else 0
            if spare<0:
                print(f'  p{pno}: OVERFLOW {it["en"][:40]!r}')
            box2=fitz.Rect(box.x0,box.y0+dy,box.x1,box.y1+dy)
            page.insert_htmlbox(box2,html,css=css,archive=ARC,scale_low=0.5)
    d.save(dst, garbage=3, deflate=True)
    return d


def apply_page(page,n,items,report):
    allspans=[s for s in spans_of(page) if s['text'].strip()]
    plan=[]
    for it in items:
        rect=fitz.Rect(it['bs'][0]['bbox'])
        for b in it['bs'][1:]: rect|=fitz.Rect(b['bbox'])
        found=[s for s in allspans if fitz.Rect(s['bbox']).intersects(rect+(-1,-1,1,1)) and (fitz.Rect(s['bbox'])&rect).get_area()>0.85*fitz.Rect(s['bbox']).get_area() and 'consectetuer' not in s['text'] and not s['text'].strip().startswith(('Lorem','euismod','ipsum'))]
        sizes=[b['size'] for b in it['bs'] if 'size' in b]
        if sizes:
            f2=[s for s in found if any(abs(s['size']-z)/z<0.03 for z in sizes)]
            if f2: found=f2
        if not found: continue
        r=fitz.Rect(found[0]['bbox'])
        for s in found[1:]: r|=fitz.Rect(s['bbox'])
        s0=found[0]
        raw=sorted(s['bbox'][1] for s in found); ys=[]
        for y in raw:
            if not ys or y-ys[-1]>8: ys.append(y)
        pitch=(ys[-1]-ys[0])/(len(ys)-1) if len(ys)>1 else s0['size']*1.25
        # alignment: centered if line centers align, else left
        cx=[ (s['bbox'][0]+s['bbox'][2])/2 for s in found]
        x0s=[s['bbox'][0] for s in found]
        align='center' if (len(found)>1 and max(cx)-min(cx)<12 and max(x0s)-min(x0s)>12) else ('left' if len(found)>1 and max(x0s)-min(x0s)<12 else 'center')
        if len(found)==1 or len(ys)==1: align='left' if s0['bbox'][0]<60 or 'Italic' in s0['font'] and r.x0<500 else 'center'
        plan.append((it,found,r,s0,pitch,align) if it['en'] is not None else None)
        for s in found: page.add_redact_annot(fitz.Rect(s['bbox'])+(-1,-1,1,1))
    for s in allspans:
        if s['text'].strip()=='a' and 1620<s['bbox'][0]<1632 and 520<s['bbox'][1]<530: page.add_redact_annot(fitz.Rect(s['bbox'])+(-1,-1,1,1))
    page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE, graphics=fitz.PDF_REDACT_LINE_ART_NONE)
    for pl in plan:
        if pl is None: continue
        it,found,r,s0,pitch,align=pl
        fn=s0['font']
        padx=0.0 if ('Futura' in fn and ('Bold' in fn or 'Black' in fn)) else 0.06*r.width
        box=fitz.Rect(r.x0-padx, r.y0-2, r.x1+padx, r.y1+2)
        title='Jost' if ('Futura' in fn or 'ChunkFive' in fn) and ('Bold' in fn or 'Black' in fn) else 'Adv'
        size0=s0['size']; col=hexc(s0['color'])
        if title=='Jost':
            import re as _re
            _f=fitz.Font(fontfile=FD+'/Jost-700-Italic.ttf'); _t=_re.sub(r'<[^>]+>','',it['en'])
            _w=_f.text_length(_t,fontsize=size0)
            if _w>box.width*0.92: size0=size0*box.width*0.92/_w
        html=it['en']
        def css_for(sz,al=None):
            al=al or align
            c=CSS_FACES+f"body{{font-family:{title};font-size:{sz}pt;color:{col};text-align:{al};line-height:{pitch*sz/size0}pt;margin:0;padding:0}} b{{font-weight:bold}}"
            if title=='Jost': c+=" body{font-weight:bold;font-style:italic}"
            return c
        tmp=fitz.open(); tp=tmp.new_page(width=page.rect.width,height=page.rect.height)
        best=None
        single = len(set(round(s_['bbox'][1]/8) for s_ in found))==1
        variants=[(box,align)]
        if single:
            variants.append((fitz.Rect(r.x0-2,box.y0,min(1900,r.x1+0.6*r.width+padx),box.y1),'left'))
        best=None
        for vbox,valign in variants:
            for extra in ((0,) if title=='Jost' else (0,0.6,1.0)):
                b2=fitz.Rect(vbox.x0,vbox.y0,vbox.x1,vbox.y1+pitch*extra)
                sz=size0; ok=False
                while sz>=size0*0.5:
                    sp,sc=tp.insert_htmlbox(b2,html,css=css_for(sz,valign),archive=ARC,scale_low=1)
                    if sp>=0: ok=True; break
                    sz*=0.95
                if not ok: continue
                cand=(sz/size0,extra,b2,sz,sp,valign)
                if best is None or cand[0]>best[0]+0.02: best=cand
                if cand[0]>=0.97: break
            if best is not None and best[0]>=0.97: break
        tmp.close()
        if best is None:
            report.append((n,'OVERFLOW',it['en'][:50])); continue
        ratio,extra,b2,sz,sp,valign=best
        dy=sp/2 if sp>0 else 0
        page.insert_htmlbox(fitz.Rect(b2.x0,b2.y0+dy,b2.x1,b2.y1+dy),html,css=css_for(sz,valign),archive=ARC,scale_low=1)
        if ratio<0.8: report.append((n,'SMALL',round(ratio,2),it['en'][:50]))
