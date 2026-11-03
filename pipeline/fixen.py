import json,sys
IMG=[
("to maintain the team's trust at its highest.","to keep the team's trust high."),
("Reward not only measures figures, but it also builds trust and strengthens commitment.","Reward doesn't only measure figures; it also builds trust and strengthens commitment."),
("Based on your results, We decided to give you an increase.","Based on your results, we decided to give you a raise."),
("* compa-ratio","* Compa-ratio"),
("within that grade Salaries may vary","within that grade. Salaries may vary"),
("and her performance is exceeded, what","and her performance exceeds expectations, what"),
("closer to the midpoint or minimum range.","closer to the midpoint or the minimum of the range."),
("midpoint; it is appropriate","midpoint, it is appropriate"),
("next","Next"),
("by focusing on evaluation and concrete data","by focusing on performance and concrete data"),
("his performance has been partially met.","his performance has only partially met expectations."),
("That’s why you will get a raise to place you within the parameters of the salary range.","That’s why you will receive a raise that places you within the parameters of the salary range."),
("Give Juan an increase anyway since his results were met, and it doesn't matter that he's still overpaid.","Give Juan an increase anyway, since he met expectations and it doesn't matter that he's still overpaid."),
("Ask Juan to go to another company since he won't be getting an increase in the future.","Ask Juan to move to another company, since he won't receive an increase in the future."),
("Roberto, an experienced employee, after the salary review and according to the policies, it was concluded that he will not receive an increase.","Roberto, an experienced employee: following the salary review and in line with company policies, it was concluded that he will not receive an increase."),
("to continue boosting your development","to continue supporting your development"),
("Commitment, free from bias, competitiveness, and salary grade.","Commitment, free from bias, competitiveness, and pay grade."),
]
SUB=[
("Reward Principles we uphold","Reward principles we uphold"),
("reflect how much we value your efforts but also ensure you feel fairly","reflect how much we value their efforts but also ensure they feel fairly"),
("our human resources are our greatest asset","our people are our greatest asset"),
("maintain the team's trust at its highest.","keep the team's trust high."),
("compensation related to the contribution of payments","pay related to employees' contributions"),
("our compensations are aligned","our compensation is aligned"),
("how much that role is being paid in the market","how much that role is paid in the market"),
("As for the fourth principle, it refers to our awareness of the importance of having clear performance expectations, as this ensures","The fourth principle reflects our awareness of the importance of clear performance expectations, as this ensures"),
("within the same salary grade","within the same pay grade"),
("This way, we all start from the starting line with clarity and confidence.","This way, we all line up at the start with clarity and confidence."),
("By applying the principle of Competitiveness,","By applying the principle of Market Competitiveness,"),
("performance in the past year was partially met according to his evaluation,","performance in the past year only partially met expectations according to his evaluation,"),
("the principle of being Bias-Free,","the principle of being Free from bias,"),
("due to her exceeding performance","due to her performance exceeding expectations"),
("answer the question correctly to boost and move faster.","answer the question correctly to get a boost and move faster."),
("has been a great contribution to the team","has made a great contribution to the team"),
("and, nonetheless, explain that","and also explain that"),
("even without an increase, he still receives a competitive salary, being at the top of his salary range.","even without an increase, he still receives a competitive salary, as he is at the top of his salary range."),
("his salary is competitive to the market","his salary is competitive with the market"),
]
def rep(s,pairs,used):
    for i,(a,b) in enumerate(pairs):
        if a in s: s=s.replace(a,b); used.add(i)
    return s
if __name__=='__main__':
    ui=set();us=set()
    for f in ('en_1_20','en_21_40','en_41_60','en_61_78'):
        d=json.load(open(f+'.json'))
        for n,gs in d.items():
            for g in gs:
                if g['en'] in ('next',): g['en']='Next'; ui.add(8); continue
                g['en']=rep(g['en'],[p for p in IMG if p[0]!='next'],ui) if False else g['en']
        json.dump(d,open(f+'.json','w'),ensure_ascii=False)
