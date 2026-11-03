import os
FNT='fnt_gr' if os.environ.get('LANGC') in ('el','bg') else 'fnt_pl' if os.environ.get('LANGC') in ('pl','lt','lv') else 'fnt'
import fitz,io
from PIL import Image,ImageDraw,ImageFont
def fix78(p,title='CONGRATULATIONS'):
    import numpy as np
    Z=2;P=fitz.Rect(90,696,1110,808)
    pm=p.get_pixmap(matrix=fitz.Matrix(Z,Z),clip=P,alpha=False)
    a=np.frombuffer(pm.samples,np.uint8).reshape(pm.height,pm.width,3).astype(float)
    t,bt=a[2].copy(),a[-3].copy()
    h=a.shape[0]
    for y in range(h):
        u=y/(h-1);a[y]=t*(1-u)+bt*u
    # smooth horizontally to avoid streaks
    from PIL import Image as I
    im=I.fromarray(a.astype(np.uint8));buf0=io.BytesIO();im.save(buf0,'PNG')
    p.insert_image(P,stream=buf0.getvalue())
    S=3;W,H=1000*S,110*S
    f=ImageFont.truetype(FNT+'/Jost-800-Italic.ttf',int(104*S))
    t=title
    while f.getlength(t)>W-30*S: f=ImageFont.truetype(FNT+'/Jost-800-Italic.ttf',int(f.size*0.97))
    bb=f.getbbox(t);tw=bb[2]-bb[0]
    mask=Image.new('L',(W,H),0);ImageDraw.Draw(mask).text((10*S-bb[0],(H-(bb[3]-bb[1]))//2-bb[1]),t,font=f,fill=255)
    out=Image.new('RGBA',(W,H),(0,0,0,0))
    sh=Image.new('RGBA',(W,H),(0,35,58,255));out.paste(sh,(6*S,6*S),mask)
    grad=Image.new('RGBA',(W,H));px=grad.load()
    for x in range(W):
        u=x/W
        c=(int(70+u*170),int(205+u*30),int(150-u*110),255)
        for y in range(H):px[x,y]=c
    out.paste(grad,(0,0),mask)
    buf=io.BytesIO();out.save(buf,'PNG')
    p.insert_image(fitz.Rect(100,697,1100,807),stream=buf.getvalue())
