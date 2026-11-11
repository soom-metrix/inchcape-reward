import sys; sys.path.insert(0,'/tmp/claude-0/shots')
from PIL import Image, ImageChops, ImageFilter
import render
RECT={68:(72.08538,422.00003,1132.99988,895.01337),72:(282.0,371.00003,1672.0,830.8123)}
def apply(L):
    for n,(x0,y0,x1,y1) in RECT.items():
        o,t=render.render(L,n,f'/tmp/claude-0/shots/raw{n}.png')
        X0,Y0,W,H=round(x0/2),round(y0/2),round((x1-x0)/2),round((y1-y0)/2)
        orr=o.resize((W,H),Image.LANCZOS);tr=t.resize((W,H),Image.LANCZOS)
        diff=ImageChops.difference(orr,tr).convert('L').point(lambda v:255 if v>10 else 0).filter(ImageFilter.MaxFilter(7))
        p=f'/tmp/claude-0/pdfw/final_{L}/s{n:02d}.jpg'
        base=Image.open(p).convert('RGB')
        base.paste(tr,(X0,Y0),diff)
        base.save(p,quality=72)
if __name__=='__main__':
    for L in sys.argv[1:]: apply(L); print('ok',L)
