import fitz
NAVY=(17/255,35/255,56/255);YEL=(0.93,0.89,0.0);CY=(0,177/255,223/255)
LANGS=['Español','English','Français','Nederlands','Ελληνικά','Polski','Български','Lietuvių','Suomi','Eesti','Latviešu']
def fix2(p):
    R=fitz.Rect(380,655,1540,860)
    p.add_redact_annot(fitz.Rect(560,690,1500,760))
    p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE,graphics=fitz.PDF_REDACT_LINE_ART_NONE)
    # cubrir botones antiguos con el color del panel
    p.draw_rect(fitz.Rect(480,650,1500,800),color=None,fill=NAVY)
    fa=fitz.Font(fontfile='fnt/texgyreadventor-regular.otf');fd=fitz.Font(fontfile='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    W,H,G=250,52,18;cols=4;rows=[LANGS[0:4],LANGS[4:8],LANGS[8:11]]
    y=660
    for r in rows:
        tot=len(r)*W+(len(r)-1)*G;x=960-tot/2
        for name in r:
            b=fitz.Rect(x,y,x+W,y+H)
            p.draw_rect(b,color=None,fill=YEL)
            p.draw_rect(fitz.Rect(x,y,x+9,y+H),color=None,fill=CY)
            f=fd if name in('Ελληνικά','Български') else fa
            sz=28;tw=f.text_length(name,fontsize=sz)
            tw_=fitz.TextWriter(p.rect)
            tw_.append((x+9+(W-9-tw)/2,y+H/2+sz*0.33),name,font=f,fontsize=sz)
            tw_.write_text(p,color=NAVY)
            x+=W+G
        y+=H+14
