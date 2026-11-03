import json,base64,os,shutil,re
PD='/tmp/claude-0/pdfw';B='/home/claude/build'
langs=['fr','nl','el','pl','bg','lt','fi','et','lv']
for L in langs:
    os.makedirs(f'{B}/{L}',exist_ok=True)
    pack={}
    for n in range(1,79):
        src=f'{PD}/final_{L}/s{n:02d}.jpg'
        d=open(src,'rb').read()
        pack[str(n)]='data:image/jpeg;base64,'+base64.b64encode(d).decode()
    json.dump(pack,open(f'{B}/{L}/pack.json','w'))
tr={L:json.load(open(f'{PD}/tr/{L}_sub.json',encoding='utf8')) for L in langs}
p=f'{B}/Inchcape_Reward_Review.html';s=open(p,encoding='utf-8').read()
i=s.index('const TR  = ');j=s.index('\n',i)
old=s[i:j]
order=re.findall(r'[,{](\w\w):\{"3"',old);print(order)
s=s[:i]+'const TR  = '+json.dumps({L:tr[L] for L in order},ensure_ascii=False)+';'+s[j:]
open(p,'w',encoding='utf-8').write(s);print('ok')
