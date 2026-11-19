/* Deterministic scenes for the installed shared film engine.
   Sources: version-4 manuscript Theorem 1, Lemma 1, Sections 1--4.
   The exact normalized decrement is presented as written mathematics, not a Lean badge. */
'use strict';
const input7 = [21,21,40,21,21,21,21,2].map(n => n / 168);
const output7 = [69468,87252,64205,82635,78360,59892,43533,32095].map(n => n / 517440);
function fade(S) { return clamp(S.u / 0.6) * clamp((S.d - S.u) / 0.5); }
function titlePair(en, zh, a) {
  txt(en, 960, 215, {size:44, fam:F.disp, w:700, align:'center', a});
  txt(zh, 960, 273, {size:36, fam:F.zh, align:'center', c:C.dim, a});
}
function histogram(vals, x, y, w, h, name, color, a) {
  panel(x,y,w,h,a,color,name);
  const left=x+55, base=y+h-64, ch=h-132, step=(w-100)/8;
  const ref=base-(1/8)/0.27*ch;
  ctx.save(); ctx.globalAlpha=a;
  ctx.strokeStyle=C.dim; ctx.lineWidth=2; ctx.setLineDash([10,9]);
  ctx.beginPath(); ctx.moveTo(x+35,ref);ctx.lineTo(x+w-25,ref);ctx.stroke();ctx.setLineDash([]);
  vals.forEach((v,k)=>{
    const bh=v/0.27*ch;
    ctx.fillStyle=color;ctx.globalAlpha=a*0.7;
    ctx.fillRect(left+k*step,base-bh,step*0.58,bh);
    ctx.globalAlpha=a;ctx.strokeStyle=C.white;ctx.lineWidth=2;
    const yy=base-bh, xx=left+k*step+step*0.29;
    ctx.beginPath();ctx.moveTo(xx,yy);ctx.lineTo(xx,ref);ctx.stroke();
    txt(String(k),xx,base+32,{size:23,align:'center',c:C.dim,a});
  });
  ctx.restore();
  txt('1/8',x+w-65,ref-12,{size:24,c:C.white,a});
}
SCENES.question = S => {
  const a=fade(S);badgeQ(S,[[0,null,'argued']]);
  titlePair('Can symmetric noise lower the score?', '对称噪声能让评分下降吗？',a);
  panel(260,350,1400,330,a,C.argued,'SPIN 4 / ORDER 7 / MIXED INPUT');
  txt('A₇(Φ(ρ)) − A₇(ρ)',960,470,{size:62,fam:F.math,align:'center',a});
  txt('= −95 / 90552 < 0',960,570,{size:68,fam:F.math,align:'center',c:C.argued,a:at(S,1,0.8)*a});
  txt('One admissible exception defeats a universal rule.',960,770,{size:33,fam:F.disp,align:'center',a:at(S,2,0.6)*a});
};
SCENES.patterns = S => {
  const a=fade(S);badgeQ(S,[[0,null,'argued']]);
  titlePair('Nine symmetric patterns → eight retained patterns','九种对称模式 → 八种保留模式',a);
  panel(120,340,760,390,a,C.cyan,'FULL SYSTEM: EIGHT QUBITS');
  for(let r=0;r<=8;r++){
    const x=205+r*73;
    for(let j=0;j<8;j++)chip(x,420+j*30,34,24,j<r?'1':'0',j<r?C.cyan:C.dim,a,15);
    txt(String(r),x,705,{size:24,align:'center',a});
  }
  txt('→',960,540,{size:80,fam:F.math,align:'center',a:at(S,1,0.6)*a});
  histogram(Array(8).fill(1/8),1040,340,760,390,'REFERENCE: SEVEN QUBITS',C.cyan,at(S,1,0.7)*a);
  txt('A₇ = 1 − distance / (7/4)',1420,810,{size:35,fam:F.math,align:'center',a:at(S,2,0.6)*a});
};
SCENES.reduction = S => {
  const a=fade(S);badgeQ(S,[[0,null,'argued'],[2,null,'computed']]);
  titlePair('Discard one qubit: two possible origins','丢掉一个比特：两种来源',a);
  panel(210,345,1500,195,a,C.cyan,'EXACT PARTIAL TRACE / 0 ≤ k ≤ 7');
  txt('pₖ⁽⁷⁾ = ((8−k)/8) pₖ + ((k+1)/8) pₖ₊₁',960,465,{size:46,fam:F.math,align:'center',a});
  chip(570,600,600,72,'k ones → discard 0',C.cyan,a,28,F.disp);
  chip(1350,600,600,72,'k+1 ones → discard 1',C.mag,a,28,F.disp);
  txt('p⁽⁷⁾ = (21,21,40,21,21,21,21,2) / 168',960,735,{size:38,fam:F.math,align:'center',a:at(S,2,0.6)*a});
  txt('Uniform = 21/168; deviations = +19/168, −19/168',960,805,{size:31,fam:F.disp,align:'center',c:C.dim,a:at(S,2,0.6)*a});
};
SCENES.channel = S => {
  const a=fade(S);badgeQ(S,[[0,null,'argued']]);
  titlePair('Rotation symmetry acts on the full system','旋转对称性约束完整系统',a);
  panel(150,345,1620,200,a,C.argued,'QUADRUPOLE CHANNEL');
  txt('Φ(X) = (3/770) Σₐ,ᵦ Qₐᵦ X Qₐᵦ',960,430,{size:48,fam:F.math,align:'center',a});
  txt('Σₐ,ᵦ Qₐᵦ² = (770/3) I',960,505,{size:38,fam:F.math,align:'center',a:at(S,1,0.5)*a});
  chip(450,640,500,85,'9 levels: ρ → Φ(ρ)',C.cyan,a,34,F.math);
  txt('↓ partial trace',450,725,{size:28,fam:F.disp,align:'center',a});
  chip(450,790,500,64,'8 levels: ρ₇',C.cyan,a,32,F.math);
  txt('⇏',930,760,{size:90,fam:F.math,align:'center',c:C.argued,a:at(S,2,0.8)*a});
  chip(1390,745,650,110,'a channel on reductions',C.argued,at(S,2,0.8)*a,30,F.disp);
};
SCENES.distance = S => {
  const a=fade(S);badgeQ(S,[[0,null,'computed']]);
  titlePair('The total absolute deviation increases','绝对偏差的总和增加',a);
  histogram(input7,120,335,800,340,'INPUT REDUCTION',C.cyan,a);
  histogram(output7,1000,335,800,340,'OUTPUT REDUCTION',C.mag,a);
  txt('Dᵢₙ = 19/84',520,730,{size:38,fam:F.math,align:'center',a:at(S,1,0.6)*a});
  txt('Dₒᵤₜ = 3933/17248',1400,730,{size:38,fam:F.math,align:'center',a:at(S,1,0.6)*a});
  txt('ΔD = 95/51744 > 0   ⇒   ΔA₇ = −95/90552 < 0',960,795,{size:36,fam:F.math,align:'center',c:C.white,a:at(S,2,0.8)*a});
};
SCENES.scope = S => {
  const a=fade(S);badgeQ(S,[[0,null,'argued'],[2,null,'open']]);
  titlePair('The missing step is a channel on the reduced space','缺少的是约化空间上的信道',a);
  panel(130,355,780,360,a,C.cyan,'TWO CONTROLS');
  txt('Mixtures of rotations',520,455,{size:37,fam:F.disp,align:'center',a:at(S,1,0.6)*a});
  txt('Full order t = N',520,540,{size:37,fam:F.math,align:'center',a:at(S,1,0.6)*a});
  txt('Both obey monotonicity.',520,650,{size:29,fam:F.disp,align:'center',c:C.dim,a:at(S,1,0.6)*a});
  panel(1010,355,780,360,a,C.open,'SEPARATE QUESTIONS');
  txt('Pure inputs',1400,455,{size:37,fam:F.disp,align:'center',a:at(S,2,0.6)*a});
  txt('Mixed inputs: t ≤ N/2',1400,540,{size:35,fam:F.math,align:'center',a:at(S,2,0.6)*a});
  txt('Universal fidelity monotonicity',1400,625,{size:28,fam:F.disp,align:'center',a:at(S,2,0.6)*a});
  txt('Ma & Zhang · version 4 · doi:10.5281/zenodo.23884885',960,765,{size:25,fam:F.mono,align:'center',c:C.dim,a});
  txt('Witness reconstructed from the existing upstream formal proof',960,807,{size:27,fam:F.disp,align:'center',c:C.dim,a});
};
FILM.poster = () => {
  titlePair('When symmetry does not control reduced distance','对称性为何不能控制约化距离',1);
  histogram(input7,140,340,770,390,'INPUT: 19/84',C.cyan,1);
  histogram(output7,1010,340,770,390,'OUTPUT: 3933/17248',C.mag,1);
  txt('ΔA₇ = −95/90552 < 0',960,835,{size:64,fam:F.math,align:'center',c:C.white});
};
