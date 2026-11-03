import json
b=json.load(open('blocks_min.json'))
T="Salary review process"
P4="<b>Part 4: Handling Difficult Situations</b>"
P4s="Managing complex cases where salary increases do not apply, offering development and well-being alternatives."
P5="<b>Part 5: Salary Review Process in the People Hub System</b>"
def g(ids,en,conf="ok",note=None):
    d={"ids":ids,"en":en,"conf":conf}
    if note:d["note"]=note
    return d
def steps(p,start=3):
    s=start
    return [g([f"{p}.{s}",f"{p}.{s+1}"],"1. Salary Increase Proposal"),
            g([f"{p}.{s+2}",f"{p}.{s+3}"],"2. Review and Validation of Proposals"),
            g([f"{p}.{s+4}"],"3. Executive Review"),
            g([f"{p}.{s+5}"],"4. Generation of Letters and Payment")]
# steps ids: 67.3/4, 5/6, 7, 8
def steps67(p,s):
    return [g([f"{p}.{s}",f"{p}.{s+1}"],"1. Salary Increase Proposal"),
            g([f"{p}.{s+2}",f"{p}.{s+3}"],"2. Review and Validation of Proposals"),
            g([f"{p}.{s+4}"],"3. Executive Review"),
            g([f"{p}.{s+5}"],"4. Generation of Letters and Payment")]
R={}
R["61"]=[g(["61.1"],"This year, based on your performance and the company’s policies, we will not be applying a salary increase. However, I want you to know that your salary is competitive in relation to the market. And I would still like us to work together on a plan to continue boosting your development within the company."),
 g(["61.2"],T),g(["61.3","61.4"],P4),g(["61.5","61.6"],P4s),
 g(["61.7"],"Roberto, we greatly value your experience and your contribution to the team.")]
R["62"]=[g(["62.1"],"I want to make sure you have the support you need for your well-being. You’ll have days off for your paternity leave. Additionally, I encourage you to consider participating in professional development and well-being programs, such as coaching sessions and stress management activities. We want you to feel supported and motivated to continue growing with us."),
 g(["62.2"],T),g(["62.3","62.4"],P4),g(["62.5","62.6"],P4s),
 g(["62.7"],"Thank you for the clarity, Carla. I understand the situation and appreciate the support you’re offering.")]
opts={"A":"Not communicate anything to Roberto. He won’t even know why he’ll have days off for his paternity leave.","B":"Simply say that there will be no increase.","C":"Acknowledge his contribution, explain the decision, and offer a development plan.","D":"Act like an angry leader and blame him for not receiving an increase due to his underperformance."}
Q="What key elements should Carla include in her conversation with Roberto?"
R["63"]=[g(["63.1"],opts["B"],note="Letter prefix 'B)' omitted"),g(["63.2"],Q),g(["63.3"],T),g(["63.4"],opts["C"],note="Letter prefix omitted"),g(["63.5"],opts["A"],note="Letter prefix omitted"),g(["63.6"],opts["D"],note="Letter prefix omitted")]
def quiz(p):
    return [g([f"{p}.1"],opts["B"],note="Letter prefix omitted"),g([f"{p}.2"],Q),g([f"{p}.3"],opts["C"],note="Letter prefix omitted"),g([f"{p}.4"],opts["A"],note="Letter prefix omitted"),g([f"{p}.5"],opts["D"],note="Letter prefix omitted")]
R["64"]=quiz("64")+[g(["64.6"],"Next"),g(["64.7"],"Great job!"),
 g(["64.8","64.9","64.10","64.11"],"Acknowledging his contribution, explaining the decision, and offering a development plan demonstrates empathy and fosters motivation, aligning with the principles of transparent communication and support for well-being."),g(["64.12"],T)]
R["65"]=quiz("65")+[g(["65.6"],"Next"),
 g(["65.7","65.8","65.9","65.10"],"Not communicating or just denying the raise lacks empathy and can demotivate Roberto. Similarly, blaming him is unprofessional and could damage both trust and the work environment."),
 g(["65.11"],"Not the right answer."),g(["65.12"],T)]
R["66"]=[g(["66.1"],"It is essential to understand how the salary review process works in the People Hub system and what tools are available to us."),g(["66.2"],T),g(["66.3"],P5)]
def hdr(p):
    return [g([f"{p}.1"],T),g([f"{p}.2"],P5)]+steps67(p,3)
R["67"]=hdr("67")
R["68"]=hdr("68")
R["69"]=hdr("69")+[g(["69.9"],"<b>Compensation Planner Manager</b>"),g(["69.10"],"Reviews proposals in People Hub."),g(["69.11"],"Approves, modifies, or returns forms for adjustments before proceeding.")]
R["70"]=hdr("70")+[g(["70.9","70.10"],"Local and Regional Reward Team"),g(["70.11","70.12","70.13"],"Once the proposal is approved, it is sent to the regional CEO for their approval.")]
R["71"]=hdr("71")+[g(["71.9"],"Compensation Letters are generated with the results of the process, available in:"),g(["71.10"],"Employee Central\nPeople Hub profile of each employee",note="Two bullets in the Spanish block; English shows two lines, no bullet glyphs")]
R["72"]=[g(["72.1"],P5,"uncertain","No overlay on this slide; same text as pp.66-71"),]+[dict(x,conf="uncertain",note="No overlay on this slide; same English as p.71") for x in steps67("72",2)]+[
 g(["72.8"],"Compensation Letters are generated with the results of the process, available in:","uncertain","No overlay on this slide; taken from p.71"),
 g(["72.9"],"Employee Central\nPeople Hub profile of each employee","uncertain","No overlay on this slide; taken from p.71"),
 g(["72.10"],T),g(["72.11","72.12"],"The compensation statement can be viewed in Employee Central as follows:")]
A73="At the end of the process, we achieve the goal of effectively applying the Reward principles. Additionally, we ensure that each employee understands the decisions made and how they can continue growing."
R["73"]=[g(["73.1"],T),g(["73.2"],A73)]
R["74"]=[g(["74.1"],"Competitiveness, bias, opacity, and commitment.",note="Letter prefix omitted"),
 g(["74.2"],"Competitiveness with the market, free from biases, transparency, and clarity, commitment to people.",note="Letter prefix omitted"),
 g(["74.3"],"What are the Reward principles that Carla applied throughout the process?"),g(["74.4"],T),
 g(["74.5"],"Promotion, Compa-ratio, free from bias, and commitment.",note="Letter prefix omitted"),
 g(["74.6"],"Commitment, free from bias, competitiveness, and salary grade.",note="Letter prefix omitted")]
FB="Competitiveness, free from bias, transparency, and commitment to people reflect the key Reward principles applied during the salary review process."
R["75"]=[g(["75.1"],A73),g(["75.2"],"Next"),g(["75.3"],"Great job!"),g(["75.4","75.5","75.6"],FB),g(["75.7"],T)]
R["76"]=[g(["76.1"],A73,"uncertain","Not visible in overlay on this slide; same as p.73/75 background"),g(["76.2"],"Not the right answer."),g(["76.3"],"Next"),g(["76.4","76.5","76.6"],FB),g(["76.7"],T)]
R["77"]=[g(["77.1"],"Conclusion"),g(["77.2"],"As a leader, now you understand your role in making the Reward process fair and motivating. We all move forward together toward success by applying the principles.")]
R["78"]=[g(["78.1"],"You have completed this unit.\nSee you next time.")]
# validate
for p in map(str,range(61,79)):
    got=[i for x in R[p] for i in x["ids"]]
    ids=[x["id"] for x in b[p]]
    assert sorted(got)==sorted(ids),(p,set(ids)^set(got))
json.dump(R,open('en_61_78.json','w'),ensure_ascii=False,indent=1)
n=sum(len(v) for v in R.values());u=sum(x["conf"]=="uncertain" for v in R.values() for x in v)
print(n,u)
