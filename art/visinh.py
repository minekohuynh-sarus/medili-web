# Cỗ máy Vi sinh: nguồn vi sinh, lớp nhầy, bồn lên men với nấm men, vi khuẩn lactic, vi khuẩn acetic.
# Mô hình minh hoạ, hiệu chỉnh theo pH thực tế của lên men ướt (Motato-Rocha 2024) và mốc dừng pH 4,3 của MeDili.
from iso import *

FILE = 'vi-sinh.html'
TITLE = 'Cỗ Máy Vi Sinh MeDili'
DESC = ('Ai đang làm việc trong bồn lên men cà phê: nấm men, vi khuẩn lactic, vi khuẩn acetic. Vi sinh đến từ đâu, lớp nhầy nuôi chúng ra sao, '
        'nhiệt độ, oxy và thời gian đổi kết quả thế nào. Mô hình tương tác của MeDili.')

TEAM = [
    ('Nấm men', 'cx1', 'Pichia, Candida, Saccharomyces…',
     [('Ăn', 'Đường trong lớp nhầy và thịt quả'), ('Cần', 'Không bắt buộc oxy; có oxy thì lớn nhanh hơn'), ('Tạo ra', 'Cồn, CO₂, ester thơm mùi trái cây, một số enzyme cắt pectin'),
      ('Tốt khi', 'Hoạt động vừa phải, cho hương trái cây sạch'), ('Hại khi', 'Để quá lâu, cồn nhiều thành nguyên liệu cho giấm')]),
    ('Vi khuẩn lactic', 'cx2', 'Leuconostoc, Lactiplantibacillus, Weissella…',
     [('Ăn', 'Đường'), ('Cần', 'Ít oxy; chịu được bồn ngâm nước, bồn kín'), ('Tạo ra', 'Acid lactic là chính; loại dị hình tạo thêm acid acetic, CO₂, cồn'),
      ('Tốt khi', 'Hạ pH đều, chua dịu, cảm giác tròn miệng'), ('Hại khi', 'Bồn quá dài, chua gắt')]),
    ('Vi khuẩn acetic', 'cx4', 'Acetobacter, Gluconobacter',
     [('Ăn', 'Cồn do nấm men tạo ra'), ('Cần', 'Oxy, bắt buộc'), ('Tạo ra', 'Acid acetic, mùi giấm'),
      ('Tốt khi', 'Rất ít, cho chút sáng vị như rượu vang'), ('Hại khi', 'Bồn mở, đảo nhiều, phơi dày ẩm: mùi giấm, chua gắt')]),
]

SOURCES6 = [('trai', 'Vỏ trái', 'Vi sinh sống sẵn trên vỏ và cuống trái. Trái dập, trái chín quá mang nhiều hơn.'),
            ('vuon', 'Đất', 'Trái rụng, bao đặt xuống đất, bánh xe, chân người mang đất vào xưởng.'),
            ('soche', 'Nước', 'Nước xát, nước ngâm, nước rửa. Nước bẩn đổ vào bồn là đổ thêm vi sinh tạp.'),
            ('quat', 'Không khí', 'Bụi, bào tử bay trong xưởng, nhất là gần đống vỏ ủ.'),
            ('may', 'Dụng cụ', 'Bồn, máy xát, bao, rổ chưa rửa sạch giữ lại vi sinh của mẻ trước.'),
            ('nguoi', 'Người', 'Tay, áo, ủng của người hái và người làm bồn.')]

READ = [
    ('trai', 'Lên men bắt đầu ngay khi hái',
     'Vi sinh có sẵn trên vỏ trái, trong đất, nước, không khí và trên tay người hái. Trái hái về để trong bao qua đêm đã bắt đầu lên men, dù chưa vào bồn. '
     'Vì vậy sơ chế trong ngày quan trọng không kém công thức bồn.', 'MeDili'),
    ('hen', 'Lâu hơn không có nghĩa là ngon hơn',
     'Khi đường đã cạn, bồn không tạo thêm vị ngọt mà chỉ thêm acid. Bồn mở cho vi khuẩn acetic thời gian biến cồn thành giấm; bồn bẩn để vi sinh tạp sinh acid butyric, propionic, '
     'dấu hiệu của lên men quá.', 'Martinez và cộng sự 2019'),
    ('kinh', 'pH thấp không có nghĩa là ngon',
     'pH cho biết bồn chua tới đâu, không cho biết chua bằng acid gì. Cùng pH 4,0, bồn nhiều acid lactic cho vị tròn, bồn nhiều acid acetic cho mùi giấm. Đo pH phải đi cùng ngửi và nếm.',
     'MeDili'),
    ('visinh', 'Có acid acetic chưa chắc do vi khuẩn acetic',
     'Vi khuẩn lactic dị hình tạo cả acid lactic, acid acetic, CO₂ và cồn, nên bồn kín vẫn có ít acid acetic. Lượng lớn thường đến từ vi khuẩn acetic khi có oxy.',
     'Motato-Rocha và cộng sự 2024'),
    ('soche', 'Vi khuẩn lactic không làm cà phê ngọt hơn',
     'Chúng ăn đường và tạo acid. Cái chúng góp là độ chua dễ chịu và cảm giác tròn miệng; vị ngọt trong ly đến từ đường còn trong nhân và từ rang.', 'MeDili'),
    ('khien', 'Oxy quyết định ai thắng',
     'Vi khuẩn acetic cần oxy để biến cồn thành giấm. Bồn ngâm nước hoặc bồn kín hạn chế chúng; mở nắp, đảo nhiều, phơi dày và ẩm thì chúng mạnh lên.', 'Vi sinh học cơ bản'),
]

SRC = [
    ('Motato-Rocha K., Román-Morales M. O., Gonzalez-Montero V. (2024). Identification of microorganisms in wet coffee fermentation… Jardín, Antioquia. Vitae 31(1): 351373. pH từ 5,0–5,8 xuống khoảng 3,5 sau 72 giờ', 'Vitae', 'https://revistas.udea.edu.co/index.php/vitae/article/download/351373/20815318?inline=1'),
    ('Martinez S. J. và cộng sự (2019). Effect of bacterial and yeast starters on the formation of volatile and organic acid compounds in coffee beans… Frontiers in Microbiology 10: 1287', 'Frontiers', 'https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.01287/pdf'),
    ('Avallone S. và cộng sự (2000). Polysaccharide constituents of coffee-bean mucilage. Journal of Food Science 65(8): 1308–1311', 'CIRAD', 'https://agritrop.cirad.fr/523161'),
    ('Ferment: lỗi chua giấm do trái chín quá, xát chậm, để lâu trong bồn', 'Sweet Maria’s', 'https://library.sweetmarias.com/glossary/ferment/'),
]


def page():
    team = ''.join(f'<div class="box tm"><span class="tmh" style="--c:var(--{c})"><i></i>{n}</span><p class="tme">Ví dụ: {ex}</p><dl class="kv">'
                   + ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in rows) + '</dl></div>' for n, c, ex, rows in TEAM)
    src6 = ''.join(f'<div class="s6">{icon(i)}<b>{t}</b><p>{p}</p></div>' for i, t, p in SOURCES6)
    body = head('Vi sinh', 'Cỗ máy',
                'Bồn lên men là một cuộc cạnh tranh của ba nhóm thợ tí hon: nấm men, vi khuẩn lactic và vi khuẩn acetic. Chọn cách lên men, nhiệt độ, độ sạch và kéo thời gian '
                'để xem nhóm nào thắng, pH xuống ra sao, và lúc nào nên dừng.')
    body += f'''
<div class="bench">
  <div class="card">
    <div class="fighead">
      <div><b>Hình 1</b> <span id="figsub"></span></div>
      <button class="btn small" id="run2" type="button">Chạy bồn</button>
    </div>
    <div class="scroller"><svg id="scene" viewBox="0 0 1040 720" aria-label="Bàn mô hình tám trạm: nguồn vi sinh, lớp nhầy, bồn lên men, nấm men, vi khuẩn lactic, vi khuẩn acetic, đo đạc, rửa và phơi. Bấm từng trạm để xem chi tiết."></svg></div>
    <div class="strip" id="strip" role="group" aria-label="Chọn trạm"></div>
    <div id="detail" aria-live="polite"></div>
  </div>

  <aside class="card ctl">
    <div class="head2"><h3>Cách lên men</h3><small>4 cách</small></div>
    <div class="row" id="meths"></div>
    <p class="mnote" id="mNote"></p>
    <div class="head2" style="margin-top:12px"><h3>Độ sạch của bồn, nước, dụng cụ</h3></div>
    <div class="row" id="hygs"></div>
    <hr>
    <div class="sl" style="margin-top:0"><label for="iT">Nhiệt độ bồn <output id="oT"></output></label><input id="iT" type="range" min="16" max="34" step="1"><p id="tNote"></p></div>
    <div class="sl"><label for="iB">Brix trái đầu vào <output id="oB"></output></label><input id="iB" type="range" min="14" max="26" step="1"><p>Trái chín đặc sản thường 18–24 °Brix. Xem <a class="lnk" href="trai-chin.html">Cỗ máy Trái chín</a>.</p></div>
    <div class="sl"><label for="iH">Thời gian <output id="oH"></output></label><input id="iH" type="range" min="0" max="96" step="1"><p id="hNote"></p></div>
    <div class="row" style="margin-top:14px"><button class="btn main" id="run" type="button">Chạy bồn</button><button class="btn" id="reset" type="button">Về mặc định</button></div>
    <div class="stats" id="stats"></div>
    <div id="verdict"></div>
    <hr>
    <span class="lbl">pH trong bồn theo giờ</span>
    <div class="charts"><svg class="ch" id="cP" viewBox="0 0 340 150" role="img" aria-label="pH trong bồn theo giờ"></svg></div>
    <div id="tip"></div>
  </aside>
</div>

<section class="card" id="ai">
  <h2>Hình 2: ai đang làm việc trong bồn</h2>
  <p class="lead">Số tế bào trên mỗi gam, thang log: mỗi vạch là gấp 10 lần. Vạch đứng là giờ đang xem. Mô hình minh hoạ, không phải số đếm của một bồn thật.</p>
  <div class="lg" id="lg2"></div>
  <div class="chw" id="w2"><svg id="c2" class="c2" role="img" aria-label="Số lượng nấm men, vi khuẩn lactic, vi khuẩn acetic và vi sinh tạp theo giờ"></svg></div>
</section>

<section class="card" id="tao-ra">
  <h2>Hình 3: bồn tạo ra gì</h2>
  <p class="lead">Đường trong lớp nhầy được giải phóng dần, nấm men biến thành cồn, vi khuẩn lactic biến thành acid lactic; khi có oxy, vi khuẩn acetic biến cồn thành acid acetic. Chỉ số tương đối, 1 là lượng đường lúc đầu.</p>
  <div class="lg" id="lg3"></div>
  <div class="chw" id="w3"><svg id="c3" class="c2" role="img" aria-label="Đường còn lại, cồn, acid lactic, acid acetic theo giờ"></svg></div>
</section>

<section class="p-sec">
  <p class="eye">Ba nhóm thợ</p>
  <h2 class="p-h2" style="margin:0">Mỗi nhóm ăn một thứ, <em>cần một thứ, để lại một thứ.</em></h2>
  <div class="g3 team">{team}</div>
</section>

<div class="cols">
  <section class="card">
    <h2>Lớp nhầy: thức ăn của vi sinh</h2>
    <p>Lớp nhầy là lớp trong suốt, trơn, bám quanh vỏ trấu, nằm giữa thịt quả và hạt. Phần lớn là nước. Phần khô gồm đường tự do (glucose, fructose, sucrose), pectin và các chất xơ khác, một ít acid hữu cơ, acid amin và khoáng.</p>
    <p>Pectin mới là thứ làm lớp nhầy nhớt. Khi tách phần không tan trong cồn của lớp nhầy, các nhà nghiên cứu thấy khoảng 30 % là chất pectin, 8 % cellulose và 18 % polysaccharide trung tính khác. Lên men giúp cắt pectin để lớp nhầy bong ra khi rửa; đường thì nuôi vi sinh.</p>
    <p class="mnote">Natural giữ nguyên trái nên vi sinh có cả thịt quả lẫn lớp nhầy để ăn. Honey giữ một phần lớp nhầy khi phơi. Washed lên men rồi rửa sạch lớp nhầy. Xem <a class="lnk" href="trai-ca-phe.html">Cấu tạo trái</a>.</p>
  </section>
  <section class="card">
    <h2>Vi sinh đến từ đâu</h2>
    <p class="lead" style="margin-bottom:8px">Vi sinh không tự sinh ra trong bồn. Chúng theo trái và theo mọi thứ chạm vào trái. Mỗi vườn, mỗi xưởng có một hệ vi sinh riêng, nên cùng giống cà phê mà hương mỗi nơi một khác.</p>
    <div class="src6">{src6}</div>
  </section>
</div>

<section class="p-sec">
  <p class="eye">MeDili đọc lại</p>
  <h2 class="p-h2" style="margin:0">Sáu điều <em>về vi sinh trong bồn.</em></h2>
  <div class="g3">{boxes(READ)}</div>
</section>

<section class="card">
  <h2>Phiếu theo dõi bồn</h2>
  <p class="lead">Chép phiếu, in ra dán cạnh bồn. Đo cùng lúc pH, Brix, nhiệt độ và ghi mùi; dừng theo pH và mùi, đồng hồ chỉ để dự kiến.</p>
  <pre class="msg" id="sheet"></pre>
  <button class="btn small" id="cpSh" type="button">Sao chép phiếu</button> <span class="cpst" id="cpShS" role="status"></span>
</section>

<section class="card src">
  <h2>Nguồn và cách đọc mô hình</h2>
  <p class="lead">Đường cong là mô hình minh hoạ: ba nhóm vi sinh lớn theo nhiệt độ, đường và pH; vi khuẩn acetic cần cồn và oxy; đường trong lớp nhầy được giải phóng dần. MeDili chỉnh mô hình để bồn ngâm nước ở 22 °C chạm pH 4,3 sau khoảng 30 giờ và xuống gần 4,0 sau 72 giờ, cùng hướng với số đo ngoài thực tế. Mỗi bồn thật khác nhau, nên luôn đo.</p>
  <ul>{srclist(SRC)}</ul>
  <div class="lnks"><a class="lnk" href="phan-biet-ca-phe.html">Cỗ máy Phân biệt cà phê</a><a class="lnk" href="len-men-men-bia.html">Lên men men bia</a><a class="lnk" href="len-men-trai-cay.html">Lên men trái cây</a><a class="lnk" href="trai-chin.html">Cỗ máy Trái chín</a><a class="lnk" href="tien-chat-huong.html">Cỗ máy Tiền chất hương</a><a class="lnk" href="journal.html">Tất cả kiến thức cà phê</a></div>
</section>
'''
    return doc(FILE, TITLE, DESC, body, css=ISO_CSS + CSS, js=ISO_JS + JS)


CSS = r'''
/* Cỗ máy Vi sinh */
#scene .soil{fill:#7A5233}#scene .soilT{fill:#8D6A45}
#scene .jug{fill:#E9DFC9}#scene .jugT{fill:#D8CBAE}
#scene .cloud{fill:#F6F0E4;stroke:#B9A274;stroke-width:1}
#scene .liqA{fill:#D9B77E;fill-opacity:.8}#scene .liqAT{fill:#E3C792}
#scene .muc{fill:#F1D9A6;fill-opacity:.7;stroke:#C9A15B;stroke-width:1.4}
#scene .bean{fill:#E9DFC4;stroke:#B9A274;stroke-width:1.2}
#scene .chan{fill:#E7CFA2;fill-opacity:.6}
#scene .bed{fill:#D9C39A}#scene .bed2{fill:#B9A274}
#scene .fl1{fill:#E3B341;fill-opacity:.85}#scene .fl2{fill:#9A5BB5;fill-opacity:.8}#scene .fl4{fill:#CB4D54;fill-opacity:.8}
#scene .bub{fill:none;stroke:#FFF6EC;stroke-width:1.2}
.running #scene .bub,#scene.running .bub{animation:bubA 1.6s ease-in infinite}
@keyframes bubA{0%{transform:translateY(4px);opacity:0}30%{opacity:1}100%{transform:translateY(-14px);opacity:0}}
.team .box{display:flex;flex-direction:column;gap:6px}
.tmh{display:flex;align-items:center;gap:8px;font:800 1.45rem/1.15 var(--display)}
.tmh i{display:block;width:14px;height:14px;border-radius:50%;background:var(--c)}
.tme{margin:0;color:var(--muted);font-size:.86rem;font-style:italic}
.team dl.kv{grid-template-columns:62px minmax(0,1fr)}
.src6{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 16px}
.s6{display:grid;grid-template-columns:30px minmax(0,1fr);gap:2px 10px;align-items:start}
.s6 svg.pi{grid-row:1/3;color:var(--accent)}
.s6 b{font:700 .95rem var(--body)}.s6 p{margin:0;font-size:.86rem;color:var(--muted)}
@media (max-width:560px){.src6{grid-template-columns:minmax(0,1fr)}}
#sheet{min-height:240px}
@media (prefers-reduced-motion:reduce){#scene .bub{animation:none!important}}
'''

JS = r'''
const U=7,OX=196,OY=118,VBW=1040;
const MTH={uot:{n:'Ướt, ngâm nước',O:.28,sub:1,dry:0,note:'Xát vỏ, ngâm hạt còn nhầy trong nước sạch. Nước hạn chế oxy, vi khuẩn lactic thường dẫn đầu.'},
 kho:{n:'Ủ khô trong bồn',O:.6,sub:1,dry:0,note:'Xát vỏ, để hạt còn nhầy ráo trong bồn, không ngâm nước. Nhiều oxy hơn, vi khuẩn acetic có cơ hội.'},
 kin:{n:'Bồn kín yếm khí',O:.06,sub:1,dry:0,note:'Bồn đậy kín có van xả CO₂. Gần như không oxy, vi khuẩn acetic bị chặn, cồn và acid lactic giữ lại.'},
 nat:{n:'Natural, nguyên trái',O:.85,sub:1.5,dry:1,note:'Phơi nguyên trái trên giàn. Vi sinh ăn cả thịt quả lẫn lớp nhầy, nhiều oxy; trái khô dần nên vi sinh chậm lại.'}};
const HY={sach:'Sạch',kem:'Kém'};
const Q={L0:6.5,Y0:5.5,kL:.04,kY:.08,gL:.2,kr:.03,fr:.3};
const DEF={m:'uot',T:22,bx:20,hyg:'sach'};
const st={...DEF,sel:3,h:30};
const GR=[{k:'Y',n:'Nấm men',c:'var(--cx1)'},{k:'L',n:'Vi khuẩn lactic',c:'var(--cx2)'},{k:'A',n:'Vi khuẩn acetic',c:'var(--cx4)'},{k:'C',n:'Vi sinh tạp',c:'var(--cx3)',d:'6 4'}];
function sim(){const M=MTH[st.m],kT=Math.pow(2,(st.T-22)/10),S0=st.bx/20*M.sub,hyg=st.hyg==='kem';
 let Y=Q.Y0,L=Q.L0,A=hyg?4.4:3.4,C=hyg?4.4:2.6,Sb=S0*(1-Q.fr),Sf=S0*Q.fr,E=0,La=0,Ac=0,B=0,pH=5.75;const out=[],dt=.25;
 for(let i=0;i<=96/dt;i++){const t=i*dt;if(i%2===0)out.push({t,Y,L,A,C,S:(Sb+Sf)/S0,E:E/S0,La:La/S0,Ac:Ac/S0,B,pH});
  const fw=M.dry?1-.55*Math.min(1,t/96):1,O=M.O,fS=Sf/(Sf+.04*S0),low=(Sb+Sf)<.04*S0;
  const fpY=clamp((pH-2.9)/1.2,0,1),fpL=clamp((pH-3.2)/1,0,1),fpA=clamp((pH-2.7)/1.2,0,1),fpC=clamp((pH-4)/.7,0,1);
  const aY=Math.pow(10,Y-7.8),aL=Math.pow(10,L-9),aA=Math.pow(10,A-7.4),aC=Math.pow(10,C-7);
  const gY=.12*kT*fw*fS*fpY*(.75+.25*O),gL=Q.gL*kT*fw*fS*fpL*(1-.45*O),gA=.14*kT*fw*O*(E/(E+.05))*fpA,gC=.08*kT*fw*fpC*(hyg?1:.4)*(1-.5*O);
  const rel=Q.kr*kT*fw*Sb,cY=Math.min(Sf/dt*.5,Q.kY*kT*fw*aY*fS),cL=Math.min(Sf/dt*.5,Q.kL*kT*fw*aL*fS),ox=.08*kT*fw*aA*O*E/(E+.04);
  Y+=dt*(gY*(1-Math.pow(10,Y-7.8))-(low?.025*kT:0));L+=dt*(gL*(1-Math.pow(10,L-9))-(low?.012*kT:0));
  A+=dt*(gA*(1-Math.pow(10,A-7.4)));C+=dt*(gC*(1-Math.pow(10,C-7))-(fpC<.1?.015*kT:0));
  Sb-=dt*rel;Sf=Math.max(0,Sf+dt*(rel-cY-cL));E=Math.max(0,E+dt*(.45*cY+.08*cL-ox));La+=dt*.8*cL;Ac+=dt*(.1*cL+.9*ox);B+=dt*.02*kT*aC*(low?1:.2);
  pH=3.35+2.4*Math.exp(-(La+.85*Ac+.6*B)/.34)}
 return out}
let SIM=[],R={};
const at=h=>SIM[clamp(Math.round(h*2),0,SIM.length-1)];
const sup=n=>String(n).split('').map(c=>'⁰¹²³⁴⁵⁶⁷⁸⁹'[+c]).join('');
const sci=x=>{const e=Math.floor(x),m=Math.pow(10,x-e);return `${vn(m,1)}×10${sup(e)}`};
const lvl=(v,a,b)=>v<a?'thấp':v<b?'vừa':'cao';
function calc(){SIM=sim();const x=at(st.h),stop=SIM.find(o=>o.pH<=4.3),acPeak=Math.max(...SIM.map(o=>o.Ac));
 R={x,stop:stop?stop.t:null,nat:st.m==='nat'};return R}

/* ====== 8 TRẠM ====== */
const ST=[
 {n:'Nguồn vi sinh',sub:'Trái, đất, nước, không khí, dụng cụ, người',mech:'Vi sinh vào bồn theo trái và mọi thứ chạm vào trái. Bồn sạch, nước sạch, trái tươi thì phần lớn là nấm men và vi khuẩn lactic có sẵn trên vỏ; bồn bẩn, nước bẩn thì thêm vi sinh tạp.',
  kv:()=>[['Độ sạch',HY[st.hyg]],['Vi sinh tạp lúc đầu',st.hyg==='kem'?'cao, khoảng '+sci(4.4)+'/g':'thấp, khoảng '+sci(2.6)+'/g'],['Vi khuẩn acetic lúc đầu',sci(st.hyg==='kem'?4.4:3.4)+'/g']],check:'Rửa bồn, máy xát, rổ bằng nước sạch sau mỗi mẻ, phơi khô. Không đặt bao trái xuống đất.',
  fail:'Nghĩ rằng lên men cần “men cũ” nên không rửa bồn. Bồn bẩn giữ lại cả vi sinh gây mùi lỗi.',tip:'Trái hái về sơ chế trong ngày, không để bao qua đêm.'},
 {n:'Lớp nhầy',sub:()=>`Thức ăn của vi sinh · trái ${st.bx} °Brix`,mech:'Lớp nhầy chứa đường tự do, pectin, một ít acid và khoáng. Đường được giải phóng dần khi pectin bị cắt, nên vi sinh có thức ăn trong nhiều giờ chứ không ăn hết ngay.',
  kv:()=>[['Brix trái',st.bx+' °Brix'],['Đường còn lại',vn(R.x.S*100,0)+' %'],['Pectin','khoảng 30 % phần không tan trong cồn']],check:'Bóp hạt giữa hai ngón: còn nhớt trơn là lớp nhầy chưa bong; nhám, kêu sạn sạn là đã bong.',
  fail:'Nghĩ lớp nhầy chỉ là đường. Phần làm nhớt là pectin.',tip:'Đo Brix trái trước khi vào bồn để dự kiến tốc độ lên men.'},
 {n:'Bồn lên men',sub:()=>`${MTH[st.m].n} · giờ ${st.h}`,mech:()=>MTH[st.m].note+' Ba nhóm vi sinh cùng ăn một nguồn đường; nhóm nào hợp điều kiện thì lớn nhanh hơn và quyết định hương của mẻ.',
  kv:()=>[['Giờ',st.h+' giờ'],['pH',vn(R.x.pH,2)],['Nhiệt độ',st.T+' °C'],['Oxy',st.m==='kin'?'rất ít':st.m==='uot'?'ít':st.m==='kho'?'vừa':'nhiều']],check:'Đo pH, Brix, nhiệt độ mỗi 6 giờ; ngửi mùi mỗi lần đo.',
  fail:'Đặt giờ cố định cho mọi mẻ. Trời nóng bồn chạy nhanh gấp đôi.',tip:'MeDili dừng bồn men bia khi chạm pH 4,3.'},
 {n:'Nấm men',sub:()=>`${sci(R.x.Y)} tế bào/g`,mech:'Nấm men ăn đường, tạo cồn, CO₂ và các ester mùi trái cây. Một số loài tiết enzyme cắt pectin, giúp lớp nhầy bong.',
  kv:()=>[['Số lượng',sci(R.x.Y)+'/g'],['Cồn',vn(R.x.E,2)+' (tương đối)'],['Đỉnh',sci(Math.max(...SIM.map(o=>o.Y)))+'/g']],check:'Mùi trái chín, rượu nhẹ là nấm men đang làm việc.',fail:'Mùi rượu nồng kéo dài: bồn quá lâu, cồn sắp thành giấm nếu có oxy.',tip:'Men bia khởi động giúp nấm men có lợi chiếm chỗ sớm. Xem Lên men men bia.'},
 {n:'Vi khuẩn lactic',sub:()=>`${sci(R.x.L)} tế bào/g`,mech:'Vi khuẩn lactic ăn đường, tạo acid lactic là chính và làm pH xuống. Loại dị hình tạo thêm acid acetic, CO₂ và cồn. Chúng ưa ít oxy nên thường dẫn đầu trong bồn ngâm nước và bồn kín.',
  kv:()=>[['Số lượng',sci(R.x.L)+'/g'],['Acid lactic',vn(R.x.La,2)+' (tương đối)'],['pH',vn(R.x.pH,2)]],check:'Chua dịu, mùi sữa chua nhẹ.',fail:'Nghĩ vi khuẩn lactic làm cà phê ngọt hơn. Chúng tạo acid, không tạo đường.',tip:'Bồn kín và nước sạch giúp nhóm này chiếm ưu thế.'},
 {n:'Vi khuẩn acetic',sub:()=>`${sci(R.x.A)} tế bào/g`,mech:'Vi khuẩn acetic cần oxy và ăn cồn do nấm men tạo ra, biến thành acid acetic, mùi giấm. Chúng lớn mạnh khi bồn mở, đảo nhiều, phơi dày và ẩm, và khi bồn để quá lâu.',
  kv:()=>[['Số lượng',sci(R.x.A)+'/g'],['Acid acetic',vn(R.x.Ac,3)+' (tương đối)'],['Mức giấm',lvl(R.x.Ac,.08,.2)]],check:'Mùi giấm, chua xộc lên mũi khi mở bồn.',fail:'Thấy có acid acetic là đổ lỗi cho vi khuẩn acetic; vi khuẩn lactic dị hình cũng tạo một ít.',tip:'Giữ bồn ít oxy và dừng đúng lúc.'},
 {n:'Đo pH, Brix, nhiệt',sub:()=>`pH ${vn(R.x.pH,2)} · ${st.T} °C`,mech:'pH cho biết bồn chua tới đâu, Brix cho biết đường còn bao nhiêu, nhiệt độ cho biết bồn chạy nhanh hay chậm. Ba số cộng với mùi là đủ để quyết định dừng.',
  kv:()=>[['pH lúc này',vn(R.x.pH,2)],['Chạm pH 4,3 lúc',R.stop==null?'chưa chạm trong 96 giờ':R.stop+' giờ'],['Đường còn',vn(R.x.S*100,0)+' %']],check:'Hiệu chuẩn máy pH bằng dung dịch chuẩn pH 4 và pH 7 trước mỗi đợt.',fail:'Chỉ nhìn đồng hồ. Cùng 30 giờ, bồn 18 °C và 30 °C cho kết quả rất khác.',tip:'Phiếu theo dõi bồn ở cuối trang.'},
 {n:'Rửa và phơi',sub:()=>R.nat?'Natural: đảo đều, phơi mỏng':(R.stop==null?'Chưa tới mốc dừng':`Dừng gợi ý: giờ ${R.stop}`),mech:()=>R.nat?'Natural không có bước rửa. Trái phơi mỏng, đảo nhiều lần mỗi ngày để khô đều, tránh ẩm đọng làm vi sinh tạp và nấm mốc phát triển.':'Khi chạm mốc pH và lớp nhầy đã bong, xả nước, rửa sạch nhầy, đưa lên giàn phơi ngay. Rửa xong là dừng hoạt động của vi sinh trên bề mặt hạt.',
  kv:()=>[['Mốc dừng',R.nat?'không áp dụng':'pH 4,3'],['Dừng gợi ý',R.nat?'—':(R.stop==null?'chưa tới':R.stop+' giờ')],['Phơi tới ẩm','10–12 %']],check:'Rửa tới khi hạt nhám, nước trong. Phơi lớp mỏng, đảo đều.',fail:'Rửa xong để hạt ướt chất đống: vi sinh tiếp tục làm việc, dễ mốc.',tip:'Đưa lên giàn trong ngày, che mưa ban đêm.'}];

/* ====== DỰNG CẢNH ====== */
const ANCH=[null,[9,14,8],[24,13,10],[40,13,12.6],[55,13,8.4],[65,13,8.4],[75,13,8.4],[88,12,6],[110,14,5.2]];
const CHIP=[null,{x:176,y:12},{x:256,y:52},{x:336,y:92},{x:420,y:134},{x:500,y:176},{x:580,y:218},{x:664,y:262},{x:760,y:316}];
function flask(x,y,c,id){return frus(x,y,0,2.9,4,1,'gl','glt')+frus(x,y,.15,2.65,2.7,1.4,c,c)+cyl(x,y,4,1,2,'gl','glt')+`<g id="${id}"></g>`}
function buildScene(){
 let h=bench(124,24,'Cỗ máy Vi sinh · Farm Di Linh',44);
 /* 1 nguồn vi sinh */
 let s=frus(5.5,17.5,0,4,2,1.8,'soil','soilT');
 [[8,9.5],[10.4,10.6],[9,8],[11.6,8.8],[10,9.6],[12.4,10.2]].forEach(([x,y])=>s+=sph(x,y,0,1.15,'#B33A24'));
 s+=cyl(14,17,0,1.5,3.2,'jug','jugT')+cyl(2.6,11.5,0,1.3,2.6,'cu2','cu');
 const cl=P(8,12,11);[[0,0,15],[16,3,12],[-15,4,11],[7,-8,11]].forEach(([dx,dy,r])=>s+=`<circle class="cloud" cx="${f1(cl[0]+dx)}" cy="${f1(cl[1]+dy)}" r="${r}"/>`);
 h+=stG(1,s);
 /* 2 lớp nhầy */
 s=box(19.5,9.5,0,9,7,1.8,['ped','ped2','ped3'])+lcd(20.1,16.5,1.7,52,'kM');
 const m0=P(24,13,9.4);s+=cyl(24,13,1.8,.3,3.4,'cu2','cu2')+`<g transform="translate(${f1(m0[0])} ${f1(m0[1])})"><ellipse class="muc" cx="0" cy="0" rx="25" ry="33"/><ellipse class="bean" cx="-7.5" cy="0" rx="13" ry="22.5"/><ellipse class="bean" cx="7.5" cy="0" rx="13" ry="22.5"/><path d="M-7.5 -15c-3.5 10 3.5 20 0 30M7.5 -15c3.5 10-3.5 20 0 30" style="fill:none;stroke:#B9A274;stroke-width:1.1"/></g>`;
 h+=stG(2,s);
 /* 3 bồn */
 s=cyl(40,13,0,6.2,10,'gl','glt')+'<g id="tankIn"></g>'+'<g id="lid"></g>'+lcd(36.4,19.2,2.6,60,'kTank');
 h+=stG(3,s);
 /* 4–6 bình */
 h+=stG(4,flask(55,13,'fl1','f4'))+stG(5,flask(65,13,'fl2','f5'))+stG(6,flask(75,13,'fl4','f6'));
 /* 7 đo đạc */
 s=box(81,8.6,0,6.4,4,2.8,['#E6DCC8','#CFC2A8','#B7A98C'])+lcd(81.4,12.6,2.6,40,'kPH');
 s+=cyl(90.5,10.5,0,.42,8,'#F4ECDD','#F4ECDD')+cyl(90.5,10.5,0,.44,2.6,'#C0432A','#C0432A')+box(88.6,13,0,3.8,2.4,1.2,['#E6DCC8','#CFC2A8','#B7A98C'])+lcd(88.7,15.4,1.15,26,'kTe');
 s+=box(82.6,15.6,0,5.6,3,1.5,['#E6DCC8','#CFC2A8','#B7A98C'])+lcd(82.8,18.6,1.4,36,'kBx');
 h+=stG(7,s);
 /* 8 rửa và phơi */
 s=box(96,4.5,0,14,5,2.4,['#CFC2A8','#B7A98C','#A99878'])+poly([P(96.4,4.9,2.2),P(109.6,4.9,2.2),P(109.6,9.1,2.2),P(96.4,9.1,2.2)],'chan');
 [[101,13],[114.5,13],[101,21.5],[114.5,21.5]].forEach(([x,y])=>s+=box(x,y,0,.45,.45,3.2,['wo2','wo2','wo2']));
 s+=box(100.4,12.4,3.2,15,10,.55,['bed','bed2','bed2'])+'<g id="bedDots"></g>';
 h+=stG(8,s);
 h+='<g id="flow"></g><g id="chips"></g><circle id="tok" r="7"/>';
 $('scene').innerHTML=h;['kM','kTank','kPH','kTe','kBx'].forEach(i=>$(i).classList.add('sm'));initStations()}
function micro(cx,cy,z,rr,x){const q=P(cx,cy,z),g=rng(4);let s='';
 const n=[Math.round(clamp(x.Y-4.5,0,4)*4),Math.round(clamp(x.L-4.5,0,4.5)*4),Math.round(clamp(x.A-3,0,4.5)*4),Math.round(clamp(x.C-2.5,0,4.5)*3)],col=['#E3B341','#9A5BB5','#CB4D54','#8D6A45'];
 n.forEach((k,j)=>{for(let i=0;i<k;i++){const a=g()*Math.PI*2,r=Math.sqrt(g())*RX(rr)*.85;s+=`<circle cx="${f1(q[0]+Math.cos(a)*r)}" cy="${f1(q[1]+Math.sin(a)*r*.6+ (g()-.5)*30)}" r="${j===0?2.6:1.9}" style="fill:${col[j]};stroke:#3A2416;stroke-width:.4"/>`}});return s}
function renderScene(){const x=R.x;
 $('kM').textContent=`Brix ${st.bx}`;$('kTank').textContent=`${st.h} giờ · pH ${vn(x.pH,1)}`;$('kPH').textContent='pH '+vn(x.pH,2);$('kTe').textContent=st.T+'°C';$('kBx').textContent=vn(st.bx*(.3+.7*x.S),1)+' Bx';
 const lv=st.m==='nat'?2.4:st.m==='kho'?4.8:7.8;
 let s=cyl(40,13,.3,5.8,lv,'liqA','liqAT')+micro(40,13,lv*.55,5,x);
 const g=rng(8);for(let i=0;i<8;i++){const q=P(36.5+g()*7,10.5+g()*5,lv+.2);s+=`<circle class="bub" cx="${f1(q[0])}" cy="${f1(q[1])}" r="${f1(1.5+g()*2)}" style="animation-delay:${f1(g()*1.5)}s"/>`}
 $('tankIn').innerHTML=s;
 const top=P(40,13,10);$('lid').innerHTML=st.m==='kin'?disc(40,13,10.05,6.3,'#B7A98C')+cyl(40,13,10.05,.7,1.3,'#8D6A33','#A9823F'):`<ellipse cx="${f1(top[0]+52)}" cy="${f1(top[1]+24)}" rx="${f1(RX(6.3))}" ry="${f1(RY(6.3)*.45)}" style="fill:#B7A98C;stroke:#3A2416;stroke-width:1"/>`;
 [['f4',55,x.Y-4.5],['f5',65,x.L-4.5],['f6',75,x.A-3]].forEach(([id,cx,v],j)=>{const q=P(cx,13,1.4),n=Math.round(clamp(v,0,4.5)*3),gg=rng(20+j);let t='';for(let i=0;i<n;i++)t+=`<circle cx="${f1(q[0]+(gg()-.5)*22)}" cy="${f1(q[1]+(gg()-.5)*10)}" r="1.8" style="fill:#FFF6EC;stroke:#3A2416;stroke-width:.4"/>`;$(id).innerHTML=t});
 const gd=rng(31);let d='';const dc=R.nat?'#7A2414':'#E9DFC4';for(let i=0;i<60;i++){const q=P(101+gd()*13.8,13+gd()*8.6,3.77);d+=`<circle cx="${f1(q[0])}" cy="${f1(q[1])}" r="2.2" style="fill:${dc};stroke:#3A2416;stroke-width:.4"/>`}$('bedDots').innerHTML=d;
 drawFlow();drawChips()}
function chipLabel(i){const x=R.x;return ['','Nguồn vi sinh · '+HY[st.hyg].toLowerCase(),`Lớp nhầy · ${st.bx} °Brix`,`Bồn · giờ ${st.h} · pH ${vn(x.pH,1)}`,`Nấm men · ${sci(x.Y)}`,`Lactic · ${sci(x.L)}`,`Acetic · ${sci(x.A)}`,`pH ${vn(x.pH,2)} · ${st.T} °C`,R.nat?'Phơi mỏng, đảo đều':(R.stop==null?'Chưa tới mốc dừng':`Dừng ở giờ ${R.stop}`)][i]}
function drawFlow(){const x=R.x,lead=[['Nấm men',x.Y],['Vi khuẩn lactic',x.L],['Vi khuẩn acetic',x.A]].sort((a,b)=>b[1]-a[1])[0][0];
 const rows=[['Cách lên men',MTH[st.m].n],['Nhiệt độ, độ sạch',`${st.T}${NB}°C · ${HY[st.hyg].toLowerCase()}`],['Đang xem',`giờ ${st.h}`],['pH',vn(x.pH,2)],['Đường còn',vn(x.S*100,0)+NB+'%'],['Nhóm đông nhất',lead],['Mức giấm',lvl(x.Ac,.08,.2)]];
 const X=16,rh=27,h=50+rows.length*rh+20,y=712-h,w=330;
 let g=`<rect x="${X}" y="${y}" width="${w}" height="${h}" rx="10" class="pa" style="stroke:var(--ink);stroke-width:1.2"/><text x="${X+16}" y="${y+26}" class="lab12" style="letter-spacing:.08em">TRONG BỒN LÚC NÀY</text>`;
 rows.forEach(([a,b],i)=>{const yy=y+48+i*rh;g+=`<text class="flowT" x="${X+16}" y="${yy+4}">${a}</text><text x="${X+w-16}" y="${yy+4}" text-anchor="end" class="mono flowT">${b}</text>`});
 g+=`<text x="${X+16}" y="${y+h-10}" class="tiny mutedt">Bản vẽ khái niệm · số liệu theo mô hình minh hoạ</text>`;$('flow').innerHTML=g}

/* ====== BIỂU ĐỒ ====== */
const xt=[0,24,48,72,96];
function drawP(){const p=SIM.map(o=>[o.t,o.pH]);
 $('cP').innerHTML=lineSVG({W:340,H:150,l:30,r:10,t:18,b:22,x0:0,x1:96,y0:3.2,y1:6,xt,yt:[3.5,4.3,5],yf:v=>vn(v,1),ttl:'pH · trục ngang: giờ',hb:R.nat?[]:[[4.1,4.5]],ser:[{c:'var(--accent)',p}],vx:st.h});
 $('tip').textContent=R.nat?`Giờ ${st.h}: pH dịch quả khoảng ${vn(R.x.pH,2)}. Natural dừng theo độ khô, không theo pH.`:`Giờ ${st.h}: pH ${vn(R.x.pH,2)}. Vùng tô là pH 4,1–4,5, quanh mốc dừng 4,3 của MeDili.`}
function big(id,wid,ser,y0,y1,yt,yf,ttl,ttlm){const W=cw(wid),mob=W<640,H=mob?250:320;
 $(id).setAttribute('viewBox',`0 0 ${W} ${H}`);
 $(id).innerHTML=lineSVG({W,H,l:mob?40:52,r:mob?26:120,t:22,b:24,x0:0,x1:96,y0,y1,xt:mob?[0,48,96]:[0,12,24,36,48,60,72,84,96],xf:v=>v+' giờ',yt,yf,ttl:mob?ttlm:ttl,ser:ser.map(s=>({...s,lab:mob?'':s.n,w:2.4})),vx:st.h,end:!mob})}
function draw2(){big('c2','w2',GR.map(g=>({c:g.c,d:g.d,n:g.n,p:SIM.map(o=>[o.t,o[g.k]])})),2,10,[3,5,7,9],v=>'10'+sup(v),'Tế bào trên mỗi gam (thang log) · trục ngang: giờ','Tế bào/g, thang log');legend('lg2',GR)}
function draw3(){const S=[{k:'S',n:'Đường còn lại',c:'var(--cx3)'},{k:'E',n:'Cồn',c:'var(--cx1)'},{k:'La',n:'Acid lactic',c:'var(--cx2)'},{k:'Ac',n:'Acid acetic',c:'var(--cx4)'}];
 big('c3','w3',S.map(s=>({c:s.c,n:s.n,p:SIM.map(o=>[o.t,o[s.k]])})),0,1,[0,.5,1],v=>vn(v,1),'Chỉ số tương đối, 1 là lượng đường lúc đầu · trục ngang: giờ','Chỉ số tương đối');legend('lg3',S)}

/* ====== ĐIỀU KHIỂN ====== */
function verdict(){const x=R.x;let k='good',t,m;
 if(x.B>.04){k='bad';t='Nguy cơ mùi hành, mùi ôi';m='Vi sinh tạp sinh acid butyric, propionic khi bồn bẩn và để lâu. Rửa bồn, thay nước sạch, rút ngắn thời gian.'}
 else if(x.Ac>.2){k='bad';t='Mùi giấm rõ';m='Vi khuẩn acetic đã biến nhiều cồn thành acid acetic. Giảm oxy, dừng sớm hơn.'}
 else if(R.nat){if(x.Ac>.08){k='warn';t='Acid acetic đang tăng';m='Natural nhiều oxy: phơi mỏng, đảo đều, tránh đống dày và ẩm.'}else{t='Natural đang ổn';m='Giữ lớp phơi mỏng, đảo nhiều lần mỗi ngày, che mưa ban đêm.'}}
 else if(x.pH>4.6){k='warn';t='Chưa xong';m=`pH ${vn(x.pH,2)}: lớp nhầy có thể chưa bong, dừng lúc này dễ ngái. ${R.stop==null?'Bồn chưa chạm pH 4,3 trong 96 giờ, kiểm tra nhiệt độ.':'Dự kiến chạm pH 4,3 ở giờ '+R.stop+'.'}`}
 else if(x.Ac>.08||x.pH<3.95){k='warn';t='Đã quá mốc dừng';m=`pH ${vn(x.pH,2)}, acid acetic ${lvl(x.Ac,.08,.2)}. Nên rửa ngay.`}
 else{t='Vùng dừng tốt';m=`pH ${vn(x.pH,2)}, acid acetic còn thấp. Kiểm tra lớp nhầy đã bong rồi rửa, đưa lên giàn.`}
 $('verdict').className=k;$('verdict').innerHTML=`<b>${k==='good'?'✓':k==='warn'?'!':'✕'} ${t}</b>${m}`}
function stats(){const x=R.x,t=(a,b)=>`<div class="stat"><span>${a}</span><b>${b}</b></div>`;
 $('stats').innerHTML=t('pH lúc này',vn(x.pH,2))+t('Đường còn',vn(x.S*100,0)+NB+'%')+t('Chạm pH 4,3',R.nat?'—':(R.stop==null?'chưa':R.stop+NB+'giờ'))+t('Mức giấm',lvl(x.Ac,.08,.2))}
function sheet(){const t=`PHIẾU BỒN LÊN MEN · MeDili
Lô: ________  Ngày: ________  Người làm: ________
Cách lên men: ${MTH[st.m].n}  ·  Brix trái: ____ °Brix  ·  Bồn: ____ kg
Mốc dừng: pH 4,3, lớp nhầy bong, không mùi giấm

Giờ | pH  | Brix | °C  | Mùi (trái cây, rượu, chua, giấm, hành) | Ghi chú
  0 | ___ | ____ | ___ | ______________________________________ | ______
  6 | ___ | ____ | ___ | ______________________________________ | ______
 12 | ___ | ____ | ___ | ______________________________________ | ______
 18 | ___ | ____ | ___ | ______________________________________ | ______
 24 | ___ | ____ | ___ | ______________________________________ | ______
 30 | ___ | ____ | ___ | ______________________________________ | ______
 36 | ___ | ____ | ___ | ______________________________________ | ______

Dừng lúc: ____ giờ, pH ____ · Rửa xong: ____ · Lên giàn: ____
Mô hình dự kiến cho ${st.T} °C: chạm pH 4,3 ở ${R.nat?'(natural, không áp dụng)':(R.stop==null?'quá 96 giờ':'giờ '+R.stop)}`;
 $('sheet').textContent=t;st.sheet=t}
function sliders(){$('iT').value=st.T;$('oT').textContent=st.T+NB+'°C';$('iB').value=st.bx;$('oB').textContent=st.bx+NB+'°Brix';$('iH').value=st.h;$('oH').textContent='giờ '+st.h;
 $('tNote').textContent=st.T<=20?'Mát: bồn chạy chậm, hương sạch, cần nhiều giờ hơn.':st.T<=26?'Khoảng nhiệt thường gặp ở xưởng vùng cao.':'Nóng: bồn chạy nhanh gấp đôi, dễ quá mốc nếu không đo.';
 $('hNote').textContent=R.nat?'Natural: theo dõi 4 ngày đầu trên giàn.':(R.stop==null?'Bồn chưa chạm pH 4,3 trong 96 giờ.':`Mô hình chạm pH 4,3 ở giờ ${R.stop}.`)}
function update(){calc();
 pills('meths',Object.entries(MTH).map(([k,v])=>[k,v.n]),st.m,k=>{st.m=k;stopRun();stopTank();calc();if(R.stop!=null&&k!=='nat')st.h=R.stop;update()});
 pills('hygs',Object.entries(HY).map(([k,v])=>[k,v]),st.hyg,k=>{st.hyg=k;stopRun();stopTank();update()});
 $('mNote').textContent=MTH[st.m].note;sliders();stats();verdict();sheet();
 $('figsub').textContent=`${MTH[st.m].n}, ${st.T} °C, giờ ${st.h}: pH ${vn(R.x.pH,2)}`;
 renderScene();drawP();draw2();draw3();renderStation()}
const onIn=(id,f)=>$(id).addEventListener('input',()=>{stopRun();stopTank();f(+$(id).value);update()});
onIn('iT',v=>st.T=v);onIn('iB',v=>st.bx=v);onIn('iH',v=>st.h=v);
let tk=0;function stopTank(){clearInterval(tk);tk=0;$('scene').classList.remove('running')}
function runTank(){stopRun();stopTank();if(still){st.h=96;update();return}st.h=0;$('scene').classList.add('running');const seq=[1,2,3,4,5,6,7,8];let k=0;
 tk=setInterval(()=>{st.h=Math.min(96,st.h+1);const want=st.h<4?1:st.h<8?2:st.h<14?3:st.h<24?4:st.h<34?5:st.h<48?6:st.h<70?7:8;if(want!==st.sel)st.sel=want;update();if(st.h>=96){stopTank();}},60)}
$('run').onclick=runTank;$('run2').onclick=runTank;
$('reset').onclick=()=>{stopRun();stopTank();Object.assign(st,DEF);calc();st.h=R.stop||30;st.sel=3;update()};
$('cpSh').onclick=()=>cp(st.sheet,'cpShS');
buildScene();calc();st.h=R.stop||30;update();
let rz=0;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(()=>{draw2();draw3()},150)});
'''
