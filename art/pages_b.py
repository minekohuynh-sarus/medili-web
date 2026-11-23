# Trang mới từ web Manus, phần 2: Coffee Journal và bài viết, Tìm gu, Liên hệ, Giao hàng & đổi trả, Bảo mật
import re, math
from kit import *
import ill
from pages_a import head, contact_methods, loc_cards

# ---------- bài viết ----------
ART = {
    'journal-phin.html': dict(
        cat='Pha chế', h1='Phin và nhịp rơi <em>của thời gian.</em>', title='Phin và nhịp rơi của thời gian',
        dek='Vì sao một dụng cụ nhỏ lại tạo ra một khoảng chờ rất Việt Nam.', svg=ill.phin,
        body='''
<p>Một chiếc phin, vài muỗng cà phê, một ấm nước vừa sôi. Rồi ai cũng phải chờ. Giọt đầu tiên rơi xuống ly sau chừng một phút, cả lượt pha mất bốn đến năm phút. Không có nút nào bấm cho nhanh hơn. Khoảng chờ ấy là một phần của ly cà phê Việt Nam.</p>
<h2>Một dòng chảy có chủ đích</h2>
<p>Pha phin không chỉ là làm theo một công thức. Nước đi qua lớp cà phê đủ chậm để người pha kịp nhìn, kịp ngửi và kịp chờ. Trong lúc đó, nước kéo ra vị đậm, vị đắng, độ ngọt và mùi thơm của hạt rang.</p>
<p>Không có một con số chung cho mọi loại cà phê. Độ xay, lượng cà phê, nhiệt độ nước và lực nén ảnh hưởng lẫn nhau:</p>
<ul>
<li>Xay mịn hơn thì nước chảy chậm hơn, ly đậm hơn và dễ đắng gắt.</li>
<li>Nén chặt hơn cũng làm nước chảy chậm lại.</li>
<li>Nước nguội hơn kéo ra ít vị hơn, ly nhạt và chua hơn.</li>
<li>Nhiều cà phê hơn cho ly đặc hơn, nước cũng cần lâu hơn để đi qua.</li>
</ul>
<p>Vì vậy, hãy xem công thức là điểm xuất phát. Mỗi lần chỉ đổi một yếu tố, rồi nếm lại.</p>
<p>Muốn thấy vì sao một nấc xay hay vài độ nước lại đổi vị cả ly, hãy thử <a class="lnk" href="chiet-xuat.html">Cỗ máy Chiết xuất</a>: chọn phin, vặn từng núm và xem acid, đường, chất đắng lần lượt rời hạt.</p>
<div class="rbox"><h3>Công thức phin khởi đầu của MeDili</h3><ol>
<li>20–25 g bột xay vừa, nén nhẹ.</li>
<li>Rót 20 ml nước 92–95 °C, ủ 30 giây.</li>
<li>Rót thêm khoảng 60–80 ml, chờ 4–5 phút.</li>
</ol><p class="note" style="margin:8px 0 0">Ly quá đắng thì xay thô hơn một chút. Ly nhạt thì xay mịn hơn hoặc thêm vài gram cà phê.</p></div>
<h2>Cách nếm chậm hơn</h2>
<p>Khi cà phê còn ấm, hãy nếm một ngụm nhỏ trước khi thêm đá hay sữa. Để ý ba điều:</p>
<ol>
<li>Mùi đầu tiên khi đưa ly lên gần mũi.</li>
<li>Cảm giác ở đầu lưỡi: đắng, chua hay ngọt, đậm hay nhẹ.</li>
<li>Vị còn lại sau khi nuốt, kéo dài hay tắt nhanh.</li>
</ol>
<p>Sau đó mới thêm thứ bạn thích: đường, sữa đặc, đá. Vì đã nếm ly đen trước, bạn sẽ biết sữa đã thay đổi ly cà phê ra sao.</p>
<p>Pha ngon không có nghĩa là ly nào cũng giống ly nào. Điều đáng giữ là hiểu vì sao một thay đổi nhỏ lại cho ra một ly khác.</p>
<blockquote>Luôn có thời gian cho một tách cà phê ngon.</blockquote>''',
        rel=[('chiet-xuat.html', 'Cỗ máy Chiết xuất', 'Chất nào vào ly khi đổi cỡ xay, nhiệt độ, thời gian.'),
             ('quay-pha.html', 'Quầy pha', 'Công thức phin, espresso, lọc tay cho từng món.'),
             ('mua-hang.html', 'Phòng chọn mua', 'Robusta Classic, Robusta Premium và Arabica cho pha phin.')]),
    'journal-tu-qua.html': dict(
        cat='Kiến thức cà phê', h1='Từ trái cà phê <em>đến hương vị.</em>', title='Từ trái cà phê đến hương vị',
        dek='Một bản đồ ngắn về những chuyển hóa đứng sau một hạt cà phê.', svg=ill.qua,
        body='''
<p>Hạt cà phê thực ra là hạt giống nằm trong một trái chín đỏ. Từ lúc trái được hái đến lúc hạt rơi vào cối xay, nó đi qua nhiều lần biến đổi, và lần nào cũng để lại dấu vết trong ly.</p>
<p>Một con số để hình dung: theo mô hình của MeDili, 100 kg trái tươi cho khoảng 18 kg nhân xanh, rồi còn khoảng 14,4 kg cà phê rang. Phần lớn khối lượng của trái mất đi trên đường từ vườn đến xưởng rang.</p>
@@PH_HAI@@
<h2>Sơ chế là một ngôn ngữ</h2>
<p>Natural, Honey và Washed là tên của ba cách sơ chế. Chúng khác nhau ở chỗ lớp nào của trái được giữ lại khi phơi.</p>
<ul>
<li><b>Natural:</b> phơi nguyên trái. Hạt nằm lâu trong thịt trái nên ly thường ngọt và đậm mùi trái chín.</li>
<li><b>Honey:</b> xát bỏ vỏ, giữ lại một phần lớp nhớt rồi phơi. Ly thường tròn vị và ngọt.</li>
<li><b>Washed:</b> xát vỏ, lên men, rửa sạch lớp nhớt rồi mới phơi. Ly thường sạch vị, chua thanh.</li>
</ul>
@@ST_SOCHE@@
<p>Tên gọi không thay cho việc nếm. Kết quả còn tùy giống cây, độ chín của trái và điều kiện phơi sấy. Hai lô cùng ghi Honey vẫn có thể cho hai ly rất khác nhau.</p>
<p>Xem năm lớp của trái và lớp nào được tách ra ở bước nào trong bài <a class="lnk" href="trai-ca-phe.html">Cấu tạo trái</a>, hoặc thử <a class="lnk" href="len-men-men-bia.html">cỗ máy lên men bảy trạm</a>.</p>
<h2>Rang là khoảnh khắc thấu hiểu hạt</h2>
<p>Trong lồng rang, nhiệt làm hạt mất nước, chuyển từ màu nhạt sang vàng rồi nâu. Đường và acid amin phản ứng với nhau (phản ứng Maillard), còn đường bị caramel hóa. Những phản ứng này tạo ra mùi thơm, màu sắc và độ giòn của hạt rang.</p>
<p>Mức rang là điểm cân bằng giữa tính chất của hạt và cách pha dự kiến. Nước đi qua bột trong phin và trong máy espresso theo hai cách khác nhau, nên MeDili rang riêng cho phin và cho máy.</p>
<p>Nước là chặng cuối. Nước mang những chất hình thành khi rang vào trong ly. Vì vậy rang và pha là hai chương liền nhau của cùng một câu chuyện. Chất nào vào ly trước, chất nào sau, bạn xem ở <a class="lnk" href="chiet-xuat.html">Cỗ máy Chiết xuất</a>.</p>
<blockquote>Rang và pha là hai chương liền nhau.</blockquote>''',
        rel=[('rang.html', 'Phòng rang', 'Tám cấp độ rang, đường cong nhiệt và phiếu rang.'),
             ('trai-ca-phe.html', 'Cấu tạo trái', 'Năm lớp bọc quanh hạt nhân.'),
             ('quay-pha.html', 'Quầy pha', 'Từ hạt rang đến từng ly.')]),
    'journal-di-linh.html': dict(
        cat='Vùng đất', h1='Di Linh <em>trong một tách cà phê.</em>', title='Di Linh trong một tách cà phê',
        dek='Đọc một vùng đất bằng sự khiêm nhường: khí hậu, độ cao và ký ức vị giác.', svg=ill.dilinh,
        body=f'''
<h2>Một địa danh, nhiều lớp nghĩa</h2>
<p>Di Linh thuộc tỉnh Lâm Đồng, nằm trên vùng cao nguyên gắn bó lâu đời với nghề trồng cà phê. Cao nguyên Di Linh nằm ở độ cao khoảng 900–1.000 m, khí hậu mát, mùa mưa và mùa khô rõ rệt. Đó là bối cảnh để người trồng, người sơ chế và người rang cùng làm việc.</p>
@@PH_SAN@@
<p>Nguyên liệu của MeDili đến từ bốn vùng trồng: Gia Bắc 2, Lộc Châu 3, Tân Nghĩa và Tà Hine, tổng diện tích {ha(TOTAL)} ha, cùng {LINKED} ha liên kết tại Di Linh. Vùng trồng canh tác từ năm 2010. Dòng được chú trọng nhất là Cà Sẻ Di Linh.</p>
<p>Một địa danh trên bao bì chỉ là chữ. Phía sau nó là những người hái trái lúc chín, những sân phơi, những mùa mưa đến sớm hay muộn.</p>
<h2>Nếm với sự tò mò</h2>
<p>Khi uống một ly cà phê có gốc Di Linh, hãy bắt đầu bằng hai câu hỏi mở.</p>
<p>Câu thứ nhất: trong ly này đang có gì? Vị đậm, vị đắng, mùi ca cao, hay chút ngọt của trái chín.</p>
<p>Câu thứ hai: điều gì chưa thể biết chỉ bằng vị giác? Vườn ở đâu, trái được hái lúc nào, phơi bao nhiêu ngày. Những điều đó cần người làm cà phê kể lại.</p>
<p>Một ly ngon có thể đưa người uống về với một địa danh. Việc của người làm cà phê là giữ cho địa danh ấy sống động, với nhiều tiếng nói và nhiều mùa vụ.</p>
<blockquote>Mê cà phê, mê Di Linh.</blockquote>''',
        rel=[('vung-trong.html', 'Vùng trồng Di Linh', f'Bốn vùng trồng, {ha(TOTAL)} ha và {LINKED} ha liên kết.'),
             ('vuon.html', 'Vườn 12 tháng', 'Lịch chăm sóc vườn Robusta qua từng tháng.'),
             ('cau-chuyen.html', 'Câu chuyện MeDili', 'Cà Sẻ Di Linh, gốc của niềm mê.')]),
}


def words(htm):
    t = re.sub(r'<[^>]+>', ' ', htm)
    return len(re.findall(r'\w+', t))


def mins(htm):
    return max(2, math.ceil(words(re.sub(r'@@\w+@@', '', htm)) / 200))


def article(fname, a, cards):
    a = dict(a, body=a['body'].replace('@@PH_HAI@@', photo('p-hai-chon.jpg', 'Bàn tay nhặt trái cà phê chín', 'Hái chọn trái chín.'))
             .replace('@@ST_SOCHE@@', strip(STRIP_SOCHE))
             .replace('@@PH_SAN@@', photo('p-san-phoi-wide.jpg', 'Cà phê phơi trên sân giữa đồi', 'Phơi cà phê giữa đồi.', cls='pfw')))
    m = mins(re.sub(r'<figure.*?</figure>|<div class="pfs">.*?</div>', '', a['body'], flags=re.S))
    rel = ''.join(f'<a href="{h}"><b>{t}</b><span>{d}</span></a>' for h, t, d in a['rel'])
    others = ''.join([c for f, c in cards if f != fname][:3])
    body = (f'<article class="p-sec" style="gap:18px"><header class="p-head">{logo()}<p class="meta"><b>Kiến thức cà phê</b><span>{a["cat"]}</span><span>{m} phút đọc</span></p>'
            f'<h1>{a["h1"]}</h1><p class="lead">{a["dek"]}</p></header>'
            f'<figure class="art-fig" style="margin:0">{a["svg"]()}</figure>'
            f'<div class="p-art">{a["body"]}</div>'
            f'<nav class="box relw" aria-label="Đọc và thử thêm"><p class="eye">Đọc và thử thêm</p><div class="rel">{rel}</div></nav></article>'
            f'<section class="p-sec"><h2 class="p-h2">Đọc thêm <em>kiến thức cà phê.</em></h2><div class="jcards">{others}</div>'
            f'<div class="lnks"><a class="lnk" href="journal.html">Tất cả bài viết</a></div></section>')
    css = ('.relw{display:grid;gap:8px}.rel{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}'
           '.rel a{display:grid;gap:2px;border-top:2px solid var(--accent);padding-top:8px;color:var(--ink);text-decoration:none;min-width:0}'
           '.rel a b{font:700 1rem var(--body)}.rel a span{font-size:.88rem;color:var(--muted)}.rel a:hover b{color:var(--accent)}'
           '@media (max-width:700px){.rel{grid-template-columns:minmax(0,1fr)}}' + FIGCSS)
    return doc(fname, a['title'], a['dek'], body, css=css, wrap_cls='wrap art')


FIGCSS = ''  # gán từ build: CSS hình trái cà phê của trang chủ


def jcard(href, cat, mins_txt, title, dek, svg):
    return f'<a href="{href}"><div class="th">{svg}</div><div class="bd"><p class="meta"><b>{cat}</b><span>{mins_txt}</span></p><h3>{title}</h3><p>{dek}</p></div></a>'


MODELS = [('phan-biet-ca-phe.html', 'soi', 'Cỗ máy Phân biệt cà phê', 'Cà Sẻ, cao sản, Arabica, Culi, Moka, Liberica.'),
          ('trai-chin.html', 'la', 'Cỗ máy Trái chín', 'Từ hoa đến trái chín, Brix, hái chọn hay hái tuốt.'),
          ('trai-ca-phe.html', 'kinh', 'Giải phẫu trái Cà Sẻ', 'Bấm từng lớp, từ vỏ ngoài vào tới nhân.'),
          ('vi-sinh.html', 'visinh', 'Cỗ máy Vi sinh', 'Nấm men, vi khuẩn lactic, acetic trong bồn lên men.'),
          ('tien-chat-huong.html', 'phantu', 'Cỗ máy Tiền chất hương', 'Hạt tích lũy gì, rang biến thành hương gì.'),
          ('banh-xe-huong.html', 'banhxe', 'Bánh xe hương MeDili', 'Chín nhóm hương, nguồn gốc mùi, phiếu nếm.'),
          ('chiet-xuat.html', 'phin', 'Cỗ máy Chiết xuất', 'Chất nào vào ly theo cỡ xay, nhiệt độ, thời gian.'),
          ('cold-brew.html', 'lanh', 'Cỗ máy Cold Brew', 'Từ vườn Di Linh đến chai và túi ủ bán trên sàn.'),
          ('rang.html', 'rang', 'Phòng rang', 'Tám cấp độ rang, đường cong nhiệt và phiếu rang.'),
          ('quay-pha.html', 'ly', 'Quầy pha', 'Công thức phin, espresso, lọc tay cho từng món.'),
          ('vuon.html', 'vuon', 'Vườn 12 tháng', 'Lịch chăm sóc vườn Robusta qua từng tháng.'),
          ('len-men-men-bia.html', 'soche', 'Lên men bằng men bia', 'Bảy trạm sơ chế và lên men.'),
          ('len-men-trai-cay.html', 'trai', 'Lên men cùng trái cây', 'Đồng lên men với nhãn, dâu tằm, chanh dây.'),
          ('tim-gu.html', 'gu', 'Tìm gu cà phê', 'Sáu câu hỏi ngắn, gợi ý dòng cà phê hợp gu.'),
          ('suc-khoe.html', 'tim', 'Cà phê và cơ thể', 'Tính lượng caffeine theo thói quen uống.'),
          ('tu-vuon-den-ly.html', 'can', 'Từ vườn đến ly', 'Một ly 35.000 đ chia cho những ai.')]


KSERIES = [('phan-biet-ca-phe.html', 'soi', 'Giống', 'Cỗ máy Phân biệt cà phê', 'Cà Sẻ Di Linh khác Robusta cao sản, Arabica, Culi, Moka, Liberica ở đâu: xem vườn, soi nhân, cân, sàng, nếm.'),
           ('trai-chin.html', 'la', 'Trái chín', 'Cỗ máy Trái chín', 'Trái lớn và chín ra sao, Brix nói gì, hái chọn khác hái tuốt thế nào.'),
           ('vi-sinh.html', 'visinh', 'Vi sinh', 'Cỗ máy Vi sinh', 'Nấm men, vi khuẩn lactic, vi khuẩn acetic làm gì trong bồn, và khi nào cần dừng.'),
           ('tien-chat-huong.html', 'phantu', 'Tiền chất hương', 'Cỗ máy Tiền chất hương', 'Nhân xanh có gì, rang biến chúng thành hương gì, pha mang gì vào ly.'),
           ('banh-xe-huong.html', 'banhxe', 'Bánh xe hương', 'Bánh xe hương MeDili', 'Chín nhóm hương gọi bằng những mùi quen thuộc với người Việt, kèm nguồn gốc mùi và phiếu nếm.')]


def feat_chiet():
    return ('<a class="box jfeat" href="chiet-xuat.html"><div class="th">' + ill.chiet() + '</div><div class="bd">'
            '<p class="meta"><b>Mô hình mới</b><span>Tự chỉnh thông số</span></p><h3>Cỗ máy Chiết xuất</h3>'
            '<p>Thời gian pha không chỉ quyết định độ đậm mà còn quyết định chất nào đi vào ly. Acid và CGA ra trước, đường và hợp chất Maillard ra giữa, chất đắng ra sau. '
            'Chỉnh cỡ xay, nhiệt độ và thời gian cho phin, ép Pháp, pour-over, espresso và cold brew.</p>'
            '<span class="lnk">Mở cỗ máy →</span></div></a>')


def journal(cards):
    body = head('Kiến thức cà phê · MeDili', 'Những ghi chép <em>bên tách cà phê.</em>',
                'Kiến thức pha chế, cách nếm, chuyện vùng trồng và những mô hình để bạn tự bấm thử. Mỗi bài viết giúp bạn để ý thêm một điều mỗi lần uống cà phê.')
    body += f'<section class="p-sec">{feat_chiet()}</section>'
    ks = ''.join(f'<a class="box kser" href="{h}">{icon(i)}<span class="k">{n:02d} · {k}</span><h3>{t}</h3><p>{d}</p><span class="lnk">Mở cỗ máy →</span></a>'
                 for n, (h, i, k, t, d) in enumerate(KSERIES, 1))
    body += (f'<section class="p-sec"><p class="eye">Bộ mới · từ giống đến hương</p><h2 class="p-h2" style="margin:0">Từ giống cây <em>đến bánh xe hương.</em></h2>'
             f'<p class="lead" style="margin:0">Năm cỗ máy đi theo đúng hành trình của hương vị: giống cây đặt nền, trái tích lũy tiền chất trên cây, vi sinh chuyển hóa trong bồn, lò rang mở khóa hương, và mũi người nếm gọi tên.</p>'
             f'<div class="g5k">{ks}</div></section>')
    body += f'<section class="p-sec"><h2 class="p-h2" style="margin:0">Bài viết</h2><div class="jcards">{"".join(c for f, c in cards)}</div></section>'
    mdl = ''.join(f'<a href="{h}">{icon(i)}<span><b>{t}</b><small>{d}</small></span></a>' for h, i, t, d in MODELS)
    body += (f'<section class="box p-sec"><p class="eye">Mô hình tương tác</p><h2 class="p-h2" style="margin:0">Bấm, chỉnh, <em>xem bên trong.</em></h2>'
             f'<p class="lead" style="margin:0">Mỗi cỗ máy là một bản vẽ để bạn tự chỉnh thông số. Số liệu mang tính minh họa, dùng để hiểu và làm mốc khởi đầu.</p>'
             f'<div class="mdl">{mdl}</div></section>')
    return doc('journal.html', 'Kiến thức cà phê MeDili',
               'Kiến thức cà phê của MeDili: cỗ máy chiết xuất, pha phin, từ trái cà phê đến hương vị, Di Linh trong một tách cà phê, cấu tạo trái, từ vườn đến ly, cà phê và cơ thể.',
               body, css=FIGCSS, wrap_cls='wrap pg')


# ---------- Tìm gu ----------
TG_UI = r'''
const st={i:0,ans:[]};const $=id=>document.getElementById(id);
const escH=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const money=n=>n.toLocaleString('vi-VN').replace(/,/g,'.');
const mix=(a,b,t)=>a.map((v,i)=>Math.round(v+(b[i]-v)*t));
function paintCup(){const s=st.ans[1]===undefined?.6:QUESTIONS[1].opts[st.ans[1]].tone,mk=st.ans[3]===undefined?0:QUESTIONS[3].opts[st.ans[3]].milk;
const c=mix(mix([176,120,66],[58,30,16],s),[226,196,160],mk),cr=mix([214,170,112],[150,96,50],s);
const cup=$('cup');cup.style.setProperty('--coffee',`rgb(${c})`);cup.style.setProperty('--crema',`rgb(${cr})`)}
function renderPicks(){$('picks').innerHTML=st.ans.length?st.ans.map((a,i)=>`<li>${escH(QUESTIONS[i].opts[a].t)}</li>`).join(''):'<li class="em">Chưa chọn câu nào</li>'}
function renderTable(top){let g='',rows='';PRODUCTS.forEach(p=>{if(p.group!==g){g=p.group;rows+=`<tr class="grp"><td colspan="4">${escH(g)}</td></tr>`}
rows+=`<tr class="${p.id===top?'top':''}"><th scope="row">${p.id===top?'★ ':''}${escH(p.name)}</th><td class="n">${money(p.prices[0])}</td><td class="n">${money(p.prices[1])}</td><td class="n">${money(p.prices[2])}</td></tr>`});
$('price-table').innerHTML=`<thead><tr><th scope="col">Sản phẩm</th><th scope="col" class="n">Giá lẻ<small>dưới 5 kg</small></th><th scope="col" class="n">Sỉ cấp 1<small>5–20 kg/tháng</small></th><th scope="col" class="n">Sỉ cấp 2<small>trên 20 kg/tháng</small></th></tr></thead><tbody>${rows}</tbody>`}
function renderQuestion(){const q=QUESTIONS[st.i];
$('panel').innerHTML=`<p class="k">Câu ${st.i+1} / ${QUESTIONS.length}</p><div class="meter" aria-hidden="true">${QUESTIONS.map((_,i)=>`<i class="${i<=st.i?'on':''}"></i>`).join('')}</div>
<h2 class="p-h2" style="margin:6px 0 2px">${escH(q.title)}</h2><p class="note">${escH(q.hint)}</p>
<div class="qo">${q.opts.map((o,i)=>`<button type="button" class="qopt" id="opt-${i}" data-i="${i}" aria-pressed="${st.ans[st.i]===i}"><b>${escH(o.t)}</b><span>${escH(o.d)}</span></button>`).join('')}</div>
${st.i>0?'<button type="button" class="btn ghost small" id="back">Quay lại câu trước</button>':''}`;
$('panel').querySelectorAll('.qopt').forEach(b=>b.addEventListener('click',()=>choose(+b.dataset.i)));
const bk=$('back');if(bk)bk.addEventListener('click',()=>{st.i--;st.ans.length=st.i;renderPicks();paintCup();renderQuestion();$('panel').querySelector('.qopt').focus()})}
function choose(n){st.ans[st.i]=n;renderPicks();if(st.i===1||st.i===3)paintCup();
$('panel').querySelectorAll('.qopt').forEach(b=>b.setAttribute('aria-pressed',String(+b.dataset.i===n)));
setTimeout(()=>{st.i++;if(st.i<QUESTIONS.length){renderQuestion();$('panel').querySelector('.qopt').focus()}else renderResult()},170)}
function renderResult(){const R=scoreAnswers(st.ans),b=R[0],s2=R[1],p=b.p,brew=QUESTIONS[0].opts[st.ans[0]].t,vi=st.ans[5],vol=QUESTIONS[5].opts[vi];
const txt=`TÌM GU MEDILI\nPhù hợp nhất: ${p.name} (${b.pct}%)\nLựa chọn thứ hai: ${s2.p.name} (${s2.pct}%)\nCách pha: ${brew}\nNhu cầu: ${vol.t}/tháng\nTrả lời: ${st.ans.map((a,i)=>QUESTIONS[i].opts[a].t).join(', ')}`;
$('panel').innerHTML=`<p class="k">Gu của bạn</p><h2 class="p-h2" style="margin:4px 0 2px">${escH(p.name)}</h2>
<p class="match"><strong>${b.pct}%</strong> hợp với câu trả lời của bạn</p><p><b>${escH(p.notes)}.</b> ${escH(p.why)}</p>
<dl class="prof">${Object.entries(profile(p)).map(([k,v])=>`<div><dt>${escH(k)}</dt><dd aria-label="${v} trên 5">${[1,2,3,4,5].map(n=>`<i class="${n<=v?'on':''}"></i>`).join('')}</dd></div>`).join('')}</dl>
<div class="quote2"><span class="k">${escH(vol.label)}</span><b>${money(p.prices[vi])} đ/kg</b><span class="note">Chưa gồm 8% VAT và phí vận chuyển. Túi 1 kg hoặc 5 kg.</span></div>
<p class="note">Lựa chọn thứ hai: ${escH(s2.p.name)} (${s2.pct}%)</p>
<div class="rc"><p class="k">Công thức ${escH(brew.toLowerCase())}</p><ol>${RECIPES[p.brew].map(x=>`<li>${escH(x)}</li>`).join('')}</ol></div>
<div class="order"><p class="k">Nhận tư vấn và đặt hàng</p><div class="p-form"><div class="row2">
<label for="ld-n">Họ tên<input id="ld-n" autocomplete="name" maxlength="80"></label>
<label for="ld-p">Số điện thoại hoặc Zalo<input id="ld-p" type="tel" inputmode="tel" autocomplete="tel" maxlength="20" placeholder="0901234567"></label></div>
<pre class="msg" id="ld-msg"></pre>
<div class="cta" style="margin-top:0"><a class="btn main off" id="ld-gf" target="_blank" rel="noopener" aria-disabled="true">Mở phiếu gửi MeDili</a><button class="btn" type="button" id="ld-cp">Sao chép tin nhắn</button><a class="btn" href="${ZALO}" target="_blank" rel="noopener">Nhắn Zalo</a></div>
<p class="fstat" id="ld-st" role="status"></p></div></div>
<div class="cta"><a class="btn" href="mua-hang.html">Xem ở Phòng chọn mua</a><button type="button" class="btn ghost" id="again">Làm lại</button></div>`;
renderTable(p.id);$('panel').querySelector('h2').setAttribute('tabindex','-1');$('panel').querySelector('h2').focus();
const sync=()=>{const nm=$('ld-n').value.trim(),ph=$('ld-p').value.replace(/[\s.()-]/g,''),full=txt+(nm?`\nKhách: ${nm}${ph?' | '+ph:''}`:'');$('ld-msg').textContent=full;
const g=$('ld-gf');if(nm&&/^(0\d{9,10}|\+\d{8,15})$/.test(ph)){const q=encodeURIComponent;g.href=FORM+'&'+FN.name+'='+q(nm)+'&'+FN.phone+'='+q(ph)+'&'+FN.txt+'='+q(full);g.classList.remove('off');g.removeAttribute('aria-disabled')}else{g.removeAttribute('href');g.classList.add('off');g.setAttribute('aria-disabled','true')}};
$('ld-n').addEventListener('input',sync);$('ld-p').addEventListener('input',sync);sync();
$('ld-gf').addEventListener('click',e=>{if(!$('ld-gf').getAttribute('href')){e.preventDefault();$('ld-st').textContent='Vui lòng nhập đúng họ tên và số điện thoại để mở phiếu gửi MeDili.';($('ld-n').value.trim()?$('ld-p'):$('ld-n')).focus()}else $('ld-st').textContent='Phiếu đã mở ở thẻ mới. Bấm Gửi ở cuối phiếu để hoàn tất.'});
$('ld-cp').addEventListener('click',async()=>{try{await navigator.clipboard.writeText($('ld-msg').textContent);$('ld-st').textContent='Đã sao chép tin nhắn. Mở Zalo MeDili rồi dán vào.'}catch(e){const r=document.createRange();r.selectNodeContents($('ld-msg'));const s=getSelection();s.removeAllRanges();s.addRange(r);$('ld-st').textContent='Đã chọn sẵn tin nhắn, bạn hãy sao chép rồi dán vào Zalo.'}});
$('again').addEventListener('click',()=>{st.i=0;st.ans=[];renderPicks();paintCup();renderTable();renderQuestion();$('panel').querySelector('.qopt').focus()})}
renderTable();paintCup();renderPicks();renderQuestion();
'''

TG_CSS = '''
.quizw{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);gap:16px;align-items:start}
@media (max-width:900px){.quizw{grid-template-columns:minmax(0,1fr)}.qs{order:-1}}
.qp{display:grid;gap:8px;min-height:360px;align-content:start}
.meter{display:flex;gap:4px}.meter i{flex:1;height:5px;border-radius:3px;background:var(--tint)}.meter i.on{background:var(--accent)}
.qo{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin:6px 0 4px}
@media (max-width:520px){.qo{grid-template-columns:minmax(0,1fr)}}
.qopt{display:grid;gap:2px;text-align:left;border:1px solid var(--rule);border-radius:12px;background:var(--bg);color:var(--ink);padding:12px 14px;cursor:pointer;font:inherit}
.qopt b{font:700 1.02rem var(--body)}.qopt span{font-size:.86rem;color:var(--muted)}
.qopt:hover{border-color:var(--accent)}.qopt[aria-pressed="true"]{border-color:var(--accent);background:var(--tint)}
.qs{display:grid;gap:8px;justify-items:center;text-align:center}
.cupw{padding:10px}
.cup{position:relative;width:170px;aspect-ratio:1;border-radius:50%;background:var(--panel);border:12px solid var(--tint);box-shadow:0 0 0 1px var(--rule),0 10px 24px rgba(46,28,18,.18);--coffee:rgb(120,70,38);--crema:rgb(190,140,88)}
.cup i{position:absolute;inset:8%;border-radius:50%;background:radial-gradient(circle at 48% 42%,var(--crema) 0 28%,var(--coffee) 72%);transition:background .35s}
.picks{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:6px;justify-content:center}
.picks li{font:600 .8rem var(--body);border:1px solid var(--rule);border-radius:999px;padding:4px 10px}
.picks li.em{border-style:dashed;color:var(--muted)}
.match{margin:0;color:var(--muted)}.match strong{font:800 1.6rem var(--display);color:var(--accent);margin-right:4px}
.prof{display:grid;gap:4px;margin:4px 0}.prof div{display:grid;grid-template-columns:110px auto;gap:10px;align-items:center}
.prof dt{font-size:.88rem;color:var(--muted)}.prof dd{margin:0;display:flex;gap:4px}.prof dd i{width:22px;height:8px;border-radius:4px;background:var(--tint)}.prof dd i.on{background:var(--accent)}
.quote2{display:grid;gap:2px;background:var(--tint);border-radius:12px;padding:12px 14px}.quote2 b{font:800 2rem var(--display);color:var(--accent)}
.rc ol{margin:4px 0 0;padding-left:20px}.rc li{margin-bottom:3px}
.order{border-top:1px solid var(--rule);padding-top:10px;margin-top:4px;display:grid;gap:8px}
.btn.off{opacity:.55;cursor:not-allowed}
.ptab th small{display:block;font-weight:400;color:var(--muted);font-size:.74rem}
.ptab td.n,.ptab th.n{text-align:right;font-family:var(--mono);font-variant-numeric:tabular-nums}
.ptab tr.grp td{font:700 .78rem var(--body);letter-spacing:.06em;text-transform:uppercase;color:var(--accent);padding-top:12px}
.ptab tr.top th,.ptab tr.top td{background:var(--tint);font-weight:700}
.ptab th[scope=row]{font-weight:600;white-space:normal;min-width:180px}
@media (prefers-reduced-motion:reduce){.cup i{transition:none}}
'''


def tim_gu(tg_js_data):
    body = head('MeDili · Tìm gu cà phê', 'Tìm gu <em>cà phê của bạn.</em>',
                'Sáu câu hỏi ngắn về cách bạn uống cà phê. Không có đáp án đúng, chỉ có ly cà phê đúng gu. Kết quả gợi ý một dòng cà phê MeDili, kèm giá theo lượng dùng và công thức pha.')
    body += '''
<section class="quizw">
 <div class="box qp" id="panel" aria-live="polite"></div>
 <aside class="box qs" aria-label="Ly cà phê của bạn">
  <div class="cupw"><div class="cup" id="cup"><i></i></div></div>
  <p class="k">Bạn đã chọn</p><ol class="picks" id="picks"></ol>
  <p class="note">Màu ly đổi theo độ đậm và loại sữa bạn chọn.</p>
 </aside>
</section>
<section class="box p-sec">
 <p class="eye">Bảng giá cà phê hạt</p>
 <h2 class="p-h2" style="margin:0">Mười một dòng <em>có giá sỉ.</em></h2>
 <p class="note">Đơn vị đ/kg cà phê rang. Giá chưa gồm 8% VAT và phí vận chuyển, có hiệu lực trong tháng. Túi 1 kg hoặc 5 kg. Giá sỉ tính theo tổng khối lượng mua trong tháng.</p>
 <div class="tw"><table class="ptab" id="price-table"></table></div>
 <div class="lnks"><a class="lnk" href="mua-hang.html">Xem đủ 14 dòng, tính lượng dùng và giá mỗi ly ở Phòng chọn mua</a></div>
</section>
'''
    js = (f"const ZALO={ZALO!r},FORM={FORM!r},FN={{name:{FORM_F['name']!r},phone:{FORM_F['phone']!r},txt:{FORM_F['txt']!r}}};\n"
          + tg_js_data + TG_UI)
    return doc('tim-gu.html', 'Tìm gu cà phê MeDili',
               'Sáu câu hỏi ngắn để tìm dòng cà phê MeDili hợp với cách bạn uống, kèm giá theo lượng dùng và công thức pha phin hoặc máy.',
               body, css=TG_CSS, js=js, wrap_cls='wrap pg')


# ---------- Liên hệ ----------
def lien_he():
    body = head('Liên hệ · Nhà rang cà phê MeDili', 'Kết nối từ vùng trồng <em>đến đối tác.</em>',
                'Bạn cần hỏi về cà phê Cà Sẻ Di Linh, cà phê rang, nhân xanh hay giải pháp cho quán, nhà hàng, khách sạn? Cách nhanh nhất là nhắn Zalo MeDili.')
    body += f'''
<section class="p-sec">{contact_methods()}</section>
<section class="p-sec"><h2 class="p-h2">Hai địa chỉ <em>của MeDili.</em></h2>{loc_cards()}</section>
<section class="box split">
 <div class="p-sec">
  <p class="eye">Tư vấn cà phê &amp; HORECA</p>
  <h2 class="p-h2" style="margin:0">Chọn cà phê <em>cho quán của bạn.</em></h2>
  <p>Chọn dòng cà phê, tính lượng dùng, giá vốn mỗi ly và bậc giá sỉ. Hồ sơ điều kiện sản xuất và an toàn thực phẩm sẽ được MeDili gửi khi trao đổi.</p>
  <div class="cta"><a class="btn main" href="horeca.html">Giải pháp HORECA</a><a class="btn" href="mua-hang.html">Phòng chọn mua</a><a class="btn" href="tim-gu.html">Tìm gu cà phê</a></div>
 </div>
 <ul class="pst" style="align-self:start">
  <li><span class="n">{icon('chat')}</span><h3>Nhắn Zalo</h3><p>Hỏi giá, đặt hàng, hẹn ghé xưởng hoặc quán.</p></li>
  <li><span class="n">{icon('mua')}</span><h3>Đặt qua phiếu</h3><p>Phòng chọn mua mở phiếu Google Form điền sẵn đơn hàng.</p></li>
 </ul>
</section>
'''
    return doc('lien-he.html', 'Liên hệ MeDili',
               'Liên hệ MeDili: Zalo và điện thoại 0966 770 788, email cafe@medili.vn, vườn và xưởng rang ở Thôn 11, Xã Di Linh, phân phối tại 143 Phạm Văn Hai, TP.HCM.',
               body, wrap_cls='wrap pg', contact=False)


# ---------- Giao hàng & đổi trả ----------
def giao_hang():
    body = head('Chính sách MeDili', 'Giao hàng <em>và đổi trả.</em>',
                'Cách đặt hàng, giao hàng và đổi trả cà phê MeDili. Mọi đơn hàng đều được MeDili xác nhận sản phẩm, quy cách, giá và phí giao trước khi giao.',
                '<a class="btn main" href="mua-hang.html">Đặt ở Phòng chọn mua</a><a class="btn" href="' + ZALO + '" target="_blank" rel="noopener">Hỏi qua Zalo</a><a class="btn" href="chinh-sach.html">Xem đủ chính sách</a>')
    items = [
        ('mua', 'Đặt hàng', 'Chọn cà phê ở Phòng chọn mua rồi mở phiếu đặt hàng, hoặc nhắn Zalo ' + PHONE + '. MeDili sẽ gọi lại để xác nhận đơn.'),
        ('so', 'Giá', 'Bảng giá đề xuất, có hiệu lực trong tháng, được xác nhận khi đặt hàng. Giá chưa gồm 8% VAT và phí vận chuyển.'),
        ('can', 'Giá sỉ', 'Giá bán lẻ áp dụng cho đơn dưới 5 kg. Mua từ 5 kg trong tháng được hưởng giá sỉ cấp 1. Khi đạt 20 kg trong tháng, phần chênh lệch được chiết khấu vào đơn kế tiếp.'),
        ('tui', 'Quy cách', 'Khách quán dùng túi 1 kg hoặc 5 kg. Khách lẻ có gói 250 g và 500 g; riêng Robusta Specialty và Culi, vui lòng liên hệ MeDili. Catimor, Culi và Blend MeDili chưa có giá sỉ, MeDili sẽ báo giá khi đặt hàng.'),
        ('xe', 'Giao hàng', 'Giao toàn quốc. Đơn từ 10 kg được miễn phí giao. Với đơn dưới 10 kg, phí và thời gian giao được báo trước khi xác nhận đơn.'),
        ('so', 'Thanh toán và hóa đơn', 'Thanh toán linh hoạt bằng chuyển khoản hoặc tiền mặt. Hóa đơn VAT do Công ty TNHH DSunfood xuất.'),
        ('doi', 'Đổi trả trong 7 ngày', 'Áp dụng cho lỗi sản xuất, lỗi đóng gói, hư hỏng khi vận chuyển hoặc giao sai loại. Bạn gửi mã đơn kèm ảnh hoặc video lỗi, MeDili phản hồi trong 3 ngày làm việc.'),
        ('ly', 'Hỗ trợ', 'Tư vấn chọn cà phê, độ xay, tỷ lệ pha, công thức cơ bản, thực đơn, máy xay và thiết bị pha chế. Phạm vi hỗ trợ được thống nhất với từng đối tác.'),
        ('khien', 'Cam kết', 'Cà phê nguyên chất, đúng thành phần công bố, không pha tạp, không thêm hương liệu hay chất bảo quản vào các dòng rang mộc.'),
    ]
    li = ''.join(f'<li><span class="n">{icon(i if i in ICON else "so")}</span><h3>{t}</h3><p>{d}</p></li>' for i, t, d in items)
    body += f'<section class="p-sec"><ol class="pst two">{li}</ol></section>'
    body += f'<section class="box p-sec"><p class="eye">Cần hỏi thêm</p><p>Nhắn Zalo hoặc gọi <span class="sel">{PHONE}</span>, email <span class="sel">{EMAIL}</span>. Khi đổi trả, bạn gửi kèm mã đơn để MeDili tra nhanh hơn.</p></section>'
    return doc('giao-hang.html', 'Giao hàng và đổi trả MeDili',
               'Chính sách đặt hàng, giá sỉ, quy cách đóng gói, giao hàng toàn quốc (miễn phí từ 10 kg), thanh toán và đổi trả trong 7 ngày của MeDili.',
               body, wrap_cls='wrap pg')


# ---------- Bảo mật ----------
def bao_mat():
    body = head('Chính sách bảo mật', 'Tôn trọng <em>thông tin của bạn.</em>',
                'Website MeDili giới thiệu cà phê và giúp bạn chuẩn bị đơn hàng. Trang này nêu rõ website sử dụng thông tin nào và dùng vào việc gì.')
    secs = [
        ('Thông tin bạn nhập trên website', 'Các ô nhập ở Phòng chọn mua, Tìm gu cà phê và trang HORECA chỉ dùng để soạn tin nhắn ngay trên máy của bạn. Website không tự gửi và không lưu những gì bạn nhập.'),
        ('Khi bạn gửi phiếu đặt hàng', 'Nút mở phiếu đưa bạn sang Google Forms với tên, số điện thoại và nội dung đơn đã điền sẵn. Thông tin chỉ đến MeDili khi bạn bấm Gửi trên phiếu đó. Google Forms do Google vận hành, theo chính sách riêng của Google.'),
        ('Khi bạn nhắn Zalo, gọi điện hoặc gửi email', 'MeDili dùng tên, số điện thoại, địa chỉ và nội dung bạn gửi để tư vấn, báo giá, xác nhận đơn và giao hàng.'),
        ('Cookie và đo lường', 'Các trang do MeDili soạn không cài cookie quảng cáo hay công cụ đo lường. Phông chữ được tải từ Google Fonts, nên trình duyệt của bạn kết nối tới máy chủ của Google. Website được lưu trữ trên máy chủ của đơn vị cung cấp dịch vụ hosting.'),
        ('Trang Giá cà phê', 'Trang Giá cà phê đọc bảng giá lưu trên chính website. Trang không thu thập thông tin người xem.'),
        ('Hỏi, sửa hoặc xóa thông tin', f'Muốn hỏi, sửa hoặc xóa thông tin đã gửi cho MeDili, bạn nhắn Zalo hoặc gọi {PHONE}, hoặc gửi email tới {EMAIL}.'),
    ]
    body += '<section class="p-sec"><div class="g2">' + ''.join(f'<div class="box"><h3>{t}</h3><p>{d}</p></div>' for t, d in secs) + '</div>'
    body += '<p class="note">Đây là thông báo bảo mật của website, chưa phải văn bản pháp lý đầy đủ. Đơn vị vận hành: Công ty TNHH DSunfood, ' + ADDR_HCM + '.</p></section>'
    return doc('bao-mat.html', 'Chính sách bảo mật MeDili',
               'Website MeDili sử dụng thông tin nào: các ô nhập chỉ soạn tin trên máy của bạn, phiếu đặt hàng qua Google Forms, không dùng cookie quảng cáo.',
               body, wrap_cls='wrap pg')
