import sys; sys.path.insert(0,'/tmp/claude-0/pdfw')
import fitz
from replace import run
P={
4:[
 dict(es=['Pista de carrera'],en='Rally track',align='left'),
 dict(es=['Para avanzar y cruzar la meta, debemos liderar juntos el proceso de revisión salarial anual','con precisión y alineación a los principios de Reward.'],en='To move forward and cross the finish line, we must lead the annual salary review process with precision and alignment to the Reward principles.',padx=0.0),
 dict(es=['Principios de','Reward'],en='Reward principles'),
 dict(es=['Conceptos clave','de Reward'],en='Key concepts of Reward'),
 dict(es=['Proceso de','Revisión salarial'],en='Salary review process'),
],
9:[
 dict(es=['En este recorrido te guiaré en…'],en='In this journey, I will guide you in...'),
 dict(es=['Alinear','las compensaciones con el','mercado para atraer y retener talento','clave.'],en='<b>Aligning</b> compensation with the market to attract and retain key talent.'),
 dict(es=['Eliminar','sesgos y tomar decisiones','basadas en datos concretos.'],en='<b>Eliminating</b> biases and making data-driven decisions.'),
 dict(es=['Explicar','cada decisión de manera','transparente para mantener la conﬁanza','del equipo al máximo.'],en="<b>Explaining</b> each decision transparently to maintain the team's trust at its highest."),
 dict(es=['Establecer','metas claras y recompensar de','manera justa el esfuerzo de cada','colaborador.'],en="<b>Setting</b> clear goals and rewarding each collaborator's effort fairly."),
],
13:[
 dict(es=['Definición de Reward'],en='Definition',align='left'),
 dict(es=['¿Qué es Reward?'],en='What is Reward?'),
 dict(es=['Área que diseña la estrategia,','herramientas y políticas que la','compañía utiliza para','recompensar','a','los colaboradores por su trabajo y','contribuciones,','con el ﬁn de atraer,','retener y motivar al talento.'],en='Area that designs the strategy, tools, and policies the company uses to <b>reward</b> employees for their work and contributions, <b>intending to attract, retain, and motivate talent.</b>'),
],
14:[
 dict(es=['Definición de Reward'],en='Definition',align='left'),
 dict(es=['1. Compensaciones'],en='1. Compensation',align='left',x0=1018,padx=0.0),
 dict(es=['2. Beneﬁcios'],en='2. Benefits',align='left',padx=0.0),
 dict(es=['3. Movilidad'],en='3. Mobility',align='left',padx=0.0),
 dict(es=['ÁREA','REWARD'],en='REWARD<br>AREA',align='left',padx=0.0),
],
}
d=run('es.pdf','sample.pdf',P)
import os; os.makedirs('out',exist_ok=True)
for n in P:
    d[n-1].get_pixmap(matrix=fitz.Matrix(0.6,0.6)).save(f'out/s{n}.png')
