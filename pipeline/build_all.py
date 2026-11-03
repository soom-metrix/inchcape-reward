import sys, json, re, os
sys.path.insert(0,'/tmp/claude-0/pdfw')
import fitz
import replace as R
blocks=json.load(open('blocks.json'))
en={}
for f in ('en_1_20.json','en_21_40.json','en_41_60.json','en_61_78.json'):
    if os.path.exists(f): en.update(json.load(open(f)))
LANGC=os.environ.get('LANGC')
EXTRA={'INITIAL':'INITIAL','MARKET':'MARKET','FINAL':'FINAL','CONG':'CONGRATULATIONS'}
if LANGC:
    _m=json.load(open(f'tr/{LANGC}_map.json'));EXTRA.update(json.load(open(f'tr/{LANGC}_extra.json')))
    for _pg,_gs in en.items():
        for _g in _gs:
            if _g['en'].strip(): _g['en']=_m.get(_g['en'],_g['en'])
SKIP={2,10}
reuse={}
def key(pg,ids): return ' '.join(x['es'] for i in ids for x in blocks[pg] if x['id']==i)
for pg,gs in en.items():
    for g in gs:
        if g['conf']=='ok' and g['en'].strip():
            reuse.setdefault(key(pg,g['ids']),g['en'])
only=[int(x) for x in sys.argv[1:]] or None
report=[]
import t78
import tD
import t2,t10
def n_has78(d,off):
    if off==0 and LANGC: t10.fix10(d[9],EXTRA.get('KIT','EMERGENCY KIT'))
    if off==0: t2.fix2(d[1])
    if off==36:
        t78.fix78(d[41],EXTRA['CONG']); return True
    return False
def make(src,off,dst):
    d=fitz.open(src)
    for i,p in enumerate(d):
        n=off+i+1
        if only and n not in only: continue
        tD.fixD(p)
        if LANGC and n==2 and 'S2_TEXT' in EXTRA:
            bm={b['id']:b for b in blocks['2']}
            R.apply_page(p,n,[dict(bs=[bm[i] for i in ('2.1','2.2','2.3','2.4')],en=None),dict(bs=[dict(bm['2.1'],bbox=[600,445,1420,600])],en=EXTRA['S2_TEXT']),dict(bs=[bm['2.5']],en='<b>'+EXTRA['S2_TITLE']+'</b>')],report)
            continue
        groups=en.get(str(n))
        if groups is None or n in SKIP: continue
        bymap={b['id']:b for b in blocks[str(n)]}
        items=[]
        ids_order=[x['id'] for x in blocks[str(n)]]
        mk=[k for k,x in enumerate(blocks[str(n)]) if any(t in x['es'] for t in ('Continuar','¡Muy bien!','No es la respuesta'))]
        hidden_before=mk[0] if mk else 0
        for g in groups:
            def same_prev(bl):
                for k in (1,2,3):
                    pb=blocks.get(str(n-k),[])
                    if all(any(p['es']==x['es'] and all(abs(p['bbox'][j]-x['bbox'][j])<=3 for j in range(4)) for p in pb) for x in bl): return True
                return False
            gbs=[bymap[i] for i in g['ids'] if i in bymap]
            if (mk or n==72) and gbs and all(x['bbox'][1]>100 and not any(t in x['es'] for t in ('Continuar','¡Muy bien!','No es la respuesta')) for x in gbs) and same_prev(gbs):
                items.append(dict(bs=gbs,en=None)); continue
            if mk and (g['conf']=='missing' or not g['en'].strip()):
                bs=[bymap[i] for i in g['ids'] if i in bymap]
                if bs: items.append(dict(bs=bs,en=None))
                continue
            if (g['conf']=='missing' or not g['en'].strip()) and key(str(n),g['ids']) in reuse:
                g=dict(g,en=reuse[key(str(n),g['ids'])],conf='ok'); report.append((n,'REUSED',g['ids'],g['en']))
            if g['conf']=='missing' or not g['en'].strip():
                report.append((n,'MISSING',g['ids'],[bymap[i]['es'] for i in g['ids'] if i in bymap])); continue
            if g['conf']=='uncertain': report.append((n,'UNCERTAIN',g['ids'],g['en'],g.get('note','')))
            bs=[bymap[i] for i in g['ids'] if i in bymap]
            if not bs: continue
            plain=lambda t: re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',t)).strip().lower()
            if plain(g['en'])==plain(' '.join(x['es'] for x in bs)): continue
            if n==72 and g['ids']==['72.11','72.12']:
                items.append(dict(bs=[dict(bs[0],bbox=[330,236,1700,276])],en=g['en'])); items.append(dict(bs=bs[1:],en=None)); continue
            if n==31 and g['ids']==['31.9']:
                for t,bb in ((EXTRA.get('MIN','Minimum'),[1170,161,1340,181]),(EXTRA.get('MAX','Maximum'),[1710,161,1880,181])):
                    items.append(dict(bs=[dict(bs[0],bbox=bb)],en=t))
                continue
            if n==31 and g['ids']==['31.7']:
                items.append(dict(bs=[dict(bs[0],bbox=[1440,161,1610,181])],en=g['en'])); continue
            if n==31 and g['ids']==['31.8']:
                for t,bb in ((f"<b>{EXTRA['INITIAL']}</b>",[1228,243,1335,272]),(f"<b>{EXTRA['MARKET']}</b>",[1452,243,1600,272]),(f"<b>{EXTRA['FINAL']}</b>",[1735,243,1822,272])):
                    items.append(dict(bs=[dict(bs[0],bbox=bb)],en=t))
                continue
            if n==34 and g['ids']==['34.3']:
                _k=EXTRA.get('S34','Salaries');en1,en2=g['en'].split(' '+_k+' ',1)
                items.append(dict(bs=[dict(bs[0],bbox=[52,687,591,809])],en=en1.strip()))
                items.append(dict(bs=[dict(bs[0],bbox=[1219,761,1848,882])],en=_k+' '+en2))
                continue
            items.append(dict(bs=bs,en=g['en']))
        R.apply_page(p,n,items,report)
        if n==32:
            ens={}
            for g in groups:
                if len(g['ids'])==1: ens[g['ids'][0]]=g['en']
            m=re.match(r'<b>(.*?)</b>\s*(.*)',ens['32.4'],re.S)
            perf,below=m.group(1).strip(),m.group(2).strip()
            cells=[([1425,255,1549,296],below),([1555,255,1656,296],ens['32.9']),([1662,255,1762,296],ens['32.10']),([1768,255,1868,296],ens['32.11'])]
            p.add_redact_annot(fitz.Rect(1258,258,1415,307),fill=(211/255,252/255,1))
            for r_,t_ in cells: p.add_redact_annot(fitz.Rect(r_),fill=(14/255,184/255,228/255))
            p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
            css=R.CSS_FACES+"body{font-family:Adv;color:#000;margin:0;padding:0;text-align:center;line-height:1.1}"
            p.insert_htmlbox(fitz.Rect(1262,266,1412,300),f"<div style='font-size:17.8pt;font-weight:bold'>{perf}</div>",css=css,archive=R.ARC,scale_low=0.4)
            for r_,t_ in cells:
                rr=fitz.Rect(r_);rr.y0+=2
                p.insert_htmlbox(rr,f"<div style='font-size:12.7pt'>{t_.replace('<b>','').replace('</b>','')}</div>",css=css+"body{display:flex}",archive=R.ARC,scale_low=0.4)
    if n_has78(d,off): pass
    d.save(dst,garbage=3,deflate=True)
    return d
