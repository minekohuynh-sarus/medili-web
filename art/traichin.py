# Cỗ máy Trái chín: từ hoa đến trái chín, đường từ lá vào hạt, Brix, hái tuốt hay hái chọn, độ cao.
# Nội dung viết mới cho MeDili, số liệu theo nguồn gốc (De Castro & Marraccini 2006, Joët 2010...).
from iso import *

FILE = 'trai-chin.html'
TITLE = 'Cỗ Máy Trái Chín MeDili'
DESC = ('Trái cà phê lớn và chín ra sao: các giai đoạn từ hoa đến trái chín, đường đi từ lá vào hạt, độ Brix, '
        'hái tuốt một lần hay hái chọn nhiều lượt, và độ cao ảnh hưởng thế nào. Mô hình tương tác của MeDili.')

READ = [
    ('trai', 'Brix là của thịt quả, không phải của nhân',
     'Khúc xạ kế đo đường và chất tan trong dịch thịt quả. Nhân nhận sucrose từ cây qua mạch dẫn ở giai đoạn làm đầy hạt, khoảng 130–190 ngày sau hoa ở Arabica. '
     'Thịt quả thì ngọt lên nhanh trong khoảng hai tháng cuối. Hai việc diễn ra ở hai phần khác nhau của trái, nên Brix cao cho biết trái đã chín, không đo được đường trong nhân.',
     'De Castro & Marraccini 2006'),
    ('nui', 'Vùng cao chín chậm hơn, không phải cứ cao là nhiều đường',
     'Lên cao 100 m, trời mát hơn khoảng 0,6 °C, trái chín chậm lại và có thêm thời gian làm đầy hạt. Nghiên cứu trên 16 lô Arabica ở đảo Réunion thấy nhiệt độ lúc hạt phát triển '
     'quyết định acid chlorogenic và acid béo; glucose tăng theo độ cao, nhưng tổng đường hoà tan không đổi theo khí hậu. Vị ngọt trong ly còn do độ chín, sơ chế và rang.',
     'Joët và cộng sự 2010'),
    ('hen', 'Robusta chín chậm hơn Arabica',
     'Arabica cần khoảng 6–8 tháng từ lúc hoa nở đến trái chín, Robusta cần 9–11 tháng. Vì vậy ở Di Linh, hoa nở tháng 3 thì đến tháng 11 mới vào mùa hái.',
     'Cannell 1985, theo De Castro & Marraccini 2006'),
    ('kinh', 'Màu đỏ là dấu hiệu, chưa phải thước đo',
     'Khi chín, diệp lục trong vỏ giảm và sắc tố đỏ anthocyanin tăng. Nhưng có giống chín màu vàng, và trái đỏ sẫm có thể đã chín quá. '
     'Nhìn màu, bóp thử độ mềm và đo Brix cùng lúc mới chắc.',
     'De Castro & Marraccini 2006'),
    ('can', 'Hái tuốt lẫn trái xanh là mất hai lần',
     'Trái xanh chưa làm đầy hạt nên nhẹ cân và kéo vị ngái, chát vào cả mẻ. Tuốt mạnh còn làm gãy cành mang trái và rụng lá, vụ sau ít trái hơn. '
     'Hái chọn tốn công hơn nhưng mẻ đồng đều, lên men và phơi dễ kiểm soát.',
     'MeDili'),
    ('lua', 'Chín quá cũng là lỗi',
     'Trái để quá lâu trên cây, hoặc hái về để qua đêm mới xát, đã bắt đầu lên men trong vỏ. Mẻ có nhiều trái như vậy dễ mang mùi chua giấm, mùi rượu.',
     'Sweet Maria’s, mục Ferment'),
]

BRIX_SOP = [
    ('Chọn mẫu', 'Mỗi lô chọn 10 cây đại diện, mỗi cây lấy 10 trái ở giữa tán, đủ các phía của cây.', '100 trái mỗi lô', 'Không chỉ hái trái đẹp nhất.'),
    ('Lấy dịch', 'Bóp vài trái lấy dịch thịt quả, nhỏ 2–3 giọt phủ kín lăng kính khúc xạ kế.', 'Khúc xạ kế 0–32 °Brix', 'Dịch không lẫn vỏ, không bọt.'),
    ('Đọc và lau', 'Đọc °Brix, rửa lăng kính bằng nước sạch, thấm khô rồi mới đo mẫu kế.', '5 lần đọc mỗi cây', 'Hiệu chuẩn bằng nước cất về 0 trước mỗi buổi.'),
    ('Ghi sổ', 'Ghi ngày, lô, màu trái, °Brix và tính trung bình từng lô.', 'Sổ Brix theo lô', 'Ghi cả trái xanh và chín quá để so.'),
    ('So với ly', 'Sau một hai vụ, so Brix lúc hái với điểm cupping của từng mẻ để biết vườn mình ngon nhất ở khoảng Brix nào.', 'Dữ liệu riêng của farm', 'Mỗi giống, mỗi lô có ngưỡng riêng.'),
]

SRC = [
    ('De Castro R. D., Marraccini P. (2006). Cytology, biochemistry and molecular changes during coffee fruit development. Braz. J. Plant Physiol. 18(1): 175–199', 'DOI', 'https://www.doi.org/10.1590/S1677-04202006000100013'),
    ('Joët T. và cộng sự (2010). Influence of environmental factors, wet processing and their interactions on the biochemical composition of green Arabica coffee beans. Food Chemistry 118(3): 693–701', 'CIRAD', 'https://agritrop.cirad.fr/551309'),
    ('Brix in coffee: trái chín đạt chuẩn đặc sản thường đọc 18–24 °Brix, tuỳ giống và điều kiện trồng', 'Green Coffee Collective', 'https://greencoffeecollective.com/pages/glossary/brix'),
    ('Ferment: lỗi chua giấm do trái chín quá, xát chậm, để lâu trong bồn', 'Sweet Maria’s', 'https://library.sweetmarias.com/glossary/ferment/'),
]


def page():
    read = boxes(READ)
    sop = ''.join(f'<li><span class="n">{i}</span><div><h3>{t}</h3><p>{d}</p></div><p><span class="lbl">Dụng cụ, số lượng</span>{a}</p><p><span class="lbl">Lưu ý</span>{c}</p></li>'
                  for i, (t, d, a, c) in enumerate(BRIX_SOP, 1))
    body = head('Trái chín', 'Cỗ máy',
                'Một trái Robusta ở Di Linh cần khoảng 9–11 tháng từ lúc hoa nở đến lúc chín. Kéo thanh ngày để xem trái lớn, hạt làm đầy, vỏ đổi màu và độ Brix tăng; '
                'rồi thử hái tuốt một lần hay hái chọn nhiều lượt để xem mẻ trái về xưởng khác nhau thế nào.')
    body += f'''
<div class="bench">
  <div class="card">
    <div class="fighead">
      <div><b>Hình 1</b> <span id="figsub"></span></div>
      <button class="btn small" id="run2" type="button">Chạy cả mùa</button>
    </div>
    <div class="scroller"><svg id="scene" viewBox="0 0 1040 720" aria-label="Bàn mô hình chín trạm: nắng và lá, hoa nở, bốn giai đoạn của trái, đo Brix, hái, tuyển nổi. Bấm từng trạm để xem chi tiết."></svg></div>
    <div class="strip" id="strip" role="group" aria-label="Chọn trạm"></div>
    <div id="detail" aria-live="polite"></div>
  </div>

  <aside class="card ctl">
    <div class="head2"><h3>Giống và vùng trồng</h3><small>2 giống</small></div>
    <div class="row" id="vars"></div>
    <p class="mnote" id="vNote"></p>
    <div class="sl"><label for="iA">Độ cao vườn <output id="oA"></output></label><input id="iA" type="range" step="50"><p id="aNote"></p></div>
    <hr>
    <div class="sl" style="margin-top:0"><label for="iD">Ngày sau khi hoa nở <output id="oD"></output></label><input id="iD" type="range" min="0" step="1"><p id="dNote"></p></div>
    <div class="head2" style="margin-top:12px"><h3>Số đợt hoa nở</h3></div>
    <div class="row" id="waves"></div>
    <div class="head2" style="margin-top:12px"><h3>Cách hái</h3></div>
    <div class="row" id="meth"></div>
    <div class="sl" id="gGap"><label for="iG">Cách nhau giữa các lượt hái <output id="oG"></output></label><input id="iG" type="range" min="7" max="35" step="1"><p id="gNote">Farm MeDili hái 3 lượt, từ tháng 11 đến đầu tháng 1.</p></div>
    <div class="sl" id="gStrip"><label for="iS">Ngày hái tuốt <output id="oS"></output></label><input id="iS" type="range" step="1"><p>Mặc định là ngày có nhiều trái chín nhất.</p></div>
    <div class="row" style="margin-top:14px"><button class="btn main" id="run" type="button">Chạy cả mùa</button><button class="btn" id="reset" type="button">Về mặc định</button></div>
    <div class="stats" id="stats"></div>
    <div id="verdict"></div>
    <hr>
    <span class="lbl">Brix dịch quả của một trái điển hình</span>
    <div class="charts"><svg class="ch" id="cB" viewBox="0 0 340 150" role="img" aria-label="Độ Brix dịch quả theo ngày sau khi hoa nở"></svg></div>
    <div id="tip"></div>
  </aside>
</div>

<section class="card" id="ben-trong">
  <h2>Hình 2: bên trong trái theo ngày</h2>
  <p class="lead">Kéo thanh ngày ở Hình 1, mặt cắt đổi theo. Mốc thời gian lấy theo tài liệu tổng hợp cho Arabica; với Robusta, MeDili quy đổi theo cùng tỷ lệ vì tài liệu chưa tách mốc riêng.</p>
  <div class="cut2">
    <div class="cutw"><svg id="cut" viewBox="0 0 560 330" role="img" aria-label="Mặt cắt trái cà phê: vỏ quả, thịt quả, vỏ trấu, perisperm và nội nhũ theo ngày"></svg></div>
    <div><div class="bars gb" id="gbars"></div><div id="tline"></div><p class="mnote" id="cutNote"></p></div>
  </div>
</section>

<section class="card" id="hai">
  <h2>Hình 3: hái tuốt một lần hay hái chọn nhiều lượt</h2>
  <p class="lead">400 trái trên một nhóm cây. Hoa nở theo số đợt chị chọn, mỗi trái chín sớm muộn khác nhau vài tuần. Vùng màu cho biết trái trên cây đang ở độ chín nào theo ngày; vạch đứt là các lượt hái. Đây là mô hình minh hoạ, không phải số đo của vườn.</p>
  <figure class="pf" style="max-width:760px;margin:6px 0 14px"><img src="assets/p-mua-chin.jpg" alt="Bàn tay hái giữa những chùm cà phê có trái xanh, ương, chín và chín quá" width="1500" height="1000" loading="lazy"><figcaption>Ảnh thực tế: trên cùng một cành có trái xanh, trái ương, trái chín và trái chín quá. Vì thế hái chọn thường phải đi nhiều lượt.</figcaption></figure>
  <div class="lg" id="lg3"></div>
  <div class="chw" id="w3"><svg id="c3" class="c2" role="img" aria-label="Tỷ lệ trái xanh, ương, chín, chín quá, khô trên cây theo ngày"></svg></div>
  <span class="lbl" style="margin-top:14px">Mẻ trái về xưởng · cột phải là tỷ lệ trái chín</span>
  <div id="mix"></div>
  <p class="mnote">Hái chọn: mỗi lượt lấy trái chín, chín quá và khô, lẫn một ít trái ương; lượt cuối vét hết trái còn lại. Hái tuốt: lấy hết trái trên cành trong một ngày.</p>
</section>

<section class="card">
  <h2>Đường đi từ lá vào hạt</h2>
  <p class="lead">Vị ngọt của ly cà phê bắt đầu từ chiếc lá, nhưng đường vào nhân và vào thịt quả theo hai lối, ở hai thời điểm khác nhau.</p>
  <div class="flowx">
    <div><span class="k">1 · Lá</span><b>Quang hợp</b><p>Nắng, CO₂ và nước thành đường. Lá khỏe, cây không mang quá nhiều trái so với lá thì hạt mới đủ nguồn nuôi.</p></div>
    <div><span class="k">2 · Mạch libe</span><b>Sucrose lên đường</b><p>Đường đi khắp cây dưới dạng sucrose, tới hoa, trái và hạt đang lớn.</p></div>
    <div><span class="k">3 · Nhân</span><b>Làm đầy hạt</b><p>Ở Arabica, khoảng ngày 130–190 sau hoa, nội nhũ tích sucrose và đạm dự trữ. Lúc thu hoạch, sucrose trong nhân trung bình 9,4 % chất khô ở Arabica, 6 % ở Robusta.</p></div>
    <div><span class="k">4 · Thịt quả</span><b>Ngọt lên cuối mùa</b><p>Khoảng hai tháng cuối, thịt quả tích đường nhanh, vỏ đổi màu. Đây là đường mà khúc xạ kế đo được.</p></div>
    <div><span class="k">5 · Lò rang</span><b>Đường thành hương</b><p>Sucrose trong nhân bị phân huỷ gần hết khi rang vừa, tạo caramel và tham gia phản ứng Maillard. Xem <a class="lnk" href="tien-chat-huong.html">Cỗ máy Tiền chất hương</a>.</p></div>
  </div>
</section>

<section class="p-sec">
  <p class="eye">MeDili đọc lại</p>
  <h2 class="p-h2" style="margin:0">Sáu điều <em>về trái chín.</em></h2>
  <div class="g3">{read}</div>
</section>

<div class="cols">
  <section class="card">
    <h2>Đo Brix ngoài vườn</h2>
    <p class="lead">Brix là công cụ chọn ngày hái, không phải điểm chất lượng. Đo đều mỗi lượt, ghi sổ, sau vài vụ farm sẽ có ngưỡng của riêng mình.</p>
    <ol class="sop tight">{sop}</ol>
  </section>
  <section class="card">
    <h2>Ở farm MeDili</h2>
    <div class="medili">
      <h3>Đang làm</h3>
      <ul>
        <li>Tưới đều cả lô để hoa nở một lần, vụ sau chín tập trung hơn (<a class="lnk" href="vuon.html">Vườn 12 tháng</a>).</li>
        <li>Chia mùa hái làm 3 lượt, từ tháng 11 đến đầu tháng 1; trái xanh tối đa 5 % mỗi mẻ (<a class="lnk" href="trai-ca-phe.html">Cấu tạo trái</a>).</li>
      </ul>
      <h3 style="margin-top:12px">Nên làm thêm</h3>
      <ul>
        <li>Đo Brix 100 trái mỗi lô trước mỗi lượt hái, ghi cùng ngày nở hoa của lô.</li>
        <li>Trái hái về xát hoặc đưa lên giàn trong ngày, không để qua đêm.</li>
        <li>Tuyển nổi trước khi sơ chế, tách riêng trái nổi để không kéo hương lỗi vào mẻ tốt.</li>
      </ul>
    </div>
  </section>
</div>

<section class="card src">
  <h2>Nguồn và cách đọc mô hình</h2>
  <p class="lead">Mốc giai đoạn theo tài liệu tổng hợp; thời gian chín đổi theo nhiệt độ bằng một mô hình đơn giản: lên cao 100 m mát hơn 0,6 °C, trái cần thêm thời gian tương ứng. Đường cong Brix, độ chín lệch giữa các trái và cách hái là minh hoạ, dùng để hiểu và làm mốc khởi đầu, không thay cho số đo của vườn.</p>
  <ul>{srclist(SRC)}</ul>
  <div class="lnks"><a class="lnk" href="phan-biet-ca-phe.html">Cỗ máy Phân biệt cà phê</a><a class="lnk" href="trai-ca-phe.html">Cấu tạo trái</a><a class="lnk" href="vuon.html">Vườn 12 tháng</a><a class="lnk" href="vi-sinh.html">Cỗ máy Vi sinh</a><a class="lnk" href="tien-chat-huong.html">Cỗ máy Tiền chất hương</a><a class="lnk" href="journal.html">Tất cả kiến thức cà phê</a></div>
</section>
'''
    return doc(FILE, TITLE, DESC, body, css=ISO_CSS + CSS, js=ISO_JS + JS)


CSS = r'''
/* Cỗ máy Trái chín */
#scene .sun{fill:#E3B341}#scene .ray{stroke:#E3B341;stroke-width:2.4;stroke-linecap:round}
#scene .can1{fill:#A9743F}#scene .can2{fill:#8D5A32}#scene .can3{fill:#C08A4E}
#scene .flw{fill:#FFF6EC;stroke:#C9A15B;stroke-width:1}
#scene .ped{fill:#E6DCC8}#scene .ped2{fill:#CFC2A8}#scene .ped3{fill:#B7A98C}
#scene .bsk{fill:#A67B47}#scene .bskT{fill:#6E4A2A}
#scene .wat{fill:#E7CFA2;fill-opacity:.55}
#scene .lcd.sm{font-size:6.5px}
#scene .nowr{fill:none;stroke:var(--accent);stroke-width:2.4;stroke-dasharray:4 3}
.cut2{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:18px 28px;align-items:center}
@media (max-width:900px){.cut2{grid-template-columns:minmax(0,1fr)}}
.cutw svg{display:block;width:100%;height:auto}
.cutw text{font:600 12.5px var(--body);fill:var(--ink)}
.cutw .lead2{stroke:var(--ink);stroke-width:1;opacity:.6}
.gb .bar{grid-template-columns:178px minmax(0,1fr) 62px}
.gb .bar i{background:var(--cx3)}
.tl2{position:relative;display:flex;height:34px;margin-top:14px;border-radius:8px;overflow:hidden;font:600 .72rem var(--body)}
.tl2>div{display:flex;align-items:center;justify-content:center;text-align:center;padding:0 3px;line-height:1.1;color:#3A2416;border-right:1px solid var(--panel);min-width:0;overflow:hidden}
.tl2 .mk{position:absolute;top:-4px;bottom:-4px;width:3px;background:var(--accent);border-radius:2px;box-shadow:0 0 0 2px var(--panel)}
.tlx{display:flex;justify-content:space-between;font:500 .74rem var(--mono);color:var(--muted);margin-top:4px}
#mix .mrow2{display:grid;grid-template-columns:150px minmax(0,1fr) 64px;gap:10px;align-items:center;padding:5px 0;font-size:.88rem;border-bottom:1px solid var(--rule)}
#mix .mrow2.tot{font-weight:700}
#mix .mrow2.sel span:first-child{color:var(--accent)}
#mix .stk{display:flex;height:20px;border-radius:5px;overflow:hidden;background:var(--tint)}
#mix .stk i{display:block;height:100%;font:700 .7rem/20px var(--mono);font-style:normal;text-align:center;color:#FFF6EC;overflow:hidden;white-space:nowrap}
#mix .stk i.lt{color:#3A2416}
#mix b{font:700 .9rem var(--mono);text-align:right}
@media (max-width:620px){#mix .mrow2{grid-template-columns:96px minmax(0,1fr) 52px}}
'''

JS = r'''
const U=7,OX=196,OY=118,VBW=1040;
const VAR={rob:{n:'Robusta Di Linh',sh:'Robusta',T0:270,a0:1000,t0:21,amin:400,amax:1300,gap:21,note:'Robusta cần 9–11 tháng từ hoa đến trái chín. Ở Di Linh hoa nở khoảng tháng 3, hái từ tháng 11.'},
 ara:{n:'Arabica Cầu Đất',sh:'Arabica',T0:240,a0:1500,t0:18,amin:800,amax:1900,gap:12,note:'Arabica cần 6–8 tháng. Ở Cầu Đất, khoảng 1.500 m, trời mát nên trái chín chậm hơn vùng thấp.'}};
const DEF={v:'rob',alt:1000,s:.7,waves:2,meth:'sel',gap:21};
const st={...DEF,sel:5,day:210,sday:0};
const WAV={1:{w:[1],o:[0]},2:{w:[.6,.4],o:[0,14]},3:{w:[.45,.35,.2],o:[0,12,24]}};
const PH=[{n:'Trái non',a:0,b:.37,i:3},{n:'Nội nhũ thay chỗ',a:.37,b:.57,i:4},{n:'Làm đầy hạt',a:.57,b:.83,i:5},{n:'Đổi màu',a:.83,b:.97,i:6},{n:'Chín tới',a:.97,b:1.06,i:6},{n:'Chín quá',a:1.06,b:1.16,i:6},{n:'Khô trên cây',a:1.16,b:9,i:6}];
const CL=[{n:'Xanh',c:'#D8D0A8',lt:1},{n:'Ương',c:'#DFA13A',lt:1},{n:'Chín',c:'#B33A24'},{n:'Chín quá',c:'#7A2414'},{n:'Khô',c:'#4E3A2C'}];
const cls=s=>s<.88?0:s<.97?1:s<1.06?2:s<1.16?3:4;
const CS=[[0,'#D8D0A8'],[.83,'#D8D0A8'],[.88,'#DDBB55'],[.93,'#D9782E'],[.97,'#C0432A'],[1.01,'#B33A24'],[1.06,'#8E2A1A'],[1.16,'#5E2A1C'],[1.3,'#4A3326']];
const BX=[[0,3],[.57,4.5],[.83,7],[.88,10],[.97,17],[1.01,20],[1.06,22.5],[1.16,26]];
const SZ=[[0,.22],[.2,.42],[.37,.86],[.57,1],[1.06,1],[1.16,.93],[1.4,.82]];
const EN=[[0,0],[.3,0],[.57,1],[2,1]],DM=[[0,0],[.5,.04],[.83,1],[2,1]];
const hx=h=>[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)),toh=a=>'#'+a.map(v=>Math.round(v).toString(16).padStart(2,'0')).join('');
function col(s){if(s<=CS[0][0])return CS[0][1];for(let i=1;i<CS.length;i++)if(s<=CS[i][0]){const t=(s-CS[i-1][0])/(CS[i][0]-CS[i-1][0]),a=hx(CS[i-1][1]),b=hx(CS[i][1]);return toh(a.map((v,k)=>v+(b[k]-v)*t))}return CS[CS.length-1][1]}
const ip=(tb,s)=>interp(tb,clamp(s,tb[0][0],tb[tb.length-1][0]));
const brix=s=>s>=1.16?null:ip(BX,s);
const temp=()=>{const V=VAR[st.v];return V.t0-.6*(st.alt-V.a0)/100};
const dur=()=>{const V=VAR[st.v];return Math.round(V.T0*(V.t0-5)/(temp()-5))};
const phase=s=>PH.find(p=>s>=p.a&&s<p.b)||PH[PH.length-1];
const wk=f=>Math.round(f*dur()/7);
const D0=new Date(2026,2,10);
const dmy=d=>{const x=new Date(D0);x.setDate(x.getDate()+Math.round(d));return String(x.getDate()).padStart(2,'0')+'/'+String(x.getMonth()+1).padStart(2,'0')};

/* ====== 400 TRÁI VÀ HAI CÁCH HÁI ====== */
let CH=null,CHK='';
function cherries(){const T=dur(),key=st.v+T+st.waves;if(key===CHK)return CH;const r=rng(11),W=WAV[st.waves],a=[];
 for(let i=0;i<400;i++){let u=r(),k=0,acc=0;for(;k<W.w.length;k++){acc+=W.w[k];if(u<=acc)break}k=Math.min(k,W.w.length-1);
  a.push({b:W.o[k]+r()*4,T:T*(1+.045*gauss(r)),e:r()})}
 CH=a;CHK=key;return a}
const sOf=(c,d)=>(d-c.b)/c.T;
function onTree(d){const n=[0,0,0,0,0];cherries().forEach(c=>n[cls(sOf(c,d))]++);return n.map(v=>v/4)}
function bestStrip(){const T=dur();let best=0,bd=Math.round(T);for(let d=Math.round(.85*T);d<=Math.round(1.25*T);d++){const r=onTree(d)[2];if(r>best){best=r;bd=d}}return bd}
function strip(d){const n=[0,0,0,0,0];cherries().forEach(c=>n[cls(sOf(c,d))]++);return {passes:[{day:d,cnt:n}],tot:n}}
function selective(){const C=cherries(),T=dur(),pk=new Array(C.length).fill(false),passes=[];let day=Math.round(.85*T);
 while(day<1.4*T){let r=0;C.forEach(c=>{if(sOf(c,day)>=.97)r++});if(r>=.25*C.length)break;day++}
 for(let p=0;p<9;p++){const n=[0,0,0,0,0];C.forEach((c,i)=>{if(pk[i])return;const k=cls(sOf(c,day));if(k>=2||(k===1&&c.e<.08)||(k===0&&c.e<.01)){pk[i]=true;n[k]++}});
  passes.push({day,cnt:n});const left=pk.filter(x=>!x).length;
  if(left<=C.length*.04||p===7){if(left){const m=[0,0,0,0,0],d2=day+st.gap;C.forEach((c,i)=>{if(!pk[i]){pk[i]=true;m[cls(sOf(c,d2))]++}});passes.push({day:d2,cnt:m,vet:true})}break}
  day+=st.gap}
 const tot=[0,0,0,0,0];passes.forEach(p=>p.cnt.forEach((v,k)=>tot[k]+=v));return {passes,tot}}
const pct=(n,k)=>{const s=n.reduce((a,b)=>a+b,0);return s?n[k]/s*100:0};
let R={};
function calc(){const T=dur(),s=st.day/T,ph=phase(s),sel=selective(),stp=strip(st.sday),act=st.meth==='sel'?sel:stp,t=act.tot;
 const fl=clamp(pct(t,4)+.5*pct(t,3)+3,0,100);
 R={T,s,ph,b:brix(s),sel,stp,act,ripe:pct(t,2),green:pct(t,0),un:pct(t,1),over:pct(t,3)+pct(t,4),fl,np:act.passes.length};return R}

/* ====== 9 TRẠM ====== */
const ST=[
 {n:'Nắng và lá',sub:'Quang hợp tạo đường',mech:'Lá dùng nắng, CO₂ và nước để làm đường. Đường đi khắp cây dưới dạng sucrose, theo mạch libe tới hoa, trái và hạt. Lá khỏe, đủ nắng, đủ nước thì trái có nguồn đường để lớn và làm đầy hạt.',
  kv:()=>[['Dạng đường đi trong cây','Sucrose'],['Đường dẫn','Mạch libe'],['Nhận nhiều nhất','Trái đang làm đầy hạt']],check:'Lá dày, bóng, không cháy mép. Cây mang quá nhiều trái so với lá sẽ thiếu đường nuôi hạt, hạt lép và nhỏ.',
  fail:'Nghĩ rằng lá tốt là đủ. Cây ôm quá nhiều trái so với lá vẫn cho hạt nhẹ, hương mỏng.',tip:'Tỉa cành và giữ cây che bóng vừa phải để lá đủ nắng mà không cháy. Xem Vườn 12 tháng.'},
 {n:'Hoa nở',sub:()=>'Ngày 0, giả sử 10/3 ở Di Linh',mech:()=>`Sau đợt tưới đầu mùa khô, mầm hoa nở trong vài ngày, thụ phấn xong thì đậu trái. Hoa nở thành ${st.waves} đợt thì trái trên cùng một cành cũng chín thành ${st.waves} đợt, lệch nhau vài tuần.`,
  kv:()=>[['Số đợt hoa',st.waves+' đợt'],['Đợt sau nở muộn hơn',st.waves>1?WAV[st.waves].o.slice(1).map(x=>x+' ngày').join(', '):'không có'],['Robusta','Thụ phấn chéo, cần gió và côn trùng']],
  check:'Ghi ngày nở của từng đợt hoa trong lô để dự kiến ngày hái.',fail:'Tưới không đều làm hoa nở rải rác, mùa hái kéo dài và khó hái chín đều.',tip:'Lịch vườn MeDili tưới đều cả lô để hoa nở một lần.'},
 {n:'Trái non',sub:()=>`Tuần 0–${wk(.37)}`,mech:'Trái nhỏ, vỏ quả và vỏ lụa non (perisperm) lớn trước. Hạt bên trong mềm, gần như toàn nước, chưa có nội nhũ rõ.',
  kv:()=>[['Kéo dài',`${wk(.37)} tuần`],['Phần lớn trong hạt','Perisperm'],['Theo Arabica','Perisperm lớn tới tuần 11–12']],check:'Trái cứng, màu nhạt, cắt ngang thấy ruột trong, mọng nước.',fail:'Thấy trái đã to là tưởng hạt đã thành. Lúc này hạt chưa tích chất gì đáng kể.',tip:'Giữ ẩm và dinh dưỡng đều, trái non rụng nhiều nếu cây bị khô hạn.'},
 {n:'Nội nhũ thay chỗ',sub:()=>`Tuần ${wk(.37)}–${wk(.57)}`,mech:'Nội nhũ, phần sẽ thành nhân cà phê, lớn dần và chiếm chỗ của perisperm cho tới khi lấp đầy khoang hạt. Perisperm còn lại thành lớp vỏ lụa mỏng bám quanh nhân.',
  kv:()=>[['Kéo dài',`${wk(.57)-wk(.37)} tuần`],['Theo Arabica','Lấp đầy khoang hạt quanh tuần 19'],['Kích thước hạt','gần đạt mức cuối']],check:'Cắt ngang thấy phần nhân trắng đục lớn dần, lớp trong suốt mỏng đi.',fail:'Thiếu nước giai đoạn này cho hạt nhỏ, nhiều hạt lép.',tip:'Đây là lúc giữ nước tưới và bón đúng đợt mùa mưa.'},
 {n:'Làm đầy hạt',sub:()=>`Tuần ${wk(.57)}–${wk(.83)}`,mech:'Hạt đã đủ kích thước. Cây chuyển sucrose, đạm dự trữ và dầu vào nhân. Đây là lúc hạt tích tiền chất hương: đường, acid amin, lipid, acid hữu cơ, caffeine.',
  kv:()=>[['Kéo dài',`${wk(.83)-wk(.57)} tuần`],['Theo Arabica','Ngày 130–190 sau hoa'],['Sucrose lúc hái',st.v==='rob'?'khoảng 6 % chất khô':'khoảng 9,4 % chất khô']],check:'Trái nặng tay, cắt ngang nhân chắc, khó bóp.',fail:'Nghĩ trái đổi màu mới bắt đầu ngọt. Nhân đã tích đường từ trước, lúc vỏ còn chưa đổi màu.',tip:'Không để cây mang quá tải ở giai đoạn này, hạt sẽ nhẹ và hương mỏng.'},
 {n:'Đổi màu và chín',sub:()=>`Chín tới quanh tuần ${wk(.97)}–${wk(1.06)}`,mech:'Diệp lục trong vỏ giảm, sắc tố đỏ tăng, trái ương rồi chín đỏ. Thịt quả tích đường nhanh trong khoảng hai tháng cuối, Brix tăng. Để quá lâu thì trái chín quá, sẫm màu, rồi khô trên cây.',
  kv:()=>[['Chín tới',`ngày ${Math.round(.97*R.T)}–${Math.round(1.06*R.T)}`],['Khoảng',`${dmy(.97*R.T)} đến ${dmy(1.06*R.T)}`],['Chín quá sau',`ngày ${Math.round(1.06*R.T)}`]],check:'Trái đỏ đều, bóp nhẹ thấy mềm, hạt trượt ra dễ.',fail:'Trái đỏ sẫm tưởng là ngon nhất. Nhiều khi đó đã là trái chín quá.',tip:'Hái theo lượt để lấy đúng khoảng chín tới.'},
 {n:'Đo Brix',sub:()=>R.b==null?'Trái khô, không còn dịch':`${vn(R.b,1)} °Brix lúc này`,mech:'Khúc xạ kế đo độ khúc xạ của dịch thịt quả để ước lượng chất tan, chủ yếu là đường. Brix tăng theo độ chín nên là công cụ chọn ngày hái tốt, nhưng không cho biết đường trong nhân.',
  kv:()=>[['Brix lúc này',R.b==null?'không đo được':vn(R.b,1)+' °Brix'],['Trái chín đặc sản thường','18–24 °Brix'],['Pha của trái',R.ph.n]],check:'Hiệu chuẩn về 0 bằng nước cất, đo dịch của nhiều trái, lấy trung bình.',fail:'Lấy Brix làm điểm chất lượng. Brix cao do trái chín quá, mất nước cũng tăng.',tip:'Lập sổ Brix theo lô, so với điểm cupping sau vài vụ.'},
 {n:'Hái',sub:()=>st.meth==='sel'?`Hái chọn ${R.np} lượt`:`Hái tuốt ngày ${st.sday}`,mech:()=>st.meth==='sel'?`Người hái quay lại sau mỗi ${st.gap} ngày, chỉ lấy trái chín, chín quá và khô, lẫn một ít trái ương. Lượt cuối vét hết trái còn lại trên cây.`:'Một lần tuốt hết cả cành: nhanh, rẻ công, nhưng lấy cả trái xanh, ương lẫn trái chín quá.',
  kv:()=>[['Trái chín trong mẻ',vn(R.ripe,0)+' %'],['Trái xanh',vn(R.green,0)+' %'],['Ương',vn(R.un,0)+' %'],['Chín quá, khô',vn(R.over,0)+' %']],check:'Đếm ngẫu nhiên 100 trái trong rổ mỗi lượt.',fail:'Hái tuốt cho nhanh rồi định loại sau. Trái xanh đã lẫn vào mẻ thì khó tách hết.',tip:'Chuẩn MeDili: trái xanh tối đa 5 % mỗi mẻ.'},
 {n:'Tuyển nổi',sub:()=>`Nổi khoảng ${vn(R.fl,0)} %`,mech:'Đổ trái vào bể nước. Trái chín chắc chìm; trái khô, lép, sâu và nhiều trái chín quá nổi lên. Vớt riêng phần nổi để không kéo hương lỗi vào mẻ tốt.',
  kv:()=>[['Phần nổi ước tính',vn(R.fl,0)+' %'],['Trái chín còn lại',vn(R.ripe,0)+' %'],['Cách hái',st.meth==='sel'?'Hái chọn':'Hái tuốt']],check:'Nước sạch, thay sau mỗi vài mẻ. Vớt kỹ lớp nổi.',fail:'Trộn lại phần nổi vào mẻ cho đủ cân.',tip:'Sau tuyển nổi, sơ chế trong ngày. Xem Cỗ máy Vi sinh.'}];

/* ====== DỰNG CẢNH ====== */
const ANCH=[null,[8,14,13],[21,14,8.6],[33,13,5.4],[44,13,6.6],[55,13,7.6],[66,13,7.9],[77,12.5,4.2],[91,13,5.2],[111,14,6.6]];
const CHIP=[null,{x:176,y:12},{x:244,y:50},{x:318,y:90},{x:396,y:130},{x:474,y:170},{x:552,y:212},{x:634,y:256},{x:716,y:304},{x:800,y:356}];
const PED=[[29,1.25],[40,2.05],[51,2.7],[62,2.9]];
function buildScene(){
 let h=bench(124,24,'Cỗ máy Trái chín · Farm Di Linh',46);
 h+=`<polyline class="flowL" points="${pts([P(11,6,9.5),P(30,5,9),P(68,5,9)])}"/>`;
 /* 1 nắng và lá */
 const sp=P(-4,8,13);let s=`<g>${[0,45,90,135,180,225,270,315].map(a=>{const r1=19,r2=27,c=Math.cos(a*Math.PI/180),n=Math.sin(a*Math.PI/180);return `<line class="ray" x1="${f1(sp[0]+c*r1)}" y1="${f1(sp[1]+n*r1)}" x2="${f1(sp[0]+c*r2)}" y2="${f1(sp[1]+n*r2)}"/>`}).join('')}<circle class="sun" cx="${f1(sp[0])}" cy="${f1(sp[1])}" r="15"/></g>`;
 s+=cyl(8,14,0,.75,9.4,'cu2','cu2');
 const cp=P(8,14,11.2);[[-22,6,'can2',22],[20,8,'can2',21],[0,-11,'can1',27],[-12,-3,'can3',17],[13,-6,'can3',16],[2,10,'can1',15]].forEach(([dx,dy,c,r])=>s+=`<ellipse class="${c}" cx="${f1(cp[0]+dx)}" cy="${f1(cp[1]+dy)}" rx="${r}" ry="${f1(r*.78)}"/>`);
 h+=stG(1,s);
 /* 2 hoa */
 s=cyl(21,14,0,.45,7.6,'cu2','cu2');const b0=P(15.6,14,7.1),b1=P(26.4,14,7.8);
 s+=`<path d="M${f1(b0[0])} ${f1(b0[1])}L${f1(b1[0])} ${f1(b1[1])}" style="stroke:#6B4226;stroke-width:4;stroke-linecap:round;fill:none"/>`;
 for(let k=0;k<7;k++){const q=P(16.4+k*1.5,14,7.25+k*.09);[[-5,-3],[4,-5],[0,3],[-4,4],[5,2],[0,-7]].forEach(([dx,dy])=>s+=`<circle class="flw" cx="${f1(q[0]+dx)}" cy="${f1(q[1]+dy-4)}" r="3"/>`);s+=`<circle cx="${f1(q[0])}" cy="${f1(q[1]-4)}" r="1.6" style="fill:#DDBB55;stroke:none"/>`}
 h+=stG(2,s);
 /* 3–6 bệ trái */
 PED.forEach(([x,r],k)=>{let t=box(x,9,0,8,8,2.6,['ped','ped2','ped3'])+lcd(x+.4,17,2.4,48,'kP'+(k+3));
  t+=sph(x+4,13,2.6,r,k===3?'#B33A24':'#D8D0A8',k===3?'chRipe':'');
  if(k===3)t+=sph(x+1.7,15.4,2.6,1.4,'#DFA13A');
  h+=stG(k+3,t)});
 h+='<g id="now"></g>';
 /* 7 Brix */
 s=box(73.5,10.5,0,7,4,1.9,['#E6DCC8','#CFC2A8','#B7A98C'])+box(74.3,11,1.9,2.2,3,.8,['#C9A15B','#A9823F','#8D6A33'])+lcd(73.9,14.5,1.75,40,'kB')+'<g id="liveCh"></g>';
 h+=stG(7,s);
 /* 8 hái: hai rổ */
 s='';[[87,'kS1','TUỐT'],[96,'kS2','CHỌN']].forEach(([x,id,lb])=>{s+=cyl(x,13,0,3.2,2.8,'bsk','bskT')+`<g id="${id}"></g>`+`<g transform="${face(x-2,16.2,1.9)}"><text class="wtx" x="0" y="8" style="font-size:8px;fill:#FFF6EC">${lb}</text></g>`});
 h+=stG(8,s)+'<g id="bskOn"></g>';
 /* 9 tuyển nổi */
 s=box(103,8,0,15,11,5.2,['glt','gl','gl'])+poly([P(103,8,4.5),P(118,8,4.5),P(118,19,4.5),P(103,19,4.5)],'wat')+'<g id="flt"></g>'+lcd(103.8,19,2,52,'kF');
 h+=stG(9,s);
 h+='<g id="flow"></g><g id="chips"></g><circle id="tok" r="7"/>';
 $('scene').innerHTML=h;[3,4,5,6].forEach(i=>$('kP'+i).classList.add('sm'));initStations()}
function dots(id,x,y,z,r,n,mix,seed){const q=P(x,y,z),g=rng(seed);let s='';const tot=mix.reduce((a,b)=>a+b,0)||1;
 for(let i=0;i<n;i++){let u=g()*tot,k=0;while(k<4&&u>mix[k]){u-=mix[k];k++}const a=g()*Math.PI*2,rr=Math.sqrt(g())*RX(r)*.82;s+=`<circle cx="${f1(q[0]+Math.cos(a)*rr)}" cy="${f1(q[1]+Math.sin(a)*rr*.58)}" r="2.6" style="fill:${CL[k].c};stroke:#3A2416;stroke-width:.5"/>`}
 $(id).innerHTML=s}
function renderScene(){const r=R,T=r.T;
 PED.forEach(([x],k)=>{const p=PH[k];$('kP'+(k+3)).textContent=k<3?`tuần ${wk(p.a)}–${wk(p.b)}`:`tuần ${wk(.83)}–${wk(1.06)}`});
 const pi=r.ph.i-3,px=PED[pi][0]+4;$('now').innerHTML=disc(px,13,2.61,3.7,'nowr');
 const q=P(79,17.6,0),rad=2*ip(SZ,r.s);$('liveCh').innerHTML=`<circle cx="${f1(q[0])}" cy="${f1(q[1]-rad*U)}" r="${f1(rad*U)}" style="fill:${col(r.s)};stroke:#3A2416;stroke-width:1"/>`;
 $('kB').textContent=r.b==null?'— °Bx':vn(r.b,1)+' °Bx';
 dots('kS1',87,13,2.8,3.2,34,r.stp.tot,3);dots('kS2',96,13,2.8,3.2,34,r.sel.tot,5);
 const bx=st.meth==='sel'?96:87;$('bskOn').innerHTML=disc(bx,13,0,4.1,'nowr');
 const g=rng(9);let s='';const nf=Math.round(r.fl/2.5);for(let i=0;i<nf;i++){const q2=P(104+g()*13,9+g()*9,4.52);s+=`<circle cx="${f1(q2[0])}" cy="${f1(q2[1])}" r="2.4" style="fill:${g()<.5?'#4E3A2C':'#7A2414'};stroke:#3A2416;stroke-width:.4"/>`}$('flt').innerHTML=s;
 $('kF').textContent='nổi '+vn(r.fl,0)+' %';
 drawFlow();drawChips()}
function chipLabel(i){const r=R;return ['','Nắng và lá',`Hoa nở · ${st.waves} đợt`,`Trái non · tuần 0–${wk(.37)}`,`Nội nhũ · tuần ${wk(.37)}–${wk(.57)}`,`Làm đầy hạt · tuần ${wk(.57)}–${wk(.83)}`,`Chín tới · tuần ${wk(.97)}–${wk(1.06)}`,
 r.b==null?'Brix · trái khô':`Brix ${vn(r.b,1)} °Bx`,st.meth==='sel'?`Hái chọn ${r.np} lượt · ${vn(r.ripe,0)} % chín`:`Hái tuốt · ${vn(r.ripe,0)} % chín`,`Tuyển nổi · nổi ${vn(r.fl,0)} %`][i]}
function drawFlow(){const r=R,V=VAR[st.v];
 const rows=[['Giống, độ cao',`${V.sh} · ${fm(st.alt)}${NB}m`],['Nhiệt độ trung bình',`khoảng ${vn(temp(),1)}${NB}°C`],['Từ hoa đến chín',`${r.T} ngày, ${vn(r.T/30.4,1)} tháng`],['Đang xem',`ngày ${st.day} · tuần ${Math.round(st.day/7)}`],['Pha của trái',r.ph.n],['Brix dịch quả',r.b==null?'không còn dịch':vn(r.b,1)+NB+'°Bx'],['Mẻ hái',`${vn(r.ripe,0)}${NB}% chín · ${r.np} lượt`]];
 const x=16,rh=27,h=50+rows.length*rh+20,y=712-h,w=330;
 let g=`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="10" class="pa" style="stroke:var(--ink);stroke-width:1.2"/><text x="${x+16}" y="${y+26}" class="lab12" style="letter-spacing:.08em">MỘT VỤ TRÁI, TỪ HOA ĐẾN XƯỞNG</text>`;
 rows.forEach(([a,b],i)=>{const yy=y+48+i*rh;g+=`<text class="flowT" x="${x+16}" y="${yy+4}">${a}</text><text x="${x+w-16}" y="${yy+4}" text-anchor="end" class="mono flowT">${b}</text>`});
 g+=`<text x="${x+16}" y="${y+h-10}" class="tiny mutedt">Bản vẽ khái niệm · số liệu ước tính theo mô hình</text>`;$('flow').innerHTML=g}

/* ====== BIỂU ĐỒ ====== */
function drawB(){const T=R.T,xmax=Math.round(1.3*T),p=[];for(let d=0;d<=xmax;d+=3){const b=brix(d/T);if(b!=null)p.push([d,b])}
 const step=T>250?100:50,xt=[];for(let v=0;v<=xmax;v+=step)xt.push(v);
 $('cB').innerHTML=lineSVG({W:340,H:150,l:28,r:12,t:18,b:22,x0:0,x1:xmax,y0:0,y1:28,xt,yt:[0,10,20],ttl:'°Brix · trục ngang: ngày sau hoa nở',bands:[[.97*T,1.06*T,'chín tới']],ser:[{c:'var(--accent)',p}],vx:clamp(st.day,0,xmax)});
 $('tip').textContent=R.b==null?`Ngày ${st.day} (${dmy(st.day)}): trái đã khô trên cây.`:`Ngày ${st.day} (${dmy(st.day)}): ${R.ph.n.toLowerCase()}, Brix khoảng ${vn(R.b,1)} °Bx.`}
function draw3(){const T=R.T,W=cw('w3'),mob=W<760,H=mob?240:300,d0=Math.round(.75*T),d1=Math.round(1.32*T),cum=[];
 for(let d=d0;d<=d1;d+=2){const f=onTree(d);let a=0;cum.push([d,f.map(v=>a+=v)])}
 const areas=CL.map((c,k)=>({c:c.c,o:.92,p:cum.map(([d,a])=>[d,k?a[k-1]:0]).concat(cum.slice().reverse().map(([d,a])=>[d,a[k]]))}));
 const vl=(st.meth==='sel'?R.sel.passes.map((p,i)=>[p.day,mob?'':(p.vet?'vét':'L'+(i+1))]):[[st.sday,mob?'':'tuốt']]);
 const step=T>250?20:15,xt=[];for(let v=Math.ceil(d0/step)*step;v<=d1;v+=step*(mob?2:1))xt.push(v);
 $('c3').setAttribute('viewBox',`0 0 ${W} ${H}`);
 $('c3').innerHTML=lineSVG({W,H,l:mob?34:42,r:14,t:22,b:24,x0:d0,x1:d1,y0:0,y1:100,xt,xf:v=>mob?v:v+' ('+dmy(v)+')',yt:[0,50,100],yf:v=>v+'%',ttl:mob?'Trái trên cây theo độ chín (%)':'Trái trên cây theo độ chín · trục ngang: ngày sau hoa nở',areas,vl,vx:clamp(st.day,d0,d1)});
 legend('lg3',CL.map(c=>({c:c.c,n:c.n,box:1})))}
function mixRows(){const row=(lab,cnt,cls2)=>{const s=cnt.reduce((a,b)=>a+b,0)||1;return `<div class="mrow2 ${cls2||''}"><span>${lab}</span><div class="stk">${cnt.map((v,k)=>v?`<i class="${CL[k].lt?'lt':''}" style="width:${f1(v/s*100)}%;background:${CL[k].c}" title="${CL[k].n} ${vn(v/s*100,0)} %">${v/s>=.09?vn(v/s*100,0):''}</i>`:'').join('')}</div><b>${vn(cnt[2]/s*100,0)} %</b></div>`};
 let h='';R.sel.passes.forEach((p,i)=>h+=row(`${p.vet?'Lượt vét':'Lượt '+(i+1)} · ${dmy(p.day)}`,p.cnt));
 h+=row(`Tổng hái chọn`,R.sel.tot,'tot'+(st.meth==='sel'?' sel':''));h+=row(`Hái tuốt · ${dmy(st.sday)}`,R.stp.tot,'tot'+(st.meth==='strip'?' sel':''));
 $('mix').innerHTML=h}
function drawCut(){const s=R.s,k=ip(SZ,s),cx=168,cy=165,ax=96*k+14,ay=128*k+14,en=ip(EN,s),dm=ip(DM,s),ex=col(s);
 const dmc=toh(hx('#F7F0DE').map((v,i)=>v+(hx('#D8C597')[i]-v)*dm));
 let g=`<ellipse cx="${cx}" cy="${cy}" rx="${f1(ax)}" ry="${f1(ay)}" style="fill:${ex};stroke:#3A2416;stroke-width:1.4"/><ellipse cx="${cx}" cy="${cy}" rx="${f1(ax-11)}" ry="${f1(ay-11)}" style="fill:#EFD6AE"/>`;
 const sx=(ax-11)*.43,sy=(ay-11)*.74,xr=cx+sx+3,ee=Math.sqrt(en),dg=Math.PI/180;
 [-1,1].forEach(d=>{const x=cx+d*(sx+3);g+=`<ellipse cx="${f1(x)}" cy="${cy}" rx="${f1(sx)}" ry="${f1(sy)}" style="fill:#F3E6C6;stroke:#C9A15B;stroke-width:2.2"/><ellipse cx="${f1(x)}" cy="${cy}" rx="${f1(sx-4)}" ry="${f1(sy-4)}" style="fill:#EDE4CB;fill-opacity:.75"/>`;
  if(en>0)g+=`<ellipse cx="${f1(x+d*(1-Math.sqrt(en))*(sx-4)*.35)}" cy="${cy}" rx="${f1((sx-4)*Math.sqrt(en))}" ry="${f1((sy-4)*Math.sqrt(en))}" style="fill:${dmc};stroke:#B9A274;stroke-width:1"/>`});
 const L=[[cx+ax*Math.cos(-50*dg),cy+ay*Math.sin(-50*dg),'Vỏ quả'],[cx+(ax-5.5)*.0+(ax-11)*.93*Math.cos(-12*dg),cy+(ay-11)*.93*Math.sin(-12*dg),'Thịt quả'],[xr+sx*Math.cos(-35*dg),cy+sy*Math.sin(-35*dg),'Vỏ trấu'],[xr+(sx-4)*.93*Math.cos(30*dg),cy+(sy-4)*.93*Math.sin(30*dg),en<.95?'Perisperm':'Vỏ lụa'],[xr+(1-ee)*(sx-4)*.35,cy+sy*.12,'Nội nhũ (nhân)']];
 const lx=340;L.forEach(([x,y,t],i)=>{const ty=60+i*48;g+=`<line class="lead2" x1="${f1(x)}" y1="${f1(y)}" x2="${lx-6}" y2="${ty-4}"/><text x="${lx}" y="${ty}">${t}</text>`});
 g+=`<text x="${lx}" y="${300}" style="font:500 12px var(--mono);fill:var(--muted)">ngày ${st.day} · ${R.ph.n.toLowerCase()}</text>`;
 $('cut').innerHTML=g;
 const B=[['Kích thước trái',k,vn(k*100,0)+' %'],['Nội nhũ trong khoang hạt',en,vn(en*100,0)+' %'],['Chất khô trong nhân',dm,vn(dm*100,0)+' %'],['Brix thịt quả',(R.b||0)/26,R.b==null?'khô':vn(R.b,1)+' °Bx']];
 $('gbars').innerHTML=B.map(([n,v,t])=>`<div class="bar"><span>${n}</span><div class="track"><i style="width:${f1(clamp(v,0,1)*100)}%"></i></div><span>${t}</span></div>`).join('');
 const segs=[['Trái non',.37,'#EFE3C2'],['Nội nhũ',.2,'#E6D4A6'],['Làm đầy',.26,'#D9C08A'],['Đổi màu',.14,'#E2A15A'],['Chín',.09,'#C0563B'],['Quá',.1,'#8E3A2A']],tot=1.16;
 $('tline').innerHTML=`<div class="tl2">${segs.map(([n,f,c])=>`<div style="flex:${f};background:${c}">${n}</div>`).join('')}<i class="mk" style="left:calc(${f1(clamp(R.s/tot,0,1)*100)}% - 1px)"></i></div><div class="tlx"><span>hoa nở</span><span>tuần ${wk(.57)}</span><span>tuần ${wk(.97)}</span><span>tuần ${wk(1.16)}</span></div>`;
 $('cutNote').textContent=R.ph.n==='Khô trên cây'?'Trái đã khô trên cây: dễ mốc, nhiễm vi sinh, hương lỗi.':{'Trái non':'Perisperm chiếm gần hết hạt, nội nhũ chưa hình thành rõ.','Nội nhũ thay chỗ':'Nội nhũ lớn dần, đẩy perisperm thành lớp mỏng.','Làm đầy hạt':'Nhân tích sucrose, đạm và dầu: phần lớn tiền chất hương vào nhân ở giai đoạn này.','Đổi màu':'Vỏ đổi màu, thịt quả bắt đầu ngọt nhanh.','Chín tới':'Khoảng hái đẹp nhất: nhân đã đầy, thịt quả ngọt.','Chín quá':'Thịt quả bắt đầu lên men trong vỏ, nên hái gấp.'}[R.ph.n]}

/* ====== ĐIỀU KHIỂN ====== */
function verdict(){const r=R;let k='good',t,m;
 if(r.green>15){k='bad';t=`Mẻ lẫn ${vn(r.green,0)} % trái xanh`;m='Quá ngưỡng 5 % của MeDili. Trái xanh kéo vị ngái, chát vào cả mẻ; hái chọn hoặc lùi ngày hái.'}
 else if(r.green>5){k='warn';t=`Mẻ có ${vn(r.green,0)} % trái xanh`;m='Vượt ngưỡng 5 % trái xanh mỗi mẻ của MeDili. Lùi ngày hái hoặc thêm một lượt hái chọn.'}
 else if(r.ripe<60){k='warn';t=`Mẻ chỉ có ${vn(r.ripe,0)} % trái chín`;m=`Trái ương ${vn(r.un,0)} %, chín quá và khô ${vn(r.over,0)} %. Trái ương chưa đủ ngọt, trái chín quá dễ lên men trong vỏ: hái chọn nhiều lượt cho mẻ đều hơn.`}
 else if(r.over>15){k='warn';t=`${vn(r.over,0)} % trái chín quá hoặc khô`;m='Dễ mang mùi lên men, mốc. Hái các lượt gần nhau hơn.'}
 else{t=`Mẻ đạt: ${vn(r.ripe,0)} % trái chín`;m=`Trái xanh ${vn(r.green,0)} %, dưới ngưỡng 5 % của MeDili.`}
 const d=r.T-VAR[st.v].T0;m+=` Ở ${fm(st.alt)} m, trái cần khoảng ${r.T} ngày từ hoa đến chín${d?`, ${d>0?'chậm':'nhanh'} hơn ${Math.abs(d)} ngày so với ${fm(VAR[st.v].a0)} m`:''}.`;
 $('verdict').className=k;$('verdict').innerHTML=`<b>${k==='good'?'✓':k==='warn'?'!':'✕'} ${t}</b>${m}`}
function sliders(){const V=VAR[st.v],T=R.T;
 $('iA').min=V.amin;$('iA').max=V.amax;$('iA').value=st.alt;$('oA').textContent=fm(st.alt)+NB+'m';$('aNote').textContent=`Ước tính khoảng ${vn(temp(),1)} °C trung bình. Lên cao 100 m, trời mát hơn khoảng 0,6 °C.`;
 $('iD').max=Math.round(1.3*T);$('iD').value=st.day;$('oD').textContent=`ngày ${st.day}`;$('dNote').textContent=`Khoảng ${dmy(st.day)} nếu hoa nở 10/3 · tuần ${Math.round(st.day/7)} · ${R.ph.n.toLowerCase()}.`;
 $('iG').value=st.gap;$('oG').textContent=st.gap+' ngày';
 $('iS').min=Math.round(.85*T);$('iS').max=Math.round(1.25*T);$('iS').value=st.sday;$('oS').textContent=`ngày ${st.sday} · ${dmy(st.sday)}`;
 $('gGap').hidden=st.meth!=='sel';$('gStrip').hidden=st.meth!=='strip'}
function stats(){const r=R,t=(a,b)=>`<div class="stat"><span>${a}</span><b>${b}</b></div>`;
 $('stats').innerHTML=t('Pha của trái',r.ph.n)+t('Brix dịch quả',r.b==null?'—':vn(r.b,1)+NB+'°Bx')+t('Trái chín trong mẻ',vn(r.ripe,0)+NB+'%')+t('Số lượt hái',r.np)}
function update(full){if(full){st.sday=bestStrip()}calc();
 pills('vars',Object.entries(VAR).map(([k,v])=>[k,v.n]),st.v,k=>{const f=st.day/R.T;st.v=k;st.alt=VAR[k].a0;st.gap=VAR[k].gap;stopRun();CHK='';calc();st.day=Math.round(f*R.T);update(1)});
 pills('waves',[1,2,3].map(x=>[x,x+' đợt']),st.waves,k=>{st.waves=+k;stopRun();update(1)});
 pills('meth',[['sel','Hái chọn nhiều lượt'],['strip','Hái tuốt một lần']],st.meth,k=>{st.meth=k;stopRun();update()});
 $('vNote').textContent=VAR[st.v].note;
 sliders();stats();verdict();
 $('figsub').textContent=`${VAR[st.v].sh}, ${fm(st.alt)} m, ngày ${st.day} sau hoa nở: ${R.ph.n.toLowerCase()}`;
 renderScene();drawB();draw3();mixRows();drawCut();renderStation()}
const onIn=(id,f,full)=>$(id).addEventListener('input',()=>{stopRun();stopSeason();f(+$(id).value);update(full)});
onIn('iA',v=>{const fr=st.day/R.T;st.alt=v;CHK='';calc();st.day=Math.round(fr*R.T)},1);
onIn('iD',v=>{st.day=v;const p=phase(v/R.T);st.sel=p.i});
onIn('iG',v=>st.gap=v);onIn('iS',v=>st.sday=v);
let sea=0;function stopSeason(){clearInterval(sea);sea=0}
function season(){stopRun();stopSeason();const end=Math.round(1.2*R.T);if(still){st.day=end;st.sel=8;update();return}st.day=0;let last=-1;
 sea=setInterval(()=>{st.day=Math.min(end,st.day+3);const p=phase(st.day/R.T);if(p.i!==last){last=p.i;st.sel=p.i}update();if(st.day>=end){stopSeason();st.sel=8;update()}},45)}
$('run').onclick=season;$('run2').onclick=season;
$('reset').onclick=()=>{stopRun();stopSeason();const v=st.v;Object.assign(st,DEF,{v,alt:VAR[v].a0,gap:VAR[v].gap});CHK='';calc();st.day=Math.round(DEF.s*R.T);st.sel=5;update(1)};
buildScene();calc();st.day=Math.round(DEF.s*R.T);update(1);
let rz=0;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(draw3,150)});
'''
