# Cỗ máy Tiền chất hương: thành phần nhân xanh, biến đổi khi rang, chất hương, dầu và caffeine vào ly.
# Số liệu thành phần theo Clarke (1987) do IARC (2018) tổng hợp; chất hương theo Buffo & Cardelli-Freire (2004).
from iso import *

FILE = 'tien-chat-huong.html'
TITLE = 'Cỗ Máy Tiền Chất Hương MeDili'
DESC = ('Hạt cà phê xanh tích sẵn đường, acid amin, dầu, acid hữu cơ, acid chlorogenic, caffeine, trigonelline. Khi rang, chúng thành caramel, '
        'chất hương và màu nâu. Mô hình tương tác của MeDili theo giống, mức rang và cách pha.')

CHAIN = [
    ('trai', 'Trái chín', 'Tích', 'Hạt làm đầy đường, đạm, dầu khi trái chín đúng độ. Hái xanh là hạt thiếu tiền chất từ gốc.', 'trai-chin.html'),
    ('visinh', 'Lên men', 'Chuyển', 'Vi sinh ăn lớp nhầy, tạo acid và ester; lên men quá thì kéo mùi giấm, mùi hành vào hạt.', 'vi-sinh.html'),
    ('phoi', 'Phơi, sấy', 'Giữ', 'Đưa ẩm hạt về 10–12 % đều tay. Phơi dày, ẩm đọng dễ mốc; sấy quá nóng làm hạt mất hương.', 'len-men-men-bia.html'),
    ('tui', 'Bảo quản', 'Giữ', 'Kho khô, mát, thoáng, kê cao khỏi nền. Nhân để lâu, ẩm hoặc nóng sẽ nhạt hương, mùi bao bố, mùi cũ.', 'xuong-rang.html'),
    ('kinh', 'Phân loại, bắn màu', 'Bỏ lỗi', 'Loại đá, kim loại, hạt đen, hạt sâu, hạt lên men. Một hạt lỗi đủ làm hỏng mùi cả mẻ rang.', 'xuong-rang.html'),
    ('can', 'Tuyển cỡ, tỷ trọng', 'Làm đều', 'Hạt cùng cỡ, cùng tỷ trọng thì chín đều trong lò; hạt nhỏ lẫn hạt to sẽ cháy và sống cùng lúc.', 'xuong-rang.html'),
    ('rang', 'Rang', 'Mở khoá', 'Lò rang không tạo hương từ con số 0, nó biến tiền chất đã có thành hàng trăm chất hương bay hơi.', 'rang.html'),
]

READ = [
    ('ly', 'Càng đắng không phải càng nhiều caffeine',
     'Caffeine có vị đắng nhưng chỉ chiếm 1–2,5 % nhân. Vị đắng của ly còn đến từ sản phẩm phân huỷ của acid chlorogenic và các sản phẩm của phản ứng Maillard, '
     'nhiều hơn khi rang đậm. Robusta đắng hơn vì có cả caffeine lẫn acid chlorogenic nhiều hơn Arabica.', 'Clarke 1987, theo IARC 2018'),
    ('rang', 'Rang đậm không làm tăng caffeine',
     'Caffeine bền nhiệt, gần như không mất khi rang. Tính trên chất khô, con số nhích lên một chút vì hạt mất khối lượng: Arabica từ 1,2 lên 1,3 %, Robusta từ 2,2 lên 2,4 % khi rang vừa. '
     'Đong bằng muỗng thì hạt rang đậm nhẹ và xốp hơn, mỗi muỗng lại ít caffeine hơn.', 'Clarke 1987, theo IARC 2018'),
    ('phin', 'Nhiều dầu không có nghĩa là thân dày',
     'Thân (body) của ly đến từ dầu, hạt mịn lơ lửng, melanoidin và polysaccharide hoà tan. Giấy lọc giữ lại gần hết dầu nhưng ly lọc vẫn có thân nếu chiết đủ.', 'Buffo & Cardelli-Freire 2004'),
    ('nhan', 'Robusta có khoảng 10 % dầu, Arabica khoảng 16 %',
     'Theo bảng thành phần thường dùng, nhân xanh Arabica chứa khoảng 16 % lipid, Robusta khoảng 10 % chất khô. Các con số khác nhau giữa nguồn, nhưng Arabica luôn nhiều dầu hơn.', 'Clarke 1987, theo IARC 2018'),
    ('la', 'Phôi rất nhỏ, nhân gần như toàn là nội nhũ',
     'Phôi là mầm cây nằm ở một đầu nhân, chỉ dài vài milimét. Gần như toàn bộ khối lượng nhân là nội nhũ, nơi cây cất đường, đạm, dầu và các tiền chất hương.', 'De Castro & Marraccini 2006'),
    ('phantu', 'Khoảng 900 chất bay hơi, nhưng chưa tới 20 chất quyết định mùi',
     'Người ta đã nhận diện khoảng 900 chất bay hơi trong cà phê rang, nhưng chỉ chưa tới 20 chất có vai trò rõ trong mùi cà phê, như 2-furfurylthiol mùi rang, furaneol mùi caramel, '
     '4-vinylguaiacol mùi đinh hương.', 'Buffo & Cardelli-Freire 2004'),
]

SRC = [
    ('IARC (2018). Monographs Vol. 116, Coffee: bảng 15 và 16, thành phần cà phê xanh và rang vừa theo Clarke (1987); diterpene trong ly lọc và espresso theo Viani (1988)', 'IARC',
     'https://publications.iarc.who.int/_publications/media/download/1796/e3b9d8b93f56977f63fd3c4b9aff66e768296f17.pdf'),
    ('Buffo R. A., Cardelli-Freire C. (2004). Coffee flavour: an overview. Flavour and Fragrance Journal 19: 99–104', 'Đại học Oregon',
     'https://pages.uoregon.edu/chendon/coffee_literature/old_literature/2004%20Flav.%20Frag.%20J.,%20An%20overview%20of%20coffee%20flavor.pdf'),
    ('Gross G. và cộng sự (1997). Analysis of the content of the diterpenes cafestol and kahweol in coffee brews. Food Chem Toxicol 35(6): 547–554', 'PubMed', 'https://pubmed.ncbi.nlm.nih.gov/9225012/'),
    ('Lang R. và cộng sự (2008). Quantitative investigation of trigonelline, nicotinic acid, and nicotinamide… J Agric Food Chem. Niacin hình thành khoảng 4–6 % lượng trigonelline ban đầu', 'TU München',
     'https://portal.fis.tum.de/en/publications/quantitative-investigation-of-trigonelline-nicotinic-acid-and-nic/'),
    ('Roasters Guild (2008). Advanced Level Craft Roasting: mất acid chlorogenic tăng theo độ rang; hương tạo ra nhiều nhất ở rang sáng', 'Sweet Maria’s', 'https://library.sweetmarias.com/wp-content/uploads/2020/08/Advanced-Level-Craft-Roasting.pdf'),
    ('Rao N. Z., Fuller M. (2018). pH và độ chua chuẩn độ của cà phê pha nóng và cold brew, Scientific Reports', 'ScienceDaily', 'https://www.sciencedaily.com/releases/2018/11/181101085137.htm'),
]

FLOW = [
    ('Đường và acid amin', 'Maillard', '2-furfurylthiol: mùi rang, bánh mì nướng · furaneol: caramel · methional: khoai tây luộc · pyrazine: hạt rang, khét khi đậm', 'sug'),
    ('Acid amin', 'Strecker', 'Aldehyde Strecker như 3-methylbutanal: mạch nha, cacao; góp phần lớn vào mùi bột cà phê mới xay', 'sug'),
    ('Đường sucrose', 'Caramel hoá', 'Mùi caramel, đường cháy, màu nâu; acid acetic, acid formic sinh ra rồi bay đi dần', 'sug'),
    ('Acid chlorogenic', 'Phân huỷ phenol', '4-vinylguaiacol: đinh hương · guaiacol: khói, nhựa · vanillin: vani; phần acid quinic để lại vị chát, chua gắt', 'dry'),
    ('Trigonelline', 'Phân huỷ nhiệt', 'Pyridine: mùi rang; khoảng 4–6 % thành niacin, tức vitamin B3', 'dry'),
    ('Carotenoid', 'Phân huỷ sắc tố', 'β-damascenone: mùi trái cây chín', 'enz'),
    ('Lipid', 'Giữ, không phản ứng nhiều', 'Giữ chất thơm, tạo cảm giác mượt; diterpene cafestol, kahweol đi vào ly qua lưới kim loại', 'lip'),
]


def page():
    chain = ''.join(f'<li><span class="n">{icon(i)}</span><h3><small>{n:02d} · {k}</small><a class="lnk" href="{h}">{t}</a></h3><p>{p}</p></li>'
                    for n, (i, t, k, p, h) in enumerate(CHAIN, 1))
    flow = ''.join(f'<div class="fr" data-g="{g}"><div><b>{a}</b></div><div class="fx"><span>{b}</span></div><div>{c}</div></div>' for a, b, c, g in FLOW)
    body = head('Tiền chất hương', 'Cỗ máy',
                'Hạt cà phê xanh gần như không thơm. Hương trong ly được làm từ những gì hạt đã tích sẵn: đường, acid amin, dầu, acid hữu cơ, acid chlorogenic, caffeine, trigonelline. '
                'Chọn giống, kéo mức rang và chọn cách pha để xem từng nhóm chất đi đâu.')
    body += f'''
<div class="bench">
  <div class="card">
    <div class="fighead">
      <div><b>Hình 1</b> <span id="figsub"></span></div>
      <button class="btn small" id="run2" type="button">Rang thử</button>
    </div>
    <div class="scroller"><svg id="scene" viewBox="0 0 1040 720" aria-label="Bàn mô hình bảy trạm: nhân xanh, giá phân tích, lò rang, phản ứng, hương bay hơi, pha, ly. Bấm từng trạm để xem chi tiết."></svg></div>
    <div class="strip" id="strip" role="group" aria-label="Chọn trạm"></div>
    <div id="detail" aria-live="polite"></div>
  </div>

  <aside class="card ctl">
    <div class="head2"><h3>Giống</h3><small>2 giống</small></div>
    <div class="row" id="vars"></div>
    <p class="mnote" id="vNote"></p>
    <hr>
    <div class="sl" style="margin-top:0"><label for="iL">Mức rang <output id="oL"></output></label><input id="iL" type="range" min="0" max="8" step="1"><p id="lNote"></p></div>
    <div class="head2" style="margin-top:12px"><h3>Cách pha</h3></div>
    <div class="row" id="brews"></div>
    <p class="mnote" id="bNote"></p>
    <div class="row" style="margin-top:14px"><button class="btn main" id="run" type="button">Rang thử</button><button class="btn" id="reset" type="button">Về mặc định</button></div>
    <div class="stats" id="stats"></div>
    <div id="verdict"></div>
    <hr>
    <span class="lbl">Còn lại so với nhân xanh</span>
    <div class="charts"><svg class="ch" id="cR" viewBox="0 0 340 160" role="img" aria-label="Phần trăm sucrose, acid chlorogenic, trigonelline, caffeine còn lại theo mức rang"></svg></div>
    <div class="lg" id="lgR"></div>
    <div id="tip"></div>
  </aside>
</div>

<section class="card" id="thanh-phan">
  <h2>Hình 2: thành phần theo chất khô</h2>
  <p class="lead" id="tpLead"></p>
  <div class="lg" id="lgT"></div>
  <div class="tp" id="tp"></div>
  <p class="mnote">Cột nhân xanh và mốc rang vừa (City+) theo bảng thành phần tổng hợp. Các mức rang khác MeDili nội suy theo hướng thay đổi đã biết; dòng trigonelline là minh hoạ vì bảng gốc gộp cả sản phẩm phân huỷ của nó.</p>
</section>

<section class="card" id="huong">
  <h2>Hình 3: từ tiền chất đến chất hương</h2>
  <p class="lead">Mỗi dòng là một con đường: tiền chất trong nhân, phản ứng khi rang, và những chất hương chính nó tạo ra. Dòng sáng hơn là con đường đang mạnh ở mức rang chị chọn.</p>
  <div class="fhd"><span>Tiền chất trong nhân</span><span>Khi rang</span><span>Chất hương, mùi</span></div>
  <div class="flowr" id="flowr">{flow}</div>
  <p class="mnote">Tên chất và mùi theo tài liệu tổng hợp; khoảng 900 chất bay hơi đã được nhận diện, chưa tới 20 chất có vai trò rõ trong mùi cà phê.</p>
</section>

<div class="cols">
  <section class="card">
    <h2>Dầu vào ly theo cách pha</h2>
    <p class="lead">Dầu cà phê mang theo hai chất diterpene là cafestol và kahweol. Giấy lọc giữ lại gần hết; lưới kim loại và nước sôi lâu cho nhiều đi qua.</p>
    <div class="tw"><table class="rich"><thead><tr><th>Cách pha</th><th>Dầu, diterpene vào ly</th></tr></thead><tbody>
      <tr><td><b>Lọc giấy</b></td><td>Gần như không</td></tr>
      <tr><td><b>Phin</b></td><td>Có một phần qua lưới kim loại; chưa có số đo riêng</td></tr>
      <tr><td><b>Ép Pháp</b></td><td>Nhiều dầu và hạt mịn, thân dày</td></tr>
      <tr><td><b>Espresso</b></td><td>Khoảng 1 mg cafestol và 1 mg kahweol mỗi ly</td></tr>
      <tr><td><b>Đun sôi kiểu Bắc Âu</b></td><td>Khoảng 7 mg cafestol mỗi ly</td></tr>
    </tbody></table></div>
    <p class="mnote">Lượng caffeine vào ly tuỳ lượng bột và cách pha. Tính theo thói quen của chị ở <a class="lnk" href="suc-khoe.html">Cà phê và cơ thể</a>, xem chất nào ra trước ở <a class="lnk" href="chiet-xuat.html">Cỗ máy Chiết xuất</a>.</p>
  </section>
  <section class="card">
    <h2>Độ chua: pH khác độ chua chuẩn độ</h2>
    <p><b>pH</b> đo nồng độ ion H⁺ tự do lúc đo. <b>Độ chua chuẩn độ</b> đo tổng lượng acid, bằng lượng kiềm cần thêm để đưa dịch về một pH nhất định, và gần với cảm giác chua trên lưỡi hơn.</p>
    <p>Cà phê pha nóng và cold brew có pH gần nhau, khoảng 4,85–5,13, nhưng ly pha nóng có độ chua chuẩn độ cao hơn, nên uống thấy chua hơn.</p>
    <p>Acid trong ly là cả một hệ: citric, malic có sẵn trong nhân giảm dần khi rang; acetic, formic sinh ra khi rang rồi bay đi; quinic tăng theo độ rang từ acid chlorogenic. Nước pha nhiều kiềm sẽ trung hoà bớt, làm ly nhạt chua.</p>
  </section>
</div>

<section class="card">
  <h2>Bảy chặng giữ tiền chất hương</h2>
  <p class="lead">Tiền chất được tích ở vườn, chuyển hoá khi lên men, giữ lại khi phơi và cất kho, lọc lỗi khi phân loại, rồi mới được mở khoá trong lò rang. Hỏng một chặng, lò rang không cứu được.</p>
  <ol class="pst two">{chain}</ol>
</section>

<section class="p-sec">
  <p class="eye">MeDili đọc lại</p>
  <h2 class="p-h2" style="margin:0">Sáu điều <em>về hạt và hương.</em></h2>
  <div class="g3">{boxes(READ)}</div>
</section>

<section class="card src">
  <h2>Nguồn và cách đọc mô hình</h2>
  <p class="lead">Thành phần nhân xanh và rang vừa theo bảng tổng hợp; các mức rang khác nội suy: sucrose và acid amin tự do cạn dần tới rang vừa, acid chlorogenic giảm theo hàm mũ khớp mốc rang vừa, caffeine và dầu gần như giữ nguyên, melanoidin tăng. Ba nhóm hương theo mức rang là minh hoạ định tính. Mười mức rang dùng chung với Phòng rang của MeDili.</p>
  <ul>{srclist(SRC)}</ul>
  <div class="lnks"><a class="lnk" href="phan-biet-ca-phe.html">Cỗ máy Phân biệt cà phê</a><a class="lnk" href="rang.html">Phòng rang</a><a class="lnk" href="chiet-xuat.html">Cỗ máy Chiết xuất</a><a class="lnk" href="banh-xe-huong.html">Bánh xe hương MeDili</a><a class="lnk" href="trai-chin.html">Cỗ máy Trái chín</a><a class="lnk" href="journal.html">Tất cả kiến thức cà phê</a></div>
</section>
'''
    return doc(FILE, TITLE, DESC, body, css=ISO_CSS + CSS, js=ISO_JS + JS)


CSS = r'''
/* Cỗ máy Tiền chất hương */
#scene .sack{fill:#C9A46A}#scene .sackT{fill:#B38C4E}
#scene .grn{fill:#D3C59A}
#scene .tube{fill:var(--panel);fill-opacity:.35}
#scene .rack{fill:#A67B47}
#scene .drum{fill:#8E897E}
#scene .lamp{stroke:#3A2416;stroke-width:1.2}
#scene .aro{stroke:#3A2416;stroke-width:1;fill-opacity:.85}
#scene .aroT{font:700 8.6px var(--body);fill:#3A2416}
#scene .cupW{fill:#F6F0E4}#scene .cupW2{fill:#E3D9C6}
.tp{display:grid;gap:2px;margin-top:6px}
.tp .r{display:grid;grid-template-columns:220px minmax(0,1fr) 120px;gap:12px;align-items:center;padding:5px 0;border-bottom:1px solid var(--rule)}
.tp .r>span:first-child{font-size:.9rem}
.tp .r small{display:block;color:var(--muted);font-size:.74rem}
.tp .bb{display:grid;gap:3px}
.tp .bb i{display:block;height:9px;border-radius:0 4px 4px 0;min-width:1px}
.tp .bb i.g{background:var(--cx1)}.tp .bb i.r2{background:var(--cx3)}
.tp b{font:700 .84rem var(--mono);text-align:right;white-space:nowrap}
@media (max-width:620px){.tp .r{grid-template-columns:118px minmax(0,1fr) 92px;gap:8px}.tp .r>span:first-child{font-size:.8rem}}
.fhd,.fr{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,.7fr) minmax(0,1.9fr);gap:12px;align-items:center}
.fhd{font:600 .72rem var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding-bottom:4px}
.flowr{display:grid;gap:6px}
.fr{background:var(--tint);border-radius:12px;padding:10px 14px;transition:opacity .25s}
.fr b{font:700 .95rem var(--body)}
.fr .fx span{display:inline-block;font:700 .8rem var(--body);color:var(--on-accent);background:var(--accent);border-radius:999px;padding:4px 10px}
.fr>div:last-child{font-size:.88rem}
.fr.hot{box-shadow:inset 4px 0 0 var(--accent)}
@media (max-width:760px){.fhd{display:none}.fr{grid-template-columns:minmax(0,1fr)}}
'''

JS = r'''
const U=7,OX=196,OY=118,VBW=1040;
const VAR={rob:{n:'Robusta Di Linh',sh:'Robusta',note:'Robusta có caffeine và acid chlorogenic nhiều gần gấp đôi Arabica, ít đường và dầu hơn: đậm, đắng, thân chắc.'},
 ara:{n:'Arabica Cầu Đất',sh:'Arabica',note:'Arabica nhiều sucrose và dầu hơn, ít caffeine và acid chlorogenic: thơm, chua sáng, ít đắng.'}};
const LV=[{n:'Nhân xanh',g:'Chưa rang',l:0,taste:'Mùi cỏ khô, đậu sống',col:'#CDBE8F'},{n:'Cinnamon',g:'Light',d:'196–200',l:15,taste:'Chua, hạt sống, mùi ngũ cốc',col:'#B98B58'},{n:'New England',g:'Light',d:'200–205',l:15.5,taste:'Hoa, cam chanh, axit cao',col:'#A87545'},{n:'City',g:'Medium-Light',d:'205–210',l:16.5,taste:'Trái cây, sáng, thân nhẹ',col:'#936237'},{n:'City+',g:'Medium',d:'210–220',l:17.5,taste:'Caramel, hạt rang, cân bằng',col:'#7A4D2A'},{n:'Full City',g:'Medium-Dark',d:'220–225',l:18.5,taste:'Sô-cô-la, đắng ngọt, ít chua',col:'#5F3920'},{n:'Vienna',g:'Dark',d:'225–228',l:19.5,taste:'Đắng đậm, thân dày',col:'#472A18'},{n:'French',g:'Dark',d:'228–230',l:21,taste:'Khói, đắng, gần hết hương gốc',col:'#3A2416'},{n:'Italian',g:'Very Dark',d:'230–235',l:22.5,taste:'Than, cháy, thân mỏng',col:'#33200F'}];
const BREW={giay:{n:'Lọc giấy',oil:0,note:'Giấy giữ lại gần hết dầu và hạt mịn: ly trong, sạch vị.'},phin:{n:'Phin',oil:1,note:'Lưới kim loại cho một phần dầu và hạt mịn qua: ly đặc, thân dày hơn lọc giấy.'},ep:{n:'Ép Pháp',oil:2,note:'Ngâm và ép qua lưới: nhiều dầu, hạt mịn, thân dày.'},esp:{n:'Espresso',oil:1.5,note:'Áp suất cao tạo nhũ tương dầu, khí và hạt mịn: lớp crema, thân đặc.'}};
const OIL=['gần như không','có, vừa','nhiều','vừa, khoảng 1 mg cafestol mỗi ly'];
/* % chất khô, nhân xanh và rang vừa */
const CP=[{k:'suc',n:'Đường sucrose',g:[8,4],m:[0,0],f:(v0,v1,p)=>v0*Math.pow(Math.max(0,1-p),2)},
 {k:'aa',n:'Acid amin tự do',g:[.5,.8],m:[0,0],f:(v0,v1,p)=>v0*Math.pow(Math.max(0,1-p),1.2)},
 {k:'pro',n:'Protein',g:[11,11],m:[10,10],f:(v0,v1,p)=>v0+(v1-v0)*Math.min(p,1.9)},
 {k:'lip',n:'Lipid (dầu)',g:[16,10],m:[17,11],f:(v0,v1,p)=>v0+(v1-v0)*Math.min(p,1.9)},
 {k:'cga',n:'Acid chlorogenic',g:[6.5,10],m:[2.5,3.8],f:(v0,v1,p)=>v0*Math.exp(-.97*p)},
 {k:'caf',n:'Caffeine',g:[1.2,2.2],m:[1.3,2.4],f:(v0,v1,p)=>v0*(1+.08*p)},
 {k:'tri',n:'Trigonelline',g:[1,.7],m:[null,null],f:(v0,v1,p)=>v0*Math.exp(-.6*p),ill:1},
 {k:'aci',n:'Acid hữu cơ',sub:'acid béo và quinic',g:[1.4,1.4],m:[2.4,2.6],f:(v0,v1,p)=>v0+(v1-v0)*p*Math.exp(1-p)},
 {k:'pol',n:'Polysaccharide, xơ',sub:'gồm pectin, lignin',g:[50,55],m:[38,42],f:(v0,v1,p)=>v0+(v1-v0)*Math.min(p,1.9)},
 {k:'min',n:'Khoáng',g:[4.2,4.4],m:[4.5,4.7],f:(v0,v1,p)=>v0+(v1-v0)*Math.min(p,1.9)},
 {k:'mel',n:'Melanoidin, chất caramel',sub:'màu nâu, vị đắng ngọt',g:[0,0],m:[23,22.5],f:(v0,v1,p)=>v1*(p<=1?p:1+.3*(p-1))}];
const AR=[{k:'enz',n:'Hương enzyme',c:'var(--cx2)',v:[.15,.95,1,.85,.6,.4,.25,.15,.08]},{k:'sug',n:'Caramel hoá đường',c:'var(--cx1)',v:[0,.35,.5,.75,1,.9,.65,.4,.25]},{k:'dry',n:'Chưng cất khô',c:'var(--cx4)',v:[0,.05,.08,.15,.3,.5,.75,.95,1]}];
const DEF={v:'rob',lv:4,b:'phin'};
const st={...DEF,sel:3};
const prog=l=>LV[l].l?(LV[l].l-12)/5.5:0;
const dml=l=>LV[l].l?Math.max(0,LV[l].l-11)/89:0;
function comp(l){const vi=st.v==='ara'?0:1,p=prog(l),o={};CP.forEach(c=>{const v0=c.g[vi],v1=c.m[vi];o[c.k]=l?c.f(v0,v1,p):v0});return o}
const keep=(k,l)=>{const c0=comp(0)[k];return c0?comp(l)[k]/c0*(1-dml(l))*100:0};
let R={};
function calc(){const c0=comp(0),c=comp(st.lv),ar=AR.map(a=>a.v[st.lv]);R={c0,c,ar,L:LV[st.lv],dom:AR[ar.indexOf(Math.max(...ar))]};return R}

/* ====== 7 TRẠM ====== */
const ST=[
 {n:'Nhân xanh',sub:()=>VAR[st.v].n,mech:'Nhân xanh gần như không thơm, chỉ có mùi cỏ khô, đậu sống. Nhưng bên trong đã có đủ nguyên liệu cho hương: đường, acid amin, dầu, acid hữu cơ, acid chlorogenic, caffeine, trigonelline.',
  kv:()=>[['Sucrose',vn(R.c0.suc,1)+' %'],['Lipid',vn(R.c0.lip,0)+' %'],['Acid chlorogenic',vn(R.c0.cga,1)+' %'],['Caffeine',vn(R.c0.caf,1)+' %']],check:'Ẩm nhân 10–12 %, hạt đều màu, không mùi mốc, mùi lên men.',fail:'Nghĩ rằng hạt xanh thơm là hạt tốt. Hạt xanh có mùi lạ thường là đã hỏng.',tip:'Cất kho khô, mát, thoáng; dùng theo thứ tự lô.'},
 {n:'Giá phân tích',sub:()=>st.lv?`So nhân xanh với ${R.L.n}`:'Thành phần nhân xanh',mech:'Mỗi ống là một nhóm chất, mực trong ống là phần trăm chất khô. Kéo mức rang để xem ống nào cạn, ống nào giữ nguyên.',
  kv:()=>[['Sucrose',`${vn(R.c0.suc,1)} → ${vn(R.c.suc,1)} %`],['Acid amin tự do',`${vn(R.c0.aa,1)} → ${vn(R.c.aa,2)} %`],['Acid chlorogenic',`${vn(R.c0.cga,1)} → ${vn(R.c.cga,1)} %`],['Melanoidin',`0 → ${vn(R.c.mel,0)} %`]],check:'Số liệu theo bảng thành phần tổng hợp; mốc giữa là ước tính của mô hình.',fail:'Nghĩ caffeine tăng khi rang đậm. Con số tính trên chất khô nhích lên vì hạt nhẹ đi, lượng thật gần như giữ nguyên.',tip:'Xem bảng đầy đủ ở Hình 2.'},
 {n:'Lò rang',sub:()=>st.lv?`${R.L.n} · ra mẻ ${R.L.d} °C`:'Chưa rang',mech:'Nhiệt trong lò làm hạt mất nước, rồi mở hàng loạt phản ứng: Maillard, caramel hoá đường, phân huỷ acid chlorogenic và trigonelline. Càng rang lâu, đậm, tiền chất càng cạn và chất mới càng nhiều.',
  kv:()=>[['Mức rang',st.lv?R.L.n+' ('+R.L.g+')':'Nhân xanh'],['Hao hụt',st.lv?vn(R.L.l,1)+' %':'0 %'],['Vị gợi ý',R.L.taste]],check:'Theo dõi nhiệt độ hạt, mốc nổ lần 1, lần 2 và thời gian phát triển.',fail:'Rang đậm để che lỗi hạt. Mùi khói, cháy át hết hương gốc.',tip:'Mười mức rang dùng chung với Phòng rang.'},
 {n:'Phản ứng',sub:()=>`Mạnh nhất: ${R.dom.n.toLowerCase()}`,mech:'Ba đèn là ba nhóm hương theo nguồn gốc: hương enzyme có sẵn từ lúc trái chín, nổi rõ ở rang sáng; caramel hoá đường và Maillard mạnh ở rang vừa; chưng cất khô, mùi khói, gia vị, nổi ở rang đậm.',
  kv:()=>AR.map((a,i)=>[a.n,vn(R.ar[i]*100,0)+' %']),check:'Ngửi bột ngay sau xay: rang sáng thơm hoa, trái cây; rang vừa caramel, hạt; rang đậm khói, gia vị.',fail:'Nghĩ hương trái cây chỉ có ở Arabica. Robusta sơ chế tốt, rang sáng vẫn có.',tip:'Xem Bánh xe hương MeDili.'},
 {n:'Hương bay hơi',sub:'Chất hương chính',mech:'Khoảng 900 chất bay hơi đã được nhận diện, nhưng chỉ chưa tới 20 chất quyết định mùi cà phê. Bóng to là chất đang mạnh ở mức rang này.',
  kv:()=>[['Furaneol','caramel'],['2-furfurylthiol','mùi rang, bánh mì nướng'],['4-vinylguaiacol','đinh hương'],['Guaiacol','khói, nhựa']],check:'Hương bay nhanh sau xay: pha trong vài phút sau khi xay.',fail:'Nghĩ càng nhiều chất thơm càng ngon. Ly ngon là ly cân bằng.',tip:'Bảo quản cà phê rang trong túi có van một chiều.'},
 {n:'Pha',sub:()=>BREW[st.b].n,mech:()=>BREW[st.b].note+' Chất tan trong nước như caffeine, acid, đường caramel ra phần lớn; dầu thì tuỳ màng lọc.',
  kv:()=>[['Cách pha',BREW[st.b].n],['Dầu vào ly',OIL[st.b==='giay'?0:st.b==='phin'?1:st.b==='ep'?2:3]],['Caffeine trong 1 g bột',vn(R.c.caf*10,0)+' mg']],check:'Cân bột, nước, thời gian để mỗi ly lặp lại được.',fail:'Lọc giấy làm mất thân. Thân còn đến từ melanoidin và polysaccharide hoà tan.',tip:'Xem Cỗ máy Chiết xuất.'},
 {n:'Ly',sub:()=>R.L.taste,mech:'Trong ly là kết quả của cả chuỗi: hạt tích gì, lên men ra sao, rang tới đâu, pha thế nào. Cân bằng giữa thơm, ngọt, chua, đắng và thân mới là ly ngon.',
  kv:()=>[['Vị gợi ý',R.L.taste],['Đắng',st.lv>=6?'đậm':st.lv>=4?'vừa':'nhẹ'],['Chua',st.lv<=3&&st.lv?'sáng':st.lv<=5?'dịu':'thấp'],['Thân',BREW[st.b].oil>=1.5?'dày':BREW[st.b].oil?'vừa':'nhẹ']],check:'Nếm khi ly nguội dần: chua và ngọt rõ hơn khi ấm.',fail:'Chấm ly chỉ bằng độ đắng.',tip:'Phiếu cupping ở Bánh xe hương MeDili.'}];

/* ====== DỰNG CẢNH ====== */
const ANCH=[null,[8,11,9],[30,11,9],[48,11,11],[64,10.5,8.5],[80,12,10],[94,13,6.5],[110,14,5]];
const CHIP=[null,{x:176,y:12},{x:262,y:54},{x:348,y:98},{x:434,y:142},{x:520,y:188},{x:606,y:236},{x:698,y:288}];
const TUBE=[{k:'suc',c:'#E3B341'},{k:'aa',c:'#9A5BB5'},{k:'lip',c:'#F1D9A6'},{k:'cga',c:'#CB4D54'},{k:'caf',c:'#8D6A45'},{k:'tri',c:'#D9782E'},{k:'mel',c:'#5E3920'}];
function buildScene(){
 let h=bench(124,24,'Cỗ máy Tiền chất hương · MeDili',44);
 /* 1 nhân xanh */
 let s=frus(7,9.5,0,4.4,7.2,3.4,'sack','sackT')+box(10.5,14.5,0,9,6.5,.9,['wo','wo2','cu2'])+'<g id="tray"></g>';
 h+=stG(1,s);
 /* 2 giá ống nghiệm */
 s=box(22,7.5,0,17,6,1.3,['rack','wo2','cu2'])+box(22,7.5,7.2,17,6,.6,['rack','wo2','cu2'])+'<g id="tubes"></g>';
 h+=stG(2,s);
 /* 3 lò rang */
 s=cyl(46,8,9.6,.7,5,'f3','f2')+box(43,6.5,0,10.5,9.5,9.6,['f1','f2','f3'])+frus(49,10.5,9.6,1.3,13,3,'f2','grn')+'<g id="drum"></g>'+lcd(43.6,16,2.6,70,'kRo');
 h+=stG(3,s);
 /* 4 phản ứng */
 s=box(58,8.5,0,13,5,8,['#E6DCC8','#CFC2A8','#B7A98C'])+'<g id="lamps"></g>';
 h+=stG(4,s);
 /* 5 hương bay hơi */
 s=cyl(80,12,0,3,1.4,'f2','f1')+cyl(80,12,1.4,.6,3.2,'f3','f2')+'<g id="aroma"></g>';
 h+=stG(5,s);
 /* 6 pha */
 s=box(89,9,0,11,9,1.4,['ped','ped2','ped3'])+'<g id="brew"></g>';
 h+=stG(6,s);
 /* 7 ly */
 s=box(104,9.5,0,13,9,1,['wo','wo2','cu2'])+'<g id="cup"></g>'+lcd(104.6,18.5,.95,52,'kCup');
 h+=stG(7,s);
 h+='<g id="flow"></g><g id="chips"></g><circle id="tok" r="7"/>';
 $('scene').innerHTML=h;['kRo','kCup'].forEach(i=>$(i).classList.add('sm'));initStations()}
function renderScene(){const c=R.c,L=R.L,g=rng(5);
 let t='';for(let i=0;i<52;i++){const q=P(11.2+g()*7.6,15.2+g()*5.2,.92);t+=`<ellipse cx="${f1(q[0])}" cy="${f1(q[1])}" rx="3" ry="2" style="fill:${L.col};stroke:#3A2416;stroke-width:.4"/>`}$('tray').innerHTML=t;
 t='';TUBE.forEach((tb,i)=>{const x=23.6+i*2.3,y=10.5,mx=tb.k==='mel'?25:tb.k==='lip'?18:tb.k==='cga'?11:tb.k==='suc'?9:2.5,v=clamp((tb.k==='mel'?c.mel:c[tb.k])/mx,0,1);
  t+=cyl(x,y,1.3,.75,7.4,'tube','tube')+(v>.01?cyl(x,y,1.35,.66,7*v,tb.c,tb.c):'')});$('tubes').innerHTML=t;
 $('drum').innerHTML=`<g transform="${face(43.6,16,8.4)}"><circle cx="38" cy="30" r="25" class="drum" style="stroke:#3A2416;stroke-width:1.2"/><circle cx="38" cy="30" r="16" style="fill:${L.col};stroke:#3A2416;stroke-width:1"/></g>`;
 $('kRo').textContent=st.lv?`${L.n} ${L.d}°C`:'nhân xanh';
 t='';AR.forEach((a,i)=>{const v=R.ar[i],cl=['#9A5BB5','#E3B341','#CB4D54'][i];t+=`<g transform="${face(58.5,13.5,7.4)}"><circle class="lamp" cx="${14+i*32}" cy="17" r="11.5" style="fill:${cl};fill-opacity:${f1(.15+.85*v)}"/><text x="${14+i*32}" y="42" text-anchor="middle" class="wtx" style="font-size:7.6px">${['enzyme','caramel','khói'][i]}</text></g>`});$('lamps').innerHTML=t;
 const ar=R.ar,A=[['thiol',ar[1]*.6+ar[2]*.4,'#C08A4E',-12,-34],['furaneol',ar[1],'#E3B341',30,-22],['pyrazine',ar[1]*.5+ar[2]*.6,'#A9743F',66,-62],['guaiacol',ar[2],'#CB4D54',34,-100],['damascenone',ar[0],'#9A5BB5',-16,-104]];
 const q=P(80,12,4.6);t='';A.forEach(([n,v,cl,dx,dy])=>{const r=7+13*v;t+=`<circle class="aro" cx="${f1(q[0]+dx)}" cy="${f1(q[1]+dy)}" r="${f1(r)}" style="fill:${cl};fill-opacity:${f1(.3+.55*v)}"/><text class="aroT" x="${f1(q[0]+dx)}" y="${f1(q[1]+dy+r+10)}" text-anchor="middle" style="paint-order:stroke;stroke:#F6EAD2;stroke-width:3px;stroke-linejoin:round">${n}</text>`});$('aroma').innerHTML=t;
 const b=st.b,bx=94.5,by=13.5;t='';
 if(b==='giay')t=cyl(bx,by,1.4,2,2.2,'cupW2','#6B4226')+frus(bx,by,3.6,1.1,8.2,3.8,'cupW','#5A3520');
 else if(b==='phin')t=cyl(bx,by,1.4,2.1,3,'cupW2','#6B4226')+cyl(bx,by,4.4,2.9,.4,'f2','f1')+cyl(bx,by,4.8,2,3,'f2','f1')+cyl(bx,by,7.8,2.1,.4,'f3','f2');
 else if(b==='ep')t=cyl(bx,by,1.4,2.3,6.8,'gl','#5A3520')+cyl(bx,by,8.2,2.45,.5,'f3','f2')+cyl(bx,by,8.7,.26,2.2,'f3','f2')+sph(bx,by,10.9,.55,'#8E897E');
 else t=box(bx-4,by-4,1.4,8,6.5,7,['f1','f2','f3'])+cyl(bx,by+3.4,1.4,1.5,1.8,'cupW2','#C9A15B');
 $('brew').innerHTML=t;
 $('cup').innerHTML=cyl(110.5,14,1,3.6,.35,'cupW2','cupW')+cyl(110.5,14,1.35,2.6,3.2,'cupW','#5A3520')+(BREW[b].oil?disc(110.5,14,4.6,2.2,b==='esp'?'#C9A15B':'#7A4A2A'):'');
 $('kCup').textContent=['dầu: ít','dầu: vừa','dầu: nhiều','dầu: vừa'][b==='giay'?0:b==='phin'?1:b==='ep'?2:3];
 drawFlow();drawChips()}
function chipLabel(i){return ['','Nhân xanh · '+VAR[st.v].sh,`Sucrose ${vn(R.c0.suc,0)} → ${vn(R.c.suc,1)} %`,st.lv?`Rang ${R.L.n}`:'Chưa rang',`Mạnh: ${R.dom.n.toLowerCase()}`,'Chất hương bay hơi',`Pha ${BREW[st.b].n.toLowerCase()}`,R.L.taste][i]}
function drawFlow(){const c=R.c;const rows=[['Giống',VAR[st.v].sh],['Mức rang',st.lv?`${R.L.n} · hao ${vn(R.L.l,1)}${NB}%`:'nhân xanh'],['Sucrose còn',vn(keep('suc',st.lv),0)+NB+'%'],['Acid chlorogenic còn',vn(keep('cga',st.lv),0)+NB+'%'],['Caffeine',vn(c.caf,1)+NB+'% chất khô'],['Melanoidin',vn(c.mel,0)+NB+'% chất khô'],['Nhóm hương mạnh',R.dom.n]];
 const X=16,rh=27,h=50+rows.length*rh+20,y=712-h,w=330;
 let g=`<rect x="${X}" y="${y}" width="${w}" height="${h}" rx="10" class="pa" style="stroke:var(--ink);stroke-width:1.2"/><text x="${X+16}" y="${y+26}" class="lab12" style="letter-spacing:.08em">TỪ NHÂN XANH ĐẾN LY</text>`;
 rows.forEach(([a,b],i)=>{const yy=y+48+i*rh;g+=`<text class="flowT" x="${X+16}" y="${yy+4}">${a}</text><text x="${X+w-16}" y="${yy+4}" text-anchor="end" class="mono flowT">${b}</text>`});
 g+=`<text x="${X+16}" y="${y+h-10}" class="tiny mutedt">Bản vẽ khái niệm · nguồn tổng hợp, mốc giữa ước tính</text>`;$('flow').innerHTML=g}

/* ====== BIỂU ĐỒ, BẢNG ====== */
const KS=[{k:'suc',n:'Sucrose',c:'var(--cx1)'},{k:'cga',n:'Acid chlorogenic',c:'var(--cx4)'},{k:'tri',n:'Trigonelline',c:'var(--cx2)',d:'5 4'},{k:'caf',n:'Caffeine',c:'var(--cx3)'}];
function drawR(){$('cR').innerHTML=lineSVG({W:340,H:160,l:32,r:22,t:18,b:22,x0:0,x1:8,y0:0,y1:110,xt:[0,2,4,6,8],xf:v=>({0:'xanh',2:'N. Eng.',4:'City+',6:'Vienna',8:'Italian'})[v],yt:[0,50,100],yf:v=>v+'%',ttl:'% còn lại · trục ngang: mức rang',ser:KS.map(s=>({c:s.c,d:s.d,p:LV.map((_,l)=>[l,keep(s.k,l)])})),vx:st.lv});
 legend('lgR',KS);$('tip').textContent=st.lv?`${R.L.n}: sucrose còn ${vn(keep('suc',st.lv),0)} %, acid chlorogenic còn ${vn(keep('cga',st.lv),0)} %, caffeine còn ${vn(keep('caf',st.lv),0)} %.`:'Nhân xanh: chưa có gì mất đi.'}
function drawTP(){const c0=R.c0,c=R.c,mx=Math.max(...CP.map(k=>Math.max(c0[k.k],c[k.k])));
 $('tpLead').textContent=`${VAR[st.v].n}: nhân xanh so với ${st.lv?R.L.n+' (hao '+vn(R.L.l,1)+' %)':'chính nó'}, phần trăm trên chất khô.`;
 legend('lgT',[{c:'var(--cx1)',n:'Nhân xanh',box:1},{c:'var(--cx3)',n:st.lv?R.L.n:'Nhân xanh',box:1}]);
 $('tp').innerHTML=CP.map(k=>`<div class="r"><span>${k.n}${k.ill?' *':''}${k.sub?`<small>${k.sub}</small>`:''}</span><div class="bb"><i class="g" style="width:${f1(c0[k.k]/mx*100)}%"></i><i class="r2" style="width:${f1(c[k.k]/mx*100)}%"></i></div><b>${vn(c0[k.k],1)} → ${vn(c[k.k],1)} %</b></div>`).join('')}
function drawFR(){const m={enz:R.ar[0],sug:R.ar[1],dry:R.ar[2],lip:.8};document.querySelectorAll('#flowr .fr').forEach(e=>{e.style.opacity=f1(.55+.45*m[e.dataset.g]);e.classList.toggle('hot',m[e.dataset.g]>=.6)})}

/* ====== ĐIỀU KHIỂN ====== */
function verdict(){const l=st.lv;let k='good',t,m;
 if(!l){t='Nhân xanh: đủ nguyên liệu, chưa có hương';m='Đường, acid amin, dầu, acid và caffeine đã nằm sẵn trong nhân. Kéo mức rang để mở khoá.'}
 else if(l<=2){k='warn';t=`${R.L.n}: hương enzyme rõ, dễ chua sống`;m=`Còn khoảng ${vn(keep('suc',l),0)} % sucrose chưa phản ứng, acid chlorogenic còn ${vn(keep('cga',l),0)} %. Hợp hạt chất lượng cao, pha lọc; dễ có mùi ngũ cốc nếu rang chưa đủ phát triển.`}
 else if(l<=5){t=`${R.L.n}: cân bằng`;m=`Sucrose gần như đã thành caramel và chất hương; acid chlorogenic còn ${vn(keep('cga',l),0)} %. Vùng rang hợp phin, pha máy và cold brew.`}
 else{k=l>=7?'bad':'warn';t=`${R.L.n}: chưng cất khô lấn át`;m=`Acid chlorogenic chỉ còn ${vn(keep('cga',l),0)} %, mùi khói, gia vị, đắng đậm át hương gốc của hạt. Dầu ra mặt hạt, dễ ôi khi cất lâu.`}
 $('verdict').className=k;$('verdict').innerHTML=`<b>${k==='good'?'✓':k==='warn'?'!':'✕'} ${t}</b>${m}`}
function stats(){const t=(a,b)=>`<div class="stat"><span>${a}</span><b>${b}</b></div>`,l=st.lv;
 $('stats').innerHTML=t('Sucrose còn',vn(keep('suc',l),0)+NB+'%')+t('Acid chlorogenic còn',vn(keep('cga',l),0)+NB+'%')+t('Caffeine',vn(R.c.caf*10,0)+NB+'mg/g')+t('Melanoidin',vn(R.c.mel,0)+NB+'%')}
function update(){calc();
 pills('vars',Object.entries(VAR).map(([k,v])=>[k,v.n]),st.v,k=>{st.v=k;stopRun();update()});
 pills('brews',Object.entries(BREW).map(([k,v])=>[k,v.n]),st.b,k=>{st.b=k;stopRun();update()});
 $('vNote').textContent=VAR[st.v].note;$('bNote').textContent=BREW[st.b].note;
 $('iL').value=st.lv;$('oL').textContent=st.lv?R.L.n:'Nhân xanh';$('lNote').textContent=st.lv?`${R.L.g}, ra mẻ ${R.L.d} °C, hao ${vn(R.L.l,1)} %. Vị: ${R.L.taste.toLowerCase()}.`:'Chưa rang. Mức rang dùng chung với Phòng rang.';
 stats();verdict();$('figsub').textContent=`${VAR[st.v].sh}, ${st.lv?R.L.n:'nhân xanh'}, pha ${BREW[st.b].n.toLowerCase()}`;
 renderScene();drawR();drawTP();drawFR();renderStation()}
$('iL').addEventListener('input',()=>{stopRun();st.lv=+$('iL').value;update()});
function roastRun(){stopRun();if(still){st.lv=8;update();return}let l=0;st.lv=0;update();$('scene').classList.add('running');
 timer=setInterval(()=>{l++;st.lv=l;st.sel=l<2?2:l<5?3:4;update();if(l>=8){clearInterval(timer);timer=0;$('scene').classList.remove('running')}},650)}
$('run').onclick=roastRun;$('run2').onclick=roastRun;
$('reset').onclick=()=>{stopRun();clearInterval(timer);Object.assign(st,DEF);st.sel=3;update()};
buildScene();update();
'''
