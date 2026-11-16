# Bánh xe hương MeDili: bánh xe 3 tầng do MeDili soạn riêng (không sao chép bánh xe SCA/WCR),
# bốn nguồn gốc của mùi, mức rang, cà phê MeDili, phiếu nếm. Màu theo phong thủy: không xanh lá, không xanh dương, không đen.
import json
from iso import *

FILE = 'banh-xe-huong.html'
TITLE = 'Bánh Xe Hương MeDili'
DESC = ('Bánh xe hương cà phê do MeDili soạn với từ ngữ gần gũi người Việt: chín nhóm hương, ba tầng từ chung đến cụ thể, nguồn gốc của từng mùi, '
        'mức rang làm nổi nhóm nào, và phiếu nếm để luyện mũi.')

# (tên nhóm, màu, mô tả, link, [(nhóm giữa, [(mùi, nguồn gốc)])])  nguồn gốc: e enzyme, s caramel hoá đường, d chưng cất khô, t mùi lỗi
SEC = [
    ('Hoa', '#C74B7A', 'Hương enzyme có sẵn từ lúc trái chín. Nhẹ và bay nhanh, rõ nhất ở rang sáng và khi ly còn ấm.', 'trai-chin.html',
     [('Hoa trắng', [('Hoa cà phê', 'e'), ('Hoa nhài', 'e'), ('Hoa bưởi', 'e')]), ('Hoa hồng, trà', [('Hoa hồng', 'e'), ('Trà ô long', 'e'), ('Trà đen', 'e')])]),
    ('Trái cây', '#B33A24', 'Từ đường và acid của trái chín, cộng thêm ester do lên men. Trái chín đủ, lên men sạch thì rõ; lên men quá thì thành rượu, giấm.', 'vi-sinh.html',
     [('Trái mọng', [('Dâu tằm', 'e'), ('Dâu tây', 'e'), ('Mâm xôi', 'e')]), ('Trái nhiệt đới', [('Mít chín', 'e'), ('Chuối chín', 'e'), ('Xoài', 'e'), ('Chanh dây', 'e')]),
      ('Táo, mơ, đào', [('Táo', 'e'), ('Mơ', 'e'), ('Đào', 'e')]), ('Trái sấy', [('Nho khô', 's'), ('Mận khô', 's'), ('Chà là', 's')])]),
    ('Chua thanh', '#D9782E', 'Từ acid citric, malic có sẵn trong nhân và acid lactic, acetic do lên men. Rang càng đậm, chua càng giảm.', 'tien-chat-huong.html',
     [('Cam chanh', [('Chanh', 'e'), ('Cam', 'e'), ('Bưởi', 'e'), ('Quýt', 'e')]), ('Kiểu chua', [('Táo xanh', 'e'), ('Sữa chua', 'e'), ('Rượu vang', 'e'), ('Me', 'e')])]),
    ('Ngọt', '#C9962B', 'Từ sucrose bị caramel hoá và phản ứng Maillard khi rang vừa. Robusta Premium sơ chế honey hay cho caramel, đường nâu.', 'tien-chat-huong.html',
     [('Đường nâu', [('Đường thốt nốt', 's'), ('Mật mía', 's'), ('Đường nâu', 's')]), ('Caramel, mật', [('Caramel', 's'), ('Mật ong', 'e'), ('Kẹo bơ', 's')]),
      ('Vani, bơ', [('Vani', 's'), ('Bơ', 's')])]),
    ('Hạt, ca cao', '#8D5A32', 'Phản ứng Maillard và Strecker ở rang vừa đến đậm. Robusta Di Linh thường mạnh nhóm này.', 'tien-chat-huong.html',
     [('Hạt rang', [('Đậu phộng rang', 's'), ('Hạt điều', 's'), ('Hạnh nhân', 's'), ('Óc chó', 's')]), ('Ca cao', [('Ca cao', 's'), ('Socola sữa', 's'), ('Socola đen', 's')])]),
    ('Gia vị', '#A0482A', 'Acid chlorogenic phân huỷ thành các phenol như 4-vinylguaiacol mùi đinh hương. Rõ hơn ở rang đậm và ở Robusta.', 'tien-chat-huong.html',
     [('Gia vị ấm', [('Quế', 'd'), ('Hồi', 'd'), ('Đinh hương', 'd')]), ('Gia vị cay', [('Tiêu đen', 'd'), ('Gừng', 'd'), ('Hạt mùi', 'd')])]),
    ('Rang, khói', '#5E3A24', 'Chưng cất khô khi rang đậm: mùi rang, khói, gỗ. Vừa đủ thì dễ chịu; quá thì át hết hương gốc của hạt.', 'rang.html',
     [('Ngũ cốc', [('Gạo rang', 's'), ('Mạch nha', 's'), ('Bánh mì nướng', 's')]), ('Rang đậm', [('Cà phê rang', 'd'), ('Khói củi', 'd'), ('Thuốc tẩu', 'd'), ('Gỗ tuyết tùng', 'd')])]),
    ('Thảo mộc', '#A8924A', 'Mùi xanh của rau củ, lá, cỏ. Một chút cho cảm giác tươi; nhiều là dấu hiệu trái xanh hoặc rang chưa tới.', 'trai-chin.html',
     [('Rau củ', [('Đậu Hà Lan', 'e'), ('Dưa leo', 'e'), ('Khoai tây', 'e')]), ('Lá, cỏ', [('Cỏ khô', 'e'), ('Lá chè', 'e'), ('Thảo mộc', 'e')])]),
    ('Mùi lỗi', '#6E5A4A', 'Từ trái hỏng, lên men quá, ẩm mốc khi phơi và cất kho, hạt cũ hoặc rang chưa tới. Một ít hạt lỗi đủ làm hỏng mùi cả mẻ.', 'vi-sinh.html',
     [('Lên men quá', [('Giấm', 't'), ('Rượu nồng', 't'), ('Trái thối', 't'), ('Hành', 't')]), ('Ẩm, mốc', [('Mốc', 't'), ('Đất ẩm', 't'), ('Bao bố', 't')]),
      ('Hoá chất', [('Thuốc', 't'), ('Cao su', 't')]), ('Cũ, sống', [('Giấy, bìa', 't'), ('Ngũ cốc sống', 't'), ('Rơm', 't')])]),
]

ORIG = [
    ('e', 'Enzyme', 'cx2', 'Hình thành khi trái lớn và chín, nằm sẵn trong hạt. Nhẹ, bay nhanh, rõ nhất ở rang sáng.',
     'Khoai tây, đậu Hà Lan, dưa leo, hoa hồng trà, hoa cà phê, chanh, mơ, táo, mật ong'),
    ('s', 'Caramel hoá đường', 'cx1', 'Đường và acid amin phản ứng khi rang, mạnh nhất ở rang vừa: Maillard và caramel hoá.',
     'Vani, bơ, bánh mì nướng, caramel, socola đen, hạnh nhân rang, đậu phộng rang, hạt phỉ rang, óc chó'),
    ('d', 'Chưng cất khô', 'cx4', 'Chất xơ và acid chlorogenic bị đốt nóng lâu, nổi rõ ở rang đậm: gỗ, gia vị, khói.',
     'Tuyết tùng, đinh hương, tiêu, hạt mùi, mạch nha, thuốc tẩu, cà phê rang'),
    ('t', 'Mùi lỗi', 'cx3', 'Không do hạt tốt tạo ra mà do trái hỏng, lên men quá, ẩm mốc, hạt cũ. Mức rang nào cũng có thể gặp.',
     'Mùi đất, rơm, vỏ thịt quả, da thuộc, thịt hầm, khói thuốc, thuốc, cao su'),
]

PRODUCTS = [  # theo mô tả sản phẩm trên trang Chọn mua của MeDili
    ('rc', 'Robusta Classic', 'Đậm đà, đắng rõ, hậu tròn, chocolate đen.', ['Socola đen', 'Ca cao'], 6),
    ('rp', 'Robusta Premium', 'Cân bằng, đường nâu, caramel, hậu ngọt.', ['Đường nâu', 'Caramel'], 4),
    ('ap', 'Arabica Premium', 'Socola, cam chanh, chua nhẹ, đắng vừa, ngọt hậu.', ['Socola sữa', 'Chanh', 'Cam'], 3),
    ('bl', 'Blend', 'Từ đậm cacao đến cân bằng, thơm, chua thanh.', ['Ca cao', 'Chanh'], 4),
]

TRAIN = [
    ('tim', 'Tuần 1: ngửi thật trước', 'Chọn 6 mùi trong bếp: chanh, cam, táo, mật ong, đậu phộng rang, ca cao. Ngửi từng thứ 10 giây, nhắm mắt, đọc tên to. Ghi lại một câu tả cảm giác.'),
    ('ly', 'Tuần 2: ghép với ly cà phê', 'Pha 2 ly khác nhau, ví dụ Robusta Classic và Arabica Premium. Ngửi bột khô, rồi ngửi ly lúc nóng và lúc nguội. Tìm lại 6 mùi tuần 1.'),
    ('banhxe', 'Tuần 3: đi từ trong ra ngoài', 'Mỗi lần nếm, chọn nhóm ở vòng trong trước (ngọt, trái cây, hạt…), rồi mới tìm nhóm giữa và mùi cụ thể. Không chắc thì dừng ở vòng trong.'),
    ('so', 'Tuần 4: ghi phiếu, so sánh', 'Dùng phiếu nếm bên dưới cho mỗi ly. Sau một tháng, so các phiếu để thấy mũi mình nhạy với nhóm nào, còn yếu nhóm nào.'),
]

SRC = [
    ('Coffee Taster’s Flavor Wheel (SCA và World Coffee Research, 2016), giấy phép CC BY-NC-ND 4.0, không cho phép bản sửa đổi; bánh xe trên trang này do MeDili soạn riêng', 'SCA',
     'https://www.sca.coffee/research/coffee-tasters-flavor-wheel'),
    ('Bộ 36 mùi Le Nez du Café xếp mùi theo nhóm như enzymatic, sugar browning; Royal Coffee kể cách dùng bộ mùi để luyện cupping', 'Royal Coffee', 'https://royalcoffee.com/exploring-scent-with-le-nez-du-cafe/'),
    ('Buffo R. A., Cardelli-Freire C. (2004). Coffee flavour: an overview. Flavour and Fragrance Journal 19: 99–104', 'Đại học Oregon',
     'https://pages.uoregon.edu/chendon/coffee_literature/old_literature/2004%20Flav.%20Frag.%20J.,%20An%20overview%20of%20coffee%20flavor.pdf'),
    ('Roasters Guild (2008). Advanced Level Craft Roasting: hương tạo ra nhiều nhất ở rang sáng, rang vừa thì mất nhiều hơn tạo', 'Sweet Maria’s',
     'https://library.sweetmarias.com/wp-content/uploads/2020/08/Advanced-Level-Craft-Roasting.pdf'),
    ('Ba nhóm hương enzyme, caramel hoá đường, chưng cất khô theo mức rang sáng, vừa, đậm', 'The Daily Meal', 'https://www.thedailymeal.com/1512848/three-coffee-aromas-explained'),
]


def page():
    data = json.dumps({'sec': [{'n': n, 'c': c, 'd': d, 'l': l, 'g': [{'n': gn, 'f': [{'n': fn, 'o': fo} for fn, fo in leaves]} for gn, leaves in groups]}
                               for n, c, d, l, groups in SEC],
                       'orig': [{'k': k, 'n': n, 'c': c, 'd': d} for k, n, c, d, _ in ORIG],
                       'prod': [{'k': k, 'n': n, 'd': d, 'f': f, 'lv': lv} for k, n, d, f, lv in PRODUCTS]}, ensure_ascii=False)
    orig = ''.join(f'<div class="box og"><span class="ogh" style="--c:var(--{c})"><i></i>{n}</span><p>{d}</p><p class="ogx"><b>Ví dụ:</b> {x}.</p></div>' for k, n, c, d, x in ORIG)
    train = ''.join(f'<li><span class="n">{icon(i)}</span><h3>{t}</h3><p>{p}</p></li>' for i, t, p in TRAIN)
    body = head('MeDili', 'Bánh xe hương',
                'Chín nhóm hương, ba tầng từ chung đến cụ thể, viết bằng những mùi người Việt quen: mít chín, đường thốt nốt, đậu phộng rang, tiêu Di Linh. '
                'Bấm một ô để xem mùi đó từ đâu ra, chọn mức rang để thấy nhóm nào nổi lên, rồi ghi phiếu nếm của chính chị.')
    body += f'''
<div class="bench bx">
  <div class="card">
    <div class="fighead">
      <div><b>Hình 1</b> <span id="figsub">Bánh xe hương MeDili. Vòng trong là nhóm chung, vòng ngoài là mùi cụ thể.</span></div>
      <button class="btn small" id="clr" type="button">Bỏ chọn</button>
    </div>
    <div class="wheelw"><svg id="wheel" viewBox="0 0 680 680" role="img" aria-label="Bánh xe hương MeDili: chín nhóm hương ở vòng trong, nhóm con ở vòng giữa và mùi cụ thể ở vòng ngoài. Danh sách đầy đủ ở phần Danh sách hương."></svg></div>
    <div id="detail" aria-live="polite"></div>
  </div>

  <aside class="card ctl">
    <div class="head2"><h3>Cà phê MeDili</h3><small>theo mô tả sản phẩm</small></div>
    <div class="row" id="prods"></div>
    <p class="mnote" id="pNote"></p>
    <hr>
    <div class="sl" style="margin-top:0"><label for="iL">Mức rang <output id="oL"></output></label><input id="iL" type="range" min="1" max="8" step="1"><p id="lNote"></p></div>
    <span class="lbl" style="margin-top:12px">Nhóm hương theo nguồn gốc ở mức rang này</span>
    <div class="bars og3" id="obars"></div>
    <p class="mnote">Ô mờ trên bánh xe là mùi ít nổi ở mức rang đang chọn. Mùi lỗi giữ nguyên vì không phụ thuộc mức rang.</p>
    <hr>
    <span class="lbl">Cách đọc</span>
    <ol class="rdl">
      <li>Ngửi, nếm, rồi chọn một nhóm ở <b>vòng trong</b>: ngọt, trái cây, hạt…</li>
      <li>Đi ra <b>vòng giữa</b> nếu thấy rõ hơn: ca cao hay hạt rang?</li>
      <li>Chỉ gọi tên <b>vòng ngoài</b> khi chắc chắn. Không chắc thì dừng ở vòng trong cũng đúng.</li>
      <li><b>Mùi lỗi</b> nằm ở đáy bánh xe. Gặp mùi ở đây thì tìm lại lỗi ở vườn, bồn lên men, sân phơi hoặc kho.</li>
    </ol>
  </aside>
</div>

<section class="p-sec">
  <p class="eye">Bốn nguồn gốc của mùi</p>
  <h2 class="p-h2" style="margin:0">Mùi trong ly <em>đến từ đâu.</em></h2>
  <p class="lead" style="margin:0 0 4px">Giới nếm cà phê hay chia mùi theo lúc nó hình thành. Cách chia này để luyện mũi, không phải hoá học chính xác: một mùi có thể đến từ nhiều đường.</p>
  <div class="g4">{orig}</div>
</section>

<section class="card" id="danh-sach">
  <h2>Danh sách hương</h2>
  <p class="lead">Cùng nội dung với bánh xe, dễ đọc trên điện thoại. Bấm một mùi để xem chi tiết ở Hình 1.</p>
  <div class="flist" id="flist"></div>
</section>

<section class="card" id="phieu">
  <h2>Phiếu nếm MeDili</h2>
  <p class="lead">Bấm “Thêm vào phiếu” ở ô chi tiết để ghi mùi, chỉnh năm thang vị, rồi chép phiếu. Ghi đều mỗi ly, sau một tháng chị sẽ thấy mũi mình nhạy với nhóm nào.</p>
  <div class="cup3">
    <div>
      <span class="lbl">Mùi đã chọn</span><div class="picked" id="picked"></div>
      <div class="sl"><label for="sC">Chua <output id="oC"></output></label><input id="sC" type="range" min="0" max="5" step="1" value="2"></div>
      <div class="sl"><label for="sN">Ngọt <output id="oN"></output></label><input id="sN" type="range" min="0" max="5" step="1" value="3"></div>
      <div class="sl"><label for="sD">Đắng <output id="oD"></output></label><input id="sD" type="range" min="0" max="5" step="1" value="3"></div>
      <div class="sl"><label for="sT">Thân <output id="oT"></output></label><input id="sT" type="range" min="0" max="5" step="1" value="3"></div>
      <div class="sl"><label for="sH">Hậu vị <output id="oH"></output></label><input id="sH" type="range" min="0" max="5" step="1" value="3"></div>
    </div>
    <div class="radw"><svg id="radar" viewBox="0 0 300 280" role="img" aria-label="Biểu đồ năm thang vị: chua, ngọt, đắng, thân, hậu vị"></svg></div>
    <div><pre class="msg" id="sheet"></pre><button class="btn small" id="cpSh" type="button">Sao chép phiếu</button> <span class="cpst" id="cpShS" role="status"></span></div>
  </div>
</section>

<section class="card">
  <h2>Luyện mũi trong bốn tuần</h2>
  <p class="lead">Mũi giỏi lên nhờ ngửi đồ thật và ghi chép đều, không cần bộ mùi đắt tiền để bắt đầu.</p>
  <ol class="pst two">{train}</ol>
</section>

<section class="card src">
  <h2>Nguồn và cách đọc</h2>
  <p class="lead">Bánh xe này do MeDili soạn cho người uống cà phê Việt, không thay cho bánh xe chuẩn quốc tế dùng trong chấm điểm. Gán nguồn gốc cho từng mùi là cách đơn giản hoá để luyện mũi. Mức nổi của ba nhóm theo mức rang là minh hoạ định tính, dùng chung với Cỗ máy Tiền chất hương. Mùi gợi ý cho từng dòng cà phê lấy theo mô tả sản phẩm của MeDili.</p>
  <ul>{srclist(SRC)}</ul>
  <div class="lnks"><a class="lnk" href="phan-biet-ca-phe.html">Cỗ máy Phân biệt cà phê</a><a class="lnk" href="tien-chat-huong.html">Cỗ máy Tiền chất hương</a><a class="lnk" href="vi-sinh.html">Cỗ máy Vi sinh</a><a class="lnk" href="trai-chin.html">Cỗ máy Trái chín</a><a class="lnk" href="rang.html">Phòng rang</a><a class="lnk" href="tim-gu.html">Tìm gu cà phê</a><a class="lnk" href="mua-hang.html">Phòng Chọn Mua</a></div>
</section>
'''
    return doc(FILE, TITLE, DESC, body, css=ISO_CSS + CSS, js=ISO_JS + 'const W=' + data + ';\n' + JS)


CSS = r'''
/* Bánh xe hương MeDili */
@media (min-width:1181px){.bx{grid-template-columns:minmax(0,1fr) 360px}}
.wheelw{max-width:680px;margin:6px auto 0}
#wheel{display:block;width:100%;height:auto}
#wheel path{stroke:#FDFAF2;stroke-width:1.2;cursor:pointer;transition:opacity .2s}
#wheel path:hover{filter:brightness(1.06)}
#wheel path.sel{stroke:#3A2416;stroke-width:2.6}
#wheel path:focus{outline:none}#wheel path:focus-visible{stroke:var(--moss);stroke-width:3}
#wheel text{pointer-events:none;font-family:var(--body)}
#wheel .t1{font:800 15.5px var(--display);letter-spacing:.02em}
#wheel .t1s{font:800 13px var(--display);letter-spacing:.02em}
#wheel .t2{font:600 10.5px var(--body)}
#wheel .t3{font:500 10px var(--body)}
#wheel .hub{fill:var(--panel);stroke:var(--rule)}
#wheel .hubT{font:italic 600 17px var(--sign);fill:var(--accent)}
#wheel .hubS{font:600 9.5px var(--body);fill:var(--muted);letter-spacing:.1em}
#wheel .star{fill:#FFF6EC;stroke:#3A2416;stroke-width:1}
.og .ogh,.og3 .bar span:first-child{display:flex;align-items:center;gap:8px}
.og .ogh{font:800 1.3rem/1.15 var(--display)}
.og .ogh i,.og3 i.dot{display:block;width:13px;height:13px;border-radius:50%;background:var(--c);flex:none}
.og p{margin:6px 0 0;font-size:.92rem}.og .ogx{color:var(--muted);font-size:.86rem}
.og3 .bar{grid-template-columns:150px minmax(0,1fr) 40px}
.rdl{margin:4px 0 0;padding-left:20px;font-size:.88rem}.rdl li{margin-bottom:5px}
.flist{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px 22px}
.fg h3{display:flex;align-items:center;gap:8px;margin:0 0 4px;font:800 1.25rem var(--display)}
.fg h3 i{display:block;width:12px;height:12px;border-radius:3px;background:var(--c)}
.fg h4{margin:8px 0 4px;font:600 .74rem var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.fg .chs{display:flex;flex-wrap:wrap;gap:5px}
.fg button{font:600 .8rem var(--body);border:1px solid var(--rule);background:var(--panel);color:var(--ink);border-radius:999px;padding:4px 10px;cursor:pointer}
.fg button.on{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.fg button.hl{box-shadow:inset 0 0 0 2px var(--accent)}
@media (max-width:1000px){.flist{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.flist{grid-template-columns:minmax(0,1fr)}}
.cup3{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.9fr) minmax(0,1.1fr);gap:18px 26px;align-items:start}
@media (max-width:1000px){.cup3{grid-template-columns:minmax(0,1fr)}}
.picked{display:flex;flex-wrap:wrap;gap:6px;min-height:34px;margin-top:4px}
.picked button{font:600 .82rem var(--body);border-radius:999px;border:1px solid var(--accent);background:var(--tint);color:var(--ink);padding:5px 10px;cursor:pointer}
.picked .em{color:var(--muted);font-size:.86rem}
.radw svg{display:block;width:100%;max-width:340px;height:auto;margin:auto}
#radar text{font:600 12px var(--body);fill:var(--ink)}
#radar .grid{fill:none;stroke:var(--rule);stroke-width:1}
#radar .area{fill:var(--accent);fill-opacity:.25;stroke:var(--accent);stroke-width:2}
#sheet{min-height:200px}
.dact{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
'''

JS = r'''
const CX=340,CY=340,R0=74,R1=150,R2=228,R3=330;
const LV=[null,{n:'Cinnamon',g:'Light'},{n:'New England',g:'Light'},{n:'City',g:'Medium-Light'},{n:'City+',g:'Medium'},{n:'Full City',g:'Medium-Dark'},{n:'Vienna',g:'Dark'},{n:'French',g:'Dark'},{n:'Italian',g:'Very Dark'}];
const AR={e:[.15,.95,1,.85,.6,.4,.25,.15,.08],s:[0,.35,.5,.75,1,.9,.65,.4,.25],d:[0,.05,.08,.15,.3,.5,.75,.95,1],t:[.7,.7,.7,.7,.7,.7,.7,.7,.7]};
const ON={e:'Enzyme',s:'Caramel hoá đường',d:'Chưng cất khô',t:'Mùi lỗi'};
const OC={e:'var(--cx2)',s:'var(--cx1)',d:'var(--cx4)',t:'var(--cx3)'};
const STR={e:'rang sáng',s:'rang vừa',d:'rang đậm',t:'mọi mức rang'};
const st={lv:4,prod:'',sel:null,picked:[]};
const LEAF=[];W.sec.forEach((s,i)=>s.g.forEach((g,j)=>g.f.forEach(f=>LEAF.push({s:i,g:j,n:f.n,o:f.o}))));
const N=LEAF.length,step=360/N;
/* xoay để nhóm Mùi lỗi nằm ở đáy */
const lastS=W.sec.length-1,iFirst=LEAF.findIndex(x=>x.s===lastS),nLast=LEAF.filter(x=>x.s===lastS).length,ROT=180-(iFirst+nLast/2)*step;
const ang=i=>ROT+i*step;
const pol=(r,a)=>{const t=(a-90)*Math.PI/180;return [CX+r*Math.cos(t),CY+r*Math.sin(t)]};
function arc(r0,r1,a0,a1){const [x0,y0]=pol(r1,a0),[x1,y1]=pol(r1,a1),[x2,y2]=pol(r0,a1),[x3,y3]=pol(r0,a0),lg=a1-a0>180?1:0;
 return `M${f1(x0)} ${f1(y0)}A${r1} ${r1} 0 ${lg} 1 ${f1(x1)} ${f1(y1)}L${f1(x2)} ${f1(y2)}A${r0} ${r0} 0 ${lg} 0 ${f1(x3)} ${f1(y3)}Z`}
const hx=h=>[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)),toh=a=>'#'+a.map(v=>Math.round(clamp(v,0,255)).toString(16).padStart(2,'0')).join('');
const tint=(h,t)=>toh(hx(h).map(v=>v+(253-v)*t));
const lum=h=>{const [r,g,b]=hx(h).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*r+.7152*g+.0722*b};
const txc=h=>lum(h)>.32?'#3A2416':'#FFF6EC';
function rtext(r,a,txt,cls,col){const [x,y]=pol(r,a),flip=(((a%360)+360)%360)>180;const rot=flip?a+90:a-90;
 return `<text class="${cls}" x="${f1(x)}" y="${f1(y)}" transform="rotate(${f1(rot)} ${f1(x)} ${f1(y)})" text-anchor="middle" dominant-baseline="central" style="fill:${col}">${txt}</text>`}
function ttext(r,a,txt,cls,col){const [x,y]=pol(r,a),n=(((a%360)+360)%360),flip=n>90&&n<270;const rot=flip?a+180:a;
 return `<text class="${cls}" x="${f1(x)}" y="${f1(y)}" transform="rotate(${f1(rot)} ${f1(x)} ${f1(y)})" text-anchor="middle" dominant-baseline="central" style="fill:${col}">${txt}</text>`}
function build(){let h='';let i=0;
 W.sec.forEach((s,si)=>{const n=s.g.reduce((a,g)=>a+g.f.length,0),a0=ang(i),a1=ang(i+n);
  h+=`<path data-k="s${si}" d="${arc(R0,R1,a0,a1)}" style="fill:${s.c}" tabindex="0" role="button" aria-label="${s.n}"/>`;
  const am=(a0+a1)/2,arcL=(n*step)*Math.PI/180*(R0+R1)/2*.9,tw=t=>t.length*8.4,wd=s.n.split(/,\s*|\s+/);
  if(arcL>=tw(s.n))h+=ttext((R0+R1)/2,am,s.n,'t1',txc(s.c));
  else if(wd.length>1){let l1,l2;if(s.n.includes(',')){const [p,q]=s.n.split(/,\s*/);l1=p+',';l2=q}else{const half=Math.ceil(wd.length/2);l1=wd.slice(0,half).join(' ');l2=wd.slice(half).join(' ')}
   const nn=((am%360)+360)%360,fl=nn>90&&nn<270,rm=(R0+R1)/2;
   if(arcL>=Math.max(tw(l1),tw(l2))){h+=ttext(fl?rm-9:rm+9,am,l1,'t1',txc(s.c))+ttext(fl?rm+9:rm-9,am,l2,'t1',txc(s.c))}else h+=rtext(rm+4,am,s.n,'t1s',txc(s.c))}
  else h+=rtext((R0+R1)/2+4,am,s.n,(R1-R0-8)>=tw(s.n)?'t1':'t1s',txc(s.c));
  let k=i;s.g.forEach((g,gi)=>{const m=g.f.length,b0=ang(k),b1=ang(k+m),c2=tint(s.c,.28);
   h+=`<path data-k="g${si}_${gi}" d="${arc(R1,R2,b0,b1)}" style="fill:${c2}" tabindex="0" role="button" aria-label="${s.n}: ${g.n}"/>`;
   const bm=(b0+b1)/2;h+=rtext((R1+R2)/2,bm,g.n,'t2',txc(c2));
   g.f.forEach((f,fi)=>{const c0=ang(k+fi),c1=ang(k+fi+1),c3=tint(s.c,.55),li=LEAF.findIndex(x=>x.s===si&&x.g===gi&&x.n===f.n);
    h+=`<path data-k="f${li}" class="leaf" d="${arc(R2,R3,c0,c1)}" style="fill:${c3}" tabindex="0" role="button" aria-label="${f.n}, nhóm ${s.n}"/>`;
    h+=rtext((R2+R3)/2,(c0+c1)/2,f.n,'t3','#3A2416')});
   k+=m});
  i+=n});
 h+=`<circle class="hub" cx="${CX}" cy="${CY}" r="${R0-4}"/><text class="hubT" x="${CX}" y="${CY-4}" text-anchor="middle">MeDili</text><text class="hubS" x="${CX}" y="${CY+16}" text-anchor="middle">BÁNH XE HƯƠNG</text><g id="stars"></g>`;
 $('wheel').innerHTML=h;
 $('wheel').querySelectorAll('path').forEach(p=>{const go=()=>pick(p.dataset.k);p.addEventListener('click',go);p.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();go()}})})}
function leafHTML(li){const L=LEAF[li],s=W.sec[L.s],g=s.g[L.g],prods=W.prod.filter(p=>p.f.includes(L.n)).map(p=>p.n);
 return `<div class="dh"><div class="dn" style="background:${s.c};color:${txc(s.c)}">${L.n.slice(0,1)}</div><h2>${L.n}<small>${s.n} · ${g.n}</small></h2></div>
 <div class="dgrid"><div><span class="lbl">Nguồn gốc</span><p><b style="color:${OC[L.o]}">${ON[L.o]}</b>. ${W.orig.find(o=>o.k===L.o).d}</p><span class="lbl">Nhóm ${s.n.toLowerCase()}</span><p>${s.d} <a class="lnk" href="${s.l}">Xem thêm</a></p></div>
 <div><span class="lbl">Thông tin nhanh</span><dl class="kv"><dt>Rõ nhất ở</dt><dd>${STR[L.o]}</dd><dt>Ở ${LV[st.lv].n}</dt><dd>${L.o==='t'?'không phụ thuộc mức rang':vn(AR[L.o][st.lv]*100,0)+' % mức nổi'}</dd><dt>Cà phê MeDili</dt><dd>${prods.length?prods.join(', '):'chưa ghi trong mô tả sản phẩm'}</dd></dl>
 <p style="margin-top:8px"></p><span class="lbl">Ngửi gì để nhớ</span><p>${L.o==='t'?'Đây là mùi cần tránh. Nhớ để nhận ra sớm, tìm lại khâu lỗi: trái, bồn, sân phơi, kho.':`Ngửi ${L.n.toLowerCase()} thật trong 10 giây, nhắm mắt, rồi ngửi ly cà phê ngay sau đó.`}</p>
 <div class="dact"><button class="btn small main" type="button" id="addP">${st.picked.includes(li)?'Bỏ khỏi phiếu':'Thêm vào phiếu'}</button></div></div></div>`}
function pick(k){if(!k)return;st.sel=k;const t=k[0],idx=k.slice(1);let h='';
 if(t==='f')h=leafHTML(+idx);
 else{const [si,gi]=idx.split('_').map(Number),s=W.sec[si],gs=gi==null||isNaN(gi)?s.g:[s.g[gi]];
  h=`<div class="dh"><div class="dn" style="background:${s.c};color:${txc(s.c)}">${si+1}</div><h2>${gi==null||isNaN(gi)?s.n:s.g[gi].n}<small>${gi==null||isNaN(gi)?'Vòng trong · '+s.g.length+' nhóm con':'Vòng giữa · nhóm '+s.n}</small></h2></div>
  <div class="dgrid"><div><span class="lbl">Từ đâu ra</span><p>${s.d} <a class="lnk" href="${s.l}">Xem thêm</a></p></div><div><span class="lbl">Mùi trong nhóm, bấm để xem</span><div class="fg"><div class="chs">${gs.map(g=>g.f.map(f=>{const li=LEAF.findIndex(x=>x.s===si&&x.n===f.n);return `<button type="button" data-li="${li}">${f.n}</button>`}).join('')).join('')}</div></div></div></div>`}
 $('detail').innerHTML=h;
 $('detail').querySelectorAll('[data-li]').forEach(b=>b.onclick=()=>pick('f'+b.dataset.li));
 const ap=$('addP');if(ap)ap.onclick=()=>{const li=+idx;const i=st.picked.indexOf(li);if(i>=0)st.picked.splice(i,1);else if(st.picked.length<8)st.picked.push(li);pick(k);sheet();list()};
 paint();list()}
function paint(){const hl=st.prod?W.prod.find(p=>p.k===st.prod).f:[];
 $('wheel').querySelectorAll('path').forEach(p=>{const k=p.dataset.k;p.classList.toggle('sel',k===st.sel);
  if(k[0]==='f'){const L=LEAF[+k.slice(1)],v=AR[L.o][st.lv];p.style.opacity=f1(.4+.6*v)}});
 let s='';hl.forEach(n=>{const li=LEAF.findIndex(x=>x.n===n);if(li<0)return;const [x,y]=pol(R3+12,ang(li+.5));s+=`<circle class="star" cx="${f1(x)}" cy="${f1(y)}" r="6.5"/><circle cx="${f1(x)}" cy="${f1(y)}" r="3" style="fill:#B33A24"/>`});
 st.picked.forEach(li=>{const [x,y]=pol(R3+12,ang(li+.5));s+=`<circle cx="${f1(x)}" cy="${f1(y)}" r="5" style="fill:#C9962B;stroke:#3A2416;stroke-width:1"/>`});
 $('stars').innerHTML=s}
function list(){const hl=st.prod?W.prod.find(p=>p.k===st.prod).f:[];
 $('flist').innerHTML=W.sec.map((s,si)=>`<div class="fg"><h3><i style="background:${s.c}"></i>${s.n}</h3>${s.g.map(g=>`<h4>${g.n}</h4><div class="chs">${g.f.map(f=>{const li=LEAF.findIndex(x=>x.s===si&&x.n===f.n);return `<button type="button" data-li="${li}" class="${st.sel==='f'+li?'on':''} ${hl.includes(f.n)?'hl':''}">${f.n}</button>`}).join('')}</div>`).join('')}</div>`).join('');
 $('flist').querySelectorAll('[data-li]').forEach(b=>b.onclick=()=>{pick('f'+b.dataset.li);$('wheel').scrollIntoView({behavior:still?'auto':'smooth',block:'center'})})}
function obars(){$('obars').innerHTML=['e','s','d'].map(o=>`<div class="bar"><span><i class="dot" style="--c:${OC[o]}"></i>${ON[o]}</span><div class="track"><i style="width:${f1(AR[o][st.lv]*100)}%;background:${OC[o]}"></i></div><span>${vn(AR[o][st.lv]*100,0)}%</span></div>`).join('')}
const VI=[['sC','Chua'],['sN','Ngọt'],['sD','Đắng'],['sT','Thân'],['sH','Hậu vị']];
function radar(){const v=VI.map(([id])=>+$(id).value),cx=150,cy=140,R=96,pt=(i,r)=>{const a=(-90+i*72)*Math.PI/180;return [cx+r*Math.cos(a),cy+r*Math.sin(a)]};
 let g='';[1,2,3,4,5].forEach(k=>g+=`<polygon class="grid" points="${VI.map((_,i)=>pt(i,R*k/5).map(f1).join(',')).join(' ')}"/>`);
 VI.forEach((_,i)=>{const [x,y]=pt(i,R);g+=`<line x1="${cx}" y1="${cy}" x2="${f1(x)}" y2="${f1(y)}" style="stroke:var(--rule)"/>`});
 g+=`<polygon class="area" points="${v.map((x,i)=>pt(i,R*x/5).map(f1).join(',')).join(' ')}"/>`;
 VI.forEach(([,n],i)=>{const [x,y]=pt(i,R+20);g+=`<text x="${f1(x)}" y="${f1(y+4)}" text-anchor="middle">${n} ${v[i]}</text>`});
 $('radar').innerHTML=g;VI.forEach(([id,n])=>$('o'+id.slice(1)).textContent=$(id).value+'/5')}
function sheet(){const d=new Date(),pd=`${String(d.getDate()).padStart(2,'0')}/${String(d.getMonth()+1).padStart(2,'0')}/${d.getFullYear()}`;
 $('picked').innerHTML=st.picked.length?st.picked.map(li=>`<button type="button" data-li="${li}" title="Bỏ khỏi phiếu">${LEAF[li].n} ✕</button>`).join(''):'<span class="em">Chưa chọn mùi nào. Bấm một ô ở vòng ngoài rồi “Thêm vào phiếu”.</span>';
 $('picked').querySelectorAll('[data-li]').forEach(b=>b.onclick=()=>{st.picked.splice(st.picked.indexOf(+b.dataset.li),1);sheet();paint()});
 const prod=st.prod?W.prod.find(p=>p.k===st.prod).n:'________';
 const t=`PHIẾU NẾM · MeDili
Cà phê: ${prod} · Mức rang: ${LV[st.lv].n} · Ngày: ${pd}
Cách pha: ________ · Tỷ lệ: ________
Mùi: ${st.picked.length?st.picked.map(li=>LEAF[li].n.toLowerCase()).join(', '):'________'}
${VI.map(([id,n])=>`${n} ${$(id).value}/5`).join(' · ')}
Nhóm mạnh nhất: ${st.picked.length?[...new Set(st.picked.map(li=>W.sec[LEAF[li].s].n))].join(', '):'________'}
Mùi lỗi: ${st.picked.some(li=>LEAF[li].o==='t')?'có, kiểm tra lại lô':'không'}
Ghi chú: ______________________________`;
 $('sheet').textContent=t;st.sheet=t;radar()}
function update(){pills('prods',[['','Tất cả']].concat(W.prod.map(p=>[p.k,p.n])),st.prod,k=>{st.prod=k;if(k){st.lv=W.prod.find(p=>p.k===k).lv}update()});
 const P=st.prod?W.prod.find(p=>p.k===st.prod):null;$('pNote').textContent=P?`${P.d} Chấm đỏ trên bánh xe là mùi nêu trong mô tả sản phẩm.`:'Chọn một dòng cà phê để đánh dấu mùi nêu trong mô tả sản phẩm của MeDili.';
 $('iL').value=st.lv;$('oL').textContent=LV[st.lv].n;$('lNote').textContent=`${LV[st.lv].g}. Mức rang dùng chung với Phòng rang và Cỗ máy Tiền chất hương.`;
 obars();paint();list();sheet();if(st.sel)pick(st.sel)}
$('iL').addEventListener('input',()=>{st.lv=+$('iL').value;update()});
VI.forEach(([id])=>$(id).addEventListener('input',sheet));
$('clr').onclick=()=>{st.sel=null;st.picked=[];$('detail').innerHTML=intro();update()};
$('cpSh').onclick=()=>cp(st.sheet,'cpShS');
const intro=()=>`<div class="dh"><div class="dn">?</div><h2>Bấm một ô trên bánh xe<small>hoặc một mùi ở Danh sách hương</small></h2></div><div class="dgrid"><div><p>Vòng trong là chín nhóm hương. Vòng giữa chia nhỏ từng nhóm. Vòng ngoài là mùi cụ thể, gọi bằng những thứ người Việt quen ngửi.</p></div><div><p>Ô càng đậm là mùi càng dễ nổi ở mức rang đang chọn. Nhóm Mùi lỗi nằm ở đáy bánh xe.</p></div></div>`;
build();$('detail').innerHTML=intro();update();
'''
