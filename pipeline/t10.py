import os
FNT='fnt_gr' if os.environ.get('LANGC') in ('el','bg') else 'fnt_pl' if os.environ.get('LANGC') in ('pl','lt','lv') else 'fnt'
import fitz,io
from PIL import Image,ImageDraw,ImageFont
def fix10(p,text):
    cx,cy=1522.5,418.5
    p.add_redact_annot(fitz.Rect(1420,368,1625,468))
    p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE,graphics=fitz.PDF_REDACT_LINE_ART_NONE)
    S=4;W,H=int(200*S),int(60*S)
    f=ImageFont.truetype(FNT+'/Jost-700-Italic.ttf',int(46*S))
    tw=f.getlength(text)
    # condensar horizontalmente para ajustar a ~185 pt
    img=Image.new('RGBA',(int(tw)+20,int(60*S)),(0,0,0,0))
    ImageDraw.Draw(img).text((10,int(4*S)),text,font=f,fill=(10,10,10,255))
    bb=img.getbbox();img=img.crop(bb)
    tgt_w=int(180*S);tgt_h=int(min(34*S,img.height))
    img=img.resize((tgt_w,tgt_h),Image.LANCZOS)
    img=img.rotate(14,expand=True,resample=Image.BICUBIC)
    buf=io.BytesIO();img.save(buf,'PNG')
    w=img.width/S;h=img.height/S
    p.insert_image(fitz.Rect(cx-w/2,cy-h/2,cx+w/2,cy+h/2),stream=buf.getvalue())
