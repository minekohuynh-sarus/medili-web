# Trang mới từ web Manus, phần 1: Câu chuyện, Đội ngũ, Vùng trồng, HORECA, Xưởng rang, MeDili Café
from kit import *
import ill

# ---------- khối dùng lại ----------
TRIP = [
    ('vuon.html', 'assets/vuon.jpg', '01 · Canh tác', 'Vườn 12 tháng', 'Đất, cây và khí hậu làm nền cho một mùa vụ. Chăm sóc Cà Sẻ theo hướng tự nhiên.'),
    ('trai-ca-phe.html', 'assets/trai-ca-phe.jpg', '02 · Thu hái', 'Cấu tạo trái', 'Chọn trái chín để bắt đầu hành trình hương vị.'),
    ('len-men-men-bia.html', 'assets/men-bia.jpg', '03 · Sơ chế', 'Lên men bằng men bia', 'Làm sạch, sơ chế, phơi khô. Mỗi lô lên men đặc biệt được ghi lại điều kiện riêng.'),
    ('rang.html', 'assets/rang.jpg', '04 · Rang', 'Phòng rang', 'Kiểm tra nhân xanh, xây dựng hồ sơ rang, làm nguội và ổn định hạt.'),
    ('quay-pha.html', 'assets/pha.jpg', '05 · Pha', 'Quầy pha', 'Nước, thời gian và sự tỉ mỉ đánh thức hương vị theo từng cách pha.'),
]


def trip():
    li = ''.join(f'<li><a href="{h}"><img src="{im}" alt="" loading="lazy" width="900" height="600"><b><small>{k}</small>{t}</b><span>{d}</span></a></li>'
                 for h, im, k, t, d in TRIP)
    return f'<ol class="trip">{li}</ol>'


def seg_block(cards=True):
    segs = ''.join(f'<i class="s{i}" style="flex:{v}" title="{n}: {ha(v)} ha">{ha(v)} ha</i>' for i, (n, p, v) in enumerate(AREAS, 1))
    out = f'<div class="seg" role="img" aria-label="Bốn vùng trồng, tổng {ha(TOTAL)} ha: ' + ', '.join(f'{n} {ha(v)} ha' for n, p, v in AREAS) + f'">{segs}</div>'
    if cards:
        out += '<div class="areas">' + ''.join(
            f'<div><b><i class="sw" style="background:var(--seg{i})"></i>{n}</b><span>{p}</span><strong>{ha(v)} ha<small>{round(v / TOTAL * 100)}%</small></strong></div>'
            for i, (n, p, v) in enumerate(AREAS, 1)) + '</div>'
    return out


def cmp_block():
    w = lambda v: f'{v / LINKED * 100:.2f}%'
    return (f'<div class="cmp" role="img" aria-label="Bốn vùng trồng {ha(TOTAL)} ha, diện tích liên kết {LINKED} ha">'
            f'<div><span><b>Bốn vùng trồng</b>MeDili canh tác</span><div class="tr"><i style="width:{w(TOTAL)}"></i><em style="left:calc({w(TOTAL)} + 8px)">{ha(TOTAL)} ha</em></div></div>'
            f'<div><span><b>Liên kết</b>tại Di Linh, tính riêng</span><div class="tr"><i class="b" style="width:{w(LINKED)}"></i><em style="left:calc({w(LINKED)} + 8px)">{LINKED} ha</em></div></div>'
            f'</div><p class="note">Hai thanh dùng chung một thước đo.</p>')


def contact_methods():
    return (f'<div class="g3">'
            f'<div class="box loc"><div class="ttl">{icon("chat")}<h3>Zalo MeDili</h3></div><div class="cp"><strong data-sel>{PHONE}</strong></div>'
            f'<div class="cta" style="margin-top:6px"><a class="btn main" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo</a><button class="btn" type="button" data-copy="{PHONE_RAW}" data-done="Đã sao chép số">Sao chép số</button></div>'
            f'<p class="note">Cách nhanh nhất để hỏi giá, đặt hàng và hẹn ghé.</p></div>'
            f'<div class="box loc"><div class="ttl">{icon("dt")}<h3>Điện thoại</h3></div><div class="cp"><strong data-sel>{PHONE}</strong></div>'
            f'<div class="cta" style="margin-top:6px"><a class="btn" href="tel:+84966770788">Gọi</a><button class="btn" type="button" data-copy="{PHONE_RAW}" data-done="Đã sao chép số">Sao chép số</button></div>'
            f'<p class="note">Nút Gọi chỉ hoạt động trên một số thiết bị. Nếu không mở được, bạn hãy sao chép số rồi gọi.</p></div>'
            f'<div class="box loc"><div class="ttl">{icon("thu")}<h3>Email</h3></div><div class="cp"><strong data-sel>{EMAIL}</strong></div>'
            f'<div class="cta" style="margin-top:6px"><button class="btn" type="button" data-copy="{EMAIL}" data-done="Đã sao chép email">Sao chép email</button></div>'
            f'<p class="note">Phù hợp để gửi hồ sơ, báo giá và yêu cầu chứng từ.</p></div></div>')


def loc_cards(extra_hcm=''):
    return (f'<div class="g2">'
            f'<div class="box loc"><div class="ttl">{icon("ghim")}<div><span class="k">Vườn &amp; xưởng rang</span><h3>Di Linh, Lâm Đồng</h3></div></div>'
            f'<p class="sel">{ADDR_FARM}</p><p class="note">Vùng trồng và xưởng rang. Vui lòng gọi trước khi ghé.</p>'
            f'<div class="lnks"><a class="lnk" href="{MAP_FARM}" target="_blank" rel="noopener">Chỉ đường đến xưởng rang ↗</a></div></div>'
            f'<div class="box loc"><div class="ttl">{icon("ghim")}<div><span class="k">Phân phối · Công ty TNHH DSunfood</span><h3>MeDili ở TP.HCM</h3></div></div>'
            f'<p class="sel">{ADDR_HCM}</p><p class="note">Điểm phân phối tại TP.HCM và MeDili Café.{extra_hcm}</p>'
            f'<div class="lnks"><a class="lnk" href="{MAP_HCM}" target="_blank" rel="noopener">Chỉ đường đến MeDili ↗</a><a class="lnk" href="quan-medili.html">Ghé MeDili Café</a></div></div></div>')


def head(eye, h1, lead, cta='', sig=''):
    return (f'<header class="p-head">{logo()}<p class="eye">{eye}</p><h1>{h1}</h1><p class="lead">{lead}</p>'
            + (f'<p class="p-sig">{sig}</p>' if sig else '') + (f'<div class="cta">{cta}</div>' if cta else '') + '</header>')


# ---------- Câu chuyện ----------
def cau_chuyen():
    body = head('Câu chuyện MeDili', 'Mê cà phê, <em>mê Cà Sẻ Di Linh.</em>',
                'MeDili là nhà rang cà phê trên cao nguyên Di Linh, Lâm Đồng. Vùng trồng canh tác từ năm 2010, xưởng rang đặt tại Thôn 11, xã Di Linh. Trung tâm của câu chuyện là Cà Sẻ, dòng Robusta đặc trưng của vùng Di Linh.',
                '<a class="btn main" href="vung-trong.html">Xem vùng trồng</a><a class="btn" href="doi-ngu.html">Gặp đội ngũ</a>',
                'Gìn giữ di sản. Chắt chiu từng hương vị.')
    body += f'''
<section class="facts" aria-label="MeDili qua các con số">
 <div><b>2010</b><span>năm vùng trồng bắt đầu canh tác</span></div>
 <div><b>{ha(TOTAL)} ha</b><span>bốn vùng trồng ở Lâm Đồng</span></div>
 <div><b>{LINKED} ha</b><span>diện tích liên kết tại Di Linh, tính riêng</span></div>
 <div><b>60 tấn</b><span>công suất rang tối đa mỗi tháng</span></div>
</section>

<section class="split">
 <div class="p-sec">
  <p class="eye">01 · Một di sản vùng miền</p>
  <h2 class="p-h2">Cà Sẻ, <em>gốc của niềm mê.</em></h2>
  <p>Cà Sẻ là dòng Robusta đặc trưng của vùng Di Linh. Những cây Cà Sẻ lâu năm cho ly cà phê ngon, giàu caffeine. MeDili chọn Cà Sẻ làm nền tảng của thương hiệu.</p>
  <p>Nhiều người kể rằng cây cà phê có mặt trên cao nguyên Di Linh từ thời Pháp. MeDili vẫn đang tìm thêm tư liệu về thời điểm, nguồn giống và con đường cây đến vùng đất này, nên trang này chưa ghi mốc năm cụ thể.</p>
  <p>Điều MeDili ghi nhận được là vườn của chính mình: canh tác từ năm 2010, cây 15 năm tuổi, chăm sóc theo hướng tự nhiên, kết hợp phân hữu cơ và giảm hóa chất.</p>
 </div>
 {photo('p-robusta-canh.jpg', 'Cành Robusta trĩu trái chín đỏ', 'Cà Sẻ chín đỏ trên cành.', cls='pv')}
</section>

<section class="p-sec">
 <blockquote class="quote" style="margin:10px 0">Cà Sẻ Di Linh. Nguồn gốc là nền tảng của mỗi mẻ rang.</blockquote>
</section>

<section class="split">
 {photo('p-may-rang-dung.jpg', 'Hạt cà phê vừa rang đảo trên khay làm nguội', 'Hạt vừa ra lò, đảo trên khay làm nguội.', cls='pv')}
 <div class="p-sec">
  <p class="eye">02 · Nhà rang cà phê chuyên nghiệp</p>
  <h2 class="p-h2">Hiểu nguyên liệu, <em>rồi mới rang.</em></h2>
  <p>MeDili rang tại xưởng ở Thôn 11, sát vùng trồng. Mỗi mẻ rang bắt đầu từ những câu hỏi về hạt: từ vườn nào, sơ chế ra sao, sẽ pha bằng phin, máy hay cold brew. Từ đó, đội rang xây dựng hồ sơ rang cho từng dòng.</p>
  <p>Xưởng rang trung bình 20 tấn mỗi tháng, tối đa 60 tấn, đóng gói bằng máy bán tự động. Khách của MeDili là gia đình, quán cà phê, nhà hàng và khách sạn.</p>
  <div class="lnks"><a class="lnk" href="xuong-rang.html">Xưởng rang &amp; năng lực</a><a class="lnk" href="horeca.html">Giải pháp HORECA</a></div>
 </div>
</section>

<section class="p-sec">
 <p class="eye">03 · Bắt đầu bằng sự chú ý</p>
 <h2 class="p-h2">Một hành trình <em>trong từng tách cà phê.</em></h2>
 <p class="lead">Hương vị hình thành qua năm công đoạn. Mỗi công đoạn có một mô hình để bạn tự bấm, chỉnh thông số và xem cách làm.</p>
 {trip()}
 <p class="note">Lô lên men cùng trái cây có trang riêng: <a class="lnk" href="len-men-trai-cay.html">Lên men cùng trái cây</a>.</p>
</section>

<section class="box split">
 <div class="p-sec">
  <p class="eye">04 · Từ Di Linh đến thành phố</p>
  <h2 class="p-h2" style="margin:0">Điểm hẹn <em>ở 143 Phạm Văn Hai.</em></h2>
  <p>Công ty TNHH DSunfood tại 143 Phạm Văn Hai, Tân Bình, là nhà phân phối của MeDili ở TP.HCM, đồng thời là MeDili Café. Bạn có thể ghé uống một ly, hỏi thực đơn trong ngày hoặc trao đổi về việc cung cấp cà phê cho quán.</p>
  <div class="cta"><a class="btn main" href="quan-medili.html">Ghé MeDili Café</a><a class="btn" href="lien-he.html">Liên hệ &amp; bản đồ</a></div>
 </div>
 <div class="illw">{ill.suada()}</div>
</section>
'''
    return doc('cau-chuyen.html', 'Câu chuyện MeDili',
               'Câu chuyện MeDili: Cà Sẻ Di Linh, vùng trồng canh tác từ 2010, xưởng rang ở Thôn 11 và hành trình năm công đoạn từ vườn đến tách.',
               body, wrap_cls='wrap pg')


# ---------- Đội ngũ ----------
def doi_ngu():
    body = head('Đội ngũ MeDili · Hai cách chú ý đến hương vị', 'Con người <em>đứng sau hương vị.</em>',
                'Ở MeDili, người rang và người pha cùng làm một việc: đưa vị của hạt vào ly. Trang này giới thiệu hai vai trò đó. Hồ sơ từng người sẽ được bổ sung khi MeDili xác nhận thông tin.')
    body += f'''
<section class="split">
 <div class="p-sec">
  <h2 class="p-h2">Những người <em>giữ lửa cho hương vị.</em></h2>
  <p class="lead">Rang và pha là hai nửa của cùng một ly. MeDili nối hai nửa đó bằng hồ sơ rang: đội rang biết hạt sẽ được pha thế nào, barista biết hạt đã được rang ra sao.</p>
 </div>
 {photo('p-tay-hai-doc.jpg', 'Bàn tay hái từng trái cà phê chín trên cành', 'Hương vị bắt đầu từ bàn tay hái.', cls='pv')}
</section>

<section class="p-sec">
 <div class="g2">
  <article class="box">
   <img src="assets/p-may-rang.jpg" alt="Hạt cà phê vừa rang trên khay làm nguội" width="1200" height="800" loading="lazy" style="display:block;width:100%;height:auto;border-radius:12px;margin-bottom:12px">
   <span class="k">01 · Hiểu nguyên liệu</span>
   <h3>Đội ngũ rang xay</h3>
   <p>Công việc bắt đầu từ nhân xanh: hạt từ vùng trồng nào, tình trạng hạt ra sao, sẽ được pha bằng gì. Đội rang điều chỉnh hồ sơ rang để kết nối ba yếu tố: nguyên liệu, nhiệt và vị trong ly.</p>
   <div class="chips"><span>Nguyên liệu</span><span>Hồ sơ rang</span><span>Hương vị</span></div>
   <div class="lnks"><a class="lnk" href="xuong-rang.html">Xưởng rang &amp; năng lực</a><a class="lnk" href="rang.html">Thử phòng rang</a></div>
  </article>
  <article class="box">
   <img src="assets/p-hat-rang.jpg" alt="Hạt cà phê rang trong phễu máy xay" width="1200" height="800" loading="lazy" style="display:block;width:100%;height:auto;border-radius:12px;margin-bottom:12px">
   <span class="k">02 · Pha trọn vị trong tách</span>
   <h3>Nghệ nhân barista</h3>
   <p>Barista đưa hồ sơ rang vào việc phục vụ hằng ngày: ly phin, shot espresso và gu của từng khách. Mỗi lần pha là một cuộc trao đổi giữa cà phê, nước, dụng cụ và khẩu vị.</p>
   <div class="chips"><span>Phin</span><span>Espresso</span><span>Gu khách hàng</span></div>
   <div class="lnks"><a class="lnk" href="quay-pha.html">Vào quầy pha</a><a class="lnk" href="tim-gu.html">Tìm gu cà phê</a></div>
  </article>
 </div>
</section>

<section class="box p-sec">
 <p class="eye">Trao đổi theo nhu cầu</p>
 <h2 class="p-h2" style="margin:0">Cùng chọn hướng rang <em>và cách pha phù hợp.</em></h2>
 <p>Cho MeDili biết bạn dùng loại cà phê nào, phục vụ ra sao và muốn ly cà phê có vị ra sao. Đội rang và barista sẽ cùng gợi ý.</p>
 <div class="cta"><a class="btn main" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo MeDili</a><a class="btn" href="lien-he.html">Mở trang liên hệ</a></div>
 <p class="note">Zalo và điện thoại: <span class="sel">{PHONE}</span> · Email: <span class="sel">{EMAIL}</span></p>
</section>
'''
    return doc('doi-ngu.html', 'Đội ngũ MeDili',
               'Hai vai trò đứng sau hương vị MeDili: đội ngũ rang xay hiểu nguyên liệu và xây dựng hồ sơ rang, nghệ nhân barista đánh thức hương vị trong từng ly.',
               body, wrap_cls='wrap pg')


# ---------- Vùng trồng ----------
def vung_trong():
    body = head('Vùng đất Di Linh', 'Di Linh. <em>Nơi câu chuyện bắt đầu.</em>',
                f'Nguyên liệu của MeDili đến từ bốn vùng trồng ở Lâm Đồng với tổng diện tích {ha(TOTAL)} ha, cùng {LINKED} ha liên kết tại Di Linh. Hai con số được tính riêng: {LINKED} ha liên kết không gộp vào {ha(TOTAL)} ha.',
                f'<a class="btn main" href="{MAP_FARM}" target="_blank" rel="noopener">Chỉ đường đến xưởng rang ↗</a><a class="btn" href="vuon.html">Vườn 12 tháng</a>')
    body += photo('p-san-phoi-wide.jpg', 'Cà phê phơi trên sân giữa đồi', 'Phơi cà phê giữa đồi.', cls='pfw', lazy=False)
    body += f'''
<section class="facts" aria-label="Vùng trồng qua các con số">
 <div><b>{ha(TOTAL)} ha</b><span>tổng bốn vùng trồng</span></div>
 <div><b>{LINKED} ha</b><span>liên kết tại Di Linh, tính riêng</span></div>
 <div><b>2010</b><span>năm bắt đầu canh tác</span></div>
 <div><b>15 năm</b><span>tuổi cây trong vườn</span></div>
</section>

<section class="pgal" aria-label="Vào mùa">
 <h2 class="p-h2" style="margin:0">Vào mùa <em>ở vườn MeDili.</em></h2>
 <p>Ảnh mùa thu hoạch 2026: trái chín trên cành, bao cà phê lên máy cày rời vườn.</p>
 {strip(STRIP_MUAVU)}
 <div class="lnks" style="margin-top:0"><a class="lnk" href="anh-vuon.html">Xem toàn bộ ảnh vườn</a></div>
</section>

<section class="box p-sec">
 <p class="eye">Bốn vùng trồng, một câu chuyện rõ ràng</p>
 <h2 class="p-h2" style="margin:0">{ha(TOTAL)} ha <em>chia theo vùng.</em></h2>
 <p class="note">Mỗi khối có kích thước tỷ lệ với diện tích vùng.</p>
 {seg_block()}
</section>

<section class="box p-sec">
 <p class="eye">Hai con số, tính riêng</p>
 <h2 class="p-h2" style="margin:0">Vùng trồng <em>và vùng liên kết.</em></h2>
 <p>{LINKED} ha là diện tích của các vườn liên kết ở Di Linh. Con số này không cộng vào {ha(TOTAL)} ha và không gộp thành tổng diện tích của MeDili.</p>
 {cmp_block()}
</section>

<div class="g2">
 <section class="box p-sec">
  {photo('p-robusta-chum.jpg', 'Cành Robusta chín dày trái')}
  <p class="eye">Cà Sẻ Di Linh</p>
  <h3>Dòng Robusta MeDili chú trọng nhất</h3>
  <p>Cà Sẻ là dòng Robusta đặc trưng của vùng Di Linh. Vườn được chăm sóc theo hướng tự nhiên, kết hợp phân hữu cơ, giảm hóa chất và tối ưu chi phí. Cây trong vườn đã 15 năm tuổi.</p>
  <p>Catimor và Culi là hai dòng cà phê trải nghiệm, trồng ở Cầu Đất, Lâm Đồng.</p>
 </section>
 <section class="box p-sec">
  <p class="eye">Xưởng rang cạnh vùng trồng</p>
  <h3>Thôn 11, Xã Di Linh</h3>
  <p>Cà phê được sơ chế và rang gần nơi trồng. Xưởng rang trung bình 20 tấn mỗi tháng, tối đa 60 tấn.</p>
  <p class="note">Gọi trước khi ghé: <span class="sel">{PHONE}</span></p>
  <div class="lnks"><a class="lnk" href="{MAP_FARM}" target="_blank" rel="noopener">Chỉ đường đến xưởng rang ↗</a><a class="lnk" href="xuong-rang.html">Xưởng rang &amp; năng lực</a></div>
 </section>
</div>

<section class="p-sec">
 <h2 class="p-h2">Đọc thêm <em>về vùng trồng.</em></h2>
 <div class="g2">
  <a class="box" href="vuon.html" style="text-decoration:none;color:inherit"><img src="assets/vuon.jpg" alt="" width="900" height="607" loading="lazy" style="display:block;width:100%;height:auto;border-radius:12px;margin-bottom:10px"><span class="k">Mô hình tương tác</span><h3>Vườn 12 tháng</h3><p>Lịch chăm sóc vườn Robusta qua từng tháng, từ bón phân đến thu hái. Số liệu trong mô hình là hướng dẫn, cần đối chiếu với điều kiện từng vườn.</p></a>
  <a class="box" href="journal-di-linh.html" style="text-decoration:none;color:inherit"><div style="background:var(--tint);border-radius:12px;margin-bottom:10px">{ill.dilinh()}</div><span class="k">Kiến thức cà phê · Vùng đất</span><h3>Di Linh trong một tách cà phê</h3><p>Đọc một vùng đất bằng sự khiêm nhường: khí hậu, độ cao và ký ức vị giác.</p></a>
 </div>
</section>
'''
    return doc('vung-trong.html', 'Vùng trồng Di Linh',
               f'Bốn vùng trồng của MeDili ở Lâm Đồng: Tà Hine, Tân Nghĩa, Lộc Châu 3, Gia Bắc 2, tổng diện tích {ha(TOTAL)} ha, cùng {LINKED} ha liên kết tại Di Linh.',
               body, wrap_cls='wrap pg')


# ---------- HORECA ----------
HORECA_JS = r'''
(()=>{const f=document.getElementById('hq');if(!f)return;const $=id=>document.getElementById(id);
const val=n=>{const c=f.querySelectorAll('[name="'+n+'"]:checked');return [...c].map(x=>x.value)};
function build(){const lines=['YÊU CẦU HORECA'];const m=$('hq-m').value;lines.push('Mô hình: '+m);
const need=val('need');lines.push('Cần: '+(need.length?need.join(', '):'chưa chọn'));lines.push('Lượng dự kiến: '+$('hq-v').value);
const a=$('hq-a').value.trim();if(a)lines.push('Khu vực giao: '+a);const nt=$('hq-n').value.trim();if(nt)lines.push('Ghi chú: '+nt);
const nm=$('hq-name').value.trim(),ph=$('hq-ph').value.replace(/[\s.()-]/g,'');if(nm)lines.push('Liên hệ: '+nm+(ph?' | '+ph:''));
return {txt:lines.join('\n'),nm,ph}}
function sync(){const r=build();$('hq-msg').textContent=r.txt;const ok=r.nm&&/^(0\d{9,10}|\+\d{8,15})$/.test(r.ph),g=$('hq-gf');
if(ok){const q=encodeURIComponent;g.href=FORM+'&'+FN.name+'='+q(r.nm)+'&'+FN.phone+'='+q(r.ph)+'&'+FN.txt+'='+q(r.txt);g.removeAttribute('aria-disabled');g.classList.remove('off')}
else{g.removeAttribute('href');g.setAttribute('aria-disabled','true');g.classList.add('off')}}
f.addEventListener('input',sync);f.addEventListener('change',sync);f.addEventListener('submit',e=>e.preventDefault());
$('hq-gf').addEventListener('click',e=>{if(!$('hq-gf').getAttribute('href')){e.preventDefault();$('hq-st').textContent='Vui lòng nhập đúng tên và số điện thoại để mở phiếu gửi MeDili.';($('hq-name').value.trim()?$('hq-ph'):$('hq-name')).focus()}else $('hq-st').textContent='Phiếu đã mở ở thẻ mới. Bấm Gửi ở cuối phiếu để hoàn tất.'});
$('hq-cp').addEventListener('click',async()=>{const t=$('hq-msg').textContent;try{await navigator.clipboard.writeText(t);$('hq-st').textContent='Đã sao chép tin nhắn. Mở Zalo MeDili rồi dán vào.'}catch(e){const r=document.createRange();r.selectNodeContents($('hq-msg'));const s=getSelection();s.removeAllRanges();s.addRange(r);$('hq-st').textContent='Đã chọn sẵn tin nhắn, bạn hãy sao chép rồi dán vào Zalo.'}});
sync();
})();
'''


def horeca(P):
    pp = lambda i: fm(P[i]['p'][0] * 1000)
    blends = [P[k]['p'][0] for k in ('b91', 'b82', 'b73', 'b55')]
    body = head('Giải pháp cà phê · HORECA', 'Cà phê cho <em>quán, nhà hàng, khách sạn.</em>',
                'MeDili là nhà rang cà phê chuyên nghiệp ở Di Linh, kết nối vùng trồng Cà Sẻ với nhu cầu vận hành hằng ngày của quầy pha: nguyên liệu ổn định, hồ sơ rang theo cách pha, quy cách đóng gói rõ ràng.',
                '<a class="btn main" href="#bao-gia">Gửi nhu cầu</a><a class="btn" href="mua-hang.html">Xem bảng giá</a>')
    body += photo('p-kho-wide.jpg', 'Xe xúc đổ cà phê trong kho, bụi vàng dưới ánh đèn', 'Mùa vụ trong kho cà phê.', cls='pfw', lazy=False)
    body += f'''
<section class="p-sec">
 <p class="eye">Năng lực rang &amp; cung ứng</p>
 <h2 class="p-h2">Đủ rõ <em>để bắt đầu.</em></h2>
 <div class="facts">
  <div><b>20 tấn</b><span>sản lượng trung bình mỗi tháng</span></div>
  <div><b>60 tấn</b><span>công suất tối đa mỗi tháng</span></div>
  <div><b>2010</b><span>năm bắt đầu canh tác</span></div>
  <div><b>{ha(TOTAL)} + {LINKED} ha</b><span>vùng trồng và vùng liên kết</span></div>
 </div>
 <p class="note">Đóng gói bằng máy bán tự động. Quy cách được xác nhận khi trao đổi với từng đối tác.</p>
</section>

<section class="box split">
 <div class="p-sec">
  <p class="eye">Nguồn gốc rõ ràng</p>
  <h2 class="p-h2" style="margin:0">Cà Sẻ <em>Di Linh.</em></h2>
  <p>Bốn vùng trồng Gia Bắc 2, Lộc Châu 3, Tân Nghĩa và Tà Hine, tổng diện tích {ha(TOTAL)} ha, cùng {LINKED} ha liên kết tại Di Linh. Vùng trồng canh tác từ năm 2010.</p>
  <div class="lnks"><a class="lnk" href="vung-trong.html">Xem bốn vùng trồng</a></div>
 </div>
 <div>{seg_block(cards=False)}<p class="note">Di Linh · Lâm Đồng · Việt Nam</p></div>
</section>

<section class="p-sec">
 <p class="eye">Bốn hướng cung cấp</p>
 <h2 class="p-h2">Một nền tảng, <em>nhiều cách phục vụ.</em></h2>
 <div class="g4">
  <div class="box">{icon('nhan')}<span class="k">Trao đổi theo nhu cầu</span><h3>Cà phê nhân xanh</h3><p>Nguyên liệu cho nhà rang. Trao đổi theo vùng trồng, mùa vụ và lô cung cấp.</p>
   <div class="ft">Liên hệ để nhận báo giá mỗi ngày. <a class="lnk" href="nhan-xanh.html">Chọn gu nhân xanh</a></div></div>
  <div class="box">{icon('phin')}<span class="k">Trao đổi theo nhu cầu</span><h3>Cà phê phin</h3><p>Nguyên hạt hoặc xay sẵn, quy cách được xác nhận theo đơn.</p>
   <div class="ft">Phin Robusta Classic từ <b>{pp('pc')} đ/kg</b>, Arabica Premium {pp('pa')} đ/kg.</div></div>
  <div class="box">{icon('may')}<span class="k">Trao đổi theo nhu cầu</span><h3>Cà phê pha máy</h3><p>Chọn nguyên liệu và hồ sơ rang theo máy pha và thực đơn của quán.</p>
   <div class="ft">Máy Robusta Classic từ <b>{pp('mc')} đ/kg</b>. Blend 9:1 đến 5:5 từ {fm(min(blends) * 1000)} đến {fm(max(blends) * 1000)} đ/kg.</div></div>
  <div class="box">{icon('lanh')}<span class="k">Trao đổi theo nhu cầu</span><h3>Cold brew</h3><p>Thống nhất hương vị, độ xay và quy cách cho mẻ ủ lạnh.</p>
   <div class="ft">Phin Robusta Premium phù hợp với cold brew, từ <b>{pp('pp')} đ/kg</b>.</div></div>
 </div>
 <p class="note">Giá bán lẻ dưới 5 kg, chưa gồm 8% VAT và phí vận chuyển. Giá sỉ theo tổng khối lượng mua trong tháng, xem ở <a class="lnk" href="mua-hang.html">Phòng chọn mua</a>.</p>
</section>

<section class="box p-sec">
 <p class="eye">Quán nên chọn gì</p>
 <h2 class="p-h2" style="margin:0">Mốc gợi ý <em>theo quy mô.</em></h2>
 <p class="note">MeDili sẽ cùng quán chốt lại sau khi thử mẫu.</p>
 <div class="tw"><table class="rich"><thead><tr><th>Quy mô</th><th>Ly mỗi ngày</th><th>Pha phin</th><th>Pha máy</th></tr></thead><tbody>
  <tr><td><b>Nhỏ</b><br><small>xe đẩy, kiosk, quán vỉa hè</small></td><td>30–80</td><td>Phin Robusta Classic</td><td>Máy Robusta Classic hoặc Blend 9:1</td></tr>
  <tr><td><b>Vừa</b><br><small>quán có chỗ ngồi</small></td><td>80–200</td><td>Phin Robusta Premium</td><td>Blend 8:2 hoặc 7:3</td></tr>
  <tr><td><b>Lớn</b><br><small>chuỗi cửa hàng, khách sạn, nhà hàng</small></td><td>Trên 200</td><td>Phin Arabica Premium</td><td>Blend 5:5, Arabica Premium hoặc Robusta Specialty</td></tr>
 </tbody></table></div>
 <div class="lnks"><a class="lnk" href="mua-hang.html">Tính lượng dùng và giá mỗi ly</a><a class="lnk" href="dong-hanh-cung-quan.html">Chọn theo ưu tiên của quán</a></div>
</section>

<section class="p-sec">
 <p class="eye">Cách bắt đầu</p>
 <h2 class="p-h2">Một cuộc trao đổi <em>đủ rõ.</em></h2>
 <ol class="pst three">
  <li><span class="n">{icon('gu')}</span><h3><small>Bước 1</small>Chọn hướng</h3><p>Bạn cần nhân xanh, cà phê phin, cà phê pha máy hay cold brew? Nếu mua nhân xanh, hãy trả lời <a class="lnk" href="nhan-xanh.html">bảng câu hỏi chọn nhân</a>.</p></li>
  <li><span class="n">{icon('ly')}</span><h3><small>Bước 2</small>Căn chỉnh</h3><p>Thử mẫu, rồi thống nhất hương vị, độ xay và cách phục vụ.</p></li>
  <li><span class="n">{icon('so')}</span><h3><small>Bước 3</small>Xác nhận</h3><p>Chốt quy cách cung cấp, bậc giá theo khối lượng tháng và hồ sơ đối tác cần nhận.</p></li>
 </ol>
</section>

<section class="box split" id="ho-so">
 <div class="p-sec">
  <p class="eye">Điều kiện sản xuất · An toàn thực phẩm</p>
  <h2 class="p-h2" style="margin:0">Hồ sơ <em>cho đối tác.</em></h2>
  <p>MeDili gửi hồ sơ khi trao đổi, ghi rõ cơ quan cấp, phạm vi và thời hạn. Website chưa đăng bản chụp hay số hiệu giấy chứng nhận.</p>
  <div class="cta"><a class="btn main" href="{ZALO}" target="_blank" rel="noopener">Xin hồ sơ qua Zalo</a><button class="btn" type="button" data-copy="{EMAIL}" data-done="Đã sao chép email">Sao chép email</button></div>
 </div>
 <ul class="pst" style="align-self:start">
  <li><span class="n">{icon('khien')}</span><h3>Chứng nhận đủ điều kiện sản xuất</h3><p>Của nhà máy và xưởng rang.</p></li>
  <li><span class="n">{icon('khien')}</span><h3>Chứng nhận cơ sở đủ điều kiện an toàn thực phẩm</h3><p>Áp dụng cho sản phẩm cà phê cung cấp.</p></li>
 </ul>
</section>

<section class="box p-sec" id="bao-gia">
 <p class="eye">Liên hệ báo giá</p>
 <h2 class="p-h2" style="margin:0">Bắt đầu <em>một báo giá phù hợp.</em></h2>
 <p class="note">Trang không tự gửi tin. Bạn mở phiếu để gửi cho MeDili, hoặc sao chép tin nhắn rồi dán vào Zalo.</p>
 <form class="p-form" id="hq" novalidate>
  <div class="row2">
   <label for="hq-m">Mô hình kinh doanh<select id="hq-m"><option>Quán cà phê</option><option>Nhà hàng</option><option>Khách sạn</option><option>Chuỗi cửa hàng</option><option>Nhà rang</option><option>Văn phòng</option><option>Khác</option></select></label>
   <label for="hq-v">Lượng dự kiến mỗi tháng<select id="hq-v"><option>Dưới 5 kg</option><option selected>5–20 kg</option><option>20–100 kg</option><option>Trên 100 kg</option><option>Theo tấn (nhân xanh)</option></select></label>
  </div>
  <fieldset><legend>Cần loại nào</legend><div class="opts">
   <label><input type="checkbox" name="need" value="Nhân xanh" id="hq-c1">Nhân xanh</label>
   <label><input type="checkbox" name="need" value="Cà phê phin" id="hq-c2" checked>Cà phê phin</label>
   <label><input type="checkbox" name="need" value="Cà phê pha máy" id="hq-c3">Pha máy</label>
   <label><input type="checkbox" name="need" value="Cold brew" id="hq-c4">Cold brew</label>
  </div></fieldset>
  <div class="row2">
   <label for="hq-name">Tên quán hoặc người liên hệ<input id="hq-name" autocomplete="name" maxlength="80" placeholder="Ví dụ: Quán Mộc, chị Lan"></label>
   <label for="hq-ph">Số điện thoại hoặc Zalo<input id="hq-ph" type="tel" inputmode="tel" autocomplete="tel" maxlength="20" placeholder="0901234567"></label>
  </div>
  <div class="row2">
   <label for="hq-a">Khu vực giao hàng <small>không bắt buộc</small><input id="hq-a" maxlength="80" placeholder="Ví dụ: Quận 3, TP.HCM"></label>
   <label for="hq-n">Ghi chú <small>không bắt buộc</small><input id="hq-n" maxlength="200" placeholder="Máy pha đang dùng, món bán chạy…"></label>
  </div>
  <div><span class="k">Tin nhắn sẽ gửi</span><pre class="msg" id="hq-msg"></pre></div>
  <div class="cta" style="margin-top:0"><a class="btn main off" id="hq-gf" target="_blank" rel="noopener" aria-disabled="true">Mở phiếu gửi MeDili</a><button class="btn" type="button" id="hq-cp">Sao chép tin nhắn</button><a class="btn" href="{ZALO}" target="_blank" rel="noopener">Mở Zalo MeDili</a></div>
  <p class="fstat" id="hq-st" role="status"></p>
 </form>
</section>

<section class="p-sec">
 <h2 class="p-h2">Hai điểm <em>kết nối.</em></h2>
 {loc_cards()}
</section>
'''
    css = '.btn.off{opacity:.55;cursor:not-allowed}'
    js = f"const FORM={FORM!r},FN={{name:{FORM_F['name']!r},phone:{FORM_F['phone']!r},txt:{FORM_F['txt']!r}}};" + HORECA_JS
    return doc('horeca.html', 'Giải pháp HORECA MeDili',
               'Cà phê MeDili cho quán, nhà hàng, khách sạn: nhân xanh, cà phê phin, pha máy, cold brew. Năng lực 20 tấn mỗi tháng, tối đa 60 tấn, hồ sơ đối tác và báo giá.',
               body, css=css, js=js, wrap_cls='wrap pg')


# ---------- Xưởng rang ----------
def xuong_rang():
    body = head('Xưởng rang &amp; năng lực · Thôn 11, Xã Di Linh', 'Sáu chặng cho <em>một mẻ rang có chủ đích.</em>',
                'Xưởng rang của MeDili đặt cạnh vùng trồng. Mỗi mẻ đi qua sáu chặng, từ kiểm tra nhân xanh đến đóng gói và đối chiếu lô.',
                '<a class="btn main" href="rang.html">Mở phòng rang tương tác</a><a class="btn" href="horeca.html#ho-so">Hồ sơ sản xuất &amp; ATTP</a>')
    steps = [('kinh', 'Kiểm tra nhân xanh', 'Đối chiếu nguồn gốc, cách sơ chế, loại lỗi và tạp chất trước khi rang.'),
             ('so', 'Chuẩn bị mẻ rang', 'Lập hồ sơ rang theo nguyên liệu, thiết bị và cỡ mẻ, rồi theo dõi mẻ rang thực tế.'),
             ('lua', 'Làm khô và chuyển nâu', 'Hạt mất nước, hương hình thành qua phản ứng Maillard. Nhiệt được giữ trong ngưỡng phù hợp để hạt không cháy, không ám khói.'),
             ('no', 'Phát triển hương vị', 'Theo dõi tiếng nổ đầu, chọn điểm dừng để cân bằng hương, độ chua và thân vị.'),
             ('quat', 'Làm nguội và nghỉ hạt', 'Làm nguội nhanh để dừng mẻ rang. Trong những ngày sau, hạt tiếp tục thoát CO₂.'),
             ('tui', 'Đóng gói và đối chiếu lô', 'Đóng gói bằng máy bán tự động theo quy cách đã thống nhất với đối tác. Hồ sơ lô đi kèm sản phẩm.')]
    li = ''.join(f'<li><span class="n">{icon(i)}</span><h3><small>Chặng {k}</small>{t}</h3><p>{d}</p></li>' for k, (i, t, d) in enumerate(steps, 1))
    body += f'''
<section class="facts" aria-label="Năng lực xưởng rang">
 <div><b>20 tấn</b><span>sản lượng trung bình mỗi tháng</span></div>
 <div><b>60 tấn</b><span>công suất tối đa mỗi tháng</span></div>
 <div><b>Bán tự động</b><span>dây chuyền đóng gói</span></div>
 <div><b>Thôn 11</b><span>Xã Di Linh, sát vùng trồng</span></div>
</section>

<div class="g2">{photo('p-may-rang.jpg', 'Hạt cà phê vừa rang trên khay làm nguội', 'Hạt vừa ra lò trên khay làm nguội.')}{photo('p-hat-rang.jpg', 'Hạt cà phê rang trong phễu máy xay', 'Hạt rang trước khi xay.')}</div>

<section class="p-sec">
 <p class="eye">01 · Nghệ thuật rang</p>
 <h2 class="p-h2">Sáu chặng <em>của một mẻ rang.</em></h2>
 <p class="lead">Đây là khung kỹ thuật, chưa phải quy trình cố định. Nhiệt độ, thời gian và điểm kết thúc phụ thuộc vào thiết bị, cỡ mẻ, độ ẩm, cách sơ chế và cách pha dự kiến.</p>
 <ol class="pst two">{li}</ol>
</section>

<section class="p-sec">
 <p class="eye">02 · Những lô lên men đặc biệt</p>
 <h2 class="p-h2">Lên men trước rang. <em>Nghỉ hạt sau rang.</em></h2>
 {strip(STRIP_LM)}
 <div class="g2">
  <div class="box">{icon('soche')}<h3>Sơ chế và lên men sau thu hoạch</h3><p>Washed, Natural, Honey và lên men có kiểm soát là những cách sơ chế khác nhau. Thông số lên men chỉ được công bố khi có hồ sơ lô đi kèm.</p>
   <div class="lnks"><a class="lnk" href="len-men-men-bia.html">Lên men bằng men bia</a><a class="lnk" href="len-men-trai-cay.html">Lên men cùng trái cây</a><a class="lnk" href="trai-ca-phe.html">Cấu tạo trái</a></div></div>
  <div class="box">{icon('quat')}<h3>Nghỉ hạt và thoát CO₂ sau rang</h3><p>Sau khi rang, hạt nhả CO₂ trong những ngày đầu. Quá trình này khác với lên men vi sinh trước rang, nên hai việc được ghi riêng trong hồ sơ lô.</p>
   <div class="lnks"><a class="lnk" href="{ZALO}" target="_blank" rel="noopener">Trao đổi về lô cà phê đặc biệt ↗</a></div></div>
 </div>
</section>

<section class="p-sec">
 <p class="eye">03 · Bước vào bên trong quy trình</p>
 <h2 class="p-h2">Bốn mô hình <em>để tự thử.</em></h2>
 <div class="g4">
  <a class="box" href="len-men-men-bia.html" style="text-decoration:none;color:inherit"><img src="assets/men-bia.jpg" alt="" width="900" height="599" loading="lazy" style="display:block;width:100%;height:auto;border-radius:10px;margin-bottom:8px"><h3>Lên men bằng men bia</h3><p>Bảy trạm: tuyển trái, xát tươi, chuẩn bị men, lên men, rửa, phơi sấy, đánh giá mẫu.</p></a>
  <a class="box" href="len-men-trai-cay.html" style="text-decoration:none;color:inherit"><img src="assets/trai-cay.jpg" alt="" width="900" height="599" loading="lazy" style="display:block;width:100%;height:auto;border-radius:10px;margin-bottom:8px"><h3>Lên men cùng trái cây</h3><p>Đồng lên men theo tỷ lệ, có đối chứng và ghi nhãn rõ ràng.</p></a>
  <a class="box" href="rang.html" style="text-decoration:none;color:inherit"><img src="assets/rang.jpg" alt="" width="900" height="607" loading="lazy" style="display:block;width:100%;height:auto;border-radius:10px;margin-bottom:8px"><h3>Phòng rang</h3><p>Tám trạm, từ sàng gió đến đóng gói túi van một chiều. So sánh 8 cấp độ rang và đường cong nhiệt.</p></a>
  <a class="box" href="quay-pha.html" style="text-decoration:none;color:inherit"><img src="assets/pha.jpg" alt="" width="900" height="599" loading="lazy" style="display:block;width:100%;height:auto;border-radius:10px;margin-bottom:8px"><h3>Quầy pha</h3><p>Từ rang đến tách: phin, espresso, lọc tay và pha lạnh.</p></a>
 </div>
 <p class="note">Số liệu trong các mô hình là ước tính để học, không phải số đo từ máy hay lô sản xuất của MeDili.</p>
</section>

<section class="box split">
 <div class="p-sec">
  <p class="eye">04 · Hồ sơ cho đối tác</p>
  <h2 class="p-h2" style="margin:0">Điều kiện sản xuất <em>và an toàn thực phẩm.</em></h2>
  <p>Giấy chứng nhận đủ điều kiện sản xuất và giấy chứng nhận cơ sở đủ điều kiện an toàn thực phẩm được gửi khi trao đổi, kèm thông tin cơ quan cấp, phạm vi và thời hạn.</p>
  <div class="cta"><a class="btn main" href="horeca.html#ho-so">Xem hồ sơ đối tác</a><a class="btn" href="horeca.html">Giải pháp HORECA</a></div>
 </div>
 <ul class="pst"><li><span class="n">{icon('khien')}</span><h3>Gửi khi trao đổi</h3><p>Website chưa đăng bản chụp hay số hiệu giấy chứng nhận.</p></li></ul>
</section>
'''
    return doc('xuong-rang.html', 'Xưởng rang MeDili',
               'Xưởng rang MeDili ở Thôn 11, Xã Di Linh: sáu chặng của một mẻ rang, lô lên men đặc biệt, năng lực 20 tấn mỗi tháng, tối đa 60 tấn.',
               body, wrap_cls='wrap pg')


# ---------- MeDili Café ----------
def quan_medili():
    menu = [('Cà phê sữa đá Việt Nam', 'Phin đậm với sữa đặc và đá.'), ('Cà phê phin', 'Pha phin truyền thống, uống đen hoặc thêm đường.'),
            ('Cappuccino', 'Espresso với sữa tươi đánh mịn, lớp bọt dày.'), ('Espresso', 'Shot đậm pha từ máy, cách rõ nhất để cảm nhận hồ sơ rang.')]
    items = ''.join(f'<li><b>{n}</b><span>{d}</span></li>' for n, d in menu)
    body = head('MeDili Café · 143 Phạm Văn Hai', 'Một tách cà phê. <em>Một cuộc hẹn.</em>',
                'Công ty TNHH DSunfood tại 143 Phạm Văn Hai là nhà phân phối của MeDili ở TP.HCM, đồng thời là MeDili Café. Bạn có thể ghé uống một ly, hỏi thực đơn trong ngày hoặc trao đổi về việc cung cấp cà phê cho quán, nhà hàng, khách sạn.',
                f'<a class="btn main" href="{MAP_HCM}" target="_blank" rel="noopener">Chỉ đường ↗</a><a class="btn" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo đặt món</a>')
    body += f'''
<section class="split">
 <div class="p-sec">
  <p class="eye">Cà phê, gần hơn một chút</p>
  <h2 class="p-h2" style="margin:0">Di Linh <em>giữa lòng thành phố.</em></h2>
  <p>MeDili Café đưa câu chuyện Di Linh vào thành phố. Thực đơn thay đổi theo ngày, bạn gọi hoặc nhắn trước để biết hôm nay có món gì. Giờ mở cửa và giá sẽ được cập nhật sau.</p>
  <div class="box menu">
   <p class="eye">Một chút vị MeDili</p>
   <h3>Hôm nay, bạn mê vị gì?</h3>
   <ul>{items}</ul>
   <p class="note">Thực đơn gợi ý. Gọi hoặc nhắn trước để xác nhận món trong ngày.</p>
   <div class="lnks"><a class="lnk" href="quay-pha.html">Xem cách pha từng món ở Quầy pha</a></div>
  </div>
 </div>
 <div class="illw">{ill.suada()}</div>
</section>

<section class="g2">
 <div class="box loc">
  <div class="ttl">{icon('ghim')}<div><span class="k">Địa chỉ</span><h3>MeDili Café · DSunfood</h3></div></div>
  <p class="sel">{ADDR_HCM}</p>
  <div class="lnks"><a class="lnk" href="{MAP_HCM}" target="_blank" rel="noopener">Mở Google Maps ↗</a><a class="lnk" href="lien-he.html">Liên hệ &amp; bản đồ</a></div>
 </div>
 <div class="box loc">
  <div class="ttl">{icon('dt')}<div><span class="k">Gọi để đặt món</span><h3>Zalo và điện thoại</h3></div></div>
  <div class="cp"><strong data-sel>{PHONE}</strong><button class="btn small" type="button" data-copy="{PHONE_RAW}" data-done="Đã sao chép số">Sao chép số</button></div>
  <div class="lnks"><a class="lnk" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo ↗</a></div>
 </div>
</section>

<section class="box split">
 <div class="p-sec">
  <p class="eye">Cho quán, nhà hàng, khách sạn</p>
  <h2 class="p-h2" style="margin:0">Trao đổi chuyện <em>cung cấp cà phê.</em></h2>
  <p>Ghé MeDili Café để nếm cà phê và trao đổi về giải pháp cho quầy pha của bạn.</p>
  <div class="cta"><a class="btn main" href="horeca.html">Giải pháp HORECA</a><a class="btn" href="tim-gu.html">Tìm gu cà phê</a></div>
 </div>
 <ul class="pst"><li><span class="n">{icon('hen')}</span><h3>Hẹn trước</h3><p>Nhắn Zalo trước giờ ghé để MeDili sắp xếp.</p></li></ul>
</section>
'''
    css = '.menu{margin-top:6px}.menu ul{list-style:none;margin:6px 0 8px;padding:0;display:grid}.menu li{display:grid;gap:1px;padding:9px 0;border-bottom:1px dashed var(--rule)}.menu li b{font:700 1.02rem var(--body)}.menu li span{color:var(--muted);font-size:.9rem}'
    return doc('quan-medili.html', 'MeDili Café Phạm Văn Hai',
               'MeDili Café tại 143 Phạm Văn Hai, Tân Bình, TP.HCM: điểm phân phối của MeDili, nơi uống cà phê, hỏi thực đơn trong ngày và trao đổi về việc cung cấp cà phê cho quán.',
               body, css=css, wrap_cls='wrap pg')
