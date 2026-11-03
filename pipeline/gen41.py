import json
T="Salary review process"
P2="<b>Part 2: Avoiding Bias in Evaluation</b>"
P3="<b>Part 3: Transparent and Clear Communication</b>"
P31="<b>Part 3.1: Transparent, Clear, and Precise Communication</b>"
D3="Develop skills to communicate salary decisions accurately and empathetically, fostering trust."
D2a="Identify and prevent common biases in salary decision-making by focusing on evaluation and concrete data."
D2b="Identify and prevent common biases in salary decision-making by focusing on performance and concrete data."
def g(ids,en,conf="ok",note=None):
    d={"ids":ids,"en":en,"conf":conf}
    if note:d["note"]=note
    return d
def m(ids,note):return g(ids,"","missing",note)
N46="no English overlay on this page (hidden under modal); identical ES on p46 has approved EN"
N51="no English overlay on this page (hidden under modal); identical ES on p51 has approved EN"
N57="no English overlay on this page (hidden under modal); identical ES on p57 has approved EN"
R={}
R["41"]=[m(["41.1"],"option text hidden under modal, no EN anywhere"),m(["41.2"],"idem"),m(["41.3","41.4"],"question hidden under modal, no EN"),m(["41.5"],"idem"),m(["41.6"],"idem"),
 g(["41.7"],"Next"),g(["41.8"],"Great job!"),
 g(["41.9","41.10","41.11"],"If Julia's performance exceeds expectations and her salary is significantly below the midpoint; it is appropriate to adjust her compensation to align with the market, recognizing her contribution to the team."),
 g(["41.12"],T)]
R["42"]=[m(["42.1"],"hidden under modal, no EN"),m(["42.2"],"idem"),m(["42.3","42.4"],"idem"),m(["42.5"],"idem"),m(["42.6"],"idem"),
 g(["42.7"],"next"),
 g(["42.8","42.9","42.10","42.11","42.12"],"The correct answer is to consider an increase. Ignoring Julia's outstanding performance or failing to adjust her salary would demotivate her and could be perceived as unfair. Additionally, basing the decision on outdated data or waiting for inflation adjustments does not ensure competitive compensation."),
 g(["42.13"],T),g(["42.14"],"Not the right answer.")]
R["43"]=[g(["43.1"],T),g(["43.2","43.3"],P2),g(["43.4","43.5","43.6"],D2a),g(["43.7","43.8"],"Roberto is an experienced employee with 12 years in the company.")]
R["44"]=[g(["44.1","44.2"],"<b>Roberto’s compa-ratio</b>",note="overlay reads 'Roberto’s compa-ratio 120%,' ; 120% is a separate number element"),
 g(["44.3","44.4","44.5"],"Above the midpoint of his salary range."),g(["44.6"],T),g(["44.7","44.8"],P2),g(["44.9","44.10","44.11"],D2b),g(["44.12"],"Competitive salary")]
R["45"]=[g(["45.1"],"<b>Partially Met Performance</b>"),g(["45.2"],"Will not receive an increase."),g(["45.3"],T),g(["45.4","45.5"],P2),g(["45.6","45.7","45.8"],D2b)]
R["46"]=[g(["46.1"],"Yes, because of seniority.",note="'A)' prefix in overlay omitted"),
 g(["46.2"],"No, because his performance does not justify it.",note="'B)' prefix omitted"),
 g(["46.3","46.4"],"Roberto has a compa-ratio of 120%, but his performance has been partially met. Is it appropriate to grant him an increase?"),
 g(["46.5"],T),
 g(["46.6"],"Yes, because Roberto mentioned to Julia that he has decided to buy a house and his wife is pregnant.",note="'C)' prefix omitted"),
 g(["46.7"],"He will not receive an increase in the salary review process, but after the process, he could be given an extra bonus because of his seniority.",note="'D)' prefix omitted")]
R["47"]=[m(["47.1"],N46),m(["47.2"],N46),m(["47.3","47.4"],N46),m(["47.5"],N46),m(["47.6"],N46),
 g(["47.7"],"Next"),g(["47.8"],"Great job!"),
 g(["47.9","47.10","47.11","47.12"],"Although Roberto has a high compa-ratio, his performance has not met the necessary standards to justify an increase, under the Reward principles."),
 g(["47.13"],T)]
R["48"]=[m(["48.1"],N46),m(["48.2"],N46),m(["48.3","48.4"],N46),m(["48.5"],N46),m(["48.6"],N46),
 g(["48.7","48.8","48.9","48.10","48.11"],"The correct answer is that it is not appropriate, as increases should be based on performance and not on factors such as seniority, personal situations, or alternatives outside the established process, to ensure fair and objective decisions."),
 g(["48.12"],"Not the right answer."),g(["48.13"],"Next"),g(["48.14"],T)]
R["49"]=[g(["49.1"],T),g(["49.2","49.3"],P3),g(["49.4","49.5","49.6"],D3),g(["49.7"],"Julia, your performance has been excellent, and we want to ensure that your salary is aligned with the market.")]
R["50"]=[g(["50.1"],T),g(["50.2","50.3"],P3),g(["50.4","50.5","50.6"],D3),g(["50.7"],"That’s why you will get a raise to place you within the parameters of the salary range.")]
R["51"]=[g(["51.1"],"So that Julia understands the criteria and feels valued.",note="'A)' prefix omitted"),
 g(["51.2"],"To fulfill a bureaucratic requirement.",note="'B)' prefix omitted"),
 g(["51.3"],"So that Julia can move to another team.",note="'D)' prefix omitted"),
 g(["51.4"],"Why is it important for Carla to explain to Julia how the decision about her salary was made?"),
 g(["51.5"],T),
 g(["51.6"],"Because if Carla doesn't do it, the People team won’t process Julia's new salary payment.",note="'C)' prefix omitted")]
R["52"]=[m(["52.1"],N51),m(["52.2"],N51),m(["52.3"],N51),m(["52.4"],N51),m(["52.5"],N51),
 g(["52.6"],"Next"),g(["52.7"],"Great job!"),
 g(["52.8","52.9","52.10","52.11","52.12"],"Explaining salary decisions clearly and transparently reinforces trust, motivates the employee, and ensures they understand how their performance is valued within the organization."),
 g(["52.13"],T)]
R["53"]=[m(["53.1"],N51),m(["53.2"],N51),m(["53.3"],N51),m(["53.4"],N51),m(["53.5"],N51),
 g(["53.6"],"Next"),
 g(["53.7","53.8","53.9","53.10","53.11"],"The correct answer is so that Julia understands the criteria and feels valued. The explanation is not merely a formality or an administrative requirement; its primary purpose is to strengthen trust and commitment."),
 g(["53.12"],T),g(["53.13"],"Not the right answer.")]
R["54"]=[g(["54.1","54.2"],P31),g(["54.3","54.4","54.5"],D3),g(["54.6"],T),
 g(["54.7","54.8","54.9","54.10","54.11"],"As a leader, it’s essential to know your team’s compa-ratio, but when speaking to each individual, it’s not necessary to share the exact result."),
 g(["54.12","54.13","54.14"],"Juan:\n•His performance evaluation result was \"met expectations\" but not \"exceeded expectations.\"\n•His compa-ratio is above the salary range established for his position (122%). Therefore, the matrix does not suggest a salary increase.")]
R["55"]=[g(["55.1","55.2"],P31),g(["55.3","55.4","55.5"],D3),g(["55.6"],T),
 g(["55.7"],"Juan, we value your work and the fact that you meet the team’s expectations. However, your salary is above the range for your position, so the merit matrix does not include a raise this year. We want to be transparent, and these decisions are based on your performance and salary positioning.")]
R["56"]=[g(["56.1","56.2"],P31),g(["56.3","56.4","56.5"],D3),g(["56.6"],T),
 g(["56.7"],"Although there may not be an increase this year, we can work together to identify the path that will allow you to continue developing and taking advantage of new opportunities within the company."),
 g(["56.8"],"I understand, thank you so much for explaining it to me this way and offering me options.")]
R["57"]=[g(["57.1"],"Be clear about the reasons and offer alternatives for the employee's development.",note="'A)' prefix omitted"),
 g(["57.2"],"Not explain the decision and simply say that there will be no increase.",note="'B)' prefix omitted"),
 g(["57.3"],"How should Carla handle the situation when an employee meets expectations but is not eligible for an increase due to their salary positioning?"),
 g(["57.4"],T),
 g(["57.5"],"Give Juan an increase anyway since his results were met, and it doesn't matter that he's still overpaid.",note="'C)' prefix omitted"),
 g(["57.6"],"Ask Juan to go to another company since he won't be getting an increase in the future.",note="'D)' prefix omitted")]
N57b="hidden under modal; identical ES on p57 has approved EN"
R["58"]=[m(["58.1"],N57b),m(["58.2"],N57b),
 m(["58.3"],"leftover Julia option from earlier quiz, no EN on this page (identical ES on p41/42 also has none)"),m(["58.4"],"idem"),m(["58.5"],"idem"),
 g(["58.6"],"Next"),g(["58.7"],"Great job!"),
 g(["58.8","58.9"],"Explaining the reasons and offering alternatives fosters transparency and maintains the employee's motivation."),
 g(["58.10"],T)]
R["59"]=[m(["59.1"],N57b),m(["59.2"],"leftover Julia option, no EN anywhere"),m(["59.3"],N57b),m(["59.4"],"idem"),m(["59.5"],"idem"),
 g(["59.6"],"Next"),
 g(["59.7","59.8","59.9","59.10","59.11"],"The correct answer is to be clear about the reasons and offer alternatives. Not explaining creates distrust, giving an increase breaks salary policies, and suggesting that they leave is unprofessional and demotivating."),
 g(["59.12"],"Not the right answer."),g(["59.13"],T)]
R["60"]=[g(["60.1"],T),g(["60.2","60.3"],"<b>Part 4: Handling Difficult Situations</b>"),
 g(["60.4","60.5"],"Managing complex cases where salary increases do not apply, offering development and well-being alternatives."),
 g(["60.6","60.7","60.8"],"Roberto, an experienced employee, after the salary review and according to the policies, it was concluded that he will not receive an increase.")]
b=json.load(open('blocks_min.json'))
for p in range(41,61):
    ids={x['id'] for x in b[str(p)]}
    got=[i for gr in R[str(p)] for i in gr['ids']]
    assert sorted(got)==sorted(ids) and len(got)==len(set(got)),(p,set(ids)^set(got))
json.dump(R,open('en_41_60.json','w'),ensure_ascii=False,indent=1)
n=sum(len(v) for v in R.values());print(n,sum(g['conf']=='missing' for v in R.values() for g in v))
