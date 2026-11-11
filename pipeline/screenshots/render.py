import sys; sys.path.insert(0,'/tmp/claude-0/shots')
from PIL import Image, ImageDraw, ImageFont
from collections import Counter
from specs import S68,M68,S72
from trs import T,K68,K72,FIL,CAN,FUL,AWD
FR='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
import os
if not os.path.exists(FR):
    import glob;FR=glob.glob('/usr/share/fonts/**/LiberationSans-Regular.ttf',recursive=True)[0];FB=FR.replace('Regular','Bold')
def font(b,s): return ImageFont.truetype(FB if b else FR,s)
def width(t,b,s): return font(b,s).getlength(t)
def calib(en,b,ow):
    lo,hi=6,60
    while hi-lo>0.5:
        m=(lo+hi)/2
        if width(en,b,m)>ow: hi=m
        else: lo=m
    return lo
def colors(im,box):
    c=im.crop(box).convert('RGB');px=list(c.getdata());bg=Counter(px).most_common(1)[0][0]
    d=sorted(px,key=lambda p:-sum(abs(p[i]-bg[i]) for i in range(3)))
    n=max(3,len(d)//40);top=d[:n];fg=tuple(sum(p[i] for p in top)//n for i in range(3))
    return bg,fg
def fit(t,b,s0,maxw):
    s=s0
    while width(t,b,s)>maxw and s>s0*0.65: s-=0.5
    return s
def draw_one(im,d,sp,txt,orig):
    y0,y1=sp['y'];b=sp['bold'];s0=calib(*sp['szref'][:1],b,sp['szref'][1]) if 'szref' in sp else calib(sp['en'],b,sp['ow'])
    al=sp.get('align','l')
    if 'cover' in sp: cx0,cx1=sp['cover']
    else: cx0,cx1=sp['x']-2,sp['x']+sp['ow']+3
    bg,fg=colors(orig,(cx0,y0,cx1,y1))
    if sp.get('chip'): bg=orig.getpixel((1140,y0+3)) if False else Counter(list(orig.crop((1140,y0+4,1160,y1-4)).convert('RGB').getdata())).most_common(1)[0][0]
    maxw=sp.get('maxw') or ((sp['rx']-sp.get('lim',60)) if 'rx' in sp else (sp['lim']-sp['x']))
    s=fit(txt,b,s0,maxw);f=font(b,s);w=f.getlength(txt)
    val=sp.get('value');vw=0
    if val: 
        vf=font(sp.get('vbold',0),s);vw=vf.getlength(val)+7
    if al=='l': x=sp['x'];ex1=max(cx1,x+w+vw+3)
    elif al=='c': x=sp['cx']-w/2;ex1=max(cx1,x+w+3)
    else: x=sp['rx']-w;ex1=cx1
    ex0=min(cx0,x-2)
    d.rectangle([ex0,y0,ex1,y1],fill=bg)
    ym=(y0+y1)/2
    if 'clipx' in sp:
        tmp=Image.new('RGB',(int(ex1-ex0)+2,y1-y0),bg);td=ImageDraw.Draw(tmp);td.text((x-ex0,ym-y0),txt,font=f,fill=fg,anchor='lm')
        tmp=tmp.crop((int(sp['clipx']-ex0),0,tmp.width,tmp.height));im.paste(tmp,(int(sp['clipx']),y0));return
    d.text((x,ym),txt,font=f,fill=fg,anchor='lm')
    if val: d.text((x+w+7,ym),val,font=vf,fill=colors(orig,(sp['x']+sp['ow']+4,y0,cx1,y1))[1] if False else fg,anchor='lm')
def draw_multi(im,d,orig,sp,lines):
    b=sp['bold']
    cv=sp['cover']
    for ((y0,y1),en,ow,*rest),txt in zip(sp['lines'],lines):
        s0=calib(en,b,ow)
        if rest: cx,maxw=rest
        else: cx,maxw=sp['cx'],sp['maxw']
        cvx0,cvx1=(cv[0],cv[1]) if (y0,y1)==sp['lines'][1][0] else (sp.get('cover1',cv)[0],sp.get('cover1',cv)[1])
        bg,fg=colors(orig,(cvx0,y0,cvx1,y1))
        s=fit(txt,b,s0,maxw);f=font(b,s);w=f.getlength(txt)
        d.rectangle([min(cvx0,cx-w/2-2),y0-1,max(cvx1,cx+w/2+2) if cvx1<1100 or True else cvx1,y1+1],fill=bg) if False else d.rectangle([cvx0,y0-1,cvx1,y1+1],fill=bg)
        d.text((cx,(y0+y1)/2),txt,font=f,fill=fg,anchor='mm')
def render(L,n,raw):
    orig=Image.open(raw).convert('RGB');im=orig.copy();d=ImageDraw.Draw(im)
    boxes=[]
    if n==68:
        tr=dict(zip(K68,T[L][0]));tr['filters']=FIL[L];tr['canedit']=CAN[L];tr['fullname']=FUL[L]
        for k,sp in S68.items():
            key={'aligned1':'aligned','aligned2':'aligned'}.get(k,k)
            draw_one(im,d,sp,tr[key],orig)
        for k,sp in M68.items():
            draw_multi(im,d,orig,sp,tr[k])
    else:
        tr=dict(zip(K72,T[L][1]));tr['award']=AWD[L]
        for k,sp in S72.items(): draw_one(im,d,sp,tr[k],orig)
    return orig,im
if __name__=='__main__':
    L=sys.argv[1]
    for n in (68,72):
        o,i=render(L,n,f'/tmp/claude-0/shots/raw{n}.png');i.save(f'/tmp/claude-0/shots/{L}_{n}.png')
