# Khung dùng chung cho các cỗ máy kiến thức (Trái chín, Vi sinh, Tiền chất hương, Bánh xe hương).
# Hình chiếu isometric, trạm, nhãn, thẻ chi tiết, biểu đồ đường. Màu theo phong thủy: không xanh lá, không xanh dương, không đen.
from kit import *

ISO_CSS = r'''
.mnote{font-size:.84rem;color:var(--muted);margin:8px 0 0;line-height:1.45}
#scene .gl{fill:var(--panel);fill-opacity:.18}
#scene .glt{fill:var(--panel);fill-opacity:.12}
#scene .lcdb{fill:#2E1C12;stroke:none}
#scene .lcd{font:700 7.6px var(--mono);fill:#F3D9A4}
#scene .wtx{font:700 8px var(--body);fill:#3A2416}
#scene .flowT{font-size:12.5px}
#scene .ped{fill:#E6DCC8}#scene .ped2{fill:#CFC2A8}#scene .ped3{fill:#B7A98C}
#scene .lcd.sm{font-size:6.5px}
#scene .nowr{fill:none;stroke:var(--accent);stroke-width:2.4;stroke-dasharray:4 3}
#scene .flowL{fill:none;stroke:var(--accent);stroke-width:2.2;stroke-dasharray:3 6;opacity:.75}
.running #scene .flowL,#scene.running .flowL{animation:flowA .8s linear infinite}
@keyframes flowA{to{stroke-dashoffset:-18}}
#tok{display:none;fill:var(--accent);stroke:var(--panel);stroke-width:2}
.running #tok{display:block}
.lg{display:flex;flex-wrap:wrap;gap:4px 16px;font-size:.82rem;margin:2px 0 0;color:var(--muted)}
.lg span{display:inline-flex;align-items:center;gap:6px}
.sw2{display:inline-block;width:16px;height:0;border-top:2.5px solid;flex:none}.sw2.d{border-top-style:dashed}
.sw3{display:inline-block;width:11px;height:11px;border-radius:3px;flex:none}
#tip{color:var(--muted)}
.rd{display:flex;flex-direction:column;gap:4px}
.rd>svg.pi{width:30px;height:30px;color:var(--accent);margin-bottom:2px}
.rd h3{font:800 1.4rem/1.15 var(--display);margin:2px 0 4px}
.rd .ft{margin-top:auto}
.src>h2{color:var(--ink)}.src>.lead{color:var(--muted);font-size:.95rem}
.src ul{line-height:1.5}.src li{margin-bottom:4px}
.src .lnks{margin-top:12px}
.cpst{font-size:.84rem;color:var(--muted)}
.chw{position:relative;margin-top:6px}
.c2{display:block;width:100%;height:auto}
.c2 text{font:500 12px var(--mono);fill:var(--muted)}
.c2 .ttl{font:600 12.5px var(--body);fill:var(--ink)}
.c2 .lab{font:600 12.5px var(--body);fill:var(--ink)}
.c2 .val{font:700 12px var(--mono);fill:var(--ink);paint-order:stroke;stroke:var(--panel);stroke-width:4px;stroke-linejoin:round}
.flowx{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px;counter-reset:fx;margin-top:6px}
.flowx>div{background:var(--tint);border-radius:14px;padding:12px 14px;min-width:0;position:relative}
.flowx b{display:block;font:800 1.15rem/1.15 var(--display);margin-bottom:4px}
.flowx p{margin:0;font-size:.88rem}
.flowx .k{margin-bottom:4px;color:var(--accent)}
@media (max-width:980px){.flowx{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.flowx{grid-template-columns:minmax(0,1fr)}}
.medili{background:var(--tint);border-radius:14px;padding:14px 16px}
.medili h3{margin:0 0 6px;font:800 1.3rem var(--display)}
.medili ul{margin:0;padding-left:18px}.medili li{margin-bottom:4px}
@media (prefers-reduced-motion:reduce){.running #tok{display:none}#scene .flowL{animation:none!important}}
'''

ISO_JS = r'''
const $=id=>document.getElementById(id);
const vn=(n,d=1)=>(+n).toFixed(d).replace('.',',');
const fm=n=>Math.round(n).toLocaleString('de-DE');
const clamp=(v,a,b)=>Math.min(b,Math.max(a,v));
const lerp=(a,b,t)=>a+(b-a)*t;
const NB=' ';
const g1=n=>Number.isInteger(+n)?String(n):vn(n,1);
const f1=n=>(+n).toFixed(1);
const P=(x,y,z=0)=>[OX+(x-y)*.866*U,OY+(x+y)*.5*U-z*U];
const pts=a=>a.map(q=>q.map(f1).join(',')).join(' ');
const pa=p=>!p?'':(p[0]==='#'||p.startsWith('rgb')||p.startsWith('var('))?` style="fill:${p}"`:` class="${p}"`;
const poly=(a,p='')=>`<polygon points="${pts(a)}"${pa(p)}/>`;
function box(x,y,z,w,d,h,c=['f1','f2','f3']){return poly([P(x,y+d,z),P(x+w,y+d,z),P(x+w,y+d,z+h),P(x,y+d,z+h)],c[1])+poly([P(x+w,y,z),P(x+w,y+d,z),P(x+w,y+d,z+h),P(x+w,y,z+h)],c[2])+poly([P(x,y,z+h),P(x+w,y,z+h),P(x+w,y+d,z+h),P(x,y+d,z+h)],c[0])}
const RX=r=>r*U*1.2247,RY=r=>r*U*.7071;
function cyl(cx,cy,z,r,h,c='f2',top='f1'){const [a,b]=P(cx,cy,z),[,t]=P(cx,cy,z+h),rx=RX(r),ry=RY(r);return `<path${pa(c)} d="M${f1(a-rx)} ${f1(t)}V${f1(b)}A${f1(rx)} ${f1(ry)} 0 0 0 ${f1(a+rx)} ${f1(b)}V${f1(t)}Z"/><ellipse${pa(top)} cx="${f1(a)}" cy="${f1(t)}" rx="${f1(rx)}" ry="${f1(ry)}"/>`}
function frus(cx,cy,z0,r0,z1,r1,c,top){const [a,b0]=P(cx,cy,z0),[,b1]=P(cx,cy,z1),x0=RX(r0),y0=RY(r0),x1=RX(r1),y1=RY(r1);return `<path${pa(c)} d="M${f1(a-x1)} ${f1(b1)}L${f1(a-x0)} ${f1(b0)}A${f1(x0)} ${f1(y0)} 0 0 0 ${f1(a+x0)} ${f1(b0)}L${f1(a+x1)} ${f1(b1)}Z"/><ellipse${pa(top)} cx="${f1(a)}" cy="${f1(b1)}" rx="${f1(x1)}" ry="${f1(y1)}"/>`}
const sph=(cx,cy,z,r,c,id)=>{const [a,b]=P(cx,cy,z);return `<circle${id?` id="${id}"`:''}${pa(c)} cx="${f1(a)}" cy="${f1(b-r*U)}" r="${f1(r*U)}"/>`};
const disc=(cx,cy,z,r,c)=>{const [a,b]=P(cx,cy,z);return `<ellipse${pa(c)} cx="${f1(a)}" cy="${f1(b)}" rx="${f1(RX(r))}" ry="${f1(RY(r))}"/>`};
const face=(x,y,z)=>{const q=P(x,y,z);return `matrix(.866 .5 0 1 ${f1(q[0])} ${f1(q[1])})`};
const faceR=(x,y,z)=>{const q=P(x,y,z);return `matrix(.866 -.5 0 1 ${f1(q[0])} ${f1(q[1])})`};
const lcd=(x,y,z,w,id,R)=>`<g transform="${(R?faceR:face)(x,y,z)}"><rect class="lcdb" x="0" y=".8" width="${w}" height="9" rx="1.4"/><text class="lcd" id="${id}" x="${w/2}" y="7.9" text-anchor="middle"></text></g>`;
const stG=(i,inner)=>`<g class="st m" data-i="${i}" tabindex="0" role="button" aria-label="Trạm ${i}: ${ST[i-1].n}">${inner}</g>`;
function bench(L,D,sign,sx){let h='<g class="m">';[[3,D-3],[L-3,D-3],[L-3,3]].forEach(([x,y])=>h+=cyl(x,y,-9,1.2,5,'cu2','cu2'));h+=box(0,0,-4,L,D,4,['wo','wo2','cu2'])+'</g>';
 const pl=P(sx,D,-.6),w=sign.length*8.3+16;
 return h+`<g transform="matrix(.866 .5 0 1 ${f1(pl[0])} ${f1(pl[1])})"><rect width="${f1(w)}" height="24" rx="3" style="fill:#D6B26A;stroke:#2A1B16;stroke-width:1.2"/><circle cx="8" cy="12" r="1.8" style="fill:#2A1B16"/><circle cx="${f1(w-8)}" cy="12" r="1.8" style="fill:#2A1B16"/><text class="sgn" x="${f1(w/2)}" y="17.5" text-anchor="middle">${sign}</text></g>`}
let isOff=()=>false;
function drawChips(){let h='';
 for(let i=1;i<=ST.length;i++){const C=CHIP[i],l=chipLabel(i),w=40+l.length*7,x=Math.min(C.x,VBW-w-8),q=P(...ANCH[i]),off=isOff(i);
  h+=`<polyline class="lead-l${i===st.sel?' on':''}" points="${f1(q[0])},${f1(q[1])} ${f1(x+20)},${C.y+13}"/><g class="chip${i===st.sel?' on':''}${off?' off':''}" data-c="${i}"><rect x="${f1(x+6)}" y="${C.y}" rx="8" width="${f1(w)}" height="26"/><circle cx="${f1(x+6)}" cy="${C.y+13}" r="13"/><text class="num" x="${f1(x+6)}" y="${C.y+18.5}" text-anchor="middle">${i}</text><text class="lab" x="${f1(x+26)}" y="${C.y+18}">${l}</text></g>`}
 const el=$('chips');el.innerHTML=h;el.querySelectorAll('.chip').forEach(g=>g.addEventListener('click',()=>select(+g.dataset.c)))}
const vf=v=>typeof v==='function'?v():v;
function renderStation(){const s=ST[st.sel-1],off=isOff(st.sel),kv=vf(s.kv)||[];
 document.querySelectorAll('#scene .st').forEach(g=>{const i=+g.dataset.i;g.classList.toggle('on',i===st.sel);g.classList.toggle('off',isOff(i))});
 document.querySelectorAll('#strip button').forEach((b,n)=>{b.classList.toggle('on',n+1===st.sel);b.classList.toggle('off',isOff(n+1));b.setAttribute('aria-pressed',n+1===st.sel)});
 $('detail').innerHTML=`<div class="dh"><div class="dn">${st.sel}</div><h2>${s.n}<small>${vf(s.sub)}${off&&s.offNote?' · '+vf(s.offNote):''}</small></h2></div><div class="dgrid"><div><span class="lbl">${s.l1||'Chuyện gì xảy ra'}</span><p>${vf(s.mech)}</p>${s.check?`<span class="lbl">${s.l2||'Đo, nhìn thế nào'}</span><p>${vf(s.check)}</p>`:''}</div><div><span class="lbl">Thông số lúc này</span><dl class="kv">${kv.map(([a,b])=>`<dt>${a}</dt><dd>${b}</dd>`).join('')}</dl>${s.fail?`<p style="margin-top:8px"></p><span class="lbl">${s.l3||'Hiểu nhầm hay gặp'}</span><p>${vf(s.fail)}</p>`:''}${s.tip?`<span class="lbl">${s.l4||'Ở MeDili'}</span><p>${vf(s.tip)}</p>`:''}</div></div>`}
function select(i,noScroll){st.sel=i;renderStation();drawChips();if(noScroll)return;const sc=document.querySelector('.scroller'),q=P(...ANCH[i]);if(sc.scrollWidth>sc.clientWidth)sc.scrollLeft=q[0]/VBW*sc.scrollWidth-sc.clientWidth/2}
function initStations(){$('strip').innerHTML=ST.map((s,i)=>`<button type="button" aria-pressed="false">${i+1} ${s.n}</button>`).join('');
 $('strip').querySelectorAll('button').forEach((b,i)=>b.onclick=()=>select(i+1));
 document.querySelectorAll('#scene .st').forEach(g=>{g.addEventListener('click',()=>select(+g.dataset.i));g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();select(+g.dataset.i)}})})}
const still=matchMedia('(prefers-reduced-motion: reduce)').matches;let timer=0;
function stopRun(){clearTimeout(timer);timer=0;$('scene').classList.remove('running')}
function tour(seq,ms,each){stopRun();if(still){each&&each(seq.length-1);select(seq[seq.length-1]);return}
 $('scene').classList.add('running');let k=0;
 const step=()=>{const i=seq[k],q=P(ANCH[i][0],ANCH[i][1],ANCH[i][2]-1),t=$('tok');t.setAttribute('cx',f1(q[0]));t.setAttribute('cy',f1(q[1]));each&&each(k);select(i);k++;
  if(k<seq.length)timer=setTimeout(step,ms||650);else timer=setTimeout(()=>$('scene').classList.remove('running'),900)};step()}
function pills(id,items,cur,cb){$(id).innerHTML=items.map(([k,n])=>`<button class="pill" type="button" data-k="${k}" aria-pressed="${String(cur)===String(k)}">${n}</button>`).join('');$(id).querySelectorAll('button').forEach(b=>b.onclick=()=>cb(b.dataset.k))}
function interp(p,x){if(!p.length||x<p[0][0]||x>p[p.length-1][0])return null;for(let i=1;i<p.length;i++)if(x<=p[i][0]){const [x0,y0]=p[i-1],[x1,y1]=p[i];return y0+(y1-y0)*(x-x0)/((x1-x0)||1)}return p[p.length-1][1]}
function lineSVG(o){const {W,H,l,r,t,b}=o,X=x=>l+(x-o.x0)/(o.x1-o.x0)*(W-l-r),Y=y=>t+(1-(y-o.y0)/(o.y1-o.y0))*(H-t-b);
 let g=o.ttl?`<text class="ttl" x="${l}" y="12">${o.ttl}</text>`:'';
 (o.bands||[]).forEach(([a,c,lab])=>g+=`<rect x="${f1(X(a))}" y="${t}" width="${f1(Math.max(0,X(c)-X(a)))}" height="${H-t-b}" style="fill:var(--good);fill-opacity:.13"/>`);
 (o.hb||[]).forEach(([a,c])=>g+=`<rect x="${l}" y="${f1(Y(c))}" width="${W-l-r}" height="${f1(Math.max(0,Y(a)-Y(c)))}" style="fill:var(--good);fill-opacity:.13"/>`);
 (o.yt||[]).forEach(v=>g+=`<line x1="${l}" x2="${W-r}" y1="${f1(Y(v))}" y2="${f1(Y(v))}" style="stroke:var(--rule);stroke-width:.8"/><text x="${l-5}" y="${f1(Y(v)+3.5)}" text-anchor="end">${o.yf?o.yf(v):v}</text>`);
 (o.xt||[]).forEach(v=>g+=`<text x="${f1(X(v))}" y="${H-5}" text-anchor="middle">${o.xf?o.xf(v):v}</text>`);
 (o.vl||[]).forEach(([x,lab])=>g+=`<line x1="${f1(X(x))}" x2="${f1(X(x))}" y1="${t}" y2="${H-b}" style="stroke:var(--muted);stroke-width:1;stroke-dasharray:3 3"/>${lab?`<text x="${f1(X(x)+3)}" y="${t+10}">${lab}</text>`:''}`);
 (o.areas||[]).forEach(s=>g+=`<polygon points="${s.p.map(([x,y])=>f1(X(x))+','+f1(Y(y))).join(' ')}" style="fill:${s.c};fill-opacity:${s.o||.9}"/>`);
 (o.ser||[]).forEach(s=>g+=`<polyline points="${s.p.map(([x,y])=>f1(X(x))+','+f1(Y(y))).join(' ')}" fill="none" style="stroke:${s.c};stroke-width:${s.w||2};stroke-linejoin:round${s.d?`;stroke-dasharray:${s.d}`:''}"/>`);
 if(o.vx!=null){g+=`<line x1="${f1(X(o.vx))}" x2="${f1(X(o.vx))}" y1="${t}" y2="${H-b}" style="stroke:var(--ink);stroke-width:1.1"/>`;
  (o.ser||[]).forEach(s=>{if(s.dot===false)return;const v=interp(s.p,o.vx);if(v!=null)g+=`<circle cx="${f1(X(o.vx))}" cy="${f1(Y(v))}" r="4" style="fill:${s.c};stroke:var(--panel);stroke-width:2"/>`})}
 if(o.end){const L=(o.ser||[]).filter(s=>s.lab).map(s=>({y:Y(s.p[s.p.length-1][1]),s:s.lab})).sort((a,c)=>a.y-c.y);for(let i=1;i<L.length;i++)if(L[i].y-L[i-1].y<12)L[i].y=L[i-1].y+12;L.forEach(e=>g+=`<text x="${W-r+5}" y="${f1(e.y+3.5)}" style="fill:var(--ink)">${e.s}</text>`)}
 (o.bands||[]).forEach(([a,c,lab])=>{if(lab)g+=`<text x="${f1((X(a)+X(c))/2)}" y="${H-b-6}" text-anchor="middle" style="paint-order:stroke;stroke:var(--panel);stroke-width:3px;stroke-linejoin:round;fill:var(--ink)">${lab}</text>`});
 return g}
const legend=(id,items)=>{$(id).innerHTML=items.map(s=>s.box?`<span><i class="sw3" style="background:${s.c}"></i>${s.n}</span>`:`<span><i class="sw2${s.d?' d':''}" style="border-color:${s.c}"></i>${s.n}</span>`).join('')};
const cw=id=>{const e=$(id);return Math.max(300,Math.round((e&&e.clientWidth)||900))};
const cp=async(txt,el)=>{try{await navigator.clipboard.writeText(txt);$(el).textContent='Đã sao chép.'}catch(e){$(el).textContent='Không sao chép được, hãy bôi đen để chép.'}setTimeout(()=>$(el).textContent='',2600)};
function rng(seed){let s=seed>>>0;return ()=>{s=(s*1664525+1013904223)>>>0;return s/4294967296}}
function gauss(r){let u=0,v=0;while(!u)u=r();while(!v)v=r();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v)}
'''


def head(title_em, title_pre, lead, tag='Kiến thức cà phê'):
    return (f'<header>\n  {logo()}<div class="brandbar"><span>Mê vị Di Linh</span><span>{tag}</span><span>Zalo <a href="#lien-he">{PHONE_RAW}</a></span></div>\n'
            f'  <h1>{title_pre} <em>{title_em}</em></h1>\n  <p>{lead}</p>\n</header>\n')


def srclist(items):
    return ''.join(f'<li>{t}. <a href="{u}" target="_blank" rel="noopener">{n} ↗</a></li>' for t, n, u in items)


def boxes(items):
    return ''.join(f'<div class="box rd">{icon(i)}<h3>{t}</h3><p>{p}</p></div>' for i, t, p, s in items)
