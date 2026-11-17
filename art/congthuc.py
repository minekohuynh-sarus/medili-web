# Cỗ máy Công thức pha: bốn bước (sơ chế, mức rang, cách pha, kỹ thuật) ra một công thức pha cụ thể:
# liều cà phê, nước, tỷ lệ, nhiệt độ, độ xay, thời gian, lịch rót, gợi ý chỉnh vị và cà phê MeDili hợp công thức.
# Cấu trúc theo dạng "trình tạo công thức pha" chị Ngân gửi ngày 17/11/2026, viết lại theo kiểu Cỗ máy của MeDili,
# đủ 4 cách pha (V60, phin, espresso, cold brew). Số liệu là mốc khởi đầu chung của nghề pha.
# Chị Ngân dặn: KHÔNG trích dẫn nguồn trên trang này. Màu theo mệnh Thổ: không xanh lá, không đen, tránh xanh dương.
import json, re
from kit import *
from pages_a import head

FILE = 'cong-thuc-pha.html'
TITLE = 'Cỗ máy Công thức pha MeDili'
DESC = ('Bốn bước ra công thức pha cà phê của riêng bạn: chọn sơ chế, mức rang, cách pha V60, phin, espresso hay cold brew '
        'và kỹ thuật. Cỗ máy tính liều cà phê, nước, nhiệt độ, độ xay, thời gian, từng lần rót và gợi ý cà phê MeDili hợp gu.')

# cà phê MeDili hợp từng cách pha, theo thứ tự ưu tiên (mã trong cuahang.py)
PICK = {'v60': ['aw', 'an', 'ng-suong', 'acd', 'ma'],
        'phin': ['pc', 'ng-nui', 'pp', 'ng-nang', 'pa', 'cul'],
        'esp': ['mp', 'b73', 'ng-rung', 'ng-may', 'ma', 'b91', 'mc'],
        'cold': ['ng-nang', 'ng-suoi', 'pp', 'b55']}


def _rk(roast):
    t = roast.lower()
    for k, v in (('medium-dark', 'vd'), ('medium dark', 'vd'), ('medium-light', 'sv'), ('medium light', 'sv'),
                 ('dark', 'd'), ('đậm', 'd'), ('medium', 'v'), ('light', 's')):
        if k in t:
            return v
    return None


def _method(x):
    if x['kind'] == 'phin': return 'phin'
    if x['kind'] == 'may': return 'esp'
    b = x['brews']
    return {'phin': 'phin', 'espresso': 'esp', 'v60': 'v60', 'coldbrew': 'cold'}[b[0]] if b else 'phin'


CSS = r'''
.rx-quick{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px}
.rx-quick label{display:flex;flex-wrap:wrap;align-items:center;gap:8px;font:600 .92rem var(--body)}
.rx-quick select{font:500 .95rem var(--body);color:var(--ink);background:var(--bg);border:1px solid var(--rule);border-radius:10px;padding:8px 10px;max-width:100%}
.rx-steps{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.rx-step{background:var(--panel);border:1px solid var(--rule);border-radius:16px;padding:16px 18px;display:grid;grid-template-columns:minmax(0,1fr);gap:10px;align-content:start;min-width:0}
.rx-hd{display:flex;align-items:baseline;gap:12px}
.rx-n{font:800 2.2rem/1 var(--display);color:var(--accent)}
.rx-hd h2{font:800 1.5rem/1.1 var(--display);margin:0}
.rx-opts{display:flex;flex-wrap:wrap;gap:6px}
.rx-opts button{font:600 .88rem/1.2 var(--body);border:1px solid var(--rule);background:var(--bg);color:var(--ink);border-radius:999px;padding:8px 13px;cursor:pointer}
.rx-opts button:hover{border-color:var(--accent)}
.rx-opts button[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.rx-opts.big button{display:grid;justify-items:center;gap:4px;border-radius:14px;padding:10px 12px;min-width:96px}
.rx-opts.big svg{width:34px;height:34px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.rx-d{margin:0;font-size:.9rem;color:var(--muted);min-height:2.6em}
.rx-out{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:18px;align-items:start}
.rx-fig{background:var(--tint);border-radius:20px;padding:18px;display:grid;gap:12px;position:sticky;top:calc(72px + env(safe-area-inset-top,0px))}
.rx-fig svg.rx-scene{display:block;width:100%;max-width:300px;height:auto;margin:auto}
.rx-scene .o{stroke:var(--ink);stroke-width:2.2;stroke-linejoin:round;stroke-linecap:round}
.rx-scene .t{font:600 11px var(--body);fill:var(--muted)}
.rx-drop{animation:rxdrop 1.6s ease-in infinite}
.rx-drop.d2{animation-delay:.8s}
@keyframes rxdrop{0%{transform:translateY(0);opacity:0}15%{opacity:1}100%{transform:translateY(26px);opacity:0}}
@media (prefers-reduced-motion:reduce){.rx-drop{animation:none}}
.rx-tl{display:block;width:100%;height:auto}
.rx-tl text{font:600 10.5px var(--mono);fill:var(--muted)}
.rx-tl .lb{font:600 10.5px var(--body);fill:var(--ink)}
.rx-cap{margin:0;font-size:.84rem;color:var(--muted);text-align:center}
.rx-card{background:var(--panel);border:2px solid var(--accent);border-radius:18px;padding:18px 20px;display:grid;grid-template-columns:minmax(0,1fr);gap:14px;min-width:0}
.rx-ttl{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:6px 14px}
.rx-ttl h2{font:800 1.9rem/1.1 var(--display);margin:0}
.rx-sum{display:flex;flex-wrap:wrap;gap:6px}
.rx-sum span{font:600 .76rem var(--body);border:1px solid var(--rule);border-radius:999px;padding:4px 10px;background:var(--bg)}
.rx-dose{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;background:var(--tint);border-radius:12px;padding:10px 12px}
.rx-dose b{font:600 .92rem var(--body)}
.rx-st{display:inline-flex;align-items:center;border:1px solid var(--rule);border-radius:999px;overflow:hidden;background:var(--panel)}
.rx-st button{width:40px;height:40px;border:0;background:transparent;color:var(--ink);font:600 1.2rem/1 var(--body);cursor:pointer}
.rx-st button:hover{background:var(--tint)}
.rx-st input{width:64px;border:0;background:transparent;color:var(--ink);text-align:center;font:700 1.1rem var(--mono);padding:6px 0}
.rx-par{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.rx-par div{background:var(--bg);border-radius:12px;padding:9px 11px;min-width:0}
.rx-par span{display:block;font:600 .68rem/1.3 var(--body);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.rx-par b{display:block;font:700 1.12rem/1.3 var(--mono);overflow-wrap:anywhere}
.rx-par small{display:block;font-size:.78rem;color:var(--muted);line-height:1.35;margin-top:2px}
.rx-pours{width:100%;border-collapse:collapse;font-size:.9rem}
.rx-pours th{font:600 .7rem var(--body);letter-spacing:.07em;text-transform:uppercase;color:var(--muted);text-align:left;padding:4px 8px 6px 0;border-bottom:1px solid var(--rule)}
.rx-pours td{padding:7px 8px 7px 0;border-bottom:1px solid var(--rule);vertical-align:top;white-space:normal}
.rx-pours th{white-space:normal}
.rx-pours td.m{font:700 .92rem var(--mono);white-space:nowrap}
.rx-pours td small{display:block;color:var(--muted);font-size:.8rem}
.rx-bal{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.rx-bal button{font:600 .82rem var(--body);border:1px solid var(--rule);background:var(--bg);color:var(--ink);border-radius:999px;padding:6px 11px;cursor:pointer}
.rx-bal output{font:600 .82rem var(--body);color:var(--muted)}
.rx-tips{margin:0;padding-left:1.1em;display:grid;gap:5px;font-size:.92rem}
.rx-sp{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.rx-sp a{display:grid;gap:2px;border:1px solid var(--rule);border-radius:12px;padding:9px 11px;text-decoration:none;color:var(--ink);background:var(--bg);min-width:0}
.rx-sp a:hover{border-color:var(--accent)}
.rx-sp i{display:block;width:18px;height:22px;border-radius:2px 2px 4px 4px;background:var(--c);clip-path:polygon(12% 0,88% 0,100% 10%,100% 100%,0 100%,0 10%)}
.rx-sp b{font:700 .92rem/1.25 var(--body)}
.rx-sp small{color:var(--muted);font-size:.78rem}
.rx-act{display:flex;flex-wrap:wrap;gap:8px}
.rx-msg{margin:0;font-size:.85rem;color:var(--muted);min-height:1.2em}
.rx-cmp{overflow-x:auto}
.rx-cmp table{border-collapse:collapse;width:100%;min-width:640px;font-size:.9rem}
.rx-cmp th,.rx-cmp td{text-align:left;padding:8px 10px 8px 0;border-bottom:1px solid var(--rule);vertical-align:top}
.rx-cmp th{font:600 .72rem var(--body);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.rx-cmp td{white-space:normal}.rx-cmp td:first-child{font-weight:700;white-space:nowrap}
.rx-fix{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:12px}
.rx-fix .box h3{font:800 1.25rem/1.15 var(--display);margin:0 0 4px}
@media (max-width:980px){.rx-out{grid-template-columns:minmax(0,1fr)}.rx-fig{position:static}}
@media (max-width:760px){.rx-steps{grid-template-columns:minmax(0,1fr)}.rx-par{grid-template-columns:repeat(2,minmax(0,1fr))}.rx-sp{grid-template-columns:minmax(0,1fr)}}
@media print{.mh,.mf,.p-head,.rx-quick,.rx-steps,.rx-fig,.rx-more,.contact,.rx-act,.rx-msg,.rx-bal button,.rx-dose .rx-st button{display:none!important}
 .rx-out{display:block}.rx-card{border:1px solid #999}body{background:#fff}}
'''

JS = r'''
const PC={washed:{n:'Washed',d:'Xát vỏ, lên men, rửa sạch nhớt rồi phơi. Ly sạch, thanh, chua sáng.',t:0,g:0},
 honey:{n:'Honey',d:'Giữ lại một phần lớp nhớt khi phơi. Ngọt hơn, thân tròn hơn washed.',t:-1,g:0},
 natural:{n:'Natural',d:'Phơi nguyên trái. Hương trái cây chín, ngọt đậm, thân dày.',t:-1,g:20},
 anaerobic:{n:'Natural yếm khí',d:'Ủ trái trong thùng kín trước khi phơi. Hương lên men rõ, như trái cây chín, rượu vang.',t:-2,g:40}};
const RO={rs:{n:'Rất sáng',d:'Hạt còn cứng, chua sáng và hương hoa nhiều.',t:2,g:-60},
 s:{n:'Sáng',d:'Chua sáng, hương trái cây rõ.',t:1,g:-30},
 sv:{n:'Sáng vừa',d:'Cân bằng giữa chua và ngọt.',t:0,g:0},
 v:{n:'Vừa',d:'Ngọt caramel, thân vừa, chua dịu.',t:-1,g:20},
 vd:{n:'Vừa đậm',d:'Đường nâu, cacao, đắng nhẹ.',t:-2,g:40},
 d:{n:'Đậm',d:'Đậm, đắng rõ, chocolate đen. Kiểu rang của ly phin truyền thống.',t:-3,g:60}};
const ICON={v60:'<svg viewBox="0 0 36 36" aria-hidden="true"><path d="M7 9h22l-8 13h-6z"/><path d="M12 26h12v5H12z"/><path d="M15 22v4M21 22v4"/></svg>',
 phin:'<svg viewBox="0 0 36 36" aria-hidden="true"><path d="M11 7h14v10H11z"/><path d="M8 17h20"/><path d="M12 20h12l-1.5 11h-9z"/></svg>',
 esp:'<svg viewBox="0 0 36 36" aria-hidden="true"><path d="M8 8h16v5H8z"/><path d="M24 10h6"/><path d="M11 18h12v6a5 5 0 0 1-5 5h-2a5 5 0 0 1-5-5z"/><path d="M23 20h2a2.5 2.5 0 0 1 0 5h-2"/></svg>',
 cold:'<svg viewBox="0 0 36 36" aria-hidden="true"><path d="M11 6h14v3H11z"/><path d="M10 9h16v20a2 2 0 0 1-2 2H12a2 2 0 0 1-2-2z"/><path d="M10 17h16"/><circle cx="27" cy="27" r="5"/><path d="M27 24.5V27l1.8 1.2"/></svg>'};
const M={
 v60:{n:'Pour over V60',d:'Phễu nón, giấy lọc, rót tay. Ly sạch, rõ hương, hợp Arabica rang sáng đến vừa.',temp:94,cold:0,
  T:{'46':{n:'4:6 · năm lần rót',d:'Hai lần rót đầu chỉnh chua và ngọt, ba lần sau chỉnh độ đậm.',dose:20,r:15,g:950,end:210},
     one:{n:'Ủ rồi rót một lần',d:'Ủ 45 giây, rót hết nước trong một lần, xoáy nhẹ rồi để chảy hết.',dose:15,r:16.5,g:650,end:180},
     three:{n:'Ba lần rót',d:'Ủ rồi rót hai lần đều nhau. Dễ làm, ly cân bằng.',dose:15,r:16,g:750,end:180},
     pulse:{n:'Rót nhịp',d:'Ủ rồi rót bốn nhịp nhỏ, nước luôn ngập bã. Ly ngọt và dày.',dose:15,r:16,g:700,end:195}}},
 phin:{n:'Phin',d:'Phin nhôm hoặc inox, nhỏ giọt chậm. Ly đậm, thân dày, hợp Robusta rang vừa đến đậm.',temp:94,cold:0,
  T:{nong:{n:'Phin đen nóng',d:'Ly đen nóng, uống chậm.',dose:20,r:5,g:600,end:270},
     da:{n:'Phin đen đá',d:'Pha đậm hơn vì đá tan sẽ làm loãng.',dose:22,r:3.6,g:600,end:270},
     sua:{n:'Phin sữa đá',d:'Cà phê sữa kiểu Sài Gòn: cà phê đậm, sữa đặc, đá.',dose:25,r:2.8,g:580,end:270},
     bx:{n:'Bạc xỉu',d:'Nhiều sữa, ít cà phê, vị béo và dịu.',dose:15,r:3,g:600,end:240}}},
 esp:{n:'Espresso',d:'Máy pha áp suất 9 bar. Ly ngắn, đặc, nhiều crema, làm nền cho Americano, latte, cappuccino.',temp:93,cold:0,
  T:{esp:{n:'Espresso 1:2',d:'Một shot đôi chuẩn, cân bằng giữa đậm và ngọt.',dose:18,r:2,g:250,end:28},
     ris:{n:'Ristretto 1:1,5',d:'Shot ngắn hơn, đặc và ngọt, ít đắng.',dose:18,r:1.5,g:230,end:23},
     lun:{n:'Lungo 1:3',d:'Shot dài hơn, nhẹ hơn, rõ hương nhưng dễ đắng.',dose:18,r:3,g:280,end:36},
     ame:{n:'Americano',d:'Một shot 1:2 pha thêm nước nóng.',dose:18,r:2,g:250,end:28},
     lat:{n:'Latte',d:'Một shot 1:2 với sữa đánh nóng, lớp bọt mỏng.',dose:18,r:2,g:250,end:28},
     cap:{n:'Cappuccino',d:'Một shot 1:2 với sữa nhiều bọt.',dose:18,r:2,g:250,end:28}}},
 cold:{n:'Cold brew',d:'Ngâm lạnh nhiều giờ. Ly êm, ngọt, ít chua, uống mát.',temp:0,cold:1,
  T:{cot:{n:'Cốt đậm đặc 1:5',d:'Ngâm cốt đặc, khi uống pha thêm nước hoặc sữa theo tỷ lệ 1:1.',dose:100,r:5,g:1100,end:16},
     lien:{n:'Uống liền 1:10',d:'Ngâm loãng, lọc xong uống ngay, không cần pha thêm.',dose:60,r:10,g:1100,end:18},
     sua:{n:'Cold brew sữa',d:'Cốt 1:5 pha với sữa tươi, thêm sữa đặc tuỳ gu.',dose:100,r:5,g:1100,end:16},
     jp:{n:'Pha nóng trên đá',d:'Pha nóng nhanh lên đá: thơm như pour over, mát ngay.',dose:20,r:15,g:650,end:165}}}};
const PICK=__PICK__,SP=__SP__,SPI=Object.fromEntries(SP.map(x=>[x.id,x]));
const K='medili-congthuc-1';
let S={pc:'washed',ro:'sv',m:'v60',t:'46',dose:20,sh:0};
try{const v=JSON.parse(localStorage.getItem(K)||'null');if(v&&M[v.m]&&M[v.m].T[v.t])S=Object.assign(S,v)}catch(e){}
const $=id=>document.getElementById(id);
const fm=n=>Math.round(n).toLocaleString('vi-VN').replace(/,/g,'.');
const f1=n=>(Math.round(n*10)/10).toLocaleString('vi-VN');
const mmss=s=>{s=Math.round(s);return Math.floor(s/60)+':'+String(s%60).padStart(2,'0')};
const E=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const grindTxt=g=>g<350?'mịn, cho máy espresso':g<600?'vừa mịn, như muối ăn':g<850?'vừa, như cát':g<1050?'vừa thô, như muối biển':'thô, như muối hột';

function recipe(){
 const m=M[S.m],t=m.T[S.t],ro=RO[S.ro],pc=PC[S.pc],d=+S.dose;
 const esp=S.m==='esp';
 const temp=m.cold&&S.t!=='jp'?null:Math.max(86,Math.min(96,(S.t==='jp'?94:m.temp)+(esp?Math.round(ro.t/2):ro.t)+pc.t));
 const gAdj=esp?Math.round(ro.g/4)+Math.round(pc.g/4):ro.g+pc.g,g=Math.max(150,t.g+gAdj);
 const R={temp,g,pours:[],ing:[],par:[],tips:[],end:t.end,unit:'s'};
 let W=d*t.r;
 if(S.m==='v60'){
  R.water=W;
  if(S.t==='46'){const q=W*.2,sh=Math.max(-q*.6,Math.min(q*.6,+S.sh||0));
   R.pours=[{at:0,w:q+sh,n:'Rót đều từ tâm ra, chờ hạt nở'},{at:45,w:q-sh,n:'Lần 2: cùng nhóm chỉnh chua ngọt'},{at:90,w:q,n:'Bắt đầu nhóm chỉnh độ đậm'},{at:130,w:q,n:''},{at:165,w:q,n:'Lần cuối, để chảy hết'}];R.bal=sh}
  else if(S.t==='one'){const b=d*2;R.pours=[{at:0,w:b,n:'Ủ, xoáy nhẹ cho bã ướt đều'},{at:45,w:W-b,n:'Rót liên tục đến hết, xong trước 1:45'},{at:105,w:0,n:'Xoáy nhẹ cho mặt bã phẳng'}]}
  else if(S.t==='three'){const b=d*2.5;R.pours=[{at:0,w:b,n:'Ủ 45 giây'},{at:45,w:W*.6-b,n:'Rót đến 60 % lượng nước'},{at:90,w:W*.4,n:'Rót đến đủ, để chảy hết'}]}
  else {const b=d*2,p=(W-b)/4;R.pours=[{at:0,w:b,n:'Ủ 40 giây'},{at:40,w:p,n:'Nhịp 1'},{at:65,w:p,n:'Nhịp 2'},{at:90,w:p,n:'Nhịp 3'},{at:115,w:p,n:'Nhịp 4, để chảy hết'}]}
  R.par=[['Nước',fm(W)+' g',''],['Tỷ lệ','1:'+f1(t.r),''],['Nhiệt độ',temp+' °C','nước vừa sôi để nguội chút'],['Độ xay','≈ '+g+' µm',grindTxt(g)],['Thời gian',mmss(t.end),'tính cả lúc chảy hết'],['Ra ly','≈ '+fm(W-d*2)+' ml','bã giữ lại khoảng gấp đôi lượng cà phê']];
 } else if(S.m==='phin'){
  R.water=W;const b=d;R.pours=[{at:0,w:b,n:'Ủ: tưới ướt đều mặt cà phê, chờ hạt nở'},{at:40,w:W-b,n:'Đổ đầy, đậy nắp, chờ nhỏ giọt'}];
  if(S.t==='da')R.ing=[['Đá viên','≈ 150 g'],['Đường','tuỳ gu']];
  if(S.t==='sua')R.ing=[['Sữa đặc',fm(d)+' ml'],['Đá viên','≈ 150 g']];
  if(S.t==='bx')R.ing=[['Sữa đặc',fm(d*2)+' ml'],['Sữa tươi',fm(d*4)+' ml'],['Đá viên','≈ 120 g']];
  R.par=[['Nước',fm(W)+' ml',''],['Tỷ lệ','1:'+f1(t.r),S.t==='nong'?'':'pha đậm vì còn sữa, đá'],['Nhiệt độ',temp+' °C','nước sôi để khoảng 30 giây'],['Độ xay','≈ '+g+' µm',grindTxt(g)],['Thời gian',mmss(t.end),'giọt chảy hết'],['Ra ly','≈ '+fm(W-d*1.6)+' ml','cà phê đậm']];
 } else if(esp){
  const y=d*t.r;R.water=y;R.pours=[{at:0,w:0,n:'Bấm chiết, vài giây đầu ngấm bã'},{at:7,w:y*.15,n:'Giọt đầu ra, màu nâu sậm'},{at:t.end,w:y*.85,n:'Ngắt khi đủ '+f1(y)+' g'}];
  if(S.t==='ame')R.ing=[['Nước nóng',fm(y*4)+' ml']];
  if(S.t==='lat')R.ing=[['Sữa tươi',fm(d*11)+' ml','đánh nóng 60–65 °C, bọt mỏng']];
  if(S.t==='cap')R.ing=[['Sữa tươi',fm(d*7)+' ml','đánh nhiều bọt']];
  R.par=[['Ra shot',f1(y)+' g','cân trên đĩa cân'],['Tỷ lệ','1:'+f1(t.r),''],['Nhiệt độ',temp+' °C','nhiệt độ nước của máy'],['Độ xay','≈ '+g+' µm',grindTxt(g)],['Thời gian',(t.end-3)+'–'+(t.end+2)+' giây','tính từ lúc bấm'],['Áp suất','9 bar','']];
 } else {
  if(S.t==='jp'){const tot=d*t.r,ice=tot*.4,hot=tot*.6;R.water=hot;R.pours=[{at:0,w:d*2,n:'Ủ 40 giây trên đá'},{at:40,w:hot-d*2,n:'Rót đến đủ nước nóng'}];R.ing=[['Đá trong bình',fm(ice)+' g','đá làm lạnh và pha loãng ly']];
   R.par=[['Nước nóng',fm(hot)+' g','cộng '+fm(ice)+' g đá'],['Tỷ lệ','1:'+f1(t.r),'tính cả đá'],['Nhiệt độ',temp+' °C',''],['Độ xay','≈ '+g+' µm',grindTxt(g)],['Thời gian',mmss(t.end),''],['Ra ly','≈ '+fm(tot-d*2)+' ml','uống ngay']]}
  else {R.unit='h';R.water=W;R.pours=[{at:0,w:W,n:'Đổ nước lạnh hoặc nước nguội, khuấy cho ướt đều'},{at:t.end,w:0,n:'Lọc qua giấy lọc hoặc túi vải'}];
   if(S.t!=='lien')R.ing=[[S.t==='sua'?'Sữa tươi khi uống':'Nước hoặc sữa khi uống','1 phần cốt : 1 phần',S.t==='sua'?'thêm sữa đặc tuỳ gu':'']];
   R.par=[['Nước',fm(W)+' ml','nước lạnh hoặc nhiệt độ phòng'],['Tỷ lệ','1:'+f1(t.r),S.t==='lien'?'uống liền':'cốt đậm đặc'],['Nhiệt độ','Lạnh','ngâm trong tủ lạnh 4 °C'],['Độ xay','≈ '+g+' µm',grindTxt(g)],['Thời gian',(t.end-2)+'–'+(t.end+2)+' giờ',''],['Ra','≈ '+fm(W-d*2)+' ml',S.t==='lien'?'':'cốt, pha 1:1 khi uống']]}
 }
 // gợi ý chỉnh
 const T=R.tips;
 if(S.ro==='rs'||S.ro==='s')T.push('Rang sáng hạt còn cứng: nước nóng hơn, xay mịn hơn một chút để ra đủ ngọt.');
 if(S.ro==='vd'||S.ro==='d')T.push('Rang đậm dễ ra đắng: giữ nước thấp hơn, rót nhẹ tay, đừng để quá giờ.');
 if(S.pc==='natural'||S.pc==='anaerobic')T.push('Hương trái cây và lên men mạnh: nhiệt thấp hơn một chút để ly không gắt.');
 if(S.pc==='washed')T.push('Washed cho ly thanh và sạch. Thấy mỏng thì tăng thêm 1 g cà phê.');
 if(S.m==='phin')T.push('Gài nắp nén nhẹ tay, không ép chặt. Khoảng 2 đến 3 giây một giọt là vừa.');
 if(esp)T.push('Giữ liều cố định, chỉnh độ xay trước. Shot chảy dưới 22 giây: xay mịn hơn. Trên 35 giây: xay thô hơn.');
 if(S.m==='cold'&&S.t!=='jp')T.push('Giữ lạnh, dùng trong 7 ngày. Xay thô để nước trong, dễ lọc.');
 if(S.m==='v60')T.push('Tráng giấy lọc bằng nước nóng trước khi cho cà phê vào để bỏ mùi giấy.');
 T.push('Chua gắt, nhạt: xay mịn hơn một nấc hoặc tăng 1 đến 2 °C. Đắng, khô miệng: xay thô hơn hoặc giảm 1 đến 2 °C.');
 return R}

function picks(){const L=(PICK[S.m]||[]).map(i=>SPI[i]).filter(Boolean);
 return L.map((x,i)=>[x,(x.pk.includes(S.pc)?2:0)+(x.rk===S.ro?1.5:0)+(x.st==='ban'?.6:0)-i*.01]).sort((a,b)=>b[1]-a[1]).slice(0,3).map(a=>a[0])}

// ---------- hình dụng cụ ----------
const LIQ='var(--i-coffee)',MILK='var(--i-milk)',CON='#E9D3AE',ICE='rgba(255,246,234,.75)',STREAM='#C69A62';
function scene(R){const m=S.m,t=S.t;let s='';
 const drops=x=>`<ellipse class="rx-drop" cx="${x}" cy="0" rx="2.4" ry="3.6" fill="${LIQ}"/><ellipse class="rx-drop d2" cx="${x}" cy="0" rx="2" ry="3" fill="${LIQ}"/>`;
 const ice=(x,y)=>`<rect x="${x}" y="${y}" width="20" height="18" rx="4" fill="${ICE}" stroke="var(--rule)"/>`;
 // ly có thành nghiêng: x0,x1 mép trên, y0,y1 đỉnh và đáy, k độ nghiêng mỗi bên
 const G=(x0,x1,y0,y1,k)=>({l:y=>x0+k*(y-y0)/(y1-y0),r:y=>x1-k*(y-y0)/(y1-y0)});
 const band=(g,ya,yb,fill,op)=>`<path d="M${g.l(ya)} ${ya}H${g.r(ya)}L${g.r(yb)} ${yb}H${g.l(yb)}z" fill="${fill}"${op?` opacity="${op}"`:''}/>`;
 if(m==='v60'||(m==='cold'&&t==='jp')){
  s+=`<path class="o" d="M150 30c20-12 44-6 52 12" fill="none"/><path d="M152 40c-14 6-28 12-38 22" stroke="${STREAM}" stroke-width="4" fill="none" stroke-linecap="round"/>`;
  s+=`<path class="o" d="M60 60h100l-34 52h-32z" fill="var(--panel)"/><path d="M68 66h84" stroke="var(--rule)" stroke-width="2"/><path d="M84 72l14 34M136 72l-14 34M110 70v38" stroke="var(--rule)" stroke-width="1.5"/>`;
  s+=`<g transform="translate(110,116)">${drops(0)}</g>`;
  const g=G(72,148,146,200,6);s+=`<path class="o" d="M72 146H148L142 200H78z" fill="var(--panel)"/>`+band(g,t==='jp'?168:176,200,LIQ);
  if(t==='jp')s+=ice(84,160)+ice(112,154);
  s+=`<path class="o" d="M72 146H148L142 200H78z" fill="none"/><rect class="o" x="66" y="138" width="88" height="10" rx="4" fill="var(--i-gold2)"/>`;
 } else if(m==='phin'){
  s+=`<rect class="o" x="84" y="22" width="52" height="10" rx="4" fill="var(--i-gold2)"/><path class="o" d="M86 34h48l-4 46H90z" fill="var(--i-gold)"/><rect class="o" x="66" y="80" width="88" height="9" rx="4" fill="var(--i-gold2)"/>`;
  s+=`<g transform="translate(110,96)">${drops(0)}</g>`;
  const g=G(70,150,122,204,8),milk={sua:16,bx:34}[t]||0,cof={nong:52,da:40,sua:30,bx:18}[t];
  s+=`<path class="o" d="M70 122H150L142 204H78z" fill="var(--panel)"/>`;
  if(milk)s+=band(g,204-milk,204,t==='bx'?MILK:CON);
  s+=band(g,204-milk-cof,204-milk,LIQ,.95);
  if(t!=='nong')s+=ice(82,150)+ice(108,142)+ice(96,164);
  s+=`<path class="o" d="M70 122H150L142 204H78z" fill="none"/>`;
 } else if(m==='esp'){
  s+=`<rect class="o" x="52" y="30" width="116" height="20" rx="6" fill="var(--i-brown)"/><path class="o" d="M80 50h60v14H80z" fill="var(--i-gold2)"/><path class="o" d="M140 56h44" stroke-width="7"/>`;
  s+=`<g transform="translate(102,72)">${drops(0)}</g><g transform="translate(118,72)">${drops(0)}</g>`;
  if(t==='lat'||t==='ame'||t==='cap'){const g=G(74,146,102,204,6);s+=`<path class="o" d="M74 102H146L140 204H80z" fill="var(--panel)"/>`;
   if(t==='ame')s+=band(g,126,204,LIQ,.85);
   else s+=band(g,t==='cap'?112:120,t==='cap'?146:132,'#F6EAD6')+band(g,t==='cap'?146:132,178,MILK)+band(g,178,204,LIQ,.9);
   s+=`<path class="o" d="M74 102H146L140 204H80z" fill="none"/>`}
  else{const h=t==='ris'?24:t==='lun'?42:32;
   s+=`<path class="o" d="M82 136h56v34a20 20 0 0 1-20 20h-16a20 20 0 0 1-20-20z" fill="var(--panel)"/><path class="o" d="M138 146h8a10 10 0 0 1 0 20h-9" fill="none"/>`;
   s+=`<path d="M85 ${186-h}h50v${h-16}a17 17 0 0 1-17 17h-16a17 17 0 0 1-17-17z" fill="${LIQ}"/><path d="M85 ${186-h}h50v5H85z" fill="var(--i-gold)"/>`;
   s+=`<path class="o" d="M82 136h56v34a20 20 0 0 1-20 20h-16a20 20 0 0 1-20-20z" fill="none"/><ellipse class="o" cx="110" cy="196" rx="44" ry="7" fill="var(--panel)"/>`}
 } else {
  s+=`<rect class="o" x="62" y="34" width="96" height="16" rx="5" fill="var(--i-gold2)"/><path class="o" d="M58 50h104v146a10 10 0 0 1-10 10H68a10 10 0 0 1-10-10z" fill="var(--panel)"/>`;
  s+=`<path d="M61 ${t==='lien'?84:110}h98v86a8 8 0 0 1-8 8H69a8 8 0 0 1-8-8z" fill="${LIQ}" opacity=".88"/><path d="M61 172h98v24a8 8 0 0 1-8 8H69a8 8 0 0 1-8-8z" fill="var(--i-brown)"/>`;
  s+=`<path class="o" d="M58 50h104v146a10 10 0 0 1-10 10H68a10 10 0 0 1-10-10z" fill="none"/>`;
  s+=`<circle class="o" cx="186" cy="62" r="20" fill="var(--panel)"/><path class="o" d="M186 50v12l8 6" fill="none"/><text class="t" x="186" y="100" text-anchor="middle">${t==='lien'?'16–20 giờ':'14–18 giờ'}</text>`;
 }
 return `<svg class="rx-scene" viewBox="0 0 220 220" role="img" aria-label="${E(M[S.m].T[S.t].n)}">${s}</svg>`}

// ---------- trục thời gian ----------
function timeline(R){const W=640,H=130,x0=34,x1=W-16,y0=100,top=18;const end=Math.max(R.end,...R.pours.map(p=>p.at))||1;
 const X=a=>x0+(x1-x0)*a/end;let cum=0;const pts=[[X(0),y0]];const tot=R.pours.reduce((a,p)=>a+p.w,0)||1;
 let s=`<line x1="${x0}" y1="${y0}" x2="${x1}" y2="${y0}" stroke="var(--rule)" stroke-width="2"/>`;
 R.pours.forEach((p,i)=>{const x=X(p.at);const yPrev=y0-(y0-top)*cum/tot;cum+=p.w;const y=y0-(y0-top)*cum/tot;
  pts.push([x,yPrev],[x,y]);
  if(p.w>0)s+=`<rect x="${x-4}" y="${y}" width="8" height="${y0-y}" rx="3" fill="var(--accent)" opacity="${.35+.5*(i===0?1:.7)}"/>`;
  s+=`<circle cx="${x}" cy="${y0}" r="4" fill="var(--accent)"/><text x="${x}" y="${y0+16}" text-anchor="middle">${R.unit==='h'?(p.at?p.at+' giờ':'0'):mmss(p.at)}</text>`;
  if(p.w>0&&R.unit!=='h'&&S.m!=='esp')s+=`<text class="lb" x="${x+6}" y="${Math.max(top+8,y-4)}">${fm(cum)} g</text>`});
 pts.push([X(end),y0-(y0-top)*cum/tot]);
 s+=`<polyline points="${pts.map(p=>p.join(',')).join(' ')}" fill="none" stroke="var(--ink)" stroke-width="2" stroke-dasharray="5 4"/>`;
 s+=`<line x1="${X(end)}" y1="${top}" x2="${X(end)}" y2="${y0}" stroke="var(--muted)" stroke-dasharray="3 4"/><text x="${X(end)}" y="${y0+30}" text-anchor="end">xong ${R.unit==='h'?end+' giờ':mmss(end)}</text>`;
 return `<svg class="rx-tl" viewBox="0 0 ${W} ${H+8}" role="img" aria-label="Trục thời gian các lần rót">${s}</svg>`}

// ---------- vẽ ----------
function opts(id,obj,cur,k,big){$(id).innerHTML=Object.entries(obj).map(([v,o])=>`<button type="button" data-k="${k}" data-v="${v}" aria-pressed="${v===cur}">${big?ICON[v]:''}<span>${E(o.n)}</span></button>`).join('')}
function save(){try{localStorage.setItem(K,JSON.stringify(S))}catch(e){}}
function text(R){const m=M[S.m],t=m.T[S.t];const L=['CÔNG THỨC PHA · MEDILI',`${PC[S.pc].n} · Rang ${RO[S.ro].n.toLowerCase()} · ${m.n} · ${t.n}`,'',`Cà phê: ${f1(S.dose)} g`];
 R.par.forEach(p=>L.push(`${p[0]}: ${p[1]}${p[2]?' ('+p[2]+')':''}`));R.ing.forEach(i=>L.push(`${i[0]}: ${i[1]}${i[2]?' ('+i[2]+')':''}`));
 L.push('','Các bước:');R.pours.forEach((p,i)=>L.push(`${i+1}. ${R.unit==='h'?(p.at?p.at+' giờ':'Bắt đầu'):mmss(p.at)}${p.w>0&&S.m!=='esp'?' · rót '+fm(p.w)+' g':''}${p.n?' · '+p.n:''}`));
 L.push('','medili.vn · Công thức là mốc khởi đầu, nếm rồi chỉnh theo gu.');return L.join('\n')}
function render(){
 const m=M[S.m],t=m.T[S.t];opts('rx-pc',PC,S.pc,'pc');opts('rx-ro',RO,S.ro,'ro');opts('rx-m',M,S.m,'m',1);opts('rx-t',m.T,S.t,'t');
 $('rx-pc-d').textContent=PC[S.pc].d;$('rx-ro-d').textContent=RO[S.ro].d;$('rx-m-d').textContent=m.d;$('rx-t-d').textContent=t.d;
 const R=recipe();
 $('rx-sum').innerHTML=[PC[S.pc].n,'Rang '+RO[S.ro].n.toLowerCase(),m.n,t.n].map(x=>`<span>${E(x)}</span>`).join('');
 $('rx-dose').value=S.dose;$('rx-unit').textContent=S.m==='cold'&&S.t!=='jp'?'g cà phê xay thô':'g cà phê';
 $('rx-par').innerHTML=R.par.map(p=>`<div><span>${p[0]}</span><b>${p[1]}</b>${p[2]?`<small>${p[2]}</small>`:''}</div>`).join('')+
  R.ing.map(i=>`<div><span>${i[0]}</span><b>${i[1]}</b>${i[2]?`<small>${i[2]}</small>`:''}</div>`).join('');
 $('rx-pours').innerHTML=`<thead><tr><th>Lúc</th><th>${S.m==='esp'?'Ra':'Rót'}</th><th>Làm gì</th></tr></thead><tbody>`+R.pours.map(p=>`<tr><td class="m">${R.unit==='h'?(p.at?p.at+' giờ':'Bắt đầu'):mmss(p.at)}</td><td class="m">${p.w>0?fm(p.w)+' g':'–'}</td><td>${E(p.n)}</td></tr>`).join('')+'</tbody>';
 $('rx-bal').hidden=!(S.m==='v60'&&S.t==='46');$('rx-bal-o').textContent=!S.sh?'Cân bằng':S.sh>0?`Lần 1 nhiều hơn ${fm(S.sh*2)} g: sáng, chua hơn`:`Lần 2 nhiều hơn ${fm(-S.sh*2)} g: ngọt hơn`;
 $('rx-tips').innerHTML=R.tips.map(x=>`<li>${E(x)}</li>`).join('');
 $('rx-sp').innerHTML=picks().map(x=>`<a href="${x.file}"><i style="--c:${x.col}" aria-hidden="true"></i><b>${E(x.n)}</b><small>${E(x.price)}</small></a>`).join('');
 $('rx-scene').innerHTML=scene(R);$('rx-tl').innerHTML=timeline(R);
 $('rx-cap').textContent=S.m==='cold'&&S.t!=='jp'?'Trục thời gian theo giờ ngâm.':S.m==='esp'?'Trục thời gian của một shot, tính bằng giây.':'Cột là lượng nước mỗi lần rót, đường đứt là tổng nước đã rót.';
 $('rx-msg').textContent='';save();window._R=R}

function setMethod(m){S.m=m;const T=M[m].T;if(!T[S.t])S.t=Object.keys(T)[0];S.dose=T[S.t].dose;S.sh=0}
document.querySelector('.rx-steps').addEventListener('click',e=>{const b=e.target.closest('button[data-k]');if(!b)return;const k=b.dataset.k,v=b.dataset.v;
 if(k==='m'){setMethod(v)}else if(k==='t'){S.t=v;S.dose=M[S.m].T[v].dose;S.sh=0}else S[k]=v;render()});
const clampDose=v=>{const lim={v60:[8,60],phin:[10,40],esp:[12,24],cold:[20,300]}[S.m],jp=S.m==='cold'&&S.t==='jp';const [a,b]=jp?[10,60]:lim;return Math.max(a,Math.min(b,v))};
$('rx-minus').addEventListener('click',()=>{S.dose=clampDose(+S.dose-(S.m==='esp'?.5:S.m==='cold'&&S.t!=='jp'?10:1));render()});
$('rx-plus').addEventListener('click',()=>{S.dose=clampDose(+S.dose+(S.m==='esp'?.5:S.m==='cold'&&S.t!=='jp'?10:1));render()});
$('rx-dose').addEventListener('change',e=>{const v=parseFloat(String(e.target.value).replace(',','.'));if(!isNaN(v))S.dose=clampDose(v);render()});
$('rx-sweet').addEventListener('click',()=>{S.sh=(+S.sh||0)-2.5;render()});
$('rx-bright').addEventListener('click',()=>{S.sh=(+S.sh||0)+2.5;render()});
$('rx-reset').addEventListener('click',()=>{S={pc:'washed',ro:'sv',m:'v60',t:'46',dose:20,sh:0};$('rx-q').value='';render()});
$('rx-copy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(text(window._R));$('rx-msg').textContent='Đã chép công thức.'}catch(e){$('rx-msg').textContent='Trình duyệt chặn chép, hãy dùng In hoặc Lưu ảnh.'}});
$('rx-print').addEventListener('click',()=>window.print());
$('rx-img').addEventListener('click',()=>{try{const R=window._R,c=document.createElement('canvas'),W=1080,P=72,nr=1+R.par.length+R.ing.length,HH=Math.max(1080,330+Math.ceil(nr/2)*92+80+R.pours.length*44+150);c.width=W;c.height=HH;const g=c.getContext('2d');
  const F='"Be Vietnam Pro",system-ui,sans-serif',D='"Big Shoulders Display","Be Vietnam Pro",sans-serif';
  g.fillStyle='#EFE4D2';g.fillRect(0,0,W,HH);g.fillStyle='#FDFAF2';g.fillRect(40,40,W-80,HH-80);g.strokeStyle='#9E3B26';g.lineWidth=4;g.strokeRect(40,40,W-80,HH-80);
  let y=130;g.fillStyle='#9E3B26';g.font=`700 30px ${F}`;g.fillText('CÔNG THỨC PHA · MEDILI',P,y);y+=74;
  g.fillStyle='#4A2C1A';g.font=`800 64px ${D}`;g.fillText(M[S.m].T[S.t].n,P,y);y+=50;
  g.fillStyle='#6B5C50';g.font=`500 30px ${F}`;g.fillText(`${PC[S.pc].n} · Rang ${RO[S.ro].n.toLowerCase()} · ${M[S.m].n}`,P,y);y+=60;
  const rows=[['Cà phê',f1(S.dose)+' g'],...R.par.map(p=>[p[0],p[1]]),...R.ing.map(i=>[i[0],i[1]])];
  rows.forEach(([a,b],i)=>{const cx=P+(i%2)*470,cy=y+Math.floor(i/2)*92;g.fillStyle='#F5E7CF';g.fillRect(cx,cy,450,78);g.fillStyle='#6B5C50';g.font=`600 22px ${F}`;g.fillText(a.toUpperCase(),cx+18,cy+30);g.fillStyle='#4A2C1A';g.font=`700 32px ${F}`;g.fillText(b,cx+18,cy+66)});
  y+=Math.ceil(rows.length/2)*92+30;g.fillStyle='#9E3B26';g.font=`700 26px ${F}`;g.fillText('CÁC BƯỚC',P,y);y+=44;g.font=`500 27px ${F}`;g.fillStyle='#4A2C1A';
  R.pours.forEach(p=>{const tt=(R.unit==='h'?(p.at?p.at+' giờ':'Bắt đầu'):mmss(p.at))+(p.w>0&&S.m!=='esp'?' · rót '+fm(p.w)+' g':'')+(p.n?' · '+p.n:'');g.fillText(tt.length>58?tt.slice(0,57)+'…':tt,P,y);y+=44});
  g.fillStyle='#9E3B26';g.font=`italic 600 28px Georgia,serif`;g.fillText('medili.vn · Mê vị Di Linh',P,HH-80);
  const a=document.createElement('a');a.download='cong-thuc-pha-medili.png';a.href=c.toDataURL('image/png');document.body.append(a);a.click();a.remove();$('rx-msg').textContent='Đã lưu ảnh công thức.'}
 catch(e){$('rx-msg').textContent='Chưa lưu được ảnh trên trình duyệt này, hãy dùng In hoặc Chép.'}});
$('rx-q').addEventListener('change',e=>{const x=SPI[e.target.value];if(!x)return;applySP(x);render()});
function applySP(x){if(x.pk[0]&&PC[x.pk[0]])S.pc=x.pk[0];if(x.rk)S.ro=x.rk;S.m=x.m;S.t=Object.keys(M[x.m].T)[0];S.dose=M[x.m].T[S.t].dose;S.sh=0}
const sp=new URLSearchParams(location.search).get('sp');if(sp&&SPI[sp]){applySP(SPI[sp]);$('rx-q').value=sp}
render();
'''


def page(catalog):
    sp = []
    for x in catalog:
        price = (f'{fm(x["p"][0] * 250)} đ/túi 250 g' if x['packs'] == [250] else f'{fm(x["p"][0] * 1000)} đ/kg') if x['p'] else 'Liên hệ'
        sp.append(dict(id=x['id'], n=x['n'], file=x['file'], col=x['col'], pk=x['pk'], rk=_rk(x['roast']), m=_method(x),
                       st=x['st'], price=price + (' · sắp mở bán' if x['st'] == 'sap' else '')))
    ids = {x['id'] for x in sp}
    assert all(i in ids for L in PICK.values() for i in L), 'mã dòng trong PICK không có trong Cửa hàng'
    js = (JS.replace('__PICK__', json.dumps(PICK, separators=(',', ':')))
            .replace('__SP__', json.dumps(sp, ensure_ascii=False, separators=(',', ':'))))
    quick = ''.join(f'<option value="{x["id"]}">{esc(x["n"])}</option>' for x in sp if x['st'] != 'sap')
    body = head('Cỗ máy Công thức pha', 'Bốn bước, <em>một công thức của riêng bạn.</em>',
                'Chọn cách sơ chế, mức rang, cách pha và kỹ thuật. Cỗ máy tính liều cà phê, lượng nước, nhiệt độ, độ xay, thời gian và từng lần rót. '
                'Đây là mốc khởi đầu: pha, nếm, rồi chỉnh theo gu của bạn.',
                '<a class="btn main" href="#cong-thuc">Bắt đầu chọn</a><a class="btn" href="cua-hang.html">Chọn cà phê MeDili</a>'
                '<a class="btn" href="chiet-xuat.html">Cỗ máy Chiết xuất</a>')
    body += f'''
<section class="box rx-quick" aria-label="Chọn nhanh theo cà phê MeDili">
 <label for="rx-q">Bạn đang có cà phê MeDili nào?<select id="rx-q"><option value="">Chọn để điền sẵn ba bước đầu</option>{quick}</select></label>
</section>
<section class="rx-steps" id="cong-thuc" aria-label="Bốn bước chọn">
 <div class="rx-step"><div class="rx-hd"><span class="rx-n">01</span><h2>Sơ chế</h2></div><div class="rx-opts" id="rx-pc" role="group" aria-label="Sơ chế"></div><p class="rx-d" id="rx-pc-d"></p></div>
 <div class="rx-step"><div class="rx-hd"><span class="rx-n">02</span><h2>Mức rang</h2></div><div class="rx-opts" id="rx-ro" role="group" aria-label="Mức rang"></div><p class="rx-d" id="rx-ro-d"></p></div>
 <div class="rx-step"><div class="rx-hd"><span class="rx-n">03</span><h2>Cách pha</h2></div><div class="rx-opts big" id="rx-m" role="group" aria-label="Cách pha"></div><p class="rx-d" id="rx-m-d"></p></div>
 <div class="rx-step"><div class="rx-hd"><span class="rx-n">04</span><h2>Kỹ thuật</h2></div><div class="rx-opts" id="rx-t" role="group" aria-label="Kỹ thuật"></div><p class="rx-d" id="rx-t-d"></p></div>
</section>
<section class="rx-out" aria-label="Công thức của bạn">
 <div class="rx-fig"><div id="rx-scene"></div><div id="rx-tl"></div><p class="rx-cap" id="rx-cap"></p></div>
 <div class="rx-card" id="rx-card" aria-live="polite">
  <div class="rx-ttl"><h2>Công thức của bạn</h2><button type="button" class="btn small ghost" id="rx-reset">Chọn lại từ đầu</button></div>
  <div class="rx-sum" id="rx-sum"></div>
  <div class="rx-dose"><b>Lượng cà phê</b><div class="rx-st"><button type="button" id="rx-minus" aria-label="Bớt cà phê">−</button><input id="rx-dose" inputmode="decimal" aria-label="Lượng cà phê, gam"><button type="button" id="rx-plus" aria-label="Thêm cà phê">+</button></div><span id="rx-unit">g cà phê</span></div>
  <div class="rx-par" id="rx-par"></div>
  <div class="rx-bal" id="rx-bal" hidden><button type="button" id="rx-sweet">Ngọt hơn</button><button type="button" id="rx-bright">Chua sáng hơn</button><output id="rx-bal-o"></output></div>
  <table class="rx-pours" id="rx-pours"></table>
  <div><p class="eye">Chỉnh cho vừa gu</p><ul class="rx-tips" id="rx-tips"></ul></div>
  <div><p class="eye">Cà phê MeDili hợp công thức này</p><div class="rx-sp" id="rx-sp" style="margin-top:6px"></div></div>
  <div class="rx-act"><button type="button" class="btn main" id="rx-img">Lưu ảnh công thức</button><button type="button" class="btn" id="rx-print">In công thức</button><button type="button" class="btn" id="rx-copy">Chép công thức</button></div>
  <p class="rx-msg" id="rx-msg" role="status"></p>
 </div>
</section>
<section class="p-sec rx-more">
 <p class="eye">So sánh nhanh</p>
 <h2 class="p-h2">Bốn cách pha, <em>bốn kiểu ly.</em></h2>
 <div class="rx-cmp"><table>
  <thead><tr><th>Cách pha</th><th>Tỷ lệ</th><th>Nước</th><th>Độ xay</th><th>Thời gian</th><th>Ly ra sao</th><th>Hợp với</th></tr></thead>
  <tbody>
   <tr><td>Pour over V60</td><td>1:15 đến 1:17</td><td>90 đến 96 °C</td><td>Vừa đến vừa thô</td><td>3 đến 3 phút 30</td><td>Sạch, rõ hương, chua sáng</td><td>Arabica rang sáng đến vừa</td></tr>
   <tr><td>Phin</td><td>1:3 đến 1:5</td><td>90 đến 96 °C</td><td>Vừa</td><td>4 đến 5 phút</td><td>Đậm, thân dày, đắng rõ</td><td>Robusta rang vừa đến đậm</td></tr>
   <tr><td>Espresso</td><td>1:1,5 đến 1:3</td><td>90 đến 94 °C</td><td>Mịn</td><td>20 đến 35 giây</td><td>Đặc, crema dày, làm nền cho sữa</td><td>Blend, Robusta Premium</td></tr>
   <tr><td>Cold brew</td><td>1:5 đến 1:10</td><td>Lạnh</td><td>Thô</td><td>14 đến 20 giờ</td><td>Êm, ngọt, ít chua</td><td>Robusta honey, blend</td></tr>
  </tbody></table></div>
</section>
<section class="p-sec rx-more">
 <p class="eye">Đọc ly cà phê</p>
 <h2 class="p-h2">Nếm rồi chỉnh <em>một thứ mỗi lần.</em></h2>
 <div class="rx-fix">
  <div class="box"><h3>Chua gắt, nhạt</h3><p>Chiết chưa đủ. Xay mịn hơn một nấc, tăng nước 1 đến 2 °C, hoặc kéo dài thời gian.</p></div>
  <div class="box"><h3>Đắng khét, khô miệng</h3><p>Chiết quá tay. Xay thô hơn, giảm nhiệt, rút ngắn thời gian hoặc rót nhẹ tay hơn.</p></div>
  <div class="box"><h3>Loãng, thiếu thân</h3><p>Tăng lượng cà phê thêm 1 đến 2 g, hoặc giảm nước: tỷ lệ từ 1:16 xuống 1:15.</p></div>
  <div class="box"><h3>Ngọt, tròn, hậu dài</h3><p>Đúng công thức của bạn. Ghi lại bằng nút Lưu ảnh để lần sau pha y như vậy.</p></div>
 </div>
</section>
'''
    return doc(FILE, TITLE, DESC, body, css=CSS, js=js, wrap_cls='wrap pg')
