import json,sys,re
L=sys.argv[1]
u=json.load(open('uniq_en.json'))
lines=open(f'tr/{L}_img.txt',encoding='utf8').read().split('\n')[:-1]
M=[]
for l in lines:
    if l.startswith('* ') and M: M[-1]+='\n'+l
    else: M.append(l)
M=[m.replace('\\n','\n') for m in M]
assert len(M)==175,len(M)
json.dump({u[i+3]:M[i] for i in range(175)},open(f'tr/{L}_map.json','w'),ensure_ascii=False)
print('ok')
