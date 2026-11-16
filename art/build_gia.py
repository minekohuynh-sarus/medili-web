# Dựng tab "Giá cà phê" cho site MeDili, dữ liệu trong gia-ca-phe.json do lịch chạy hằng ngày cập nhật
import os, re, json, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '..', 'site-new2')     # bản đang chạy
LIVE = os.path.join(HERE, '..', 'site-live')
OUT = os.path.join(HERE, '..', 'site-new3')
os.makedirs(OUT, exist_ok=True)
rd = lambda f: open(os.path.join(BASE, f), encoding='utf8').read()

PAGE = 'gia-ca-phe.html'
DATA = 'gia-ca-phe.json'
NAVLBL = 'Giá cà phê'
BLD = {'name': 'Báo Lâm Đồng', 'url': 'https://baolamdong.vn/gia-ca-phe/tinh-lam-dong'}
VNN = {'name': 'VietNamNet', 'url': 'https://dantocphattrien.vietnamnet.vn/gia-ca-phe'}

SEED = {
 'version': 1,
 'updated': '2026-11-07T12:37:00+07:00',
 'days': [
  {'date': '2026-10-31', 'vn': {'lamdong': 86500}, 'src': [BLD]},
  {'date': '2026-11-02', 'vn': {'lamdong': 84200}, 'src': [BLD]},
  {'date': '2026-11-03', 'vn': {'lamdong': 84000}, 'src': [BLD]},
  {'date': '2026-11-04', 'vn': {'lamdong': 83300}, 'src': [BLD]},
  {'date': '2026-11-05', 'vn': {'lamdong': 83500}, 'src': [BLD]},
  {'date': '2026-11-06', 'vn': {'lamdong': 83600, 'daklak': 84200, 'gialai': 84000, 'daknong': 84500},
   'world': {'robusta': 3241, 'robustaChg': 13, 'robustaPct': 0.40, 'robustaTerm': '01/2027',
             'arabica': 277.15, 'arabicaChg': -2.60, 'arabicaPct': -0.93, 'arabicaTerm': '12/2026'}, 'src': [BLD, VNN]},
  {'date': '2026-11-07', 'time': '12:37', 'vn': {'lamdong': 84000, 'daklak': 84500, 'gialai': 84500, 'daknong': 84700},
   'world': {'robusta': 3270, 'robustaChg': 29, 'robustaPct': 0.89, 'robustaTerm': '01/2027',
             'arabica': 280.00, 'arabicaChg': 2.85, 'arabicaPct': 1.03, 'arabicaTerm': '12/2026'}, 'src': [BLD, VNN]},
 ],
 'fresh': [
  {'date': '2026-11-05', 'low': 18000, 'high': 18000, 'place': '', 'note': 'trên dưới 18.000 đ/kg',
   'src': {'name': 'Tuổi Trẻ', 'url': 'https://tuoitre.vn/gia-ca-dau-ngay-nho-than-go-gia-200000-dong-kg-ca-phe-dau-vu-tiep-tuc-rot-gia-10026110508561234.htm'}},
  {'date': '2026-11-03', 'low': 17500, 'high': 17800, 'place': 'Bảo Lâm, Lâm Đồng', 'note': 'trái chín nhiều được 17.800 đ/kg',
   'src': {'name': 'Dân Trí', 'url': 'https://dantri.com.vn/kinh-doanh/gia-ca-phe-giam-manh-nong-dan-co-dong-thai-bat-ngo-20261103183301042.htm'}},
 ],
}
_LIVEJ = os.path.join(HERE, '..', 'run-check', DATA)
if os.path.exists(_LIVEJ):
    SEED = json.load(open(_LIVEJ, encoding='utf8'))  # ảnh chụp mới nhất của file giá trên site
open(os.path.join(OUT, DATA), 'w', encoding='utf8').write(json.dumps(SEED, ensure_ascii=False, indent=1) + '\n')

suc = open(os.path.join(LIVE, 'suc-khoe.html'), encoding='utf8').read()
SHARED = re.findall(r'<style>(.*?)</style>', suc, flags=re.S)[1]
FONTS = re.search(r'<link rel="preconnect" href="https://fonts.googleapis.com">\s*<link rel="preconnect"[^>]*>\s*<link rel="stylesheet"[^>]*>', suc).group(0)

NAV_RE = re.compile(r'(<nav aria-label="Menu chính">)')


def nav(html, current=False):
    if 'href="' + PAGE + '"' in html:
        return html
    link = f'<a href="{PAGE}" class=on aria-current=page>{NAVLBL}</a>' if current else f'<a href="{PAGE}">{NAVLBL}</a>'
    html, n = NAV_RE.subn(r'\1' + link, html, count=1)
    assert n == 1
    return html


MNAV = re.search(r'<div class="mnav">.*?</div></div>', rd('tu-vuon-den-ly.html'), flags=re.S).group(0)
MNAV = MNAV.replace(' class=on aria-current=page', '')
MNAV = nav(MNAV, current=True)

PAGE_CSS = '''
/* Trang Giá cà phê: bốn ô giá hôm nay, biểu đồ Lâm Đồng và bảng các tỉnh, rồi giá thế giới, lịch sử và cách đọc. */
:root{--moss:#8D4E22;--good:#8D4E22;--line:#9E3B26;--grid:#E4D8C3;--tip:#FDFAF2}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--moss:#E2A774;--good:#E2A774;--line:#EBA58D;--grid:#3A2E25;--tip:#2B211B}}
:root[data-theme="dark"]{--moss:#E2A774;--good:#E2A774;--line:#EBA58D;--grid:#3A2E25;--tip:#2B211B}
a{color:var(--accent)}
.upd{margin:10px 0 0;font-size:.9rem;color:var(--muted)}.upd b{color:var(--ink);font-weight:600}
.tiles{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.tile{background:var(--panel);border:1px solid var(--rule);border-radius:16px;padding:14px 16px;display:grid;gap:4px;align-content:start;min-width:0}
.tile .lb{font:600 .78rem/1.3 var(--body);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.tile .v{font:800 2.3rem/1.05 var(--display);font-variant-numeric:tabular-nums;overflow-wrap:anywhere}
.tile .v small{font:600 .9rem var(--body);color:var(--muted);margin-left:4px}
.tile .d{font-size:.86rem;color:var(--ink)}.tile .d i{font-style:normal;color:var(--muted)}
.tile .s{font-size:.8rem;color:var(--muted);line-height:1.4}
@media (max-width:1000px){.tiles{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:420px){.tile .v{font-size:1.9rem}}
.chartw{position:relative;margin-top:8px}
.chartw svg{display:block;width:100%;height:auto;overflow:visible;touch-action:pan-y}
.chartw svg:focus-visible{outline:3px solid var(--moss);outline-offset:4px;border-radius:6px}
.ax text{font:500 11px var(--mono);fill:var(--muted)}
.gl{stroke:var(--grid);stroke-width:1}
.ln{fill:none;stroke:var(--line);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.pt{fill:var(--line);stroke:var(--panel);stroke-width:2}
.endl{font:700 12px var(--mono);fill:var(--ink)}
.xh{stroke:var(--ink);stroke-width:1;opacity:.45}
.tip{position:absolute;top:0;pointer-events:none;background:var(--tip);border:1px solid var(--rule);border-radius:10px;padding:7px 10px;box-shadow:0 6px 18px rgba(42,27,22,.14);font-size:.82rem;white-space:nowrap;transform:translateX(-50%);z-index:2}
.tip b{display:block;font:700 .95rem var(--mono)}.tip span{color:var(--muted)}
.empty{margin:14px 0 4px;padding:18px;border:1px dashed var(--rule);border-radius:12px;color:var(--muted);font-size:.9rem;text-align:center}
.rng{margin-top:4px}
table.pv{width:100%}
table.pv td,table.pv th{padding:8px 10px 8px 0}
table.pv td.n,table.pv th.n{text-align:right;font-family:var(--mono);font-variant-numeric:tabular-nums}
table.pv tr.me td{font-weight:700}
.chg{font-size:.82rem;color:var(--muted);font-family:var(--body)!important}
.fresh{display:grid;gap:10px;margin-top:6px}
.fq{border-top:1px solid var(--rule);padding-top:10px}
.fq b{font:700 1.05rem var(--mono)}.fq span{display:block;font-size:.84rem;color:var(--muted)}
.two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
@media (max-width:820px){.two{grid-template-columns:minmax(0,1fr)}}
.two h3{font:800 1.3rem var(--display);margin:0}
.two .u{font-size:.82rem;color:var(--muted)}
#hist th{position:sticky;top:0;background:var(--panel)}
#hist td.n,#hist th.n{text-align:right;font-family:var(--mono)}
.histw{max-height:420px;overflow:auto}
ul.plain li b{color:var(--ink)}
@media (prefers-reduced-motion:reduce){.tip{transition:none}}
'''

JS = r'''
const $=id=>document.getElementById(id);
const PROV=[['lamdong','Lâm Đồng'],['daklak','Đắk Lắk'],['gialai','Gia Lai'],['daknong','Đắk Nông (cũ)']];
const fm=n=>String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,'.');
const f2=n=>n.toFixed(2).replace('.',',');
const pc=n=>Math.abs(n).toFixed(2).replace('.',',')+' %';
const dd=s=>{const [y,m,d]=s.split('-');return `${d}/${m}/${y}`};
const dshort=s=>{const [y,m,d]=s.split('-');return `${d}/${m}`};
const tday=s=>Date.UTC(+s.slice(0,4),+s.slice(5,7)-1,+s.slice(8,10));
const arrow=v=>v>0?'▲':v<0?'▼':'■';
const el=(t,c,txt)=>{const e=document.createElement(t);if(c)e.className=c;if(txt!=null)e.textContent=txt;return e};
let D=JSON.parse($('snap').textContent),range=30;
const fscore=q=>q.place&&/Di Linh/i.test(q.place)?2:q.place?1:0;
const fsort=a=>[...(a||[])].sort((x,y)=>x.date<y.date?1:x.date>y.date?-1:fscore(y)-fscore(x));
function days(){return [...(D.days||[])].sort((a,b)=>a.date<b.date?-1:1)}
function prevWith(list,i,get){for(let j=i-1;j>=0;j--){const v=get(list[j]);if(v!=null)return [v,list[j].date]}return [null,null]}
function latestWith(get){const L=days();for(let i=L.length-1;i>=0;i--){const v=get(L[i]);if(v!=null)return [v,L[i],i,L]}return [null,null,-1,L]}
function tiles(){
 const box=$('tiles');box.textContent='';
 const t=(lb,v,unit,d,s)=>{const e=el('div','tile');e.append(el('span','lb',lb));const vv=el('span','v',v);if(unit)vv.append(el('small','',unit));e.append(vv);if(d)e.append(d);if(s)e.append(el('span','s',s));box.append(e)};
 const [ld,day,i,L]=latestWith(x=>x.vn&&x.vn.lamdong);
 if(ld!=null){const [pv,pd]=prevWith(L,i,x=>x.vn&&x.vn.lamdong);const d=el('span','d');if(pv!=null){d.textContent=`${arrow(ld-pv)} ${fm(Math.abs(ld-pv))} đ `;d.append(el('i','',`so với ${dshort(pd)}`))}t('Nhân xô Lâm Đồng',fm(ld),'đ/kg',d,`Ngày ${dd(day.date)}. Di Linh, Bảo Lộc, Lâm Hà theo giá chung.`)}
 const F=fsort(D.fresh)[0];
 if(F){t('Trái tươi',F.low===F.high?fm(F.low):`${fm(F.low)}–\u200b${fm(F.high)}`,'đ/kg',null,`Báo giá ngày ${dd(F.date)}${F.place?', '+F.place:''}, theo ${F.src.name}.`)}
 for(const [k,lb,unit,dg] of [['robusta','Robusta London','USD/tấn',0],['arabica','Arabica New York','cent/lb',2]]){
  const [v,dy]=latestWith(x=>x.world&&x.world[k]);if(v==null)continue;const w=dy.world;const d=el('span','d');
  if(w[k+'Pct']!=null){d.textContent=`${arrow(w[k+'Pct'])} ${pc(w[k+'Pct'])} `;if(w[k+'Term'])d.append(el('i','',`kỳ hạn ${w[k+'Term']}`))}
  t(lb,dg?f2(v):fm(v),unit,d,`Phiên gần nhất tính đến ${dd(dy.date)}.`)}
}
function provTable(){
 const L=days(),tb=$('prov');tb.textContent='';let any=false;
 for(const [k,name] of PROV){const [v,day,i]=latestWith(x=>x.vn&&x.vn[k]);if(v==null)continue;any=true;const [pv]=prevWith(L,i,x=>x.vn&&x.vn[k]);
  const tr=el('tr',k==='lamdong'?'me':'');tr.append(el('td','',name));const td=el('td','n',fm(v));tr.append(td);const c=el('td','n chg',pv!=null?`${arrow(v-pv)} ${fm(Math.abs(v-pv))}`:'–');tr.append(c);tb.append(tr)}
 $('provd').textContent=any?`Đơn vị đ/kg, nhân xô Robusta. So với ngày có giá trước đó.`:'Chưa có dữ liệu.';
}
function freshList(){
 const box=$('fresh');box.textContent='';const F=fsort(D.fresh).slice(0,5);
 if(!F.length){box.append(el('p','empty','Chưa có báo giá trái tươi.'));return}
 for(const q of F){const e=el('div','fq');e.append(el('b','',(q.low===q.high?fm(q.low):`${fm(q.low)}–${fm(q.high)}`)+' đ/kg'));
  const s=el('span','',`${dd(q.date)} · ${q.place||'bài không nêu nơi thu mua'} · `);const a=el('a','',q.src.name);a.href=q.src.url;a.target='_blank';a.rel='noopener';s.append(a);e.append(s);box.append(e)}
}
function chart(id,get,fmt,unit){
 const box=$(id);box.textContent='';const L=days().filter(x=>get(x)!=null);
 const last=L.length?tday(L[L.length-1].date):0;const P=L.filter(x=>range>=9999||tday(x.date)>=last-(range-1)*864e5).map(x=>({t:tday(x.date),v:get(x),d:x.date}));
 if(P.length<2){box.append(el('p','empty',P.length?`Mới có giá ngày ${dd(P[0].d)}. Biểu đồ hiện khi có từ 2 ngày.`:'Chưa có dữ liệu.'));return}
 const W=Math.max(280,box.clientWidth||600),H=W<480?210:250,m={l:58,r:62,t:14,b:28};
 let lo=Math.min(...P.map(p=>p.v)),hi=Math.max(...P.map(p=>p.v));const span=hi-lo||Math.abs(hi)*.02||1;
 const raw=span/4,mag=Math.pow(10,Math.floor(Math.log10(raw))),step=[1,2,2.5,5,10].map(s=>s*mag).find(s=>s>=raw);
 lo=Math.floor((lo-span*.08)/step)*step;hi=Math.ceil((hi+span*.08)/step)*step;
 const t0=P[0].t,t1=P[P.length-1].t,X=t=>m.l+(t-t0)/(t1-t0||1)*(W-m.l-m.r),Y=v=>m.t+(hi-v)/(hi-lo)*(H-m.t-m.b);
 const NS='http://www.w3.org/2000/svg',s=document.createElementNS(NS,'svg');s.setAttribute('viewBox',`0 0 ${W} ${H}`);s.setAttribute('tabindex','0');s.setAttribute('role','img');
 s.setAttribute('aria-label',`${unit}: từ ${fmt(P[0].v)} ngày ${dd(P[0].d)} đến ${fmt(P[P.length-1].v)} ngày ${dd(P[P.length-1].d)}`);
 const add=(t,a,p=s)=>{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);p.append(e);return e};
 const ax=add('g',{class:'ax'});
 for(let v=lo;v<=hi+step/2;v+=step){const y=Y(v);add('line',{class:'gl',x1:m.l,x2:W-m.r,y1:y,y2:y},ax);const tx=add('text',{x:m.l-8,y:y+4,'text-anchor':'end'},ax);tx.textContent=fmt(v)}
 const n=P.length,every=Math.max(1,Math.ceil(n/(W<480?4:7)));
 P.forEach((p,i)=>{if(i%every&&i!==n-1)return;const tx=add('text',{x:X(p.t),y:H-8,'text-anchor':i===0?'start':i===n-1?'end':'middle'},ax);tx.textContent=dshort(p.d)});
 add('path',{class:'ln',d:P.map((p,i)=>(i?'L':'M')+X(p.t).toFixed(1)+' '+Y(p.v).toFixed(1)).join('')});
 P.forEach(p=>add('circle',{class:'pt',cx:X(p.t),cy:Y(p.v),r:4}));
 const e=P[n-1],lab=add('text',{class:'endl',x:X(e.t)+8,y:Y(e.v)+4});lab.textContent=fmt(e.v);
 const xh=add('line',{class:'xh',y1:m.t,y2:H-m.b,x1:m.l,x2:m.l,opacity:0});box.append(s);
 const tip=el('div','tip');tip.hidden=true;box.append(tip);
 const show=i=>{const p=P[i];xh.setAttribute('x1',X(p.t));xh.setAttribute('x2',X(p.t));xh.setAttribute('opacity',1);tip.textContent='';tip.append(el('b','',`${fmt(p.v)} ${unit}`),el('span','',dd(p.d)));tip.hidden=false;const r=s.getBoundingClientRect(),k=r.width/W;tip.style.left=Math.min(Math.max(X(p.t)*k,60),r.width-60)+'px';tip.style.top=Math.max(Y(p.v)*k-58,0)+'px';cur=i};
 const hide=()=>{tip.hidden=true;xh.setAttribute('opacity',0)};let cur=n-1;
 s.addEventListener('pointermove',ev=>{const r=s.getBoundingClientRect(),x=(ev.clientX-r.left)*W/r.width;let b=0;P.forEach((p,i)=>{if(Math.abs(X(p.t)-x)<Math.abs(X(P[b].t)-x))b=i});show(b)});
 s.addEventListener('pointerleave',hide);s.addEventListener('blur',hide);s.addEventListener('focus',()=>show(cur));
 s.addEventListener('keydown',ev=>{if(ev.key==='ArrowLeft'){ev.preventDefault();show(Math.max(0,cur-1))}if(ev.key==='ArrowRight'){ev.preventDefault();show(Math.min(n-1,cur+1))}});
}
function hist(){
 const tb=$('histb');tb.textContent='';const L=days().reverse();
 for(const x of L){const tr=el('tr');tr.append(el('td','',dd(x.date)));for(const [k] of PROV)tr.append(el('td','n',x.vn&&x.vn[k]?fm(x.vn[k]):'–'));
  tr.append(el('td','n',x.world&&x.world.robusta?fm(x.world.robusta):'–'),el('td','n',x.world&&x.world.arabica?f2(x.world.arabica):'–'));tb.append(tr)}
}
function srcs(){
 const ul=$('srcl');ul.textContent='';const seen=new Set();const L=days().reverse();
 const add=(s,txt)=>{if(!s||seen.has(s.url))return;seen.add(s.url);const li=el('li');const a=el('a','',s.name);a.href=s.url;a.target='_blank';a.rel='noopener';li.append(a,document.createTextNode(': '+txt));ul.append(li)};
 for(const x of L.slice(0,1))for(const s of x.src||[])add(s,s.name==='Báo Lâm Đồng'?'giá nhân xô Lâm Đồng và các tỉnh, lịch sử theo ngày.':'giá Robusta London, Arabica New York kèm kỳ hạn.');
 for(const q of fsort(D.fresh).slice(0,5))add(q.src,`giá trái tươi ngày ${dd(q.date)}.`);
}
function upd(){const L=days(),x=L[L.length-1];if(!x)return;$('upd').textContent=`${dd(x.date)}${x.time?', '+x.time:''}`}
function charts(){chart('cld',x=>x.vn&&x.vn.lamdong,fm,'đ/kg');chart('crb',x=>x.world&&x.world.robusta,fm,'USD/tấn');chart('car',x=>x.world&&x.world.arabica,f2,'cent/lb')}
function all(){upd();tiles();provTable();freshList();charts();hist();srcs()}
$('rng').addEventListener('click',e=>{const b=e.target.closest('.pill');if(!b)return;range=+b.dataset.r;document.querySelectorAll('#rng .pill').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));charts()});
let rz;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(charts,150)});
all();
fetch('__DATA__',{cache:'no-store'}).then(r=>r.ok?r.json():null).then(j=>{if(j&&j.days&&j.days.length&&(j.updated||'')>=(D.updated||'')){D=j;all()}}).catch(()=>{});
const copyTo=async(t,msg,srcEl,done)=>{try{await navigator.clipboard.writeText(t);$(msg).textContent=done}catch(e){const r=document.createRange();r.selectNodeContents($(srcEl));const s=getSelection();s.removeAllRanges();s.addRange(r);$(msg).textContent='Đã bôi đen, hãy sao chép bằng tay.'}};
$('copyZalo').onclick=()=>copyTo('0966770788','zaloMsg','zaloNo','Đã sao chép số Zalo.');
'''.replace('__DATA__', DATA)

SNAP = json.dumps(SEED, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

BODY = f'''{MNAV}

<div class="wrap">
<header>
  <span class="lgw"><img class="lgL" src="assets/logo-mau.png" alt="MeDili Café Di Linh" width="240" height="77"><img class="lgD" src="assets/logo-kem.png" alt="MeDili Café Di Linh" width="240" height="77"></span><div class="brandbar"><span>Mê vị Di Linh</span></div>
  <h1>Giá Cà Phê <em>Hôm Nay</em></h1>
  <p>Giá cà phê nhân xô Tây Nguyên, giá trái tươi và giá Robusta, Arabica trên sàn thế giới. Trang tự cập nhật mỗi ngày, khoảng 14 giờ.</p>
  <p class="upd">Cập nhật <b id="upd">07/11/2026, 12:37</b>. Giá tham khảo, giá mua thực tế tuỳ đại lý, chất lượng và số lượng.</p>
</header>
<div class="tiles" id="tiles" aria-live="polite"></div>
<div class="bench">
  <div class="card">
    <div class="fighead"><div><b>Hình 1</b> <span>Giá nhân xô Lâm Đồng, đ/kg</span></div></div>
    <div class="row rng" id="rng" role="group" aria-label="Khoảng thời gian"><button class="pill" type="button" data-r="30" aria-pressed="true">30 ngày</button><button class="pill" type="button" data-r="90" aria-pressed="false">90 ngày</button><button class="pill" type="button" data-r="9999" aria-pressed="false">Tất cả</button></div>
    <div class="chartw" id="cld"></div>
  </div>
  <aside class="card ctl">
    <div class="head2"><h3>Các tỉnh hôm nay</h3></div>
    <div class="tw"><table class="pv"><thead><tr><th>Vùng</th><th class="n">Giá</th><th class="n">Thay đổi</th></tr></thead><tbody id="prov"></tbody></table></div>
    <p class="src" id="provd"></p>
    <div class="head2" style="margin-top:14px"><h3>Trái tươi</h3></div>
    <div class="fresh" id="fresh"></div>
    <p class="src">Báo chí không đưa giá trái tươi mỗi ngày. Trang ghi các báo giá gần nhất, kèm ngày và nơi thu mua.</p>
  </aside>
</div>

<section class="card">
  <h2>Giá thế giới</h2>
  <p class="lead">Hợp đồng kỳ hạn gần trên sàn ICE. Mỗi ngày ghi phiên đóng cửa gần nhất.</p>
  <div class="two">
    <div><h3>Robusta London</h3><span class="u">USD/tấn</span><div class="chartw" id="crb"></div></div>
    <div><h3>Arabica New York</h3><span class="u">US cent/lb, 1 lb khoảng 0,454 kg</span><div class="chartw" id="car"></div></div>
  </div>
</section>

<section class="card">
  <h2>Lịch sử giá</h2>
  <p class="lead">Nhân xô đ/kg theo tỉnh, Robusta USD/tấn, Arabica cent/lb. Ngày mới nhất ở trên.</p>
  <div class="tw histw"><table id="hist"><thead><tr><th>Ngày</th><th class="n">Lâm Đồng</th><th class="n">Đắk Lắk</th><th class="n">Gia Lai</th><th class="n">Đắk Nông</th><th class="n">Robusta</th><th class="n">Arabica</th></tr></thead><tbody id="histb"></tbody></table></div>
</section>

<div class="cols">
  <section class="card">
    <h2>Đọc bảng giá</h2>
    <ul class="plain">
      <li><b>Nhân xô:</b> cà phê nhân Robusta chưa phân loại, giá đại lý thu mua.</li>
      <li><b>Trái tươi:</b> trái chín bán tại vườn. Trái chín đều thường được giá cao hơn.</li>
      <li><b>Robusta London:</b> giá sàn ICE châu Âu, tính USD cho một tấn.</li>
      <li><b>Arabica New York:</b> giá sàn ICE Mỹ, tính US cent cho một pound.</li>
      <li><b>Di Linh:</b> các trang giá tính chung mức giá Lâm Đồng cho Di Linh, Bảo Lộc, Lâm Hà.</li>
    </ul>
  </section>
  <section class="card">
    <h2>Một ly theo giá hôm nay</h2>
    <p class="lead" style="margin-bottom:8px">Trang Từ vườn đến ly lấy giá nhân xô mới nhất ở đây để tính phần tiền của người trồng trong một ly cà phê.</p>
    <a class="btn main" href="tu-vuon-den-ly.html">Tính một ly</a>
  </section>
</div>

<section class="card src">
  <h2 style="color:var(--ink)">Nguồn số liệu</h2>
  <ul id="srcl"></ul>
</section>

<section class="contact" id="lien-he">
  <div>
    <img class="lgK" src="assets/logo-kem.png" alt="MeDili Café Di Linh" width="260" height="83">
    <div class="tagline">Mê vị Di Linh</div>
    <p>Cà phê nguồn gốc Di Linh từ Medili Coffee Farm. Liên hệ qua Zalo để tìm hiểu vườn và cà phê.</p>
  </div>
  <div class="zalo">
    <span>Zalo MeDili</span>
    <strong id="zaloNo">0966770788</strong>
    <div><a href="https://zalo.me/3942166996018015136" target="_blank" rel="noopener">Nhắn Zalo</a><button type="button" id="copyZalo">Sao chép số</button></div>
    <small id="zaloMsg" role="status"></small>
  </div>
</section>
<footer>Medili - Farm Robusta Cà Sẻ Di Linh</footer>
</div>
<script type="application/json" id="snap">{SNAP}</script>
'''

DESC = 'Giá cà phê nhân xô Lâm Đồng và Tây Nguyên, giá trái tươi, giá Robusta London và Arabica New York, cập nhật mỗi ngày.'
HEAD = (f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        f'<meta name="description" content="{DESC}"><meta property="og:title" content="Giá Cà Phê MeDili"><meta property="og:description" content="{DESC}">'
        f'<style>*{{box-sizing:border-box}}:root{{padding-top:env(safe-area-inset-top,0);padding-bottom:env(safe-area-inset-bottom,0)}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>'
        f'<title>Giá Cà Phê MeDili</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}\n')
assert '</script' not in JS.lower()
html = HEAD + '<style>' + SHARED + '</style>\n<style>' + PAGE_CSS + '</style></head><body>' + BODY + '\n<script>' + JS + '</script>\n</body></html>\n'
open(os.path.join(OUT, PAGE), 'w', encoding='utf8').write(html)
open(os.path.join(HERE, '_gia.check.js'), 'w', encoding='utf8').write(JS)

# trang Từ vườn đến ly lấy giá nhân xô mới nhất
f2c = rd('tu-vuon-den-ly.html')
HOOK = "calc();\n"
assert f2c.count(HOOK) == 1
LIVEP = ("calc();\n"
         "fetch('" + DATA + "',{cache:'no-store'}).then(r=>r.ok?r.json():null).then(j=>{if(!j||!j.days)return;"
         "const L=[...j.days].filter(x=>x.vn&&x.vn.lamdong).sort((a,b)=>a.date<b.date?-1:1),x=L[L.length-1];if(!x)return;"
         "const i=$('gx');if(num('gx')!==83600||document.activeElement===i)return;"
         "i.value=fm(x.vn.lamdong);const [y,m,d]=x.date.split('-');i.parentElement.querySelector('small').textContent=`Lâm Đồng ngày ${d}/${m}/${y}: ${fm(x.vn.lamdong)} đ/kg, theo trang Giá cà phê.`;calc()}).catch(()=>{});\n")
f2c = f2c.replace(HOOK, LIVEP)
for a, b in [('Phép tính dưới đây dùng giá nhân xô Lâm Đồng ngày 7/11/2026', 'Phép tính dưới đây dùng giá nhân xô Lâm Đồng sáng 7/11/2026'),
             ('<small>Lâm Đồng ngày 7/11/2026: 83.600&nbsp;đ/kg.</small>', '<small>Lâm Đồng sáng 7/11/2026: 83.600&nbsp;đ/kg.</small>'),
             ('Báo Lào Cai, 7/11/2026</a>: giá nhân xô Lâm Đồng 83.600&nbsp;đ/kg.', 'Báo Lào Cai, 7/11/2026</a>: giá nhân xô Lâm Đồng buổi sáng 83.600&nbsp;đ/kg, dùng cho phép tính mẫu.')]:
    assert f2c.count(a) == 1, a
    f2c = f2c.replace(a, b)
pages = {'tu-vuon-den-ly.html': f2c}
for f in ['index.html', 'vuon.html', 'trai-ca-phe.html', 'len-men-men-bia.html', 'len-men-trai-cay.html', 'rang.html', 'quay-pha.html', 'suc-khoe.html', 'mua-hang.html']:
    pages[f] = rd(f)
for f, h in pages.items():
    open(os.path.join(OUT, f), 'w', encoding='utf8').write(nav(h))
print('trang giá', len(html.encode()) // 1024, 'KB')
