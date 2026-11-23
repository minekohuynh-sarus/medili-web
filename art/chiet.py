# Cỗ máy Chiết xuất: dịch và mở rộng bức hình "Chemistry Review" (thời gian pha quyết định chất nào ra).
# Mô hình minh họa, không phải số đo. Màu 4 nhóm chất là token --cx1..--cx4 trong CORE_CSS (đã chạy validate_palette).
from kit import *

FILE = 'chiet-xuat.html'
TITLE = 'Cỗ máy Chiết xuất MeDili'
DESC = ('Thời gian pha quyết định chất nào vào ly: acid và CGA ra trước, đường và Maillard ra giữa, chất đắng ra sau. '
        'Mô hình chiết xuất cho phin, ép Pháp, pour-over, espresso và cold brew, kèm bản dịch và giải thích.')

SRC = [
    ('SCA Golden Cup: EY 18–22%, TDS 11,5–13,5 g/l (1,15–1,35%)', 'Moccamaster, What is the Golden Cup standard',
     'https://support.moccamaster.com/hc/en-us/articles/1500009409121-What-is-the-Golden-Cup-standard'),
    ('Fuller M., Rao N. Z. (2017). The effect of time, roasting temperature, and grind size on caffeine and chlorogenic acid concentrations in cold brew coffee. Scientific Reports 7, 17979',
     'PubMed', 'https://pubmed.ncbi.nlm.nih.gov/29269877/'),
    ('Battling bitter coffee: chemists identify roasting as the main culprit (2007), nhóm của Thomas Hofmann', 'ScienceDaily, nguồn ACS',
     'https://www.sciencedaily.com/releases/2007/08/070821143629.htm'),
    ('Jeszka-Skowron M. và cộng sự (2016). Chlorogenic acids, caffeine content and antioxidant properties of green coffee extracts. European Food Research and Technology 242',
     'Springer', 'https://link.springer.com/article/10.1007/s00217-016-2643-y'),
    ('5 minutes of science: coffee extraction (2020), tóm tắt tổng quan của Cordoba và cộng sự', 'Kaffeemacher',
     'https://kaffeemacher.de/en/blogs/kaffeewissen/5-minuten-kaffee-wissenschaft-die-extraktion'),
    ('Mức chiết tối đa 28–32% theo Moroney và cộng sự (2015)', 'Barista Hustle', 'https://www.baristahustle.com/?p=770'),
    ('Plunger, espresso or filter coffee? (2022), lượng caffeine theo cách pha, dẫn Angeloni và cộng sự 2019', 'The Conversation, đăng lại trên Phys.org',
     'https://phys.org/news/2022-08-plunger-espresso-filter-coffee-bitter.pdf'),
]

KNOBS = [
    ('Cỡ xay mịn hơn', 'Diện tích tiếp xúc lớn hơn, chất tan ra nhanh hơn. Phin, pour-over, espresso còn chảy chậm lại.', 'Xay mịn hơn một nấc', 'Xay thô hơn một nấc'),
    ('Nhiệt độ nước', 'Tan nhanh hơn, nhóm đắng ra sớm hơn.', 'Nâng lên 94–96 °C', 'Hạ xuống 88–91 °C'),
    ('Thời gian tiếp xúc', 'EY tăng. Qua mốc cân bằng, phần thêm vào chủ yếu là chất đắng.', 'Kéo dài', 'Rút ngắn'),
    ('Lượng nước, tỷ lệ', 'Ly loãng hơn, EY tăng nhẹ.', 'Giữ tỷ lệ, chỉnh cỡ xay trước', 'Giữ tỷ lệ, chỉnh cỡ xay trước'),
    ('Khuấy, xoáy, rót mạnh', 'Nước chạm bột đều và nhanh hơn.', 'Khuấy nhẹ lúc ủ', 'Bớt khuấy, rót nhẹ tay'),
    ('Mức rang đậm hơn', 'Hạt xốp, dễ tan, nhiều chất đắng sinh ra khi rang hơn.', 'Chọn rang đậm hơn hoặc nước nóng hơn', 'Chọn rang sáng hơn hoặc nước nguội hơn'),
]

READ = [
    ('khien', 'Điểm 2 và ly 4 phút', 'Chuẩn SCA là 18–22%, không phải 14–20%',
     'Chuẩn vàng (Golden Cup) cho ly lọc là tỷ lệ chiết xuất 18–22% và độ đậm 1,15–1,35%, tức 11,5–13,5 g chất tan mỗi lít. Ở 14–18%, ly vẫn còn chiết xuất thiếu. Vùng 14–20% trong hình chỉ nên hiểu là chặng mà đường và Maillard ra nhiều.',
     'Golden Cup, SCA'),
    ('cung', 'Đường caffeine nét đứt', 'Caffeine ra sớm, pha ngắn không giảm được bao nhiêu',
     'Caffeine tan rất tốt. Trong cold brew, caffeine và CGA cùng đạt cân bằng sau 6–7 giờ. Với loại cà phê trong một nghiên cứu, hầu hết cách pha cho khoảng 10 mg caffeine mỗi gram bột, ép Pháp thấp hơn, khoảng 7 mg. Muốn ít caffeine thì dùng ít bột hơn hoặc chọn Arabica: Robusta có caffeine khoảng gấp đôi.',
     'Fuller & Rao 2017 · The Conversation 2022 · Jeszka-Skowron 2016'),
    ('ly', 'Điểm 2: đường ra ở giữa', 'Đường đơn tan nhanh, thứ cần thời gian là vị ngọt tròn',
     'Đường, acid hữu cơ và caffeine tan rất nhanh ngay từ đầu, hơn 90%. Phần cần thêm thời gian thường được giải thích là các chất lớn hơn sinh ra khi rang, góp phần vào màu, thân và độ tròn vị. Ly dừng sớm vì thế thường chua lấn ngọt.',
     'Kaffeemacher, tóm tắt Cordoba 2020'),
    ('rang', 'Điểm 3: phenolic đắng', 'Chất đắng chính sinh ra khi rang',
     'Các nhà nghiên cứu ước tính chỉ khoảng 15% vị đắng đến từ caffeine. Phần lớn đến từ lacton của acid chlorogenic, chiếm ưu thế ở rang sáng đến vừa, và phenylindane, sản phẩm phân hủy của chúng, nhiều hơn ở rang đậm và espresso. Nhân xanh không có hai nhóm này. Mức rang đặt ra lượng chất đắng có sẵn, thời gian pha quyết định lấy ra bao nhiêu.',
     'ScienceDaily 2007, nguồn ACS'),
    ('phin', 'Dòng cuối của hình', 'Mốc 4 phút chỉ đúng cho một kiểu pha',
     '4 phút là mốc của ngâm toàn phần với 15 g bột, 250 ml nước, xay thô, nước khoảng 93 °C. Xay mịn hơn hay nước nóng hơn, đường cong dời sang trái và 4 phút đã thành chiết xuất quá mức. Phin thường 5–8 phút tính cả lúc ủ, pour-over 2:30–4:00, espresso 25–30 giây, cold brew 12–24 giờ.',
     'Mô hình MeDili, thử ở Hình 1'),
    ('vuon', 'Polyphenol và chống oxy hóa', 'Mức rang và loại hạt quyết định CGA nhiều hơn thời gian',
     'Rang càng đậm, CGA càng bị phân hủy: nhân xanh có thể chứa 5-CQA cao gấp đôi cà phê rang. Trong cold brew, rang vừa cho nhiều 3-CGA hơn rang đậm, còn cỡ xay không tạo khác biệt đáng kể. Dịch chiết Robusta có CGA, caffeine và hoạt tính chống oxy hóa cao nhất trong các mẫu được so. Muốn nhiều CGA, chọn rang sáng đến vừa trước, rồi mới tới chuyện dừng đúng lúc.',
     'Jeszka-Skowron 2016 · Fuller & Rao 2017'),
]


def page():
    knobs = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in KNOBS)
    read = ''.join(f'<div class="box rd">{icon(i)}<p class="k">Hình nói · {k}</p><h3>{h}</h3><p>{p}</p></div>'
                   for i, k, h, p, s in READ)
    src = ''.join(f'<li>{t}. <a href="{u}" target="_blank" rel="noopener">{n} ↗</a></li>' for t, n, u in SRC)
    body = f'''
<header>
  {logo()}<div class="brandbar"><span>Mê vị Di Linh</span><span>Kiến thức cà phê</span><span>Zalo <a href="#lien-he">{PHONE}</a></span></div>
  <h1>Cỗ máy <em>Chiết xuất</em></h1>
  <p>Thời gian pha không chỉ quyết định ly đậm hay nhạt. Nó quyết định chất nào vào ly: acid và CGA ra trước, đường và hợp chất Maillard ra giữa, chất đắng ra sau cùng. Chọn cách pha, chỉnh cỡ xay, nhiệt độ và thời gian để xem từng nhóm chất rời hạt.</p>
</header>

<div class="bench">
  <div class="card">
    <div class="fighead">
      <div><b>Hình 1</b> <span id="figsub"></span></div>
      <button class="btn small" id="run2" type="button">Pha thử</button>
    </div>
    <div class="scroller"><svg id="scene" viewBox="0 0 1040 690" aria-label="Bàn chiết xuất bảy trạm: cối xay, nước và nhiệt, cân, bình chiết, bốn ống chất tan, ly và khúc xạ kế, bã cà phê. Bấm từng trạm để xem chi tiết."></svg></div>
    <div class="strip" id="strip" role="group" aria-label="Chọn trạm"></div>
    <div id="detail" aria-live="polite"></div>
  </div>

  <aside class="card ctl">
    <div class="head2"><h3>Cách pha</h3><small>5 cách</small></div>
    <div class="row" id="meths"></div>
    <p class="mnote" id="methNote"></p>
    <div class="head2" style="margin-top:12px"><h3>Cà phê và mức rang</h3></div>
    <div class="row" id="beans"></div>
    <div class="row" id="roasts"></div>
    <p class="mnote" id="beanNote"></p>
    <hr>
    <div class="sl" style="margin-top:0"><label for="iT">Thời gian chiết <output id="oT"></output></label><input id="iT" type="range"><p id="tNote"></p></div>
    <div class="sl"><label for="iG">Cỡ xay <output id="oG"></output></label><input id="iG" type="range" min="0" max="4" step="1"><p id="gNote"></p></div>
    <div class="sl"><label for="iC">Nhiệt độ nước <output id="oC"></output></label><input id="iC" type="range" step="1"></div>
    <div class="sl"><label for="iD">Cà phê <output id="oD"></output></label><input id="iD" type="range"></div>
    <div class="sl"><label for="iW"><span id="wLbl">Nước</span> <output id="oW"></output></label><input id="iW" type="range"></div>
    <div class="row" style="margin-top:14px"><button class="btn main" id="run" type="button">Pha thử</button><button class="btn" id="reset" type="button">Về công thức chuẩn</button></div>
    <div class="stats">
      <div class="stat"><span>Chiết xuất EY</span><b id="sE"></b></div>
      <div class="stat"><span>Độ đậm TDS</span><b id="sS"></b></div>
      <div class="stat"><span>Ly ra</span><b id="sB"></b></div>
      <div class="stat"><span>Tỷ lệ bột : nước</span><b id="sR"></b></div>
    </div>
    <div id="verdict"></div>
    <hr>
    <span class="lbl">EY theo thời gian. Kéo trên biểu đồ để đổi lúc dừng</span>
    <div class="charts"><svg class="ch" id="cE" viewBox="0 0 340 156" role="img" aria-label="Tỷ lệ chiết xuất theo thời gian pha"></svg></div>
    <div id="tip"></div>
    <hr>
    <span class="lbl">Đã rời hạt, phần trăm của từng nhóm chất</span>
    <div class="bars cx" id="cbars"></div>
    <hr>
    <span class="lbl">Hướng vị dự đoán, chỉ số mô hình 0–100</span>
    <div class="bars" id="bars"></div>
  </aside>
</div>

<section class="card" id="hinh2">
  <h2>Hình 2: từ một mẻ bột, chất nào ra trước</h2>
  <p class="lead">Trục ngang là tỷ lệ chiết xuất (EY): phần trăm khối lượng bột đã tan vào ly. Trục dọc là phần trăm của từng nhóm chất đã rời hạt. Vạch đậm là ly bạn đang pha. Rê chuột hoặc chạm vào biểu đồ để đọc số.</p>
  <div class="lg" id="lg2"></div>
  <div class="chw" id="w2"><svg id="c2" class="c2" viewBox="0 0 920 400" role="img" aria-label="Phần trăm acid và CGA, caffeine, đường và Maillard, chất đắng đã rời hạt theo tỷ lệ chiết xuất"></svg><div class="tipbox" id="tip2" hidden></div></div>
  <details><summary>Xem bảng số theo từng mốc EY</summary><div class="tw"><table id="t2"></table></div></details>
</section>

<section class="card" id="hinh3">
  <h2 id="h3t">Hình 3: cùng liều, cùng nước, khác thời gian</h2>
  <p class="lead" id="h3l"></p>
  <div class="cups" id="cups"></div>
  <p class="bline" id="bline"></p>
</section>

<section class="card" id="ban-dich">
  <h2>Bản dịch bức hình</h2>
  <p class="lead">Dịch sát bức hình “Chemistry Review” (Ôn lại hóa học). Chỗ nào cần hiểu khác, MeDili ghi ở phần “Đọc lại” ngay sau.</p>
  <div class="tl">
    <p class="k">Ôn lại hóa học</p>
    <h3>Thời gian pha không chỉ quyết định độ đậm. Nó quyết định <em>chất nào</em> đi ra.</h3>
    <p class="tls">Polyphenol ra trước. Chất đắng ra sau cùng. Cùng một mẻ bột cho ra những ly khác nhau, tùy lúc bạn dừng.</p>
    <ol class="tl3">
      <li><span class="n" style="background:var(--cx1)">1</span><p>Acid chlorogenic (CGA) và các acid tạo vị chua thanh ra <b>trước</b>. Phần lớn đã ra hết khi tỷ lệ chiết xuất đạt <b>14%</b>.</p></li>
      <li><span class="n" style="background:var(--cx3)">2</span><p>Đường và hợp chất Maillard ra <b>ở giữa</b> (14–20%). Hình gọi đây là khoảng “lý tưởng” của SCA.</p></li>
      <li><span class="n" style="background:var(--cx4)">3</span><p>Phenolic đắng ra <b>sau cùng</b> (sau 22%). Chiết xuất quá mức chỉ thêm đắng, không thêm polyphenol.</p></li>
    </ol>
    <div class="tlg">
      <div><p class="k">Biểu đồ: từ một mẻ bột, chất nào ra trước</p><ul class="plain">
        <li><b>Ra trước:</b> acid, CGA, polyphenol.</li>
        <li><b>Ra giữa:</b> đường, hợp chất Maillard.</li>
        <li><b>Ra sau:</b> phenolic đắng.</li>
        <li>Trục dọc: phần trăm hợp chất đã rời bột. Trục ngang: tỷ lệ chiết xuất (EY) 0–25%. Bốn đường: CGA, đường, chất đắng và caffeine (nét đứt).</li></ul></div>
      <div><p class="k">Ba ly: cùng liều, cùng nước, khác thời gian</p><ul class="plain">
        <li>15 g bột, 250 ml nước. Thứ thay đổi là chất nào đi ra.</li>
        <li><b>1 phút:</b> chiết xuất thiếu.</li>
        <li><b>4 phút:</b> lý tưởng theo SCA, cân bằng.</li>
        <li><b>8 phút:</b> chiết xuất quá mức.</li>
        <li>Mỗi ly có ba thanh: CGA, caffeine, chất đắng.</li></ul></div>
    </div>
    <p class="bl2">Muốn có polyphenol mà không đắng? Dừng ở khoảng <b>4 phút</b>. Kéo dài chỉ thêm <b>chất đắng</b>, không thêm chất chống oxy hóa.</p>
  </div>
</section>

<section class="p-sec">
  <p class="eye">MeDili đọc lại</p>
  <h2 class="p-h2" style="margin:0">Sáu điều <em>cần hiểu đúng.</em></h2>
  <p class="lead" style="margin:0 0 4px;color:var(--muted);max-width:72ch">Bức hình đúng ở ý chính: chất tan ra theo thứ tự, và kéo dài chủ yếu thêm đắng. Vài chi tiết cần chỉnh lại theo nghiên cứu.</p>
  <div class="g3">{read}</div>
</section>

<section class="card">
  <h2>Sáu núm vặn của chiết xuất</h2>
  <p class="lead">Mỗi lần chỉ vặn một núm, rồi nếm lại. Cỡ xay thường là núm mạnh nhất.</p>
  <div class="tw"><table class="rich"><thead><tr><th>Núm vặn</th><th>Tăng lên thì</th><th>Ly chua, nhạt, hậu ngắn</th><th>Ly đắng, khô, gắt</th></tr></thead><tbody>{knobs}</tbody></table></div>
</section>

<section class="card">
  <h2>Công thức chuẩn theo cách pha</h2>
  <p class="lead">Bấm một hàng để nạp công thức vào Hình 1. EY và TDS là số của mô hình, dùng làm mốc khởi đầu rồi nếm để chốt.</p>
  <div class="tw"><table class="rich"><thead><tr><th>Cách pha</th><th>Cà phê</th><th>Bột : nước</th><th>Cỡ xay</th><th>Nước</th><th>Thời gian</th><th>Mô hình</th><th></th></tr></thead><tbody id="mt"></tbody></table></div>
</section>

<div class="cols">
  <section class="card">
    <h2>Đo chiết xuất thật</h2>
    <p class="lead">Có khúc xạ kế thì nhập số đo. EY = TDS × khối lượng ly ÷ lượng bột.</p>
    <div class="calc three">
      <label for="qT">TDS đo được (%)<input id="qT" type="text" inputmode="decimal" autocomplete="off" value="1,30"></label>
      <label for="qB">Khối lượng ly (g)<input id="qB" type="text" inputmode="decimal" autocomplete="off" value="220"></label>
      <label for="qD">Lượng bột (g)<input id="qD" type="text" inputmode="decimal" autocomplete="off" value="15"></label>
    </div>
    <div id="qR" aria-live="polite"></div>
    <p class="mnote">Ngưỡng TDS 1,15–1,35% chỉ dành cho ly lọc. Với espresso, phin và cold brew, hãy dựa vào EY rồi nếm.</p>
  </section>
  <section class="card">
    <h2>Phiếu pha</h2>
    <p class="lead">Sao chép phiếu để ghi lại lần pha và lần chỉnh sau.</p>
    <div id="sheet"></div>
    <button class="btn main" id="copy" type="button">Sao chép phiếu pha</button> <span id="copied" role="status"></span>
  </section>
</div>

<section class="card src">
  <h2>Nguồn và cách đọc mô hình</h2>
  <p class="lead">Đường cong trong Hình 1–3 là mô hình minh họa, dựng theo một hình minh họa phổ biến và chỉnh lại theo tài liệu tổng hợp. Không phải số đo của MeDili. Giả định chính: trần chiết xuất 28% ở nước nóng, 21% ở nước lạnh; công thức chuẩn của từng cách pha cho EY 19–20%.</p>
  <ul>{src}</ul>
  <div class="lnks"><a class="lnk" href="quay-pha.html">Quầy pha: công thức từng món</a><a class="lnk" href="rang.html">Phòng rang: tám cấp rang</a><a class="lnk" href="cold-brew.html">Cỗ máy Cold Brew MeDili</a><a class="lnk" href="tien-chat-huong.html">Cỗ máy Tiền chất hương</a><a class="lnk" href="suc-khoe.html">Cà phê và cơ thể: tính caffeine</a><a class="lnk" href="journal.html">Tất cả kiến thức cà phê</a></div>
</section>
'''
    return doc(FILE, TITLE, DESC, body, css=CSS, js=JS)


CSS = r'''
/* Cỗ máy Chiết xuất */
.mnote{font-size:.84rem;color:var(--muted);margin:8px 0 0;line-height:1.45}
#scene .gl{fill:var(--panel);fill-opacity:.18}
#scene .glt{fill:var(--panel);fill-opacity:.14}
#scene .liq,#scene .liqt{fill:#7A4D2A}
#scene .grd{fill:#5A3520}#scene .grdT{fill:#6B4226}
#scene .mug,#scene .drp{fill:var(--i-milk)}
#scene .bean{fill:#6B4226}#scene .bean2{fill:#4A2C1A}
#scene .lcdb{fill:#2E1C12;stroke:none}
#scene .lcd{font:700 7.8px var(--mono);fill:#F3D9A4}
#scene .wtx{font:700 8.4px var(--body);fill:#3A2416}
#scene .zl{font:600 12px var(--body)}
.pour{fill:none;stroke:var(--muted);stroke-width:2.2;stroke-dasharray:4 6;opacity:0;transition:opacity .3s}
.running .pour{opacity:.9;animation:pourA .7s linear infinite}
@keyframes pourA{to{stroke-dashoffset:-20}}
.drip{opacity:0}
.running .drip{animation:dripA .9s linear infinite}
.running .drip.d2{animation-delay:.45s}
@keyframes dripA{0%{opacity:0;transform:translateY(-5px)}25%{opacity:1}100%{opacity:0;transform:translateY(14px)}}
#stream{opacity:0;transition:opacity .2s}.running #stream{opacity:1}
.steam{fill:none;stroke:var(--muted);stroke-width:1.6;stroke-linecap:round;opacity:.55}
.bars.cx .bar{grid-template-columns:128px minmax(0,1fr) 34px}
#tip{color:var(--muted)}
.chw{position:relative;margin-top:6px}
.c2{display:block;width:100%;height:auto;touch-action:pan-y;cursor:crosshair;user-select:none;-webkit-user-select:none}
.c2 text{font:500 12px var(--mono);fill:var(--muted)}
.c2 .zh{font:700 11.5px var(--mono);letter-spacing:.08em;fill:var(--ink)}
.c2 .zs{font:500 12px var(--body);fill:var(--muted)}
.c2 .lab{font:600 13px var(--body);fill:var(--ink)}
.c2 .val{font:700 12px var(--mono);fill:var(--ink);paint-order:stroke;stroke:var(--panel);stroke-width:4px;stroke-linejoin:round}
.c2 .gr{stroke:var(--rule);stroke-width:1}
.c2 .cur{stroke:var(--ink);stroke-width:1.6}
.c2 .hov{stroke:var(--muted);stroke-width:1;stroke-dasharray:3 3}
.c2 .sca{fill:var(--good)}
.tipbox{position:absolute;z-index:2;pointer-events:none;background:var(--panel);border:1px solid var(--rule);border-radius:10px;padding:8px 10px;font:500 .8rem/1.55 var(--body);box-shadow:0 8px 20px rgba(46,28,18,.14);min-width:196px;color:var(--ink)}
.tipbox p{margin:0;display:flex;align-items:center;gap:6px}.tipbox p b{margin-left:auto;font:700 .8rem var(--mono);padding-left:12px}
.tipbox .h{font:700 .78rem var(--mono);color:var(--muted);margin-bottom:2px}
.sw2{display:inline-block;width:16px;height:0;border-top:2.5px solid;flex:none}.sw2.d{border-top-style:dashed}
.lg{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:.88rem;margin:2px 0 0}
.lg span{display:inline-flex;align-items:center;gap:8px}
.cups{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:6px}
@media (max-width:900px){.cups{grid-template-columns:minmax(0,1fr)}}
.cupc{background:var(--tint);border-radius:14px;padding:14px 16px;display:grid;gap:8px;min-width:0;align-content:start}
.cupc .top{display:flex;align-items:center;gap:14px}
.cupc svg{width:92px;height:auto;flex:none}
.cupc .ct{display:block;font:800 2.2rem/1 var(--display)}
.cupc .sub{display:block;font-size:.8rem;color:var(--muted);margin-top:2px}
.vt{display:inline-block;font:700 .72rem var(--body);letter-spacing:.06em;text-transform:uppercase;border:1.5px solid currentColor;border-radius:6px;padding:3px 8px;margin-top:6px}
.vt.good{color:var(--good)}.vt.warn{color:var(--warn)}.vt.bad{color:var(--bad)}
.cupc .bars{margin-top:0}.cupc .bar{grid-template-columns:118px minmax(0,1fr) 34px}
.cm{margin:0;font:500 .82rem var(--mono);color:var(--muted)}
.bline{margin:14px 0 0;background:var(--ink);color:var(--bg);border-radius:12px;padding:14px 18px;font-weight:600;line-height:1.5;text-align:center;text-wrap:balance}
.bline b{color:inherit}
.tl{display:grid;gap:12px;background:var(--bg);border:1px solid var(--rule);border-radius:14px;padding:18px 20px}
.tl h3{font:800 clamp(1.5rem,3vw,2.15rem)/1.15 var(--display);margin:0;letter-spacing:.01em;text-wrap:balance}
.tl h3 em{font-style:normal;color:var(--accent)}
.tls{margin:0;color:var(--muted);max-width:74ch}
.tl3{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px 18px}
.tl3 li{display:grid;grid-template-columns:32px minmax(0,1fr);gap:10px;align-items:start}
.tl3 .n{width:30px;height:30px;border-radius:50%;display:grid;place-items:center;font:800 1.05rem var(--display);color:#FFF6EC}
.tl3 p{margin:0}
.tlg{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 24px;border-top:1px solid var(--rule);padding-top:12px}
.tlg .k{margin-bottom:6px}
.bl2{margin:0;background:var(--tint);border-radius:10px;padding:12px 14px;font-weight:600}
@media (max-width:900px){.tl3,.tlg{grid-template-columns:minmax(0,1fr)}}
.rd{display:flex;flex-direction:column;gap:4px}
.rd>svg.pi{width:30px;height:30px;color:var(--accent);margin-bottom:2px}
.rd h3{font:800 1.4rem/1.15 var(--display);margin:2px 0 4px}
.rd .ft{margin-top:auto}
#mt td:last-child{text-align:right}
#mt .btn{white-space:nowrap}
#qR{margin-top:12px;border-radius:10px;padding:10px 12px;background:var(--tint);font-size:.9rem;line-height:1.5}
#qR b{display:block;font:700 1.15rem var(--mono)}
#qR.good b{color:var(--good)}#qR.warn b{color:var(--warn)}#qR.bad b{color:var(--bad)}
#copied{font-size:.86rem;color:var(--muted)}
.src>h2{color:var(--ink)}.src>.lead{color:var(--muted);font-size:.95rem}
.src ul{line-height:1.5}.src li{margin-bottom:4px}
.src .lnks{margin-top:12px}
@media (prefers-reduced-motion:reduce){.running .pour,.running .drip{animation:none}.pour{transition:none}}
'''

JS = r'''
/* ====== DỮ LIỆU ====== */
const $=id=>document.getElementById(id);
const vn=(n,d=1)=>n.toFixed(d).replace('.',',');
const clamp=(v,a,b)=>Math.min(b,Math.max(a,v));
const pc=v=>Math.round(clamp(v,0,1)*100);
const NB=' ';
const K0=.442,BETA=.716;
const GR=[
 {n:'Mịn',u:'Espresso',f:1.8,r:1.15},
 {n:'Vừa mịn',u:'Pour-over, moka',f:1.3,r:1.7},
 {n:'Vừa',u:'Lọc máy, AeroPress',f:1,r:2.4},
 {n:'Vừa thô',u:'Phin',f:.78,r:3.1},
 {n:'Thô',u:'Ép Pháp, cold brew',f:.6,r:4}];
const ROAST=[
 {n:'Rang sáng',k:.88,acid:1.15,sweet:.85,bit:.65,sh:.8,note:'Rang sáng giữ nhiều acid và CGA, hạt chắc nên khó tan hơn.'},
 {n:'Rang vừa',k:1,acid:.9,sweet:1,bit:1,sh:0,note:'Rang vừa cân bằng chua, ngọt, đắng.'},
 {n:'Rang đậm',k:1.12,acid:.6,sweet:.85,bit:1.35,sh:-1,note:'Rang đậm xốp, dễ tan, nhiều chất đắng sinh ra khi rang.'}];
const BEAN={
 rob:{n:'Robusta',full:'Robusta Di Linh',caf:2.4,acid:.8,bit:1.15,note:'Robusta có caffeine khoảng gấp đôi Arabica, thân dày, đắng đậm.'},
 ara:{n:'Arabica',full:'Arabica Cầu Đất',caf:1.35,acid:1.1,bit:.85,note:'Arabica nhiều acid thơm, ít caffeine hơn.'}};
const SER=[{k:'cga',n:'Acid & CGA',ab:'Acid',c:'var(--cx1)'},{k:'caf',n:'Caffeine',ab:'Caf',c:'var(--cx2)',d:'6 4'},{k:'sug',n:'Đường & Maillard',ab:'Ngọt',c:'var(--cx3)'},{k:'bit',n:'Chất đắng',ab:'Đắng',c:'var(--cx4)'}];
const ME={
 phin:{n:'Phin',nl:'phin',kind:'Nhỏ giọt qua lớp bột nén',p:{bean:'rob',roast:2,g:3,T:94,dose:25,water:80,t:6},target:19.5,al:.35,ret:1.4,t3:[2,6,12],sl:[1,14,.25],uf:1,tk:2,Tr:[80,100],dr:[12,35,1],wr:[40,200,5],top:9.6,
  note:'Nhỏ giọt qua lớp bột nén nhẹ. Tốc độ giọt do cỡ xay và lực nén quyết định. Ly ra rất đặc, thường pha với sữa đặc hoặc đá.'},
 fp:{n:'Ép Pháp',nl:'ép Pháp',kind:'Ngâm toàn phần',p:{bean:'ara',roast:1,g:4,T:93,dose:15,water:250,t:4},target:19.5,al:.12,ret:2,t3:[1,4,8],sl:[.5,12,.25],uf:1,tk:2,Tr:[80,100],dr:[8,60,1],wr:[120,1000,10],top:13.1,
  note:'Ngâm toàn phần. Đây là kiểu pha dùng làm mốc: 15 g bột, 250 ml nước, dừng ở 1, 4 hoặc 8 phút.'},
 po:{n:'Pour-over',nl:'pour-over',kind:'Rót liên tục qua phễu giấy',p:{bean:'ara',roast:1,g:1,T:93,dose:15,water:240,t:3},target:20,al:.35,ret:2,t3:[1.5,3,6],sl:[1,8,.25],uf:1,tk:1,Tr:[80,100],dr:[8,40,1],wr:[120,700,10],top:9.8,
  note:'Nước rót liên tục qua phễu giấy. Nước mới luôn còn “đói” chất tan nên chiết nhanh, giấy giữ dầu và cặn nên ly sạch vị.'},
 esp:{n:'Espresso',nl:'espresso',kind:'Ép nước nóng khoảng 9 bar',p:{bean:'rob',roast:1,g:0,T:93,dose:18,water:36,t:28/60},target:20,al:.5,ret:0,t3:[12/60,28/60,55/60],sl:[10,60,1],uf:1/60,tk:10,Tr:[85,98],dr:[14,22,.5],wr:[18,72,1],top:11.4,
  note:'Nước nóng khoảng 9 bar ép qua bột mịn nén chặt trong 25–30 giây. Ly đặc gấp nhiều lần ly lọc.'},
 cb:{n:'Cold brew',nl:'cold brew',kind:'Ngâm nước lạnh nhiều giờ',p:{bean:'rob',roast:1,g:4,T:20,dose:100,water:800,t:840},target:19,al:.12,ret:2,t3:[240,840,1440],sl:[2,24,.5],uf:60,tk:4,Tr:[2,30],dr:[40,200,5],wr:[300,2000,50],top:10.4,
  note:'Ngâm bột thô trong nước lạnh 12–24 giờ. Nước lạnh tan chậm và kéo ít chất đắng. Pha đặc rồi pha loãng khi uống.'}};
const ORDER=['phin','fp','po','esp','cb'];

/* ====== MÔ HÌNH ====== */
const FT=T=>Math.exp(.035*(T-93));
const EYM=T=>28-7*clamp((93-T)/73,0,1);
for(const k in ME){const m=ME[k],p=m.p,x=-Math.log(1-m.target/EYM(p.T));m.M=x/(Math.pow(p.t,BETA)*K0*GR[p.g].f*FT(p.T)*ROAST[p.roast].k);m.R0=p.water/p.dose}
const kEff=s=>{const m=ME[s.m];return K0*m.M*GR[s.g].f*FT(s.T)*Math.pow(s.water/s.dose/m.R0,m.al)*ROAST[s.roast].k};
const EY=(s,t)=>EYM(s.T)*(1-Math.exp(-kEff(s)*Math.pow(Math.max(t,0),BETA)));
const bitC=s=>20.3+3*clamp((93-s.T)/73,-.15,1)+ROAST[s.roast].sh;
const FR={cga:e=>1-Math.exp(-Math.pow(e/6.5,1.6)),caf:e=>1-Math.exp(-Math.pow(e/10,1.3)),sug:e=>1-Math.exp(-Math.pow(e/15,3)),bit:(e,s)=>1/(1+Math.exp(-(e-bitC(s))/1.5))};
const fx=(s,e)=>({cga:FR.cga(e),caf:FR.caf(e),sug:FR.sug(e),bit:FR.bit(e,s)});
const BEV=s=>{const m=ME[s.m];return m.ret?Math.max(5,s.water-m.ret*s.dose):s.water};
const TDS=(s,e)=>e*s.dose/BEV(s);
const goal=s=>s.m==='cb'?Math.min(19,.95*EYM(s.T)):Math.min(clamp(bitC(s)-1.65,18,20),.95*EYM(s.T));
const tStop=s=>{const em=EYM(s.T),x=-Math.log(1-goal(s)/em);return Math.pow(x/kEff(s),1/BETA)};
function taste(s,e){const b=BEAN[s.bean],r=ROAST[s.roast],f=fx(s,e),T=TDS(s,e);
 return [['Chua thanh',100*f.cga*(1-.55*f.sug)*r.acid*b.acid],['Ngọt, tròn',100*f.sug*(1-.6*f.bit)*r.sweet],['Đắng',100*(.12*f.caf+.88*f.bit*r.bit*b.bit)],['Đậm, thân',100*clamp(Math.log(T/.6)/Math.log(25),0,1)]].map(([n,v])=>[n,clamp(v,0,100)])}
const filt=m=>m==='fp'||m==='po';
const short=(e,sca)=>e<16?['bad','Chiết thiếu']:e<18?['warn','Hơi thiếu']:e<=22?['good',sca?'Cân bằng · SCA':'Cân bằng']:e<=24?['warn','Hơi quá']:['bad','Chiết quá'];
const sym=k=>k==='good'?'✓':k==='warn'?'!':'✕';
function verdict(s,e,T){const f=fx(s,e);let k,t,m;
 if(e<16){k='bad';t='Chiết thiếu';m='Ly dễ chua gắt, mặn nhẹ, hậu ngắn. Acid đã ra gần hết nhưng đường và Maillard chưa kịp ra. Xay mịn hơn, tăng nhiệt hoặc kéo dài thời gian.'}
 else if(e<18){k='warn';t='Hơi thiếu';m='Gần tới vùng cân bằng. Thêm chút thời gian hoặc xay mịn hơn một nấc.'}
 else if(e<=22){k='good';t=filt(s.m)?'Vùng cân bằng, chuẩn SCA 18–22'+'%':'Vùng cân bằng, EY 18–22'+'%';m=`Acid và CGA đã ra ${pc(f.cga)}%, chất đắng mới ra ${pc(f.bit)}%.`}
 else if(e<=24){k='warn';t='Hơi quá';m='Bắt đầu đắng, khô ở hậu vị. Rút ngắn thời gian, xay thô hơn hoặc hạ nhiệt.'}
 else{k='bad';t='Chiết quá';m='Phần thêm vào chủ yếu là chất đắng, CGA gần như không tăng. Rút ngắn thời gian, xay thô hơn hoặc hạ nhiệt.'}
 if(s.m==='fp'||s.m==='po'){if(T<1.15)m+=` Độ đậm ${vn(T,2)}% loãng hơn mốc 1,15–1,35% của SCA: thêm bột hoặc bớt nước.`;else if(T>1.35)m+=` Độ đậm ${vn(T,2)}% đặc hơn mốc 1,15–1,35% của SCA: bớt bột hoặc thêm nước.`}
 if(s.m==='esp'&&(T<8||T>12))m+=` TDS ${vn(T,1)}% nằm ngoài mốc tham khảo 8–12% của espresso.`;
 if(s.m==='cb')m+=' Cold brew pha đặc, khi uống thường pha loãng với nước, sữa hoặc đá.';
 return {k,t,m}}

/* ====== TRẠNG THÁI ====== */
const st={m:'fp',...ME.fp.p,sel:5};
const ftime=(t,m=st.m)=>{if(m==='esp')return Math.round(t*60)+NB+'giây';if(m==='cb'){const h=t/60;return (Math.abs(h-Math.round(h))<.01?Math.round(h):vn(h,1))+NB+'giờ'}const s=Math.round(t*60);return Math.floor(s/60)+':'+String(s%60).padStart(2,'0')};
const g1=n=>Number.isInteger(n)?String(n):vn(n,1);
const cur=()=>{const e=EY(st,st.t),T=TDS(st,e);return {e,T,f:fx(st,e),B:BEV(st)}};
const mix=(a,b,t)=>a.map((v,i)=>Math.round(v+(b[i]-v)*t));
const cofArr=(T,e)=>{const v=clamp(.5*Math.pow(clamp(Math.log(T/.5)/Math.log(28),0,1),.6)+.5*clamp(e/26,0,1),0,1);return v<.5?mix([228,198,152],[170,104,52],v/.5):mix([170,104,52],[60,33,18],(v-.5)/.5)};
const rgb=a=>`rgb(${a.join(',')})`;
const cofCol=(T,e)=>rgb(cofArr(T,e));

/* ====== HÌNH HỌC ====== */
const U=7.8,OX=220,OY=96;
const P=(x,y,z=0)=>[OX+(x-y)*.866*U,OY+(x+y)*.5*U-z*U];
const f1=n=>n.toFixed(1);
const pts=a=>a.map(q=>q.map(f1).join(',')).join(' ');
const poly=(a,c='')=>`<polygon points="${pts(a)}" class="${c}"/>`;
const line=(a,w,col,cls='')=>`<polyline${cls?` class="${cls}"`:''} points="${pts(a)}" fill="none" style="${w?`stroke-width:${w};`:''}${col?`stroke:${col}`:''}"/>`;
function box(x,y,z,w,d,h,c=['f1','f2','f3']){return poly([P(x,y+d,z),P(x+w,y+d,z),P(x+w,y+d,z+h),P(x,y+d,z+h)],c[1])+poly([P(x+w,y,z),P(x+w,y+d,z),P(x+w,y+d,z+h),P(x+w,y,z+h)],c[2])+poly([P(x,y,z+h),P(x+w,y,z+h),P(x+w,y+d,z+h),P(x,y+d,z+h)],c[0])}
const RX=r=>r*U*1.2247,RY=r=>r*U*.7071;
function cyl(cx,cy,z,r,h,c='f2',top='f1'){const [a,b]=P(cx,cy,z),[,t]=P(cx,cy,z+h),rx=RX(r),ry=RY(r);return `<path class="${c}" d="M${f1(a-rx)} ${f1(t)}V${f1(b)}A${f1(rx)} ${f1(ry)} 0 0 0 ${f1(a+rx)} ${f1(b)}V${f1(t)}Z"/><ellipse class="${top}" cx="${f1(a)}" cy="${f1(t)}" rx="${f1(rx)}" ry="${f1(ry)}"/>`}
function frus(cx,cy,z0,r0,z1,r1,c,top){const [a,b0]=P(cx,cy,z0),[,b1]=P(cx,cy,z1),x0=RX(r0),y0=RY(r0),x1=RX(r1),y1=RY(r1);return `<path class="${c}" d="M${f1(a-x1)} ${f1(b1)}L${f1(a-x0)} ${f1(b0)}A${f1(x0)} ${f1(y0)} 0 0 0 ${f1(a+x0)} ${f1(b0)}L${f1(a+x1)} ${f1(b1)}Z"/><ellipse class="${top}" cx="${f1(a)}" cy="${f1(b1)}" rx="${f1(x1)}" ry="${f1(y1)}"/>`}
const ring=(cx,cy,z,r,col,w=2)=>{const [a,b]=P(cx,cy,z),rx=RX(r),ry=RY(r);return `<path fill="none" style="stroke:${col};stroke-width:${w}" d="M${f1(a-rx)} ${f1(b)}A${f1(rx)} ${f1(ry)} 0 0 0 ${f1(a+rx)} ${f1(b)}"/>`};
const face=(x,y,z)=>{const q=P(x,y,z);return `matrix(.866 .5 0 1 ${f1(q[0])} ${f1(q[1])})`};
const lcd=(x,y,z,w,id)=>`<g transform="${face(x,y,z)}"><rect class="lcdb" x="0" y=".8" width="${w}" height="8.6" rx="1.4"/><text class="lcd" id="${id}" x="${w/2}" y="7.6" text-anchor="middle"></text></g>`;
const stG=(i,inner)=>`<g class="st m" data-i="${i}" tabindex="0" role="button" aria-label="Trạm ${i}: ${ST[i-1].name}">${inner}</g>`;

/* ====== 7 TRẠM ====== */
const MT={
 phin:{mech:'Nước ngấm qua lớp bột nén nhẹ rồi nhỏ giọt xuống ly. Rót 20–30 ml nước đầu để ủ cho bột nở và thoát khí, rồi mới rót tiếp. Tốc độ giọt do cỡ xay và lực nén quyết định, nên với phin, chỉnh cỡ xay cũng là chỉnh thời gian.',check:'Giọt đều, không chảy thành dòng. Nước rút quá nhanh là bột thô hoặc nén lỏng, quá lâu là bột mịn hoặc nén chặt.',fail:'Nén quá chặt làm nước đọng lâu, ly đắng gắt. Bột quá mịn lọt qua lỗ phin làm ly đục.',tip:'Ly pha sữa đặc vẫn nên nếm vài giọt đen trước để biết ly đã chiết đúng chưa.'},
 fp:{mech:'Bột ngâm toàn phần trong nước. Mọi hạt bột tiếp xúc nước suốt thời gian pha, nên thời gian là núm vặn rõ nhất. Đây là kiểu pha dùng làm mốc: 15 g bột, 250 ml nước, dừng ở 1, 4 hoặc 8 phút.',check:'Khuấy nhẹ lớp bột nổi sau 30–60 giây đầu, đậy nắp, hết giờ thì nhấn và rót ra ngay.',fail:'Để cà phê nằm lại trong bình sau khi nhấn, bột dưới đáy vẫn tiếp tục chiết và ly đắng dần.',tip:'Rót qua thêm một lớp giấy lọc nếu muốn ly sạch cặn.'},
 po:{mech:'Nước rót liên tục qua lớp bột trong phễu giấy rồi chảy xuống bình. Nước mới luôn còn “đói” chất tan nên chiết nhanh. Giấy giữ lại dầu và cặn nên ly sạch vị.',check:'Ủ 30–45 giây với lượng nước gấp đôi lượng bột, rồi rót chậm theo vòng. Tổng thời gian khoảng 2:30–4:00.',fail:'Rót mạnh vào một chỗ tạo rãnh, nước chảy tắt qua bột. Một phần bột chiết quá, phần khác chiết thiếu.',tip:'Xả giấy lọc bằng nước nóng trước để bớt mùi giấy.'},
 esp:{mech:'Máy ép nước nóng khoảng 9 bar qua bột mịn nén chặt. Áp suất và bột mịn giúp chiết đủ trong 25–30 giây, ra ly rất đặc. Theo các nghiên cứu về vị đắng, cách pha áp suất và nhiệt cao như espresso thường cho nhiều chất đắng nhất.',check:'18 g bột cho khoảng 36 g espresso trong 25–30 giây.',fail:'Chảy dưới 20 giây là bột thô hoặc nén lệch, ly chua mỏng. Trên 35 giây là bột quá mịn, ly đắng gắt.',tip:'Cân ly ra bằng gram thay vì nhìn vạch, vì lớp crema làm sai thể tích.'},
 cb:{mech:'Bột thô ngâm trong nước lạnh. Nước lạnh tan chậm và kéo ít chất đắng hơn. Caffeine và CGA trong cold brew đạt cân bằng sau 6–7 giờ, sớm hơn mốc 10–24 giờ của các công thức thường gặp. Ngâm lâu hơn vẫn tiếp tục kéo các chất khác.',check:'Ngâm ở nhiệt độ phòng 12–16 giờ hoặc trong tủ lạnh 18–24 giờ, rồi lọc kỹ và giữ lạnh.',fail:'Lọc không kỹ, cặn mịn tiếp tục chiết làm ly đục và gắt dần.',tip:'Pha đặc 1:8 rồi pha loãng khoảng 1:1 với nước, sữa hoặc đá khi uống.'}};
const ST=[
 {name:'Cối xay',sub:()=>'Cỡ bột quyết định tốc độ tan',
  mech:()=>`Xay càng mịn, bột càng nhiều mặt tiếp xúc và nước vào lõi hạt càng nhanh, nên chất tan ra sớm hơn. Với phin, pour-over và espresso, bột mịn còn làm nước chảy chậm lại, tức là kéo dài thời gian tiếp xúc. Vì vậy cỡ xay là núm vặn mạnh nhất. Đang chọn <b>${GR[st.g].n.toLowerCase()}</b>, phù hợp với ${GR[st.g].u.toLowerCase()}.`,
  kv:()=>[['Cỡ xay',GR[st.g].n],['Phù hợp với',GR[st.g].u],['Tốc độ so với xay vừa','×'+vn(GR[st.g].f,2)],['Gợi ý cho '+ME[st.m].n,GR[ME[st.m].p.g].n]],
  check:'Bốc một nhúm bột: mịn giống bột mì, vừa giống đường cát, thô giống muối hạt. Bột phải đều, ít bụi.',
  fail:'Lưỡi cối mòn tạo nhiều bụi mịn lẫn mảnh to. Bụi chiết quá nhanh nên đắng, khô, mảnh to chiết thiếu nên chua. Ly vừa chua vừa đắng thường do bột không đều.',
  tip:'Xay ngay trước khi pha. Bột xay sẵn mất mùi thơm nhanh hơn hạt nguyên.'},
 {name:'Nước & nhiệt',sub:()=>'Nhiệt độ đổi tốc độ và thứ tự tan',
  mech:()=>`Nước nóng hòa tan nhanh hơn và kéo được cả những chất khó tan. Hạ nhiệt làm mọi thứ chậm lại, nhất là nhóm đắng ra sau. Vì vậy cold brew cần hàng giờ thay vì vài phút, và ra ít chất đắng hơn. Ở ${st.T}${NB} °C, mô hình tính tốc độ chiết bằng ×${vn(FT(st.T),2)} so với 93${NB} °C.`,
  kv:()=>[['Nhiệt nước',st.T+NB+'°C'],['Tốc độ so với 93'+NB+'°C','×'+vn(FT(st.T),2)],['Trần chiết xuất',vn(EYM(st.T),0)+'%'],['Chất đắng bắt đầu rõ','từ EY ~'+vn(bitC(st)-2,0)+'%']],
  check:'Nước vừa sôi, để nghỉ một chút cho hết sủi rồi rót. Có nhiệt kế thì giữ 90–96 °C cho phin và lọc.',
  fail:'Nước chưa đủ nóng làm ly chua, nhạt. Nước có mùi clo hay mùi bồn chứa đi thẳng vào ly. Nước quá tinh khiết, không còn khoáng, thường cho ly phẳng vị.',
  tip:'Tráng phin, bình và ly bằng nước nóng để giữ nhiệt trong lúc chiết.'},
 {name:'Cân & tỷ lệ',sub:()=>'Tỷ lệ quyết định ly đặc hay loãng',
  mech:()=>`Tỷ lệ bột : nước quyết định ly đặc hay loãng (TDS) nhiều hơn là chiết được bao nhiêu (EY). Thêm nước giúp chiết thêm một chút nhưng ly loãng đi. Phin và espresso dùng rất ít nước nên ly đặc. ${st.m==='esp'?'Với espresso, mô hình tính theo khối lượng ly ra.':`Bã giữ lại khoảng ${Math.round(ME[st.m].ret*st.dose)}${NB}ml nước, phần này không vào ly.`}`,
  kv:()=>{const B=BEV(st);return [['Bột',g1(st.dose)+NB+'g'],[st.m==='esp'?'Ra ly':'Nước',st.water+NB+(st.m==='esp'?'g':'ml')],['Tỷ lệ','1:'+vn(st.water/st.dose,1)],['Ly ra',Math.round(B)+NB+(st.m==='esp'?'g':'ml')]]},
  check:'Cân bột và nước bằng gram. Đong bằng muỗng có thể lệch vài gram tùy cỡ xay và độ rang.',
  fail:'Đổi tỷ lệ để sửa vị chua hay đắng thường không trúng. Ly loãng mà không chua thì thêm bột. Ly đậm mà chua thì chỉnh cỡ xay hoặc thời gian.',
  tip:'Ghi lại công thức đang dùng. Mỗi lần chỉ đổi một yếu tố rồi nếm lại.'},
 {name:'Bình chiết',sub:()=>ME[st.m].n+' · '+ME[st.m].kind.toLowerCase(),
  mech:()=>MT[st.m].mech,
  kv:()=>[['Cách chiết',ME[st.m].kind],['Thời gian',ftime(st.t)],['Mốc ba ly ở Hình 3',ME[st.m].t3.map(t=>ftime(t)).join(', ')],['Dừng gợi ý',`${ftime(tStop(st))}, EY ${vn(goal(st),1)}%`]],
  check:'',fail:'',tip:''},
 {name:'Thứ tự tan',sub:()=>'Bốn nhóm chất của bức hình',
  mech:()=>'Mỗi ống là một nhóm chất trong bức hình, đầy tới đâu là nhóm đó đã rời hạt bấy nhiêu phần trăm. Acid và CGA là phân tử nhỏ, dễ tan nên ra trước. Caffeine cũng ra sớm. Đường, hợp chất caramel và Maillard tạo vị ngọt, thân, ra ở giữa. Nhóm đắng gắt ra sau cùng.',
  kv:()=>{const c=cur();return SER.map(s=>[s.n,pc(c.f[s.k])+'%'])},
  check:'Nếm theo thứ tự: chua ở đầu lưỡi, ngọt và thân ở giữa, đắng và khô ở cuối và hậu vị.',
  fail:'Ly đủ chua nhưng thiếu ngọt là dừng quá sớm. Ly đắng khô đọng ở hậu vị là kéo quá lâu, nước quá nóng hoặc bột quá mịn.',
  tip:'Đường cong dựng theo bức hình, có chỉnh lại theo nghiên cứu. Đây là mô hình minh họa, không phải số đo.'},
 {name:'Ly & khúc xạ kế',sub:()=>'Đo TDS, tính EY',
  mech:()=>{const c=cur();return `Khúc xạ kế đo TDS, tức phần trăm chất tan trong ly. Biết TDS, khối lượng ly và lượng bột thì tính được EY = TDS × khối lượng ly ÷ lượng bột. SCA xem ly lọc đạt chuẩn vàng khi EY 18–22% và TDS 1,15–1,35%. Ly này: ${vn(c.T,2)}% × ${Math.round(c.B)}${NB}g ÷ ${g1(st.dose)}${NB}g = ${vn(c.e,1)}%.`},
  kv:()=>{const c=cur();return [['TDS',vn(c.T,2)+'%'],['Ly ra',Math.round(c.B)+NB+'g'],['EY',vn(c.e,1)+'%'],['Chuẩn SCA cho ly lọc','EY 18–22'+'%, TDS 1,15–1,35'+'%']]},
  check:'Khuấy đều, lấy mẫu, để nguội về nhiệt độ phòng rồi mới đo.',
  fail:'Đo khi mẫu còn nóng cho số sai. Mẫu espresso nhiều cặn cần lọc nếu máy đo yêu cầu.',
  tip:'Không có khúc xạ kế thì nếm: chua mặn là thiếu, đắng khô là quá. Ô tính ở cuối trang đổi số đo ra EY.'},
 {name:'Bã cà phê',sub:()=>'Phần không bao giờ tan',
  mech:()=>{const c=cur();return `Các thí nghiệm đo được mức chiết tối đa khoảng 28–32%. Phần còn lại của bột là khung xơ, không tan. Với EY ${vn(c.e,1)}%, khoảng ${pc(1-c.e/100)}% khối lượng bột nằm lại trong bã. Vì phần tan được có giới hạn, chiết xuất quá mức không làm ly “nhiều hơn”, chỉ kéo thêm nhóm chất không mong muốn.`},
  kv:()=>{const c=cur();return [['Bột vào',g1(st.dose)+NB+'g'],['Chất tan vào ly',vn(st.dose*c.e/100,1)+NB+'g'],['Nằm lại trong bã',vn(st.dose*(1-c.e/100),1)+NB+'g'],['Nước bã giữ',ME[st.m].ret?Math.round(ME[st.m].ret*st.dose)+NB+'ml':'theo bánh bột']]},
  check:'Bã phin và pour-over phẳng, đều. Bã có hố hay rãnh là nước chảy lệch.',
  fail:'Nước chảy theo rãnh làm một phần bột chiết quá, phần khác chiết thiếu.',
  tip:'Bã đã pha có thể ủ làm phân bón, hoặc phơi khô để khử mùi tủ lạnh.'}];

/* ====== DỰNG CẢNH ====== */
const G={x:124,y:440,r:70},MG={x:312,y:534,r:36};
const gAng=v=>(-210+clamp(v,0,28)/28*240)*Math.PI/180;
function brewer(m){
 if(m==='fp')return cyl(52,12.5,0,3.15,.6,'cu2','cu2')+'<g id="bl"></g>'+cyl(52,12.5,.6,2.95,8.8,'gl','glt')+ring(52,12.5,1.7,2.95,'var(--copper)',2.4)+ring(52,12.5,8.4,2.95,'var(--copper)',2.4)
  +cyl(52,12.5,9.4,3.05,.55,'cu','cu')+line([P(52,12.5,9.95),P(52,12.5,12.5)],2.2,'var(--s3)')+cyl(52,12.5,12.3,.7,.8,'cu2','cu')
  +line([P(54.9,12.5,8.6),P(56.7,12.5,8.4),P(57,12.5,3.4),P(54.9,12.5,2.8)],3.4,'var(--copper2)');
 if(m==='phin')return '<g id="bl"></g>'+cyl(52,12.5,0,2.6,5.4,'gl','glt')+cyl(52,12.5,5.4,3.3,.35,'f2','f1')+cyl(52,12.5,5.75,2.15,2.9,'f2','f1')+ring(52,12.5,7.9,2.15,'var(--s3)',1.4)
  +cyl(52,12.5,8.65,2.25,.4,'f3','f1')+cyl(52,12.5,9.05,.55,.55,'f3','f2')+drips(52,12.5,5.2);
 if(m==='po')return '<g id="bl"></g>'+cyl(52,12.5,0,2.7,5.2,'gl','glt')+cyl(52,12.5,5.2,2.3,.3,'drp','drp')+frus(52,12.5,5.5,1.15,9.8,3.2,'drp','drp')
  +(()=>{const [a,b]=P(52,12.5,9.6);return `<ellipse class="grdT" cx="${f1(a)}" cy="${f1(b)}" rx="${f1(RX(2.7))}" ry="${f1(RY(2.7))}"/>`})()+drips(52,12.5,5.1);
 if(m==='esp'){const cup=P(49.5,15.9,2.8),gh=P(49.5,15.6,5.4);
  return box(44.2,14.4,0,12.6,4.2,.9,['f1','f2','f3'])+box(44.2,6,0,12.6,8.4,11,['f1','f2','f3'])+box(44.2,6,11,12.6,8.4,.35,['f2','f3','f3'])
  +`<g transform="${face(53.4,14.4,9.6)}"><circle cx="9" cy="9" r="8.5" class="pa" style="stroke:var(--ol);stroke-width:1.2"/><line x1="9" y1="9" x2="13.5" y2="4.5" style="stroke:var(--accent);stroke-width:1.6"/><text class="lcd" x="9" y="15.4" text-anchor="middle" style="fill:var(--ink)">9 bar</text></g>`
  +cyl(49.5,15.6,6.3,1.55,1.4,'f3','f2')+cyl(49.5,15.6,5.4,1.65,.9,'f3','f3')
  +line([P(49.5,17.2,5.95),P(49.5,21.6,5.6)],4.2,'#4A2C1A')
  +`<line id="stream" x1="${f1(gh[0])}" y1="${f1(gh[1])}" x2="${f1(cup[0])}" y2="${f1(cup[1])}" style="stroke-width:2.6"/>`
  +cyl(49.5,15.9,.9,1.45,1.9,'pa','liqt')}
 return '<g id="bl"></g>'+cyl(52,12.5,0,3.6,9.4,'gl','glt')+cyl(52,12.5,9.4,3.7,.8,'cu','cu')+ring(52,12.5,1.2,3.6,'var(--copper)',2);
}
function drips(cx,cy,z){const a=P(cx,cy,z-.4),b=P(cx,cy,z-1.4);return `<ellipse class="drip liqt" cx="${f1(a[0])}" cy="${f1(a[1])}" rx="1.3" ry="2"/><ellipse class="drip d2 liqt" cx="${f1(b[0])}" cy="${f1(b[1])}" rx="1.2" ry="1.8"/>`}
function buildScene(){
 let h='<g class="m">';
 [[3,23],[109,23],[109,3]].forEach(([x,y])=>h+=cyl(x,y,-9,1.2,5,'cu2','cu2'));
 h+=box(0,0,-4,112,27,4,['wo','wo2','cu2'])+'</g>';
 const pl=P(66,27,-.6);
 h+=`<g transform="matrix(.866 .5 0 1 ${f1(pl[0])} ${f1(pl[1])})"><rect width="245" height="24" rx="3" style="fill:#D6B26A;stroke:#2A1B16;stroke-width:1.2"/><circle cx="8" cy="12" r="1.8" style="fill:#2A1B16"/><circle cx="237" cy="12" r="1.8" style="fill:#2A1B16"/><text class="sgn" x="122" y="17.5" text-anchor="middle">MeDili Coffee Farm · Di Linh</text></g>`;
 /* 1 cối xay */
 const bt=P(8.5,11.5,11.1);
 h+=stG(1,box(5,8,0,7,7,6.5,['f1','f2','f3'])+box(7.3,15,2.4,2.4,1.3,1.1,['f2','f3','f3'])+cyl(8.5,11.5,6.5,1.5,1.3,'f3','f2')
  +frus(8.5,11.5,7.8,1.25,11.1,2.75,'bean','bean')
  +[[-9,-2],[0,-4],[9,-1],[-4,3],[6,4],[-12,2],[13,2],[1,1]].map(([dx,dy])=>`<ellipse class="bean2" cx="${f1(bt[0]+dx)}" cy="${f1(bt[1]+dy)}" rx="3" ry="2" transform="rotate(${dx*4} ${f1(bt[0]+dx)} ${f1(bt[1]+dy)})"/>`).join('')
  +frus(8.5,11.5,7.8,1.4,12.4,3.1,'gl','glt')+cyl(8.5,17.6,0,1.7,2.3,'pa','grdT'));
 /* 2 nước và nhiệt */
 const tip=P(29.6,12.5,6.6);
 h+=stG(2,box(18.6,9,0,7,7,1.1,['f1','f2','f3'])+lcd(19.6,16,1.05,34,'kT')
  +line([P(19.4,12.5,5.2),P(18,12.5,5.4),P(17.4,12.5,4),P(17.9,12.5,2.2),P(19.4,12.5,2)],3,'var(--copper2)')
  +cyl(22.1,12.5,1.1,2.8,4.4,'cu','cu')+ring(22.1,12.5,2.3,2.8,'var(--copper2)',1.6)
  +cyl(22.1,12.5,5.5,1.4,.5,'cu2','cu')+cyl(22.1,12.5,6,.45,.6,'cu2','cu2')
  +line([P(24.6,12.5,1.9),P(26.6,12.5,4.4),P(28.1,12.5,6.3),P(29.6,12.5,6.6)],3.2,'var(--copper2)')
  +`<g id="steam"><path class="steam" d="M${f1(tip[0]+4)} ${f1(tip[1]-6)}c-5-6 5-9 0-16"/><path class="steam" d="M${f1(tip[0]+11)} ${f1(tip[1]-4)}c-5-6 5-9 0-15"/></g>`);
 /* 3 cân */
 h+=stG(3,box(32,8.6,0,10.4,8,1.2,['f1','f2','f3'])+lcd(32.8,16.6,1.1,64,'kD')+frus(36.2,12.3,1.2,1.6,2.9,2.4,'pa','grdT'));
 /* 4 bình chiết */
 h+=`<path class="pour" id="pour" d="M${f1(tip[0])} ${f1(tip[1])}Q410 150 ${f1(P(51.4,12.5,ME[st.m].top-1)[0])} ${f1(P(51.4,12.5,ME[st.m].top-1)[1])}"/>`;
 h+=stG(4,brewer(st.m));
 /* 5 bốn ống */
 const tl=['Acid','Caf','Ngọt','Đắng'];
 h+=stG(5,box(62,9,0,15,2,13.2,['wo','wo2','cu2'])+`<g transform="${face(62.8,11,12.8)}"><text class="wtx" x="0" y="4">THỨ TỰ TAN</text></g>`
  +box(62,11,0,15,4.4,1.4,['wo','wo2','cu2'])+'<g id="tubes"></g>'
  +`<g transform="${face(62,15.4,1.3)}">${tl.map((t,i)=>`<text class="wtx" x="${f1((1.7+i*3.4)*7.8)}" y="7.6" text-anchor="middle">${t}</text>`).join('')}</g>`);
 /* 6 ly và khúc xạ kế */
 const c6=P(85,13,3.6);
 h+=stG(6,cyl(85,13,0,2.9,4,'mug','mug')+`<ellipse class="liqt" id="cupTop" cx="${f1(c6[0])}" cy="${f1(c6[1])}" rx="${f1(RX(2.5))}" ry="${f1(RY(2.5))}"/>`
  +line([P(87.7,13,3.5),P(89.2,13,3.3),P(89.3,13,1.3),P(87.7,13,1.1)],4.6,'var(--ol)')+line([P(87.7,13,3.5),P(89.2,13,3.3),P(89.3,13,1.3),P(87.7,13,1.1)],2.6,'var(--i-milk)')
  +box(90.8,9.4,0,6.2,3.6,1.5,['f1','f2','f3'])+lcd(91.3,13,1.4,40,'kS')
  +(()=>{const q=P(92.6,11,1.5);return `<ellipse cx="${f1(q[0])}" cy="${f1(q[1])}" rx="5" ry="2.8" class="lcdb"/>`})());
 /* 7 bã */
 h+=stG(7,box(100,10,0,7.4,6,3.4,['wo','wo2','cu2'])+cyl(103.7,13,3.4,2.1,.6,'grd','grdT')+`<g transform="${face(100.6,16,3)}"><text class="wtx" id="kB" x="0" y="11"></text></g>`);
 /* đồng hồ EY, kính lúp, nhãn */
 h+=buildGauge()+'<g id="mag"></g>';
 h+=`<g><rect x="20" y="614" width="322" height="64" rx="8" class="pa" style="stroke:var(--ink);stroke-width:1.2"/><text x="34" y="643" class="sgn2">MeDili Coffee Farm · Di Linh</text><text x="34" y="663" class="tiny mutedt">Bản vẽ khái niệm · mô hình minh họa, không phải số đo</text></g>`;
 h+='<g id="chips"></g>';
 $('scene').innerHTML=h;
 document.querySelectorAll('#scene .st').forEach(g=>{g.addEventListener('click',()=>select(+g.dataset.i));g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();select(+g.dataset.i)}})});
}
function buildGauge(){
 const arc=(a,b,r)=>{const A=gAng(a),B=gAng(b);return `M${f1(G.x+r*Math.cos(A))} ${f1(G.y+r*Math.sin(A))}A${r} ${r} 0 0 1 ${f1(G.x+r*Math.cos(B))} ${f1(G.y+r*Math.sin(B))}`};
 let h=`<g class="m"><line x1="${G.x}" y1="${G.y+G.r}" x2="${G.x}" y2="${G.y+G.r+12}"/><circle cx="${G.x}" cy="${G.y}" r="${G.r}" class="pa" style="stroke-width:2.4"/></g>`;
 h+=`<path d="${arc(0,18,G.r-13)}" fill="none" style="stroke:var(--rule);stroke-width:8"/><path d="${arc(18,22,G.r-13)}" fill="none" style="stroke:var(--good);stroke-width:8"/><path d="${arc(22,28,G.r-13)}" fill="none" style="stroke:var(--bad);stroke-width:8"/>`;
 for(let v=0;v<=28;v+=7){const A=gAng(v);h+=`<text x="${f1(G.x+(G.r-31)*Math.cos(A))}" y="${f1(G.y+(G.r-31)*Math.sin(A)+3.5)}" text-anchor="middle" class="mono" style="font-size:10.5px">${v}</text>`}
 h+=`<line id="needle" x1="${G.x}" y1="${G.y}" x2="${G.x}" y2="${G.y-42}" style="stroke:var(--accent);stroke-width:3;stroke-linecap:round"/><circle cx="${G.x}" cy="${G.y}" r="5" class="ac"/>`;
 h+=`<text id="gv" x="${G.x}" y="${G.y+43}" text-anchor="middle" class="mono" style="font-size:16px"></text><text x="${G.x}" y="${G.y+57}" text-anchor="middle" class="tiny mutedt">chiết xuất EY</text>`;
 h+=`<text id="gt" x="${G.x}" y="${G.y-G.r-12}" text-anchor="middle" class="lab12"></text>`;
 return h;
}
function drawMag(){
 const R=GR[st.g].r,N=clamp(Math.round(620/(R*R*4)),9,90),cup=P(8.5,17.6,1);
 let h=`<polyline class="lead-l" points="${f1(cup[0])},${f1(cup[1])} ${MG.x-22},${MG.y-28}"/><line x1="${MG.x+25}" y1="${MG.y+25}" x2="${MG.x+44}" y2="${MG.y+44}" style="stroke:var(--ink);stroke-width:6;stroke-linecap:round"/>`;
 h+=`<circle cx="${MG.x}" cy="${MG.y}" r="${MG.r}" class="pa" style="stroke:var(--ink);stroke-width:2.4"/>`;
 for(let i=0;i<N;i++){const rr=(MG.r-R-4)*Math.sqrt((i+.5)/N),th=i*2.39996,j=Math.abs(Math.sin(i*12.9898)*43758.5453)%1,s=R*(.75+.5*j);
  h+=`<ellipse cx="${f1(MG.x+rr*Math.cos(th))}" cy="${f1(MG.y+rr*Math.sin(th))}" rx="${f1(s)}" ry="${f1(s*.8)}" transform="rotate(${Math.round(j*180)} ${f1(MG.x+rr*Math.cos(th))} ${f1(MG.y+rr*Math.sin(th))})" style="fill:${j>.5?'#6B4226':'#8D5A32'}"/>`}
 h+=`<text x="${MG.x}" y="${MG.y+MG.r+18}" text-anchor="middle" class="lab12">Bột ${GR[st.g].n.toLowerCase()}</text>`;
 $('mag').innerHTML=h;
}
const CHIP=[null,{x:236,y:14},{x:318,y:66},{x:404,y:118},{x:520,y:170},{x:648,y:222},{x:764,y:306},{x:846,y:398}];
const anch=i=>[null,[8.5,11.5,12.4],[22.1,12.5,6.6],[36.2,12.3,2.9],[52,12.5,ME[st.m].top],[69.5,13,13.2],[85,13,4],[103.7,13,4]][i];
function chipLabel(i,c,tv){
 if(i===1)return 'Xay '+GR[st.g].n.toLowerCase();
 if(i===2)return (st.T<40?'Nước lạnh ':'Nước ')+st.T+NB+'°C';
 if(i===3)return st.m==='esp'?`${g1(st.dose)}${NB}g → ${st.water}${NB}g`:`${g1(st.dose)}${NB}g · ${st.water}${NB}ml`;
 if(i===4)return ME[st.m].n+' · '+ftime(tv);
 if(i===5)return 'EY '+vn(c.e,1)+'%';
 if(i===6)return 'TDS '+vn(c.T,c.T<3?2:1)+'%';
 return 'Bã giữ '+pc(1-c.e/100)+'%'}
function drawChips(c,tv){let h='';
 for(let i=1;i<=7;i++){const C=CHIP[i],l=chipLabel(i,c,tv),w=40+l.length*7.2,x=Math.min(C.x,1030-w-6),q=P(...anch(i));
  h+=`<polyline class="lead-l${i===st.sel?' on':''}" data-l="${i}" points="${f1(q[0])},${f1(q[1])} ${f1(x+20)},${C.y+13}"/><g class="chip${i===st.sel?' on':''}" data-c="${i}"><rect x="${f1(x+6)}" y="${C.y}" rx="8" width="${f1(w)}" height="26"/><circle cx="${f1(x+6)}" cy="${C.y+13}" r="13"/><text class="num" x="${f1(x+6)}" y="${C.y+18.5}" text-anchor="middle">${i}</text><text class="lab" x="${f1(x+26)}" y="${C.y+18}">${l}</text></g>`}
 const el=$('chips');el.innerHTML=h;el.querySelectorAll('.chip').forEach(g=>g.addEventListener('click',()=>select(+g.dataset.c)))}

/* ====== VẼ PHẦN ĐỘNG ====== */
function renderDyn(tv,k){
 const e=EY(st,tv),T=TDS(st,e),f=fx(st,e),c={e,T,f},col=cofCol(T,e),m=st.m;
 /* ống chất */
 let h='';SER.forEach((s,i)=>{const x=63.7+i*3.4,y=13,lv=f[s.k];
  if(lv>.004)h+=cyl(x,y,1.55,.98,9.4*lv,'',``).replace(/class=""/g,`style="fill:${s.c}"`);
  h+=cyl(x,y,1.4,1.15,10,'gl','glt')});
 $('tubes').innerHTML=h;
 /* chất lỏng */
 const bl=$('bl');if(bl){let g='';
  if(m==='fp'){g=cyl(52,12.5,.6,2.75,7.4,'liq','liqt')+cyl(52,12.5,7.1,2.75,.9,'grd','grdT')}
  else if(m==='phin'||m==='po'){const H=(m==='phin'?4.4:4.2)*clamp(k,0,1);if(H>.05)g=cyl(52,12.5,.1,2.42,H,'liq','liqt')}
  else if(m==='cb'){g=cyl(52,12.5,.2,3.45,8.2,'liq','liqt')+cyl(52,12.5,.2,3.45,1.5,'grd','grdT')}
  bl.innerHTML=g}
 document.querySelectorAll('#scene .liq,#scene .liqt').forEach(x=>x.style.fill=col);
 const sm=$('stream');if(sm)sm.style.stroke=col;
 /* đồng hồ, chữ */
 $('needle').setAttribute('transform',`rotate(${f1(gAng(e)*180/Math.PI+90)} ${G.x} ${G.y})`);
 $('gv').textContent=vn(e,1)+'%';
 $('gt').textContent=(k<1?'Đang pha ':'Dừng ở ')+ftime(tv);
 $('kT').textContent=st.T+NB+'°C';
 $('kD').textContent=st.m==='esp'?`${g1(st.dose)} g → ${st.water} g`:`${g1(st.dose)} g · ${st.water} ml`;
 $('kS').textContent=vn(T,T<3?2:1)+'%';
 $('kB').textContent='còn '+pc(1-e/100)+'%';
 $('steam').style.display=st.T>=70?'':'none';
 drawChips(c,tv);
 drawE(tv);
 $('cbars').innerHTML=SER.map(s=>`<div class="bar"><span>${s.n}</span><span class="track"><i style="width:${pc(f[s.k])}%;background:${s.c}"></i></span><span>${pc(f[s.k])}</span></div>`).join('');
}

/* ====== BIỂU ĐỒ EY THEO THỜI GIAN ====== */
function drawE(tv){
 const m=ME[st.m],W=340,H=156,l=30,r=10,t=18,b=22,tmax=m.sl[1]*m.uf,X=x=>l+x/tmax*(W-l-r),Y=v=>t+(1-v/28)*(H-t-b);
 const un=st.m==='esp'?'giây':st.m==='cb'?'giờ':'phút';
 let g=`<text class="ttl" x="${l}" y="11">EY (%) · trục ngang: ${un}</text>`;
 g+=`<rect x="${l}" y="${f1(Y(22))}" width="${W-l-r}" height="${f1(Y(18)-Y(22))}" style="fill:var(--good);fill-opacity:.16"/><text x="${W-r-3}" y="${f1(Y(22)+9)}" text-anchor="end">SCA 18–22</text>`;
 [0,10,20,28].forEach(v=>g+=`<line x1="${l}" x2="${W-r}" y1="${f1(Y(v))}" y2="${f1(Y(v))}" style="stroke:var(--rule);stroke-width:.7"/><text x="${l-5}" y="${f1(Y(v)+3.5)}" text-anchor="end">${v}</text>`);
 for(let u=0;u*m.uf<=tmax+1e-9;u+=m.tk){const x=u*m.uf;g+=`<text x="${f1(X(x))}" y="${H-5}" text-anchor="middle">${u}</text>`}
 const p=[];for(let i=0;i<=80;i++){const x=tmax*i/80;p.push(f1(X(x))+','+f1(Y(EY(st,x))))}
 g+=`<polyline points="${p.join(' ')}" fill="none" style="stroke:var(--accent);stroke-width:2"/>`;
 m.t3.forEach(x=>{if(x<=tmax)g+=`<circle cx="${f1(X(x))}" cy="${f1(Y(EY(st,x)))}" r="3" style="fill:var(--panel);stroke:var(--ink);stroke-width:1.2"/>`});
 const ts=tStop(st);if(ts<=tmax)g+=`<line x1="${f1(X(ts))}" x2="${f1(X(ts))}" y1="${t}" y2="${H-b}" style="stroke:var(--good);stroke-width:1;stroke-dasharray:3 3"/>`;
 g+=`<line x1="${f1(X(tv))}" x2="${f1(X(tv))}" y1="${t}" y2="${H-b}" style="stroke:var(--ink);stroke-width:1"/><circle cx="${f1(X(tv))}" cy="${f1(Y(EY(st,tv)))}" r="4.5" style="fill:var(--accent);stroke:var(--panel);stroke-width:2"/>`;
 $('cE').innerHTML=g;
}
function scrubE(ev,set){
 const m=ME[st.m],r=$('cE').getBoundingClientRect(),x=(ev.clientX-r.left)/r.width*340,tmax=m.sl[1]*m.uf;
 let v=clamp((x-30)/300,0,1)*tmax/m.uf;v=clamp(Math.round(v/m.sl[2])*m.sl[2],m.sl[0],m.sl[1]);
 const t=v*m.uf,e=EY(st,t);
 $('tip').textContent=`Dừng ở ${ftime(t)}: EY ${vn(e,1)}%, TDS ${vn(TDS(st,e),2)}%`;
 if(set&&Math.abs(t-st.t)>1e-9){st.t=t;update()}
}

/* ====== HÌNH 2 ====== */
let D2={W:920,H:400,L:58,R:150,T:70,B:46,mob:false};
function dims2(){const w=Math.round($('w2').clientWidth)||920,W=clamp(w,300,1400),mob=W<640;return {W,H:mob?340:400,L:mob?46:58,R:mob?14:150,T:mob?56:70,B:mob?42:46,mob}}
const X2=e=>D2.L+e/28*(D2.W-D2.L-D2.R),Y2=v=>D2.T+(1-v)*(D2.H-D2.T-D2.B);
function drawC2(hov){
 D2=dims2();const {W,H,L,R,T,B,mob}=D2,c=cur();let g='';
 $('c2').setAttribute('viewBox',`0 0 ${W} ${H}`);
 [[0,14,'var(--cx1)','RA TRƯỚC','acid · CGA · polyphenol'],[14,20,'var(--cx3)','RA GIỮA','đường · Maillard'],[20,28,'var(--cx4)','RA SAU','chất đắng']].forEach(([a,b,col,hd,sb])=>{
  const cx=f1((X2(a)+X2(b))/2);
  g+=`<rect x="${f1(X2(a))}" y="${T}" width="${f1(X2(b)-X2(a))}" height="${H-T-B}" style="fill:${col};fill-opacity:.07"/>`;
  g+=mob?`<text class="zh" x="${cx}" y="${T-28}" text-anchor="middle" style="font-size:10px;letter-spacing:.02em">${hd}</text>`:`<text class="zh" x="${cx}" y="${T-46}" text-anchor="middle">${hd}</text><text class="zs" x="${cx}" y="${T-30}" text-anchor="middle">${sb}</text>`;
  if(a>0)g+=`<line x1="${f1(X2(a))}" x2="${f1(X2(a))}" y1="${T}" y2="${H-B}" class="gr" style="stroke-dasharray:3 4"/>`});
 [0,.25,.5,.75,1].forEach(v=>g+=`<line x1="${L}" x2="${W-R}" y1="${f1(Y2(v))}" y2="${f1(Y2(v))}" class="gr"/><text x="${L-8}" y="${f1(Y2(v)+4)}" text-anchor="end">${v*100}%</text>`);
 [0,5,10,15,20,25].forEach(e=>g+=`<text x="${f1(X2(e))}" y="${H-B+18}" text-anchor="middle">${e}%</text>`);
 g+=`<text x="${f1((L+W-R)/2)}" y="${H-6}" text-anchor="middle">tỷ lệ chiết xuất EY</text>`;
 if(!mob)g+=`<text transform="translate(13 ${f1((T+H-B)/2)}) rotate(-90)" text-anchor="middle">% chất đã rời hạt</text>`;
 g+=`<rect class="sca" x="${f1(X2(18))}" y="${H-B-7}" width="${f1(X2(22)-X2(18))}" height="7" rx="2"/><text x="${f1(X2(20))}" y="${H-B-12}" text-anchor="middle" class="val" style="font-size:11px">SCA 18–22%</text>`;
 const ends=[];
 SER.forEach(s=>{const p=[];for(let e=0;e<=28.001;e+=.25)p.push(f1(X2(e))+','+f1(Y2(FR[s.k](e,st))));
  g+=`<polyline points="${p.join(' ')}" fill="none" stroke-linejoin="round" style="stroke:${s.c};stroke-width:2${s.d?';stroke-dasharray:'+s.d:''}"/>`;
  ends.push({s,y:Y2(FR[s.k](28,st))})});
 if(!mob){ends.sort((a,b)=>a.y-b.y);for(let i=0;i<ends.length;i++){ends[i].ly=i?Math.max(ends[i].y,ends[i-1].ly+17):Math.max(ends[i].y,T+6)}
  const ov=ends[ends.length-1].ly-(H-B-6);if(ov>0)ends.forEach(o=>o.ly-=ov);
  ends.forEach(o=>{const x=X2(28);g+=`<polyline points="${f1(x)},${f1(o.y)} ${f1(x+10)},${f1(o.ly)} ${f1(x+16)},${f1(o.ly)}" fill="none" style="stroke:${o.s.c};stroke-width:1.5${o.s.d?';stroke-dasharray:3 2':''}"/><text class="lab" x="${f1(x+20)}" y="${f1(o.ly+4.5)}">${o.s.n}</text>`})}
 const em=EYM(st.T);if(em<27.9){const mx=f1((X2(em)+X2(28))/2),my=(T+H-B)/2;g+=`<rect x="${f1(X2(em))}" y="${T}" width="${f1(X2(28)-X2(em))}" height="${H-T-B}" style="fill:var(--panel);fill-opacity:.72"/><text class="zs" x="${mx}" y="${f1(my+50)}" text-anchor="middle"${mob?' style="font-size:10.5px"':''}>nước ${st.T}${NB} °C</text><text class="zs" x="${mx}" y="${f1(my+66)}" text-anchor="middle"${mob?' style="font-size:10.5px"':''}>không tới</text>`}
 const ex=X2(c.e),right=ex>(L+W-R)/2;
 g+=`<line class="cur" x1="${f1(ex)}" x2="${f1(ex)}" y1="${T-14}" y2="${H-B}"/><text class="val" x="${f1(ex+(right?-6:6))}" y="${T-5}" text-anchor="${right?'end':'start'}">${mob?'':'Ly của bạn · '}EY ${vn(c.e,1)}%</text>`;
 SER.forEach(s=>g+=`<circle cx="${f1(ex)}" cy="${f1(Y2(c.f[s.k]))}" r="5" style="fill:${s.c};stroke:var(--panel);stroke-width:2"/>`);
 if(hov!=null){const hx=X2(hov);g+=`<line class="hov" x1="${f1(hx)}" x2="${f1(hx)}" y1="${T}" y2="${H-B}"/>`;SER.forEach(s=>g+=`<circle cx="${f1(hx)}" cy="${f1(Y2(FR[s.k](hov,st)))}" r="4.5" style="fill:var(--panel);stroke:${s.c};stroke-width:2"/>`)}
 $('c2').innerHTML=g;
}
function hover2(ev){
 const svg=$('c2'),r=svg.getBoundingClientRect(),x=(ev.clientX-r.left)/r.width*D2.W,e=(x-D2.L)/(D2.W-D2.L-D2.R)*28;
 if(e<0||e>28){leave2();return}
 drawC2(e);
 const tb=$('tip2'),w=$('w2').getBoundingClientRect();
 tb.innerHTML=`<p class="h">EY ${vn(e,1)}%</p>`+SER.map(s=>`<p><i class="sw2${s.d?' d':''}" style="border-color:${s.c}"></i>${s.n}<b>${pc(FR[s.k](e,st))}%</b></p>`).join('');
 tb.hidden=false;const bw=tb.offsetWidth,px=ev.clientX-w.left,py=ev.clientY-w.top;
 tb.style.left=f1(clamp(px+16+bw>w.width?px-16-bw:px+16,0,Math.max(0,w.width-bw)))+'px';tb.style.top=f1(clamp(py-40,0,Math.max(0,w.height-tb.offsetHeight)))+'px';
}
function leave2(){$('tip2').hidden=true;drawC2(null)}
function table2(){const rows=[];for(let e=0;e<=28;e+=2)rows.push(`<tr><td>${e}%</td>${SER.map(s=>`<td>${pc(FR[s.k](e,st))}%</td>`).join('')}</tr>`);
 $('t2').innerHTML=`<thead><tr><th>EY</th>${SER.map(s=>`<th>${s.n}</th>`).join('')}</tr></thead><tbody>${rows.join('')}</tbody>`}

/* ====== HÌNH 3 ====== */
function mugSvg(a){const body=rgb(a),rim=rgb(mix(a,[246,235,217],.3)),liq=rgb(mix(a,[42,23,16],.35));
 return `<svg viewBox="0 0 120 96" aria-hidden="true"><ellipse cx="54" cy="90" rx="44" ry="5" style="fill:var(--rule)"/><path d="M97 34h7a14 14 0 0 1 0 28h-9" fill="none" style="stroke:var(--ink);stroke-width:8"/><path d="M97 34h7a14 14 0 0 1 0 28h-9" fill="none" style="stroke:${body};stroke-width:4"/><path d="M12 22h86v38a28 28 0 0 1-28 28H40a28 28 0 0 1-28-28z" style="fill:${body};stroke:var(--ink);stroke-width:2.4"/><path d="M20 32v24a20 20 0 0 0 9 16" fill="none" style="stroke:#FFF6EC;stroke-width:4;stroke-linecap:round;opacity:.28"/><ellipse cx="55" cy="22" rx="43" ry="9" style="fill:${rim};stroke:var(--ink);stroke-width:2.4"/><ellipse cx="55" cy="23" rx="37" ry="6.4" style="fill:${liq}"/></svg>`}
function drawCups(){
 const m=ME[st.m],lab=['Rút sớm','Đúng mốc','Để quá'];
 $('h3l').textContent=`Cùng ${g1(st.dose)}${NB}g bột, ${st.water}${NB}${st.m==='esp'?'g ra ly':'ml nước'}, xay ${GR[st.g].n.toLowerCase()}, nước ${st.T}${NB} °C, ${BEAN[st.bean].n} ${ROAST[st.roast].n.toLowerCase()}, pha ${ME[st.m].nl}. Thứ thay đổi là chất nào vào ly. Đổi thông số ở Hình 1, ba ly đổi theo.`;
 $('cups').innerHTML=m.t3.map((t,i)=>{const e=EY(st,t),T=TDS(st,e),f=fx(st,e),[k,vt]=short(e,filt(st.m));
  return `<div class="cupc"><div class="top">${mugSvg(cofArr(T,e))}<div><b class="ct">${ftime(t)}</b><span class="sub">${lab[i]}</span><span class="vt ${k}">${sym(k)} ${vt}</span></div></div>
  <div class="bars">${SER.map(s=>`<div class="bar"><span>${s.n}</span><span class="track"><i style="width:${pc(f[s.k])}%;background:${s.c}"></i></span><span>${pc(f[s.k])}</span></div>`).join('')}</div>
  <p class="cm">EY ${vn(e,1)}% · TDS ${vn(T,T<3?2:1)}%</p></div>`}).join('');
 const ts=tStop(st),e=EY(st,ts),f=fx(st,e);
 $('bline').innerHTML=st.T<40?`Nước lạnh kéo rất ít chất đắng: ở <b>${ftime(ts)}</b>, chất đắng mới ra ${pc(f.bit)}% trong khi CGA đã ra ${pc(f.cga)}%. Caffeine và CGA gần cân bằng sau 6–7 giờ, ngâm lâu hơn chủ yếu để có thêm thân và vị.`
  :`Muốn có CGA mà không đắng? Với ${ME[st.m].nl} và thông số này, dừng ở khoảng <b>${ftime(ts)}</b>: CGA đã ra ${pc(f.cga)}%, chất đắng mới ra ${pc(f.bit)}%. Kéo dài thêm chủ yếu là thêm chất đắng.`;
}

/* ====== BẢNG CÔNG THỨC ====== */
function drawMT(){
 $('mt').innerHTML=ORDER.map(k=>{const m=ME[k],p=m.p,s={m:k,...p},e=EY(s,p.t),T=TDS(s,e);
  return `<tr class="pick${k===st.m?' on':''}" data-k="${k}" tabindex="0"><td><b>${m.n}</b><br><small>${m.kind}</small></td><td>${BEAN[p.bean].n}<br><small>${ROAST[p.roast].n}</small></td><td>${p.dose}${NB}g : ${p.water}${NB}${k==='esp'?'g':'ml'}<br><small>1:${vn(p.water/p.dose,1)}</small></td><td>${GR[p.g].n}</td><td>${p.T}${NB} °C</td><td>${ftime(p.t,k)}<br><small>ba ly: ${m.t3.map(t=>ftime(t,k)).join(', ')}</small></td><td>EY ${vn(e,1)}%<br><small>TDS ${vn(T,T<3?2:1)}%</small></td><td><button class="btn small" type="button" data-k="${k}">Nạp</button></td></tr>`}).join('');
 $('mt').querySelectorAll('tr').forEach(r=>{const go=()=>{setMethod(r.dataset.k);$('scene').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'center'})};r.onclick=go;r.onkeydown=e=>{if(e.key==='Enter'){e.preventDefault();go()}}});
}

/* ====== ĐIỀU KHIỂN ====== */
function pills(id,items,cur,cb){$(id).innerHTML=items.map(([k,n])=>`<button class="pill" type="button" data-k="${k}" aria-pressed="${String(cur)===String(k)}">${n}</button>`).join('');$(id).querySelectorAll('button').forEach(b=>b.onclick=()=>cb(b.dataset.k))}
function setMethod(k){stopAnim();Object.assign(st,{m:k},ME[k].p);buildScene();update()}
function sliders(){
 const m=ME[st.m],set=(id,a,b,s,v)=>{const el=$(id);el.min=a;el.max=b;el.step=s;el.value=v};
 set('iT',m.sl[0],m.sl[1],m.sl[2],st.t/m.uf);set('iG',0,4,1,st.g);set('iC',m.Tr[0],m.Tr[1],1,st.T);set('iD',m.dr[0],m.dr[1],m.dr[2],st.dose);set('iW',m.wr[0],m.wr[1],m.wr[2],st.water);
 $('oT').textContent=ftime(st.t);$('oG').textContent=GR[st.g].n;$('oC').textContent=st.T+NB+'°C';$('oD').textContent=g1(st.dose)+NB+'g';
 $('wLbl').textContent=st.m==='esp'?'Ra ly':'Nước';$('oW').textContent=st.water+NB+(st.m==='esp'?'g':'ml');
 {const g=goal(st);$('tNote').textContent=`Dừng gợi ý ${ftime(tStop(st))}: EY ${vn(g,1)}%, chất đắng mới ra ${pc(FR.bit(g,st))}%. Ba ly ở Hình 3: ${m.t3.map(t=>ftime(t)).join(', ')}.`}
 $('gNote').textContent=`${GR[st.g].u}. Công thức chuẩn của ${m.n.toLowerCase()} dùng xay ${GR[m.p.g].n.toLowerCase()}.`;
}
function renderStation(){
 const s=ST[st.sel-1],mt=st.sel===4?MT[st.m]:s;
 document.querySelectorAll('#scene .st').forEach(g=>g.classList.toggle('on',+g.dataset.i===st.sel));
 document.querySelectorAll('#strip button').forEach((b,n)=>{b.classList.toggle('on',n+1===st.sel);b.setAttribute('aria-pressed',n+1===st.sel)});
 $('detail').innerHTML=`<div class="dh"><div class="dn">${st.sel}</div><h2>${s.name}<small>${s.sub()}</small></h2></div><div class="dgrid"><div><span class="lbl">Cách hoạt động</span><p>${s.mech()}</p><span class="lbl">Kiểm tra thế nào</span><p>${mt.check}</p></div><div><span class="lbl">Thông số lúc này</span><dl class="kv">${s.kv().map(([a,b])=>`<dt>${a}</dt><dd>${b}</dd>`).join('')}</dl><p style="margin-top:8px"></p><span class="lbl">Lỗi hay gặp</span><p>${mt.fail}</p><span class="lbl">Mẹo</span><p>${mt.tip}</p></div></div>`;
}
function select(i){st.sel=i;renderStation();drawChips(cur(),st.t);const sc=document.querySelector('.scroller'),q=P(...anch(i));if(sc.scrollWidth>sc.clientWidth)sc.scrollLeft=q[0]/1040*sc.scrollWidth-sc.clientWidth/2}
function sheet(){const c=cur(),m=ME[st.m],ts=tStop(st);
 const t=`PHIẾU PHA · MeDili
Cách pha: ${m.n} (${m.kind.toLowerCase()})
Cà phê: ${BEAN[st.bean].full}, ${ROAST[st.roast].n.toLowerCase()}, xay ${GR[st.g].n.toLowerCase()}
Bột ${g1(st.dose)} g · ${st.m==='esp'?'ra ly':'nước'} ${st.water} ${st.m==='esp'?'g':'ml'} (1:${vn(st.water/st.dose,1)}) · ${st.T} °C · ${ftime(st.t)}
Mô hình: EY ${vn(c.e,1)}% · TDS ${vn(c.T,c.T<3?2:1)}% · ly ra ${Math.round(c.B)} ${st.m==='esp'?'g':'ml'}
Đã rời hạt: acid & CGA ${pc(c.f.cga)}%, caffeine ${pc(c.f.caf)}%, đường & Maillard ${pc(c.f.sug)}%, chất đắng ${pc(c.f.bit)}%
Dừng gợi ý: ${ftime(ts)} (EY ${vn(goal(st),1)}%)
Ghi tay: TDS đo ____ % | vị ____________ | lần sau chỉnh ____________`;
 $('sheet').textContent=t.replace(/(\d) (g|ml|%|°C)/g,'$1 $2');st.sheet=t}
function update(){
 const c=cur(),B=c.B,v=verdict(st,c.e,c.T);
 pills('meths',ORDER.map(k=>[k,ME[k].n]),st.m,k=>setMethod(k));
 pills('beans',Object.entries(BEAN).map(([k,b])=>[k,b.n]),st.bean,k=>{st.bean=k;update()});
 pills('roasts',ROAST.map((r,i)=>[i,r.n]),st.roast,k=>{st.roast=+k;update()});
 $('methNote').textContent=ME[st.m].note;
 $('beanNote').textContent=BEAN[st.bean].note+' '+ROAST[st.roast].note;
 sliders();
 $('figsub').textContent=`bàn chiết xuất 7 trạm, đang pha ${ME[st.m].nl} · ${ftime(st.t)}`;
 $('sE').textContent=vn(c.e,1)+'%';$('sS').textContent=vn(c.T,c.T<3?2:1)+'%';$('sB').textContent=Math.round(B)+NB+(st.m==='esp'?'g':'ml');$('sR').textContent='1:'+vn(st.water/st.dose,1);
 $('verdict').className=v.k;$('verdict').innerHTML=`<b>${sym(v.k)} ${v.t}</b>${v.m}`;
 $('bars').innerHTML=taste(st,c.e).map(([n,x])=>`<div class="bar"><span>${n}</span><span class="track"><i style="width:${x.toFixed(0)}%"></i></span><span>${x.toFixed(0)}</span></div>`).join('');
 $('tip').textContent=`Dừng ở ${ftime(st.t)}: EY ${vn(c.e,1)}%, TDS ${vn(c.T,2)}%`;
 drawMag();renderDyn(st.t,1);drawC2(null);table2();drawCups();drawMT();sheet();renderStation();
}

/* ====== HOẠT ẢNH ====== */
const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
let raf=0;
function stopAnim(){cancelAnimationFrame(raf);raf=0;$('scene').classList.remove('running')}
function run(){
 stopAnim();if(still){update();return}
 const T=st.t,t0=performance.now(),D=3600;$('scene').classList.add('running');
 const step=now=>{const k=clamp((now-t0)/D,0,1);renderDyn(T*k,k);if(k<1)raf=requestAnimationFrame(step);else{stopAnim();renderDyn(T,1)}};
 raf=requestAnimationFrame(step);
}

/* ====== Ô TÍNH ====== */
const num=id=>parseFloat($(id).value.replace(/\s/g,'').replace(',','.'));
function calc(){const T=num('qT'),Bm=num('qB'),D=num('qD'),out=$('qR');
 if(!(T>0&&Bm>0&&D>0)){out.className='';out.innerHTML='<b>–</b>Nhập đủ ba số để tính.';return}
 const e=T*Bm/D,[k,t]=short(e,false);let m='';
 if(e<18)m='Thấp hơn vùng 18–22'+'%: xay mịn hơn, tăng nhiệt hoặc kéo dài.';else if(e<=22)m='Nằm trong vùng 18–22'+'% của SCA.';else m='Cao hơn vùng 18–22'+'%: xay thô hơn, hạ nhiệt hoặc rút ngắn.';
 if(T>=1.15&&T<=1.35)m+=' TDS nằm trong mốc 1,15–1,35'+'% cho ly lọc.';
 out.className=k;out.innerHTML=`<b>${sym(k)} EY ${vn(e,1)}% · ${t}</b>${m}`}

/* ====== KHỞI ĐỘNG ====== */
$('strip').innerHTML=ST.map((s,i)=>`<button type="button" aria-pressed="false">${i+1} ${s.name}</button>`).join('');
$('strip').querySelectorAll('button').forEach((b,i)=>b.onclick=()=>select(i+1));
$('lg2').innerHTML=SER.map(s=>`<span><i class="sw2${s.d?' d':''}" style="border-color:${s.c}"></i>${s.n}</span>`).join('')+`<span><i class="sw2" style="border-color:var(--ink)"></i>Ly của bạn</span>`;
const onIn=(id,f)=>$(id).addEventListener('input',()=>{stopAnim();f(+$(id).value);update()});
onIn('iT',v=>st.t=v*ME[st.m].uf);onIn('iG',v=>st.g=v);onIn('iC',v=>st.T=v);onIn('iD',v=>st.dose=v);onIn('iW',v=>st.water=v);
$('run').onclick=run;$('run2').onclick=run;$('reset').onclick=()=>setMethod(st.m);
const cE=$('cE');let drag=false;
cE.addEventListener('pointerdown',e=>{drag=true;stopAnim();try{cE.setPointerCapture(e.pointerId)}catch(_){}scrubE(e,true)});
cE.addEventListener('pointermove',e=>scrubE(e,drag));
['pointerup','pointercancel'].forEach(n=>cE.addEventListener(n,()=>{drag=false}));
cE.addEventListener('pointerleave',()=>{if(!drag){const c=cur();$('tip').textContent=`Dừng ở ${ftime(st.t)}: EY ${vn(c.e,1)}%, TDS ${vn(c.T,2)}%`}});
const c2=$('c2');c2.addEventListener('pointermove',hover2);c2.addEventListener('pointerdown',hover2);c2.addEventListener('pointerleave',leave2);
['qT','qB','qD'].forEach(id=>$(id).addEventListener('input',calc));
$('copy').onclick=async()=>{try{await navigator.clipboard.writeText(st.sheet);$('copied').textContent='Đã sao chép.'}catch(e){const r=document.createRange();r.selectNodeContents($('sheet'));const s=getSelection();s.removeAllRanges();s.addRange(r);$('copied').textContent='Đã chọn sẵn số, bạn hãy tự sao chép.'}setTimeout(()=>$('copied').textContent='',2600)};
let rz=0;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(()=>drawC2(null),120)});
buildScene();update();calc();
{const sc=document.querySelector('.scroller');if(sc.scrollWidth>sc.clientWidth+4)sc.scrollLeft=P(60,13,6)[0]/1040*sc.scrollWidth-sc.clientWidth/2}
'''
