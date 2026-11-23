# Trang Chính sách MeDili (23/11/2026): bốn chính sách khách sỉ, đổi trả, kiểm hàng, hoàn tiền trong một trang có thẻ chọn.
# Mục lục tham khảo bộ chính sách của một nhà cung cấp cà phê; câu chữ viết riêng cho MeDili.
# Điều đã có trên web giữ nguyên: đổi trả 7 ngày, phản hồi 3 ngày làm việc, giá sỉ theo khối lượng tháng, giá chưa gồm 8% VAT,
# giao toàn quốc (phí và thời gian báo trước), cam kết nguyên chất, mẫu thử 50 g miễn phí, phản hồi Zalo 60 phút (6:30–22:30).
# Chị Ngân chốt 23/11/2026 (để trong PENDING): thanh toán chuyển khoản hoặc tiền mặt, linh hoạt; hoàn tiền trong 5 ngày;
# 24/11/2026: khách lẻ trả ngay trong giỏ hàng (chuyển khoản mã QR vào tài khoản công ty DSunfood) hoặc tiền mặt khi nhận hàng;
# miễn phí giao từ 10 kg; hóa đơn VAT do Công ty TNHH DSunfood xuất.
from kit import *
from pages_a import head

FILE = 'chinh-sach.html'
UPDATED = '11/2026'

PENDING = dict(
    pay_si='Thanh toán linh hoạt bằng chuyển khoản hoặc tiền mặt. Thời hạn thanh toán được thống nhất và ghi trong xác nhận đơn hàng.',
    pay_le='Khi đặt hàng trên web, bạn chuyển khoản ngay bằng mã QR ở trang <a class="lnk" href="thanh-toan.html">Thanh toán</a> (app ngân hàng, MoMo, ZaloPay), hoặc trả tiền mặt khi nhận hàng. Phí giao của đơn dưới 10 kg được MeDili báo và thu sau.',
    refund_time='MeDili hoàn tiền bằng chuyển khoản vào tài khoản bạn cung cấp, trong 5 ngày kể từ khi xác nhận hủy đơn hoặc nhận lại hàng.',
    ship_si='Đơn từ 10 kg được miễn phí giao hàng. Với đơn dưới 10 kg, phí giao được báo trước khi xác nhận đơn. Thời gian giao được báo cùng lúc.',
    vat='Hóa đơn VAT do Công ty TNHH DSunfood xuất. Cần hóa đơn, bạn gửi tên công ty, mã số thuế, địa chỉ và email nhận hóa đơn khi đặt hàng.',
)

TABS = [('khach-si', 'Khách sỉ', 'can'), ('doi-tra', 'Đổi trả', 'doi'), ('kiem-hang', 'Kiểm hàng', 'kinh'), ('hoan-tien', 'Hoàn tiền', 'so')]


def ul(items):
    return '<ul>' + ''.join(f'<li>{x}</li>' for x in items if x) + '</ul>'


def card(no, title, items, note=''):
    return (f'<div class="box cs-c"><h3><span>{no}</span>{title}</h3>{ul(items)}'
            + (f'<p class="note">{note}</p>' if note else '') + '</div>')


def panel(pid, no, title, lead, cards):
    return (f'<section class="cs-p" id="{pid}" role="tabpanel" aria-labelledby="t-{pid}" tabindex="-1">'
            f'<div class="cs-ph"><p class="eye">{no} · Chính sách MeDili</p><h2 class="p-h2">{title}</h2>'
            f'<p class="lead">{lead}</p><p class="k">Cập nhật {UPDATED}</p></div>'
            f'<div class="cs-g">{"".join(cards)}</div></section>')


def page():
    P = PENDING
    tabs = ''.join(f'<a class="cs-tab" id="t-{i}" href="#{i}" role="tab" aria-controls="{i}">{icon(k)}<span>{t}</span></a>' for i, t, k in TABS)
    hero = head('Chính sách MeDili', 'Rõ ràng trước, <em>yên tâm khi nhận cà phê.</em>',
                'Bốn chính sách áp dụng cho đơn hàng cà phê MeDili: khách sỉ, đổi trả, kiểm hàng và hoàn tiền. '
                'Cách đặt hàng và giao hàng xem ở trang Giao hàng, việc dùng thông tin của bạn xem ở trang Bảo mật.',
                f'<a class="btn main" href="{ZALO}" target="_blank" rel="noopener">Hỏi MeDili qua Zalo</a>'
                '<a class="btn" href="giao-hang.html">Giao hàng &amp; đổi trả</a><a class="btn" href="bao-mat.html">Chính sách bảo mật</a>')

    khach_si = panel('khach-si', '01', 'Chính sách <em>khách sỉ.</em>',
        'Áp dụng cho quán cà phê, nhà hàng, khách sạn, văn phòng, đại lý và nhà rang mua cà phê rang MeDili theo tháng.', [
        card('1', 'Ai được giá sỉ', [
            'Giá bán lẻ áp dụng cho đơn dưới 5 kg.',
            'Mua từ 5 kg cà phê rang trong tháng: giá sỉ cấp 1.',
            'Đạt 20 kg trong tháng: giá sỉ cấp 2. Phần chênh lệch so với giá đã trả được chiết khấu vào đơn kế tiếp.',
            'Khối lượng tính theo tổng các đơn trong cùng một tháng.',
            'Catimor, Culi và Blend MeDili chưa có giá sỉ, MeDili báo giá khi đặt hàng.']),
        card('2', 'Sản phẩm và quy cách', [
            'Cà phê rang nguyên hạt, hoặc xay sẵn cho phin, cho máy espresso, cho pha thủ công.',
            'Đóng túi 1 kg hoặc 5 kg bằng máy bán tự động.',
            'Quy cách khác được thống nhất trước bằng tin nhắn hoặc email. Chi phí phát sinh, nếu có, được báo trước khi làm.',
            'Các dòng rang mộc: cà phê nguyên chất, đúng thành phần công bố, không pha tạp, không thêm hương liệu hay chất bảo quản.',
            'Hồ sơ đối tác (chứng nhận đủ điều kiện sản xuất, chứng nhận cơ sở đủ điều kiện an toàn thực phẩm) được gửi khi trao đổi.']),
        card('3', 'Giá bán', [
            'Bảng giá đề xuất có hiệu lực trong tháng và được xác nhận khi đặt hàng.',
            'Giá chưa gồm 8% VAT và phí vận chuyển. Đơn từ 10 kg được miễn phí giao hàng.',
            'Bảng giá đầy đủ theo từng bậc ở <a class="lnk" href="mua-hang.html">Phòng chọn mua</a>.']),
        card('4', 'Đặt hàng và xác nhận đơn', [
            f'Đặt qua Zalo hoặc điện thoại {PHONE}, phiếu đặt hàng ở Phòng chọn mua, hoặc email {EMAIL}.',
            'Mỗi đơn ghi rõ sản phẩm, độ xay, khối lượng, địa chỉ và thời gian muốn nhận.',
            'Đơn được tính là đã xác nhận khi MeDili gửi lại xác nhận gồm sản phẩm, quy cách, giá, phí giao và thời gian giao, bằng tin nhắn hoặc email.']),
        card('5', 'Giao hàng', [
            'Giao toàn quốc.',
            P['ship_si'],
            'Khi nhận hàng, hai bên đối chiếu số lượng theo xác nhận đơn. Xem thêm <a class="lnk" href="#kiem-hang">Chính sách kiểm hàng</a>.']),
        card('6', 'Thanh toán và hóa đơn', [P['pay_si'], P['vat']]),
        card('7', 'Mẫu thử và hỗ trợ vận hành', [
            'Quán nhận mẫu thử 50 g miễn phí trước khi đặt hàng.',
            'MeDili hướng dẫn công thức, chỉnh cối xay theo máy pha của quán và bảo trì máy; tư vấn chọn cà phê, độ xay, tỷ lệ pha và thực đơn.',
            'MeDili phản hồi qua Zalo trong 60 phút, từ 6:30 đến 22:30.'],
            'Phạm vi hỗ trợ được thống nhất với từng đối tác.'),
        card('8', 'Khiếu nại về chất lượng', [
            'Lỗi nhìn thấy được (thiếu hàng, sai loại, bao bì rách hoặc hở): báo trong 7 ngày kể từ khi nhận, kèm ảnh hoặc video.',
            'Lỗi về hương vị, chất lượng: quán gửi lại mẫu của lô hàng để MeDili cùng kiểm tra.',
            'Lỗi do MeDili: MeDili đổi hàng và chịu chi phí phát sinh.',
            'MeDili phản hồi trong 3 ngày làm việc kể từ khi nhận khiếu nại.',
            'Cà phê cần bảo quản nơi khô, mát, tránh nắng theo hướng dẫn trên bao bì. Hư hỏng do bảo quản sai không thuộc phạm vi đổi trả.']),
        card('9', 'Hình ảnh và thông tin sản phẩm', [
            'Đối tác bán cà phê MeDili được dùng ảnh và thông tin sản phẩm do MeDili cung cấp để giới thiệu và bán đúng sản phẩm MeDili.',
            'Không dùng ảnh, tên MeDili cho sản phẩm khác hoặc cho mục đích trái pháp luật.']),
    ])

    doi_tra = panel('doi-tra', '02', 'Chính sách <em>đổi trả.</em>',
        'MeDili đổi hàng khi cà phê đến tay bạn không đúng như đơn đã xác nhận.', [
        card('1', 'Thời hạn', ['Trong 7 ngày kể từ khi bạn nhận hàng.']),
        card('2', 'Trường hợp được đổi', [
            'Lỗi sản xuất: túi hở, rách miệng hàn, cà phê bị ẩm hoặc mốc.',
            'Lỗi đóng gói.',
            'Hư hỏng khi vận chuyển.',
            'Giao sai loại, sai độ xay hoặc sai khối lượng so với xác nhận đơn.']),
        card('3', 'Trường hợp không áp dụng', [
            'Đổi ý, hoặc không hợp khẩu vị sau khi đã mở túi. Khách quán có thể nhận mẫu thử 50 g miễn phí trước khi đặt.',
            'Cà phê bảo quản sai hướng dẫn trên bao bì.',
            'Báo lỗi sau 7 ngày kể từ khi nhận hàng.']),
        card('4', 'Điều kiện', [
            'Sản phẩm còn bao bì và nhãn.',
            'Lỗi phát hiện khi mở túi: giữ lại phần cà phê còn lại để MeDili kiểm tra.',
            'Có mã đơn hoặc số điện thoại đặt hàng, kèm ảnh hoặc video lỗi.']),
        card('5', 'Các bước đổi hàng', [
            f'Chụp ảnh hoặc quay video lỗi, nhắn Zalo hoặc gọi {PHONE}, hoặc email {EMAIL}, kèm mã đơn.',
            'MeDili phản hồi trong 3 ngày làm việc và hướng dẫn cách gửi lại hàng nếu cần.',
            'Lỗi do MeDili: MeDili chịu phí gửi lại và phí giao hàng thay thế.',
            'MeDili gửi hàng thay thế sau khi xác nhận lỗi. Không còn sản phẩm tương đương thì hoàn tiền theo <a class="lnk" href="#hoan-tien">Chính sách hoàn tiền</a>.']),
    ])

    kiem_hang = panel('kiem-hang', '03', 'Chính sách <em>kiểm hàng.</em>',
        'Bạn được kiểm tra hàng cùng người giao trước khi nhận, để chắc chắn đơn đúng và nguyên vẹn.', [
        card('1', 'Bạn được kiểm tra', [
            'Mở thùng hoặc hộp ngoài cùng người giao hàng.',
            'Đối chiếu tên sản phẩm, độ xay, khối lượng và số túi với xác nhận đơn.',
            'Bao bì nguyên vẹn: không rách, thủng, móp, không có dấu bóc mở.',
            'Ngày rang và hạn sử dụng trên nhãn.'],
            'Túi cà phê nên giữ nguyên miệng hàn đến khi dùng để giữ hương.'),
        card('2', 'Khi hàng có vấn đề', [
            'Sai sản phẩm, hư hỏng hoặc có dấu hiệu bất thường: bạn có thể từ chối nhận hàng.',
            'Ghi lý do vào biên bản giao nhận nếu có, và chụp ảnh tình trạng hàng.',
            f'Báo MeDili ngay qua Zalo hoặc gọi {PHONE} để được gửi lại đơn đúng.']),
        card('3', 'Sau khi đã nhận hàng', [
            'Nên quay video lúc mở thùng để MeDili xác minh và xử lý nhanh.',
            'Lỗi phát hiện sau khi nhận được xử lý theo <a class="lnk" href="#doi-tra">Chính sách đổi trả</a> trong 7 ngày.']),
        card('4', 'Đơn sỉ', [
            'Hai bên đối chiếu số lượng khi giao, ký biên bản giao nhận hoặc xác nhận qua tin nhắn.',
            'Quán tự nhận hàng bằng xe riêng: MeDili gửi ảnh xác nhận khi bàn giao hàng cho người nhận.']),
    ])

    hoan_tien = panel('hoan-tien', '04', 'Chính sách <em>hoàn tiền.</em>',
        'Áp dụng cho đơn đã thanh toán mà MeDili không giao được, giao thiếu, hoặc không còn hàng để đổi.', [
        card('1', 'Trường hợp được hoàn tiền', [
            'Bạn đã thanh toán nhưng MeDili không giao được hàng, hoặc sản phẩm đã hết.',
            'Bạn hủy đơn đã thanh toán trước khi MeDili giao hàng cho đơn vị vận chuyển.',
            'Giao thiếu so với xác nhận đơn và MeDili không gửi bù được.',
            'Hàng lỗi hoặc giao sai mà MeDili không còn sản phẩm tương đương để đổi.']),
        card('2', 'Mức hoàn', [
            'Hoàn đủ giá trị phần sản phẩm bị lỗi, bị thiếu hoặc không giao được.',
            'Phí giao hàng được hoàn khi lỗi do MeDili.']),
        card('3', 'Cách hủy đơn', [
            f'Nhắn Zalo hoặc gọi {PHONE}, hoặc email {EMAIL}, kèm mã đơn.',
            'Đơn đã giao cho đơn vị vận chuyển: MeDili xử lý hoàn tiền khi hàng được gửi trả về.']),
        card('4', 'Cách và thời gian hoàn tiền', [
            P['refund_time'],
            'Bạn gửi kèm mã đơn, tên chủ tài khoản, số tài khoản và ngân hàng nhận tiền.',
            P['pay_le']]),
    ])

    contact = (f'<section class="box p-sec cs-ct"><p class="eye">Liên hệ về chính sách</p>'
               f'<div class="g2"><div><h3>Công ty TNHH DSunfood · phân phối MeDili</h3><p>{ADDR_HCM}</p>'
               f'<p>Vườn và xưởng rang: {ADDR_FARM}</p></div>'
               f'<div><h3>Zalo, điện thoại <span class="sel">{PHONE}</span></h3><p>Email <span class="sel">{EMAIL}</span>. '
               'Phản hồi qua Zalo trong 60 phút, từ 6:30 đến 22:30. Khi đổi trả hoặc hoàn tiền, bạn gửi kèm mã đơn để MeDili tra nhanh hơn.</p>'
               f'<div class="cta"><a class="btn main" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo MeDili</a>'
               f'<button class="btn" type="button" data-copy="{EMAIL}" data-done="Đã sao chép email">Sao chép email</button></div></div></div>'
               f'<p class="note">Chính sách có thể được cập nhật. Bản đang áp dụng là bản trên trang này.</p></section>')

    body = (hero + f'<nav class="cs-tabs" id="cs-tabs" role="tablist" aria-label="Chọn chính sách">{tabs}</nav>'
            + khach_si + doi_tra + kiem_hang + hoan_tien + contact)
    desc = ('Chính sách MeDili: khách sỉ (giá theo khối lượng tháng, miễn phí giao từ 10 kg, mẫu thử 50 g miễn phí), đổi trả trong 7 ngày, '
            'kiểm hàng khi nhận, hoàn tiền trong 5 ngày. Áp dụng cho đơn cà phê MeDili.')
    return doc(FILE, 'Chính sách MeDili', desc, body, css=CSS, js=JS, wrap_cls='wrap pg')


CSS = '''
/* Chính sách MeDili: thẻ chọn bốn chính sách */
.cs-tabs{position:sticky;top:calc(56px + env(safe-area-inset-top,0px));z-index:20;display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding:10px 0;background:var(--bg);border-bottom:1px solid var(--rule)}
.cs-tabs::-webkit-scrollbar{display:none}
.cs-tab{display:inline-flex;align-items:center;gap:8px;flex:none;border:1px solid var(--rule);background:var(--panel);color:var(--ink);border-radius:999px;padding:9px 16px;text-decoration:none;font:600 .95rem var(--body)}
.cs-tab svg{width:18px;height:18px;flex:none}
.cs-tab:hover{border-color:var(--accent);color:var(--accent)}
.cs-tab[aria-selected="true"]{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.cs-p{display:grid;gap:14px;scroll-margin-top:130px;outline:none}
.cs-p+.cs-p{margin-top:26px}
.cs-ph{display:grid;gap:4px}
.cs-ph .p-h2 em{font-style:normal;color:var(--accent)}
.cs-ph .lead{margin:0}
.cs-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:start}
.cs-c h3{display:flex;align-items:baseline;gap:10px;margin:0 0 8px;font:700 1.05rem/1.3 var(--body)}
.cs-c h3 span{font:800 1.5rem/1 var(--display);color:var(--accent);min-width:1.1em}
.cs-c ul{margin:0;padding-left:1.15em;display:grid;gap:6px}
.cs-c li{line-height:1.55;font-size:.95rem}
.cs-c li::marker{color:var(--accent)}
.cs-c .note{margin-top:8px}
.cs-ct h3{font:700 1.02rem/1.35 var(--body);margin:0 0 6px}
.cs-ct p{margin:0 0 6px}
html.cs-js .cs-p+.cs-p{margin-top:0}
@media (max-width:900px){.cs-g{grid-template-columns:minmax(0,1fr)}}
@media (max-width:600px){.cs-tabs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));overflow:visible}.cs-tab{justify-content:center;padding:9px 10px}}
@media print{.cs-p[hidden]{display:grid!important}.cs-tabs{display:none}}
'''

JS = r'''
(()=>{const tabs=[...document.querySelectorAll('.cs-tab')],panes=[...document.querySelectorAll('.cs-p')];if(!tabs.length)return;
document.documentElement.classList.add('cs-js');
const ids=panes.map(p=>p.id);
function show(id,focus){if(!ids.includes(id))id=ids[0];
 tabs.forEach(t=>{const on=t.getAttribute('aria-controls')===id;t.setAttribute('aria-selected',on?'true':'false');t.tabIndex=on?0:-1;if(on&&focus)t.focus()});
 panes.forEach(p=>{p.hidden=p.id!==id})}
function go(id,focus){show(id,focus);try{history.replaceState(null,'','#'+id)}catch(e){}}
tabs.forEach((t,i)=>{t.addEventListener('click',e=>{e.preventDefault();go(t.getAttribute('aria-controls'))});
 t.addEventListener('keydown',e=>{const n=tabs.length;let j=null;if(e.key==='ArrowRight')j=(i+1)%n;if(e.key==='ArrowLeft')j=(i-1+n)%n;if(e.key==='Home')j=0;if(e.key==='End')j=n-1;
  if(j!==null){e.preventDefault();go(tabs[j].getAttribute('aria-controls'),true)}})});
document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]');if(!a||a.classList.contains('cs-tab'))return;const id=a.getAttribute('href').slice(1);
 if(ids.includes(id)){e.preventDefault();go(id);document.getElementById('cs-tabs').scrollIntoView({block:'start',behavior:'smooth'})}});
addEventListener('hashchange',()=>show(location.hash.slice(1)));
show(location.hash.slice(1));
})();
'''
