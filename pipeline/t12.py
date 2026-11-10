import fitz,io
from PIL import Image,ImageDraw,ImageFont
FB='/tmp/claude-0/pdfw/fnt_gr/'
def fix12(p,text):
    r=fitz.Rect(930,205,1500,312)
    p.draw_rect(r,color=None,fill=(248/255,248/255,248/255))
    S=3
    import glob
    ff=[f for f in glob.glob('/tmp/claude-0/pdfw/fnt_gr/*Bold*')+glob.glob('/tmp/claude-0/pdfw/fnt_gr/*700*')+['/tmp/claude-0/pdfw/fnt/texgyreadventor-bold.otf']][0]
    f=ImageFont.truetype(ff,120*S)
    img=Image.new('RGBA',(int(f.getlength(text))+40,160*S),(0,0,0,0))
    ImageDraw.Draw(img).text((20,10),text,font=f,fill=(10,10,10,255))
    img=img.crop(img.getbbox())
    tw=min(img.width/S,500);th=min(img.height/S,80)
    k=min(500/(img.width/S),80/(img.height/S),1.0)
    w,h=img.width/S*k,img.height/S*k
    b=io.BytesIO();img.save(b,'PNG')
    cx,cy=1212,259
    p.insert_image(fitz.Rect(cx-w/2,cy-h/2,cx+w/2,cy+h/2),stream=b.getvalue())
