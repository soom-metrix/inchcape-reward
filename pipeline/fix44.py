import fitz
FD='/tmp/claude-0/pdfw/fnt/texgyreadventor-bold.otf'
def fix44(p):
    f=fitz.Font(fontfile=FD);p.insert_font(fontname='advB44',fontfile=FD)
    w=f.text_length('120%',fontsize=35)
    p.insert_text(fitz.Point(1225.5-w/2,668.4),'120%',fontname='advB44',fontsize=35,color=(0,0,0))
