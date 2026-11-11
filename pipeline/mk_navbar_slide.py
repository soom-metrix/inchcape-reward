from PIL import Image, ImageDraw, ImageFont
S=960/742
src=Image.open('/tmp/claude-0/nav/base.png').convert('RGB')
base=src.resize((960,540),Image.LANCZOS)
base.save('base.png')
base.convert('RGB').save('en.jpg',quality=72)
P='/tmp/claude-0/pdfw/'
FD={'fr':'fnt','nl':'fnt','fi':'fnt','et':'fnt','el':'fnt_gr','bg':'fnt_gr','pl':'fnt_pl','lt':'fnt_pl','lv':'fnt_pl'}
T={'fr':['Sous-titres','Retour','Arrêter','Lecture','Suivant'],
'nl':['Ondertitels','Terug','Stop','Afspelen','Volgende'],
'el':['Υπότιτλοι','Πίσω','Στοπ','Αναπαραγωγή','Επόμενο'],
'pl':['Napisy','Wstecz','Zatrzymaj','Odtwórz','Dalej'],
'bg':['Субтитри','Назад','Стоп','Пусни','Напред'],
'lt':['Subtitrai','Atgal','Stabdyti','Leisti','Toliau'],
'fi':['Tekstitys','Takaisin','Pysäytä','Toista','Seuraava'],
'et':['Subtiitrid','Tagasi','Peata','Esita','Edasi'],
'lv':['Subtitri','Atpakaļ','Apturēt','Atskaņot','Tālāk']}
tags=[(14,76),(481,542),(544,603),(606,666),(669,731)]
FILL=(17,36,56)
K=4
for L,labels in T.items():
    im=base.copy()
    fp=P+FD[L]+'/texgyreadventor-bold.otf'
    for (a,b),txt in zip(tags,labels):
        x0=round((a+3)*S);x1=round((b-2)*S);y0=round(361*S);y1=round(374*S)
        d=ImageDraw.Draw(im);d.rectangle([x0,y0,x1,y1],fill=FILL)
        w=x1-x0;h=y1-y0
        size=13*K
        while True:
            f=ImageFont.truetype(fp,size)
            bb=f.getbbox(txt)
            if bb[2]-bb[0]<=(w-4)*K or size<=6*K: break
            size-=1
        patch=Image.new('RGB',(w*K,h*K),FILL);pd=ImageDraw.Draw(patch)
        bb=f.getbbox(txt)
        # center using x-height-ish: use cap bbox of 'H'
        hb=f.getbbox('H')
        px=(w*K-(bb[2]-bb[0]))//2-bb[0]
        py=(h*K-(hb[3]-hb[1]))//2-hb[1]
        pd.text((px,py),txt,font=f,fill=(255,255,255))
        im.paste(patch.resize((w,h),Image.LANCZOS),(x0,y0))
    im.save(f'{L}.jpg',quality=72)
print('ok')
