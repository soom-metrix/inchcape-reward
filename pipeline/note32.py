import sys
from PIL import Image,ImageDraw,ImageFont
NOTE={'en':'This table is an illustrative example only.',
'fr':"Ce tableau est présenté à titre d’exemple uniquement.",
'nl':'Deze tabel is slechts een illustratief voorbeeld.',
'el':'Αυτός ο πίνακας είναι μόνο ενδεικτικό παράδειγμα.',
'pl':'Ta tabela jest przykładem ilustrującym zagadnienie.',
'bg':'Тази таблица е само илюстративен пример.',
'lt':'Ši lentelė yra tik iliustracinis pavyzdys.',
'fi':'Tämä taulukko on vain havainnollistava esimerkki.',
'et':'See tabel on ainult illustreeriv näide.',
'lv':'Šī tabula ir tikai ilustratīvs piemērs.'}
def apply(im,L,font='/tmp/claude-0/pdfw/fnt_pl/texgyreadventor-italic.otf'):
    im=im.convert('RGB'); W,H=im.size; k=W/960
    d=ImageDraw.Draw(im)
    x0,x1,y0,y1=605*k,949*k,245*k,271*k
    d.rectangle([x0,y0,x1,y1],fill=(255,255,255))
    size=int(11.5*k); t=NOTE[L]
    while True:
        f=ImageFont.truetype(font,size)
        w=d.textlength(t,font=f)
        if w<=(x1-x0)-12*k or size<8: break
        size-=1
    d.text(((x0+x1)/2,(y0+y1)/2),t,font=f,fill=(70,70,70),anchor='mm')
    return im
if __name__=='__main__':
    L=sys.argv[1]
    p=f'/tmp/claude-0/pdfw/final_{L}/s32.jpg'
    apply(Image.open(p),L).save(p,quality=90)
    print('note ok',L)
