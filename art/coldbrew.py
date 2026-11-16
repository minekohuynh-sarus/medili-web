# Cỗ máy Cold Brew MeDili: dây chuyền từ farm Di Linh đến chai cold brew và hộp túi ủ bán trên sàn TMĐT.
# Mô hình minh hoạ. Chiết xuất lạnh dùng cùng hệ số với Cỗ máy Chiết xuất. Màu theo phong thủy: không xanh lá, không đen.
from kit import *

FILE = 'cold-brew.html'
TITLE = 'Cỗ Máy Cold Brew MeDili'
DESC = ('Quy trình làm Cold Brew MeDili từ trái chín ở farm Di Linh đến chai cold brew và hộp túi ủ lạnh bán trên sàn thương mại điện tử: '
        'công thức theo mẻ, sản lượng, hạn dùng, bao bì, an toàn thực phẩm và hồ sơ cần có.')

SAFE = [
    ('khien', 'Cold brew là thực phẩm ít axit',
     'Cà phê pha nóng và cold brew có pH khoảng 4,85–5,13, cao hơn mốc 4,6 dùng để phân biệt thực phẩm axit. '
     'Trong chai kín, ít oxy, nếu để ấm, vi khuẩn Clostridium botulinum có thể sinh độc tố. Vì vậy chai cold brew phải giữ lạnh từ lúc ngâm đến lúc khách uống.',
     'Rao & Fuller 2018'),
    ('lanh', 'Ngâm lạnh, giữ lạnh dưới 5 °C',
     'Hướng dẫn an toàn thực phẩm cho cold brew không qua xử lý nhiệt: ngâm, bảo quản và phục vụ ở 5 °C trở xuống. '
     'Hướng dẫn của bình ủ thương mại: ngâm 16–20 giờ trong tủ lạnh dưới 4,4 °C.',
     'Wisconsin DATCP · Toddy'),
    ('hen', 'Hạn dùng ngắn nếu không xử lý',
     'Cùng hướng dẫn trên giới hạn ghi hạn tối đa 7 ngày kể từ ngày làm, với cơ sở không có kế hoạch HACCP. MeDili dùng mốc 7 ngày cho chai lạnh. '
     'Muốn hạn dài hơn phải kiểm nghiệm vi sinh theo thời gian, hoặc xử lý áp suất cao (HPP): một nghiên cứu cho thấy HPP 600 MPa trong 3 phút '
     'giảm hơn 6 log vi khuẩn gây bệnh và giữ an toàn 90 ngày, nhưng chưa thử với bào tử C. botulinum.',
     'Wisconsin DATCP · Polanco-Estibález 2023'),
    ('nhan', 'Không thổi nitơ, không đóng lon tuỳ tiện',
     'Ở Mỹ đã có những vụ thu hồi lon cold brew, kể cả loại thổi nitơ, vì quy trình có thể để C. botulinum sinh độc tố, '
     'hoặc quy trình cho thực phẩm ít axit đóng hộp chưa được duyệt. Chưa ghi nhận ca bệnh, nhưng cho thấy đóng kín, ít oxy là điểm rủi ro.',
     'Food Safety News 2017 · Daily Coffee News 2024'),
    ('soche', 'Nước, bồn, túi lọc sạch',
     'Dùng nước uống đạt chuẩn: nước RO đã kiểm nghiệm hoặc nước uống đóng bình. Bồn inox 304, túi lọc vải thực phẩm, chai và nắp được rửa, khử trùng, để khô trước mỗi mẻ. '
     'Mỗi lô có phiếu ghi giờ, nhiệt độ, TDS và lưu 2 chai mẫu đến hết hạn.',
     'Thực hành tốt của MeDili'),
    ('xe', 'Giao lạnh trong ngày',
     'Chai lạnh chỉ giao nội thành trong ngày, thùng xốp có đá gel, nhắc khách cất tủ lạnh ngay khi nhận. Không gửi chai lạnh đi tỉnh bằng giao hàng thường. '
     'Bán toàn quốc trên sàn thì dùng túi ủ lạnh: hàng khô, khách tự ủ ở nhà.',
     'Thực hành tốt của MeDili'),
]

DOCS = [
    ('so', 'Đăng ký kinh doanh có ngành thực phẩm',
     'Công ty TNHH DSunfood đứng tên tổ chức chịu trách nhiệm về sản phẩm. Kiểm tra ngành nghề sản xuất, kinh doanh thực phẩm trên giấy đăng ký.'),
    ('khien', 'Giấy chứng nhận cơ sở đủ điều kiện an toàn thực phẩm',
     'Bắt buộc với nơi sản xuất (Điều 11 Nghị định 15/2018), trừ các trường hợp ở Điều 12, ví dụ cơ sở đang có HACCP, ISO 22000 hoặc FSSC 22000 còn hiệu lực. '
     'Nếu thuê gia công, chọn xưởng đã có giấy này. Cơ sở chỉ kinh doanh thực phẩm bao gói sẵn không thuộc diện cấp.'),
    ('kinh', 'Kiểm nghiệm sản phẩm',
     'Gửi mẫu tới phòng kiểm nghiệm được chỉ định hoặc đạt ISO 17025. Phiếu kết quả phải trong vòng 12 tháng tính đến ngày nộp hồ sơ. Phòng kiểm nghiệm tư vấn bộ chỉ tiêu: '
     'chai cold brew thường đối chiếu QCVN 6-2:2010/BYT cho đồ uống không cồn, túi ủ là cà phê rang xay, tham khảo TCVN 5251:2015.'),
    ('so', 'Tự công bố sản phẩm',
     'Theo Điều 4–5 Nghị định 15/2018: bản tự công bố theo Mẫu 01 kèm phiếu kiểm nghiệm; đăng công khai trên trang web của mình hoặc niêm yết tại trụ sở, '
     'nộp 1 bản cho cơ quan do UBND tỉnh chỉ định. Được bán ngay sau khi tự công bố. Nghị định 15/2018 đang áp dụng vì Nghị định 46/2026 tạm ngưng từ 06/04/2026 '
     'theo Nghị quyết 15/2026. Kiểm tra lại khi Luật An toàn thực phẩm sửa đổi có hiệu lực.'),
    ('tui', 'Nhãn đủ nội dung bắt buộc',
     'Theo Nghị định 43/2017, sửa đổi bởi Nghị định 111/2021: tên sản phẩm, tổ chức chịu trách nhiệm, xuất xứ, định lượng, ngày sản xuất, hạn sử dụng, thành phần, '
     'hướng dẫn sử dụng, bảo quản và cảnh báo. Nhãn phụ ở phần Bao bì tự điền theo mẻ.'),
    ('mua', 'Đăng bán trên sàn',
     'Đưa bản tự công bố và giấy tờ lên gian hàng khi sàn yêu cầu với ngành hàng thực phẩm, đồ uống. Ghi đúng cách bảo quản và khu vực giao. '
     'Quy định từng sàn thay đổi theo thời gian, kiểm tra trong trung tâm người bán trước khi đăng.'),
]

SRC = [
    ('Toddy Commercial Cold Brewer: 5 lb cà phê, 14 quart nước, ngâm 16–20 giờ trong tủ lạnh dưới 40 °F, pha cốt 1:1', 'Hướng dẫn của Toddy',
     'https://cdn.shopify.com/s/files/1/0190/2618/files/Cold_Brew_Instructions_Updated_0916.pdf'),
    ('Cold brew coffee fact sheet: giữ dưới 41 °F, ghi hạn tối đa 7 ngày nếu không có HACCP', 'Wisconsin DATCP',
     'https://datcp.wi.gov/Documents2/ColdBrewFactSheet.pdf'),
    ('Rao N. Z., Fuller M. (2018). pH cà phê 4,85–5,13, Scientific Reports', 'ScienceDaily', 'https://www.sciencedaily.com/releases/2018/11/181101085137.htm'),
    ('Fuller M., Rao N. Z. (2017). Caffeine và CGA trong cold brew đạt cân bằng sau 6–7 giờ, Scientific Reports 7, 17979', 'PubMed',
     'https://pubmed.ncbi.nlm.nih.gov/29269877/'),
    ('Polanco-Estibález B. và cộng sự (2023). High-Pressure Processing for Cold Brew Coffee, Foods 12(23), 4231', 'MDPI', 'https://mdpi.com/2304-8158/12/23/4231'),
    ('Death Wish Coffee pulls Nitro because of botulism risk (2017)', 'Food Safety News',
     'https://www.foodsafetynews.com/2017/09/death-wish-coffee-pulls-nitro-because-of-botulism-risk/'),
    ('Snapchill recalls all cold brew cans due to toxic growth risk (2024)', 'Daily Coffee News',
     'https://dailycoffeenews.com/2024/06/19/snapchill-recalls-all-cold-brew-cans-due-to-toxic-growth-risk'),
    ('Nghị định 15/2018/NĐ-CP hướng dẫn Luật An toàn thực phẩm, Điều 4, 5, 11, 12', 'caselaw.vn',
     'https://caselaw.vn/van-ban-phap-luat/302817-nghi-dinh-so-15-2018-nd-cp-ngay-02-02-2018-cua-chinh-phu-huong-dan-luat-an-toan-thuc-pham'),
    ('Nghị quyết 15/2026/NQ-CP tạm ngưng Nghị định 46/2026, tiếp tục áp dụng Nghị định 15/2018', 'Sở Tư pháp Cần Thơ',
     'https://pbgdpl.cantho.gov.vn/tam-ngung-hieu-luc-nghi-dinh-so-462026nd-cp-den-khi-co-luat-an-toan-thuc-pham-sua-doi'),
    ('Nội dung bắt buộc trên nhãn theo Nghị định 111/2021/NĐ-CP', 'Sở KH&CN Sóc Trăng',
     'https://soctrang.gov.vn/SiteFolders/sokhcn/Nam%202025/Thang%203/huong%20dan%20ghi%20nhan.pdf'),
    ('QCVN 6-2:2010/BYT đối với đồ uống không cồn', 'Thư viện Pháp luật',
     'https://thuvienphapluat.vn/van-ban/Thuong-mai/Thong-tu-35-2010-TT-BYT-Quy-chuan-ky-thuat-quoc-gia-cac-san-pham-107526.aspx'),
    ('TCVN 5251:2015 Cà phê bột', 'Thư viện Pháp luật', 'https://thuvienphapluat.vn/TCVN/Cong-nghe-Thuc-pham/TCVN-5251-2015-Ca-phe-bot-914830.aspx'),
]


def page():
    safe = ''.join(f'<div class="box rd">{icon(i)}<h3>{t}</h3><p>{p}</p></div>' for i, t, p, s in SAFE)
    docs = ''.join(f'<li><span class="n">{icon(i)}</span><h3><small>{n:02d}</small>{t}</h3><p>{p}</p></li>' for n, (i, t, p) in enumerate(DOCS, 1))
    src = ''.join(f'<li>{t}. <a href="{u}" target="_blank" rel="noopener">{n} ↗</a></li>' for t, n, u in SRC)
    body = f'''
<header>
  {logo()}<div class="brandbar"><span>Mê vị Di Linh</span><span>Mô hình sản phẩm</span><span>Zalo <a href="#lien-he">{PHONE_RAW}</a></span></div>
  <h1>Cỗ máy <em>Cold Brew MeDili</em></h1>
  <p>Từ trái chín ở farm MeDili, Di Linh, đến chai cold brew và hộp túi ủ lạnh bán trên sàn thương mại điện tử. Chọn dạng sản phẩm, chỉnh mẻ, xem công thức, sản lượng, hạn dùng, bao bì và hồ sơ cần có.</p>
</header>

<div class="bench">
  <div class="card">
    <div class="fighead">
      <div><b>Hình 1</b> <span id="figsub"></span></div>
      <button class="btn small" id="run2" type="button">Chạy dây chuyền</button>
    </div>
    <div class="scroller"><svg id="scene" viewBox="0 0 1040 720" aria-label="Dây chuyền mười trạm từ vườn cà phê Di Linh đến kiện hàng Cold Brew MeDili. Bấm từng trạm để xem chi tiết."></svg></div>
    <div class="strip" id="strip" role="group" aria-label="Chọn trạm"></div>
    <div id="detail" aria-live="polite"></div>
  </div>

  <aside class="card ctl">
    <div class="head2"><h3>Dạng sản phẩm</h3><small>3 dạng</small></div>
    <div class="row" id="fmts"></div>
    <p class="mnote" id="fNote"></p>
    <div class="head2" style="margin-top:12px"><h3>Cà phê từ farm MeDili</h3></div>
    <div class="row" id="beans"></div>
    <p class="mnote" id="bNote"></p>
    <hr>
    <div class="sl" style="margin-top:0"><label for="iR">Cà phê rang mỗi mẻ <output id="oR"></output></label><input id="iR" type="range" min="2" max="60" step="1"></div>
    <div id="grpC">
      <div class="sl"><label for="iRa">Tỷ lệ cà phê : nước <output id="oRa"></output></label><input id="iRa" type="range" min="4" max="10" step="0.5"><p>1:5 cho cốt cô đặc. Bình ủ thương mại thường dùng khoảng 1:5,8.</p></div>
      <div class="sl"><label for="iT">Nhiệt độ ngâm <output id="oT"></output></label><input id="iT" type="range" min="2" max="28" step="1"><p id="tNote"></p></div>
      <div class="sl"><label for="iH">Thời gian ngâm <output id="oH"></output></label><input id="iH" type="range" min="8" max="24" step="1"></div>
      <div class="sl" id="grpR"><label for="iS">Độ đậm chai uống liền <output id="oS"></output></label><input id="iS" type="range" min="1.2" max="2.4" step="0.1"><p>TDS đo bằng khúc xạ kế. Ly lọc chuẩn SCA khoảng 1,15–1,35 %, cold brew uống liền thường đậm hơn.</p></div>
      <div class="head2" style="margin-top:12px"><h3>Dung tích chai</h3></div><div class="row" id="vols"></div>
    </div>
    <div id="grpB">
      <div class="sl"><label for="iB">Cà phê mỗi túi lọc <output id="oB"></output></label><input id="iB" type="range" min="20" max="60" step="5"><p id="bgNote"></p></div>
      <div class="head2" style="margin-top:12px"><h3>Túi mỗi hộp</h3></div><div class="row" id="pers"></div>
    </div>
    <div class="row" style="margin-top:14px"><button class="btn main" id="run" type="button">Chạy dây chuyền</button><button class="btn" id="reset" type="button">Về công thức chuẩn</button></div>
    <div class="stats" id="stats"></div>
    <div id="verdict"></div>
    <hr>
    <span class="lbl" id="cLbl"></span>
    <div class="charts"><svg class="ch" id="cT" viewBox="0 0 340 162" role="img" aria-label="Độ đậm cốt cold brew theo số giờ ngâm"></svg></div>
    <div class="lg" id="lgT"></div>
    <div id="tip"></div>
  </aside>
</div>

<section class="card" id="cong-thuc">
  <h2 id="sopH"></h2>
  <p class="lead">Làm theo đúng thứ tự. Số liệu tính theo mẻ đang chọn ở Hình 1. TDS là ước tính của mô hình, mỗi lô đo thật bằng khúc xạ kế.</p>
  <ol class="sop" id="sop"></ol>
  <div class="cols eqc">
    <div><h3 class="eqh">Dụng cụ và vật tư cho mẻ này</h3><div class="tw"><table class="rich"><thead><tr><th>Dụng cụ</th><th>Cho mẻ này</th><th>Ghi chú</th></tr></thead><tbody id="eqT"></tbody></table></div></div>
    <div><h3 class="eqh">Phiếu lô</h3><p class="mnote" style="margin:0 0 8px">Chép hoặc in phiếu, điền tay mỗi lô. Giữ phiếu ít nhất đến hết hạn dùng của lô.</p><pre class="msg" id="sheet"></pre><button class="btn small" id="cpSh" type="button">Sao chép phiếu lô</button> <span class="cpst" id="cpShS" role="status"></span></div>
  </div>
</section>

<section class="card" id="bao-bi">
  <h2>Hình 3: bao bì Cold Brew MeDili</h2>
  <p class="lead">Màu thương hiệu MeDili: kem, nâu cà phê, đỏ đất và vàng đất. Chai và hộp đổi chữ theo dạng sản phẩm và mẻ đang chọn. Nhãn phụ tự điền ngày sản xuất, hạn dùng và mã lô.</p>
  <div class="pk">
    <figure><div class="pkw" id="pkBottle"></div><figcaption id="pkBc"></figcaption></figure>
    <figure><div class="pkw" id="pkBox"></div><figcaption id="pkXc"></figcaption></figure>
    <figure class="pkl"><div class="backlbl" id="backlbl"></div><figcaption>Nhãn phụ mẫu theo Nghị định 111/2021. Điền số tự công bố sau khi có, đối chiếu địa chỉ với giấy đăng ký kinh doanh trước khi in.</figcaption><button class="btn small" id="cpLbl" type="button">Sao chép nội dung nhãn</button> <span class="cpst" id="cpLblS" role="status"></span></figure>
  </div>
  <div class="g3 pkspec">
    <div class="box"><span class="k">Chai</span><h3>Thủy tinh nâu</h3><p>Chai 250–500 ml, nắp thiếc có vòng niêm phong. Thủy tinh nâu chắn bớt ánh sáng, giữ màu và mùi. Nhãn decal giấy chống ẩm quấn thân, không bong khi đọng hơi nước.</p></div>
    <div class="box"><span class="k">Túi ủ</span><h3>Túi lọc và túi bạc</h3><p>Túi lọc không dệt dùng cho thực phẩm, có dây và thẻ MeDili. 5 túi trong một túi bạc nhiều lớp có van một chiều, thổi nitơ rồi hàn.</p></div>
    <div class="box"><span class="k">Hộp</span><h3>Kraft in hai màu</h3><p>Hộp giấy kraft in nâu cà phê và đỏ đất, hướng dẫn ủ ở mặt sau. Thùng giao chai lạnh là thùng xốp có đá gel, băng keo đỏ in "Giữ lạnh 0–4 °C".</p></div>
  </div>
</section>

<section class="card" id="ban-san">
  <h2>Bán trên sàn: dạng nào đi kênh nào</h2>
  <p class="lead">Chai lạnh có hạn 7 ngày và cần giữ lạnh, nên chỉ hợp kênh giao nhanh nội thành. Túi ủ là hàng khô, đi được mọi sàn và mọi tỉnh.</p>
  <div class="cols">
    <div class="tw"><table class="rich"><thead><tr><th>Dạng</th><th>Bán ở đâu</th><th>Giao</th><th>Hạn dùng</th></tr></thead><tbody>
      <tr><td><b>Túi ủ lạnh</b></td><td>Gian hàng MeDili trên Shopee, TikTok Shop, Lazada, toàn quốc</td><td>Giao thường, nhiệt độ thường</td><td>6 tháng, mốc đề xuất</td></tr>
      <tr><td><b>Chai cô đặc</b></td><td>Nội thành TP.HCM: GrabMart, ShopeeFood, quán MeDili, hoặc giao trong ngày trên sàn nếu khu vực có hỗ trợ</td><td>Thùng xốp đá gel, trong ngày</td><td>7 ngày, 0–4 °C</td></tr>
      <tr><td><b>Chai uống liền</b></td><td>Như chai cô đặc, thêm văn phòng và quán đặt định kỳ</td><td>Thùng xốp đá gel, trong ngày</td><td>7 ngày, 0–4 °C</td></tr>
    </tbody></table></div>
    <div><span class="lbl">Tiêu đề và mô tả gợi ý cho dạng đang chọn</span><pre class="msg" id="lst"></pre><button class="btn small" id="cpLst" type="button">Sao chép mô tả</button> <span class="cpst" id="cpLstS" role="status"></span></div>
  </div>
</section>

<section class="p-sec">
  <p class="eye">An toàn thực phẩm</p>
  <h2 class="p-h2" style="margin:0">Sáu điều <em>không được bỏ qua.</em></h2>
  <p class="lead" style="margin:0 0 4px">Cold brew ngon nhờ ngâm lạnh lâu, và cũng vì thế mà cần giữ vệ sinh, giữ lạnh nghiêm hơn cà phê pha nóng.</p>
  <div class="g3">{safe}</div>
</section>

<section class="card">
  <h2>Hồ sơ để bán hợp lệ</h2>
  <p class="lead">Sáu việc trước khi đăng Cold Brew MeDili lên sàn. Thông tin tham khảo theo văn bản đang áp dụng tháng 11/2026, đối chiếu văn bản gốc hoặc hỏi cơ quan quản lý trước khi nộp hồ sơ.</p>
  <ol class="pst two">{docs}</ol>
</section>

<section class="card src">
  <h2>Nguồn và cách đọc mô hình</h2>
  <p class="lead">Chiết xuất lạnh dùng cùng mô hình với Cỗ máy Chiết xuất: trần chiết xuất 21 % ở nước lạnh, bã giữ khoảng 2 lít nước mỗi kg bột. Hao hụt rang City+ 17,5 % theo Phòng rang. 100 kg trái chín cho khoảng 18 kg nhân xanh theo trang Cấu tạo trái. Túi ủ dùng tỷ lệ 1:8 và 18–24 giờ như công thức cold brew ở Quầy pha. Mọi con số là ước tính để lên kế hoạch, không thay cho kiểm nghiệm.</p>
  <ul>{src}</ul>
  <div class="lnks"><a class="lnk" href="chiet-xuat.html">Cỗ máy Chiết xuất</a><a class="lnk" href="rang.html">Phòng rang</a><a class="lnk" href="quay-pha.html">Quầy pha: cold brew tại quán</a><a class="lnk" href="trai-ca-phe.html">Cấu tạo trái</a><a class="lnk" href="vung-trong.html">Vùng trồng Di Linh</a><a class="lnk" href="mua-hang.html">Phòng Chọn Mua</a></div>
</section>
'''
    return doc(FILE, TITLE, DESC, body, css=CSS, js=JS_HEAD + JS)


CSS = r'''
/* Cỗ máy Cold Brew MeDili */
.mnote{font-size:.84rem;color:var(--muted);margin:8px 0 0;line-height:1.45}
#scene .gl{fill:var(--panel);fill-opacity:.18}
#scene .glt{fill:var(--panel);fill-opacity:.12}
#scene .liqt{fill:#4A2A18}
#scene .grd{fill:#5A3520}#scene .grdT{fill:#6B4226}
#scene .beanT{fill:#5E3920}
#scene .cherT{fill:#7A2A1C}
#scene .hill{fill:#B8894A}#scene .hillT{fill:#D9B77E}
#scene .bed{fill:#D9C39A}#scene .bed2{fill:#B9A274}
#scene .amb{fill:#6E3F1C}#scene .ambT{fill:#8A5226}
#scene .capc{fill:#C9A15B}
#scene .labc{fill:#F4E8D2}
#scene .kr{fill:#DDBB7A}#scene .kr2{fill:#C9A15B}#scene .kr3{fill:#A9823F}
#scene .foil{fill:#DCD3C4}#scene .foil2{fill:#C4B9A6}#scene .foil3{fill:#AFA38E}
#scene .bagw{fill:#F6F0E4}#scene .bagw2{fill:#E3D9C6}
#scene .pcl{fill:#F4ECDD}#scene .pcl2{fill:#E3D6BE}#scene .pcl3{fill:#CDBD9F}
#scene .door{fill:var(--panel);fill-opacity:.35;stroke:var(--ol);stroke-width:1.2}
#scene .lcdb{fill:#2E1C12;stroke:none}
#scene .lcd{font:700 7.6px var(--mono);fill:#F3D9A4}
#scene .wtx{font:700 8px var(--body);fill:#3A2416}
#scene .ptx{font:800 9px var(--display);fill:#4A2C1A;letter-spacing:.04em}
#scene .frost{stroke:#FFF6EC;stroke-width:1.6;stroke-linecap:round;fill:none;opacity:.9}
#scene .flowT{font-size:12.5px}
#tok{display:none;fill:var(--accent);stroke:var(--panel);stroke-width:2}
.running #tok{display:block}
.lg{display:flex;flex-wrap:wrap;gap:4px 16px;font-size:.82rem;margin:2px 0 0;color:var(--muted)}
.lg span{display:inline-flex;align-items:center;gap:6px}
.sw2{display:inline-block;width:16px;height:0;border-top:2.5px solid;flex:none}.sw2.d{border-top-style:dashed}
#tip{color:var(--muted)}
.sop li>p{font-size:.88rem}.sop li>p .lbl{margin-bottom:1px}
.pk{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.05fr) minmax(0,1.1fr);gap:16px;align-items:stretch;margin-top:4px}
.pk figure{margin:0;display:flex;flex-direction:column;gap:10px;align-items:center;justify-content:space-between;background:var(--tint);border-radius:16px;padding:18px 14px 14px;min-width:0}
.pkw{width:100%;flex:1;display:grid;place-items:center}
.pkw svg{display:block;width:100%;height:auto}
#pkBottle svg{max-width:210px}#pkBox svg{max-width:300px}
.pk figcaption{font-size:.84rem;color:var(--muted);text-align:center;max-width:44ch}
.pk .pkl{align-items:stretch}
.backlbl{background:#F4E8D2;color:#3A2416;border:1px solid #C9B58F;border-radius:10px;padding:14px 16px;font:500 .79rem/1.5 var(--body);box-shadow:0 1px 0 #E3D3B3 inset}
.backlbl h4{margin:0 0 6px;font:800 1.05rem/1.15 var(--display);letter-spacing:.03em;color:#4A2C1A}
.backlbl p{margin:0 0 4px}.backlbl b{color:#4A2C1A}
.backlbl .dt{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;margin:8px 0;padding:8px 0;border-block:1px dashed #C9B58F;font:700 .76rem var(--mono)}
.backlbl .dt span{display:block;font:600 .64rem var(--body);letter-spacing:.06em;text-transform:uppercase;color:#7A5A3A}
.backlbl .red{color:#9E3B26;font-weight:700}
.pk .btn{align-self:flex-start}
.cpst{font-size:.84rem;color:var(--muted)}
.pkspec{margin-top:14px}
.pkspec .box{background:var(--bg)}
@media (max-width:1080px){.pk{grid-template-columns:repeat(2,minmax(0,1fr))}.pk .pkl{grid-column:1/-1}}
@media (max-width:620px){.pk{grid-template-columns:minmax(0,1fr)}}
.pkT{font:800 23px var(--display);letter-spacing:.05em}
.pkS{font:700 11px var(--body)}.pkS2{font:500 9.5px var(--body)}.pkB{font:700 9.6px var(--body);letter-spacing:.1em}
.pkTag{font:700 7.6px var(--body);letter-spacing:.06em}
#lst{min-height:160px}
.eqc{margin-top:18px;padding-top:16px;border-top:1px solid var(--rule)}
.eqh{font:700 1.05rem var(--body);margin:0 0 8px}
#eqT td{min-width:0}#eqT td:first-child{width:40%}
#sheet{min-height:220px}
.rd{display:flex;flex-direction:column;gap:4px}
.rd>svg.pi{width:30px;height:30px;color:var(--accent);margin-bottom:2px}
.rd h3{font:800 1.4rem/1.15 var(--display);margin:2px 0 4px}
.rd .ft{margin-top:auto}
.src>h2{color:var(--ink)}.src>.lead{color:var(--muted);font-size:.95rem}
.src ul{line-height:1.5}.src li{margin-bottom:4px}
.src .lnks{margin-top:12px}
@media (prefers-reduced-motion:reduce){.running #tok{display:none}}
'''

JS_HEAD = f"const ADDR={ADDR_HCM!r},ADDR_FARM={ADDR_FARM!r},PHONE={PHONE!r};\n"

JS = r'''
/* ====== DỮ LIỆU ====== */
const $=id=>document.getElementById(id);
const vn=(n,d=1)=>n.toFixed(d).replace('.',',');
const fm=n=>Math.round(n).toLocaleString('de-DE');
const clamp=(v,a,b)=>Math.min(b,Math.max(a,v));
const NB=' ';
const g1=n=>Number.isInteger(n)?String(n):vn(n,1);
/* chiết xuất lạnh: cùng hệ số với Cỗ máy Chiết xuất (cold brew, xay thô, rang vừa) */
const K0=.442,BETA=.716,FT=T=>Math.exp(.035*(T-93)),EYM=T=>28-7*clamp((93-T)/73,0,1);
const CBM=(()=>{const x=-Math.log(1-19/EYM(20));return x/(Math.pow(840,BETA)*K0*.6*FT(20))})();
const EY=(T,h,r)=>EYM(T)*(1-Math.exp(-K0*CBM*.6*FT(T)*Math.pow(r/8,.12)*Math.pow(Math.max(h,0)*60,BETA)));
const LOSS=.175,GREEN=.18,RET=2;
const FMT={
 conc:{n:'Chai cô đặc',life:7,note:'Cốt cold brew đậm, khách pha 1 phần cốt với 2 phần nước, sữa hoặc đá. Giữ lạnh 0–4 °C, giao nội thành trong ngày.'},
 rtd:{n:'Chai uống liền',life:7,note:'Pha loãng sẵn tới độ đậm uống liền, mở nắp là uống. Giữ lạnh 0–4 °C, giao nội thành trong ngày.'},
 bag:{n:'Túi ủ lạnh',life:180,note:'Cà phê xay thô trong túi lọc, khách tự ủ trong tủ lạnh. Hàng khô nên giao được toàn quốc qua sàn.'}};
const BEAN={
 rp:{n:'Robusta Premium',proc:'honey',full:'Robusta Premium, sơ chế honey',note:'Dòng MeDili gợi ý cho cold brew: ngọt, caramel, đường nâu, ít gắt khi ủ lạnh.',cher:'#9A5A2B'},
 rc:{n:'Robusta Classic',proc:'natural',full:'Robusta Classic, phơi nguyên trái',note:'Đậm, cacao đen, hậu dày. Hợp uống với sữa.',cher:'#6E2418'}};
const DEF={f:'conc',bean:'rp',R:10,ratio:5,T:4,h:18,tds:1.6,vol:250,bag:35,per:10};
const st={...DEF,sel:5};
const use=(i,f=st.f)=>[[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,0],[1,1,0],[1,1,0],[0,0,1],[1,1,1],[1,1,1]][i-1][f==='conc'?0:f==='rtd'?1:2];

/* ====== MÔ HÌNH MẺ ====== */
function calc(){
 const s=st,green=s.R/(1-LOSS),cherry=green/GREEN,r={green,cherry,life:FMT[s.f].life};
 if(s.f==='bag'){r.bags=Math.floor(s.R*1000*.99/s.bag);r.boxes=Math.floor(r.bags/s.per);r.water=s.bag*8;r.out=r.water-RET*s.bag;r.tdsB=EY(4,20,8)*s.bag/r.out;return r}
 r.W=s.R*s.ratio;const bev=Math.max(0,r.W-RET*s.R);r.Vc=bev*.98;r.ey=EY(s.T,s.h,s.ratio);r.tdsC=bev>0?r.ey*s.R/bev:0;
 r.low=s.f==='rtd'&&r.tdsC<s.tds;
 r.Vout=s.f==='rtd'&&!r.low?r.Vc*r.tdsC/s.tds:r.Vc;r.add=r.Vout-r.Vc;
 r.n=Math.floor(r.Vout*1000*.99/s.vol);return r}
function verdict(r){
 const s=st;
 if(s.f==='bag')return {k:'good',t:'Hàng khô, giao toàn quốc',m:`Khách ủ 1 túi với ${s.bag*8}${NB}ml nước trong ngăn mát 18–24 giờ, được khoảng ${fm(r.out)}${NB}ml cốt, TDS khoảng ${vn(r.tdsB,1)}${NB}%, pha 1:1 khi uống. Hạn dùng đề xuất 6 tháng, xác lập bằng kiểm nghiệm.`};
 if(s.T>8)return {k:'bad',t:`Ngâm ở ${s.T}${NB}°C không hợp chai bán ra ngoài`,m:'Ngâm ở nhiệt độ phòng chỉ hợp cho quán pha và dùng trong ngày. Chai bán online nên ngâm ở 2–5 °C để hạn chế vi sinh.'};
 if(r.low)return {k:'bad',t:'Cốt chưa đủ đậm để pha loãng',m:`Cốt chỉ đạt TDS khoảng ${vn(r.tdsC,1)}${NB}%, thấp hơn mốc uống liền ${vn(s.tds,1)}${NB}%. Tăng lượng cà phê (tỷ lệ 1:4–1:5) hoặc ngâm lâu hơn.`};
 if(s.h<12)return {k:'warn',t:'Ngâm hơi ngắn',m:`Ở ${s.T}${NB}°C, ${s.h} giờ chưa kéo đủ chất, cốt TDS khoảng ${vn(r.tdsC,1)}${NB}%. Hướng dẫn thường gặp là 16–20 giờ trong tủ lạnh.`};
 if(s.h>22)return {k:'warn',t:'Ngâm hơi dài',m:'Qua khoảng 20 giờ, cốt đậm thêm rất ít mà dễ có vị gỗ, chát. Thử dừng ở 18–20 giờ.'};
 if(s.f==='conc')return {k:'good',t:'Công thức đạt cho chai cô đặc',m:`Cốt TDS khoảng ${vn(r.tdsC,1)}${NB}%, pha 1:2 ra ly khoảng ${vn(r.tdsC/3,1)}${NB}%. Giữ 0–4 °C, hạn 7 ngày, giao nội thành trong ngày.`};
 return {k:'good',t:'Công thức đạt cho chai uống liền',m:`Pha ${vn(r.Vc,1)}${NB}L cốt với ${vn(r.add,1)}${NB}L nước tới TDS ${vn(s.tds,1)}${NB}%. Giữ 0–4 °C, hạn 7 ngày, giao nội thành trong ngày.`};
}

/* ====== HÌNH HỌC ====== */
const U=7,OX=196,OY=118;
const P=(x,y,z=0)=>[OX+(x-y)*.866*U,OY+(x+y)*.5*U-z*U];
const f1=n=>n.toFixed(1);
const pts=a=>a.map(q=>q.map(f1).join(',')).join(' ');
const poly=(a,c='')=>`<polygon points="${pts(a)}" class="${c}"/>`;
const line=(a,w,col)=>`<polyline points="${pts(a)}" fill="none" style="${w?`stroke-width:${w};`:''}${col?`stroke:${col}`:''}"/>`;
function box(x,y,z,w,d,h,c=['f1','f2','f3']){return poly([P(x,y+d,z),P(x+w,y+d,z),P(x+w,y+d,z+h),P(x,y+d,z+h)],c[1])+poly([P(x+w,y,z),P(x+w,y+d,z),P(x+w,y+d,z+h),P(x+w,y,z+h)],c[2])+poly([P(x,y,z+h),P(x+w,y,z+h),P(x+w,y+d,z+h),P(x,y+d,z+h)],c[0])}
const RX=r=>r*U*1.2247,RY=r=>r*U*.7071;
function cyl(cx,cy,z,r,h,c='f2',top='f1'){const [a,b]=P(cx,cy,z),[,t]=P(cx,cy,z+h),rx=RX(r),ry=RY(r);return `<path class="${c}" d="M${f1(a-rx)} ${f1(t)}V${f1(b)}A${f1(rx)} ${f1(ry)} 0 0 0 ${f1(a+rx)} ${f1(b)}V${f1(t)}Z"/><ellipse class="${top}" cx="${f1(a)}" cy="${f1(t)}" rx="${f1(rx)}" ry="${f1(ry)}"/>`}
function side(cx,cy,z,r,h,c){const [a,b]=P(cx,cy,z),[,t]=P(cx,cy,z+h),rx=RX(r),ry=RY(r);return `<path class="${c}" d="M${f1(a-rx)} ${f1(t)}V${f1(b)}A${f1(rx)} ${f1(ry)} 0 0 0 ${f1(a+rx)} ${f1(b)}V${f1(t)}A${f1(rx)} ${f1(ry)} 0 0 1 ${f1(a-rx)} ${f1(t)}Z"/>`}
function frus(cx,cy,z0,r0,z1,r1,c,top){const [a,b0]=P(cx,cy,z0),[,b1]=P(cx,cy,z1),x0=RX(r0),y0=RY(r0),x1=RX(r1),y1=RY(r1);return `<path class="${c}" d="M${f1(a-x1)} ${f1(b1)}L${f1(a-x0)} ${f1(b0)}A${f1(x0)} ${f1(y0)} 0 0 0 ${f1(a+x0)} ${f1(b0)}L${f1(a+x1)} ${f1(b1)}Z"/><ellipse class="${top}" cx="${f1(a)}" cy="${f1(b1)}" rx="${f1(x1)}" ry="${f1(y1)}"/>`}
const face=(x,y,z)=>{const q=P(x,y,z);return `matrix(.866 .5 0 1 ${f1(q[0])} ${f1(q[1])})`};
const lcd=(x,y,z,w,id)=>`<g transform="${face(x,y,z)}"><rect class="lcdb" x="0" y=".8" width="${w}" height="9" rx="1.4"/><text class="lcd" id="${id}" x="${w/2}" y="7.9" text-anchor="middle"></text></g>`;
const stG=(i,inner)=>`<g class="st m" data-i="${i}" tabindex="0" role="button" aria-label="Trạm ${i}: ${ST[i-1].n}">${inner}</g>`;
function bottle(x,y,z,lab){return cyl(x,y,z,.7,2.5,'amb','ambT')+(lab?side(x,y,z+.7,.72,1.15,'labc'):'')+cyl(x,y,z+2.5,.34,.75,'amb','ambT')+cyl(x,y,z+3.25,.38,.32,'capc','capc')}

/* ====== 10 TRẠM ====== */
const ST=[
 {n:'Vườn Di Linh',sub:()=>'Farm MeDili, Thôn 11, Xã Di Linh',
  mech:r=>`Cà phê cho Cold Brew MeDili là Robusta từ farm MeDili ở Di Linh. Chỉ hái trái chín đỏ: trái xanh cho vị ngái, chát; trái chín quá dễ lên men lạ. Mẻ này cần khoảng <b>${fm(r.cherry)}${NB}kg trái tươi</b>, theo tỷ lệ của MeDili: 100${NB}kg trái tươi cho khoảng 18${NB}kg nhân xanh.`,
  kv:r=>[['Trái tươi cần',fm(r.cherry)+NB+'kg'],['Nhân xanh thu được',vn(r.green,1)+NB+'kg'],['Giống','Robusta Di Linh']],
  check:'Đếm ngẫu nhiên 100 trái trong rổ: từ 90 trái chín đỏ trở lên.',fail:'Hái tuốt cả cành lẫn trái xanh làm cốt cold brew ngái, chát.',tip:'Ghi mã vườn lên bao để truy xuất tới từng chai.'},
 {n:'Sơ chế & phơi',sub:()=>BEAN[st.bean].proc==='honey'?'Honey, phơi trên giàn':'Natural, phơi nguyên trái',
  mech:()=>BEAN[st.bean].proc==='honey'?'Robusta Premium: xát bỏ vỏ, giữ lại lớp nhớt rồi phơi trên giàn, đảo đều mỗi ngày. Lớp nhớt cho vị ngọt, caramel rất hợp với ủ lạnh. Phơi tới khi nhân còn ẩm 10–12 %, rồi xát khô ra nhân.':'Robusta Classic: phơi nguyên trái trên giàn tới khô, đảo đều mỗi ngày, rồi xát lấy nhân. Vị đậm, cacao, thân dày. Phơi tới khi nhân còn ẩm 10–12 %.',
  kv:r=>[['Ẩm nhân sau phơi','10–12'+NB+'%'],['Thời gian phơi','khoảng 10–20 ngày, tuỳ nắng'],['Nhân xanh',vn(r.green,1)+NB+'kg']],
  check:'Đo ẩm nhân trước khi đóng bao; nhân khô đều, không mốc.',fail:'Phơi dày, ít đảo: lên men quá, mùi chua lạ đi thẳng vào cốt.',tip:'Giàn phơi cao, có mái che mưa, không phơi sát đất.'},
 {n:'Rang & ủ khí',sub:()=>'City+, nghỉ 3–10 ngày',
  mech:r=>`Rang riêng cho cold brew ở mức City+ (rang vừa), ra mẻ khoảng 210–220${NB}°C, hao hụt khoảng 17,5${NB}% như Phòng rang. Nước lạnh khó kéo chất từ hạt rang quá sáng, còn rang quá đậm cho vị khét, gắt. Sau rang nghỉ 3–10 ngày trong thùng kín có van một chiều cho CO₂ thoát bớt, bột ngấm nước đều hơn.`,
  kv:r=>[['Cà phê rang',g1(st.R)+NB+'kg'],['Cấp rang','City+, ra mẻ 210–220'+NB+'°C'],['Hao hụt','khoảng 17,5'+NB+'%'],['Nghỉ sau rang','3–10 ngày']],
  check:'Bẻ hạt: ruột và vỏ cùng màu. Cupping mẫu trước khi xay.',fail:'Xay ngay sau rang: CO₂ đẩy nước ra, bột ngấm không đều.',tip:'Ghi ngày rang lên thùng, dùng theo thứ tự.'},
 {n:'Xay thô',sub:()=>'Thô như muối hạt',
  mech:()=>`Xay thô như muối hạt, ngay trước khi ${st.f==='bag'?'đóng túi lọc':'ngâm'}. Bột quá mịn làm cốt đục, đắng gắt và khó lọc; bột quá thô thì nhạt.`,
  kv:()=>[['Cỡ xay','Thô, như muối hạt'],['Bột cho mẻ',vn(st.R*.99,1)+NB+'kg'],['Hao khi xay','khoảng 1'+NB+'%']],
  check:'Rây thử 100 g bột: phần bụi mịn càng ít càng tốt.',fail:'Lưỡi cối mòn tạo nhiều bụi mịn: lọc chậm, cốt đục.',tip:'Xay từng đợt vừa đủ một bồn ngâm.'},
 {n:'Ngâm lạnh',sub:()=>'Bồn inox trong kho lạnh',
  mech:r=>`Bột trong túi lọc vải thực phẩm, mỗi túi không quá 2,5${NB}kg để nước ngấm đều, đặt vào bồn inox 304. Rót nước uống đạt chuẩn đã làm lạnh theo tỷ lệ 1:${vn(st.ratio,1)}, ấn nhẹ cho bột ngấm hết, đậy kín, ngâm <b>${st.h} giờ ở ${st.T}${NB}°C</b>. Hướng dẫn ngâm thương mại thường là 16–20 giờ trong tủ lạnh dưới 4,4${NB}°C.`,
  kv:r=>[['Nước ngâm',fm(r.W)+NB+'L'],['Tỷ lệ cà phê : nước','1:'+vn(st.ratio,1)],['Nhiệt độ, thời gian',st.T+NB+'°C, '+st.h+' giờ'],['EY ước tính',vn(r.ey,1)+NB+'%']],
  check:'Nhiệt kế kho đọc 2–5 °C. Ghi giờ bắt đầu và kết thúc vào phiếu lô.',fail:'Ngâm ở nhiệt độ phòng cho chai bán ra ngoài: vi sinh phát triển nhanh hơn.',tip:'Đảo nhẹ một lần sau giờ đầu để bột không vón khô.'},
 {n:'Lọc & đo TDS',sub:()=>st.f==='rtd'?'Lọc hai tầng, pha loãng':'Lọc hai tầng, chuẩn hoá lô',
  mech:()=>'Nhấc túi, để ráo 15–20 phút, không vắt mạnh vì vắt làm cốt đục và gắt. Lọc tinh qua giấy lọc hoặc vải lọc thực phẩm. Đo TDS bằng khúc xạ kế để chuẩn hoá từng lô: chai cô đặc ghi TDS lên phiếu lô, chai uống liền pha loãng tới TDS mục tiêu.',
  kv:r=>[['Cốt sau lọc',vn(r.Vc,1)+NB+'L'],['TDS cốt, ước tính',vn(r.tdsC,1)+NB+'%'],['Nước bã giữ lại',fm(RET*st.R)+NB+'L']].concat(st.f==='rtd'&&!r.low?[['Nước pha thêm',vn(r.add,1)+NB+'L'],['TDS uống liền',vn(st.tds,1)+NB+'%']]:[]),
  check:'Cốt trong, không cặn. Nếm so với mẫu chuẩn của lô trước.',fail:'Lọc một lần qua lưới thô: cặn mịn tiếp tục chiết, chai đục và đắng dần.',tip:'Lệch quá 10 % so với TDS mốc thì chỉnh mẻ sau.'},
 {n:'Chiết rót',sub:()=>'Chai thủy tinh nâu '+st.vol+' ml',
  mech:()=>`Chiết vào chai thủy tinh nâu ${st.vol}${NB}ml đã rửa, khử trùng, để khô úp ngược. Chừa khoảng trống ở cổ chai, đóng nắp có vòng niêm phong, dán nhãn có ngày sản xuất, hạn dùng và mã lô ngay khi chiết. Không thổi nitơ, không đóng lon khi chưa có quy trình được thẩm định.`,
  kv:r=>[['Số chai',fm(r.n)+' chai '+st.vol+NB+'ml'],['Hao khi chiết','khoảng 1'+NB+'%'],['Mã lô',lot()]],
  check:'Lật ngược 5 chai mỗi lô: không rỉ nắp.',fail:'Chai còn ẩm, nắp không niêm phong: dễ nhiễm và khách khó tin.',tip:'Chai nâu chắn bớt ánh sáng, giữ màu và mùi.'},
 {n:'Đóng túi ủ',sub:()=>st.bag+' g mỗi túi lọc',
  mech:()=>`Máy định lượng ${st.bag}${NB}g bột thô vào túi lọc không dệt dùng cho thực phẩm, hàn kín, có dây và thẻ MeDili. Mỗi 5 túi vào một túi bạc nhiều lớp có van một chiều, thổi nitơ rồi hàn. ${st.per===10?'Hai túi bạc':'Một túi bạc'} vào một hộp ${st.per} túi.`,
  kv:r=>st.f==='bag'?[['Số túi',fm(r.bags)+' túi × '+st.bag+NB+'g'],['Số hộp',fm(r.boxes)+' hộp × '+st.per+' túi'],['Mỗi túi pha',st.bag*8+NB+'ml nước, ra khoảng '+fm(r.out)+NB+'ml cốt'],['Hạn dùng','6 tháng, mốc đề xuất']]:[['Dùng cho','dạng túi ủ lạnh']],
  check:'Cân ngẫu nhiên 10 túi: lệch không quá 1 g. Túi bạc hàn kín, không xì.',fail:'Đóng túi khi bột còn nhiều khí: túi bạc phồng.',tip:'In hướng dẫn ủ lên mặt sau hộp và trên thẻ túi.'},
 {n:'Bao bì',sub:()=>'Cold Brew MeDili',
  mech:()=>'Bao bì mang tên Cold Brew MeDili theo màu thương hiệu: kem, nâu cà phê, đỏ đất và vàng đất. Chai có nhãn quấn thân chống ẩm, logo MeDili, chữ COLD BREW lớn, dải đỏ ghi dạng sản phẩm và dung tích; nhãn phụ ghi đủ nội dung bắt buộc. Túi ủ đựng trong hộp kraft in hai màu. Xem mẫu ở Hình 3.',
  kv:()=>[['Chai',st.vol+NB+'ml, thủy tinh nâu'],['Nhãn','Decal giấy chống ẩm'],['Hộp túi ủ','Kraft, '+st.per+' túi']],
  check:'Đối chiếu nhãn với bản tự công bố trước khi in số lượng lớn.',fail:'Nhãn thiếu hạn dùng hoặc hướng dẫn bảo quản.',tip:'In thử 20 nhãn, dán lên chai lạnh xem có bong khi đọng hơi nước.'},
 {n:'Kho & giao',sub:()=>st.f==='bag'?'Kho khô, giao toàn quốc':'Kho 0–4 °C, giao trong ngày',
  mech:()=>st.f==='bag'?'Hộp túi ủ là hàng khô: kho khô, thoáng, tránh nắng. Giao toàn quốc qua sàn, đóng thùng carton có chèn chống sốc.':'Chai vào kho lạnh 0–4 °C ngay sau khi chiết, ghi nhiệt độ hai lần mỗi ngày. Hạn dùng 7 ngày kể từ ngày sản xuất. Giao nội thành trong ngày bằng thùng xốp có đá gel, nhắc khách cất tủ lạnh ngay. Không gửi chai lạnh đi tỉnh bằng giao hàng thường.',
  kv:()=>st.f==='bag'?[['Kho','Khô, dưới 30'+NB+'°C'],['Hạn dùng','6 tháng, mốc đề xuất'],['Kênh bán','Sàn TMĐT toàn quốc']]:[['Nhiệt độ kho','0–4'+NB+'°C'],['Hạn dùng','7 ngày'],['Kênh bán','Nội thành, giao trong ngày']],
  check:'',fail:'',tip:''}];
const K10={cold:{check:'Đo nhiệt độ chai khi giao: dưới 5 °C.',fail:'Để chai ngoài tủ lạnh khi chờ shipper.',tip:'Lưu 2 chai mẫu mỗi lô đến hết hạn để đối chiếu.'},
 dry:{check:'Kiểm túi bạc không xì trước khi đóng thùng.',fail:'Kho nóng ẩm làm bột mất mùi nhanh.',tip:'Lô cũ xuất trước, lô mới xuất sau.'}};
const today=()=>{const d=new Date();d.setHours(12,0,0,0);return d};
const dmy=d=>String(d.getDate()).padStart(2,'0')+'/'+String(d.getMonth()+1).padStart(2,'0')+'/'+d.getFullYear();
const addD=(d,n)=>{const e=new Date(d);e.setDate(e.getDate()+n);return e},addM=(d,n)=>{const e=new Date(d);e.setMonth(e.getMonth()+n);return e};
const lot=()=>{const d=today();return (st.f==='bag'?'TU':'CB')+String(d.getFullYear()).slice(2)+String(d.getMonth()+1).padStart(2,'0')+String(d.getDate()).padStart(2,'0')+'-01'};

/* ====== DỰNG CẢNH ====== */
const ANCH=[null,[8,13,9],[22,12,3.2],[34.5,11,8.8],[46,11,8.8],[58,12,10],[69,11.5,8],[82.5,13.5,8.6],[93.5,11.3,8.8],[105.5,13,6.4],[118.5,12,9.8]];
function buildScene(){
 let h='<g class="m">';
 [[3,23],[125,23],[125,3]].forEach(([x,y])=>h+=cyl(x,y,-9,1.2,5,'cu2','cu2'));
 h+=box(0,0,-4,128,26,4,['wo','wo2','cu2'])+'</g>';
 const pl=P(56,26,-.6);
 h+=`<g transform="matrix(.866 .5 0 1 ${f1(pl[0])} ${f1(pl[1])})"><rect width="252" height="24" rx="3" style="fill:#D6B26A;stroke:#2A1B16;stroke-width:1.2"/><circle cx="8" cy="12" r="1.8" style="fill:#2A1B16"/><circle cx="244" cy="12" r="1.8" style="fill:#2A1B16"/><text class="sgn" x="126" y="17.5" text-anchor="middle">Cold Brew MeDili · Farm Di Linh</text></g>`;
 /* 1 vườn */
 let s=frus(8,13,0,6.2,2,3.3,'hill','hillT');
 [[6.6,11.2],[10.2,10.8],[9.6,14.8]].forEach(([x,y],k)=>{const b=P(x,y,2),t=P(x,y,7);
  s+=`<path d="M${f1(b[0])} ${f1(b[1])}L${f1(t[0])} ${f1(t[1])}" style="stroke:#6B4226;stroke-width:3.2;stroke-linecap:round;fill:none"/>`;
  s+=`<ellipse cx="${f1(t[0])}" cy="${f1(t[1]-2)}" rx="15" ry="12" style="fill:#8D5A32"/><ellipse cx="${f1(t[0]-6)}" cy="${f1(t[1]-7)}" rx="8" ry="6" style="fill:#A9743F;stroke:none"/>`;
  [[-8,-4],[5,-8],[9,2],[-3,5],[1,-14],[-11,4],[12,-6]].forEach(([dx,dy])=>s+=`<circle cx="${f1(t[0]+dx)}" cy="${f1(t[1]+dy-2)}" r="2.4" style="fill:#B33A24;stroke:none"/>`)});
 s+=cyl(3.6,20.6,0,1.8,1.6,'wo2','cherT')+[[-5,-1],[0,-2],[5,0],[-2,2],[3,2]].map(([dx,dy])=>{const q=P(3.6,20.6,1.6);return `<circle cx="${f1(q[0]+dx)}" cy="${f1(q[1]+dy)}" r="2.6" style="fill:#B33A24;stroke:none"/>`}).join('');
 h+=stG(1,s);
 /* 2 phơi giàn */
 s='';[[17.3,8.3],[26.4,8.3],[17.3,15.4],[26.4,15.4]].forEach(([x,y])=>s+=box(x,y,0,.35,.35,2.4,['wo2','wo2','wo2']));
 s+=box(17,8,2.4,10,8,.45,['bed','bed2','bed2'])+'<g id="cher"></g>';
 h+=stG(2,s);
 /* 3 rang */
 const dr=P(31.4,14,5.2);
 s=cyl(32.4,9.4,6,.5,4.6,'f3','f2')+box(31,8,0,6.6,6,6,['f1','f2','f3'])
  +`<g transform="${face(31.6,14,5.4)}"><circle cx="22" cy="19" r="14" class="f3" style="stroke:var(--ol);stroke-width:1.2"/><circle cx="22" cy="19" r="8.5" class="cu2" style="stroke:var(--ol);stroke-width:1"/><rect x="34" y="30" width="8" height="5" rx="1" class="cu" style="stroke:var(--ol);stroke-width:1"/></g>`
  +frus(34.6,11,6,.8,8.8,2.1,'f2','beanT')+cyl(40.6,13.2,0,2.4,1.4,'f2','beanT');
 h+=stG(3,s);
 /* 4 xay thô */
 s=box(44,9,0,4,4,4.6,['f1','f2','f3'])+cyl(46,11,4.6,.9,1,'f3','f2')+frus(46,11,5.6,.8,8.6,2,'beanT','beanT')+frus(46,11,5.6,.9,8.8,2.1,'gl','glt')
  +cyl(48.6,15.6,0,1.5,2,'pa','grdT');
 h+=stG(4,s);
 /* 5 ngâm lạnh */
 s=cyl(58,12,0,3.2,6.4,'f2','f1')+(()=>{const q=P(58,12,6.2);return `<ellipse class="grdT" cx="${f1(q[0])}" cy="${f1(q[1])}" rx="${f1(RX(2.6))}" ry="${f1(RY(2.6))}"/>`})()
  +box(52.4,6.6,0,11.2,11,9.6,['glt','gl','gl'])
  +`<g transform="${face(53,17.6,9)}">${[[14,10],[40,6],[66,14],[28,27]].map(([x,y])=>`<path class="frost" d="M${x} ${y-4.5}v9M${x-3.9} ${y-2.25}l7.8 4.5M${x-3.9} ${y+2.25}l7.8 -4.5"/>`).join('')}</g>`
  +lcd(53.4,17.6,1.7,68,'kC');
 h+=stG(5,s);
 /* 6 lọc và TDS */
 s=cyl(69,11.5,0,2,3.8,'f2','liqt')+frus(69,11.5,3.8,.6,7.6,2.4,'f1','grdT')+box(71.6,14.6,0,3.2,2.2,1,['f1','f2','f3'])+lcd(71.9,16.8,.95,24,'kS');
 h+=stG(6,s);
 /* 7 chiết rót */
 s=box(76.6,12.6,0,11.6,2.8,1.4,['f2','f3','f3'])+box(77.4,12,1.4,.5,.5,6.6,['f3','f3','f3']);
 [79.2,81.4,83.6,85.8].forEach(x=>s+=bottle(x,14,1.4,0));
 s+=box(86.6,12,1.4,.5,.5,6.6,['f3','f3','f3'])+box(77.4,12,8,9.8,3.4,1.4,['f1','f2','f3']);
 [80.2,82.6,85].forEach(x=>{const a=P(x,13.7,8),b=P(x,13.7,6.6);s+=`<line x1="${f1(a[0])}" y1="${f1(a[1])}" x2="${f1(b[0])}" y2="${f1(b[1])}" style="stroke:var(--ol);stroke-width:2.2"/>`});
 h+=stG(7,s);
 /* 8 đóng túi ủ */
 s=box(90.4,9,0,5,4.6,6.6,['f1','f2','f3'])+frus(92.9,11.3,6.6,.7,8.8,1.8,'f2','beanT')+box(91.4,13.6,1.6,2.2,1.4,.6,['f2','f3','f3']);
 for(let i=0;i<4;i++)s+=box(91.6,15.6,i*.24,1.6,1.3,.22,['bagw','bagw2','bagw2']);
 s+=box(95.6,14.6,0,1.8,.6,2.7,['foil','foil2','foil3'])+box(97.8,14.2,0,1.8,.6,2.7,['foil','foil2','foil3']);
 h+=stG(8,s);
 /* 9 bao bì */
 s=box(100,9,0,10,8,2.2,['wo','wo2','cu2'])+bottle(101.8,11.2,2.2,1)+bottle(103.6,11.2,2.2,1)+bottle(102.6,13.4,2.2,1)
  +box(105.4,10.2,2.2,3.6,2.6,2.8,['kr','kr2','kr3'])+`<g transform="${face(105.5,12.8,4.8)}"><rect x="1" y="2" width="23" height="5" style="fill:#9E3B26"/><text class="ptx" x="12.5" y="15" text-anchor="middle">COLD</text><text class="ptx" x="12.5" y="23" text-anchor="middle">BREW</text></g>`
  +box(105.8,14,2.2,2.8,2.2,3.1,['kr','kr2','kr3'])+`<g transform="${face(105.9,16.2,5.1)}"><text class="ptx" x="9.6" y="10" text-anchor="middle" style="font-size:7px">MeDili</text><rect x="1" y="14" width="17.6" height="3.4" style="fill:#9E3B26"/></g>`;
 h+=stG(9,s);
 /* 10 kho và giao */
 s=box(113,7.6,0,5.2,5,9.8,['f1','f2','f3'])+`<g transform="${face(113.3,12.6,9.4)}"><rect x="0" y="0" width="31" height="60" rx="2" class="door"/>${[14,30,46].map(y=>`<line x1="2" x2="29" y1="${y}" y2="${y}" style="stroke:var(--ol);stroke-width:1"/>`+[5,12,19,26].map(x=>`<rect x="${x-1.6}" y="${y-8}" width="3.2" height="8" rx="1" style="fill:#6E3F1C"/>`).join('')).join('')}</g>`
  +lcd(113.5,12.6,9.6,24,'kF')+'<g id="parcel"></g>';
 h+=stG(10,s);
 h+='<g id="flow"></g><g id="chips"></g><circle id="tok" r="7"/>';
 $('scene').innerHTML=h;
 document.querySelectorAll('#scene .st').forEach(g=>{g.addEventListener('click',()=>select(+g.dataset.i));g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();select(+g.dataset.i)}})});
}
function parcel(){const cold=st.f!=='bag',c=cold?['pcl','pcl2','pcl3']:['kr','kr2','kr3'];
 let s=box(119.6,13,0,7,5,4.2,c)+`<polygon points="${pts([P(122.7,13,4.2),P(123.5,13,4.2),P(123.5,18,4.2),P(122.7,18,4.2)])}" style="fill:#9E3B26;stroke:none"/>`;
 s+=`<g transform="${face(119.6,18,4.2)}"><text class="wtx" x="24.5" y="9.5" text-anchor="middle" style="font-size:6.6px">COLD BREW</text><text class="wtx" x="24.5" y="17.5" text-anchor="middle" style="font-size:6.6px">MEDILI</text><text class="wtx" x="24.5" y="26" text-anchor="middle" style="font-size:6.2px;fill:#9E3B26">${cold?'GIỮ LẠNH':'HÀNG KHÔ'}</text></g>`;
 $('parcel').innerHTML=s}
function cherries(){const c=BEAN[st.bean].cher;let s='';
 for(let i=0;i<8;i++)for(let j=0;j<6;j++){const q=P(17.7+i*1.18,8.7+j*1.2,2.86);s+=`<ellipse cx="${f1(q[0]+(j%2)*1.5)}" cy="${f1(q[1])}" rx="2.3" ry="1.5" style="fill:${c};stroke:none"/>`}
 $('cher').innerHTML=s}
function chipLabel(i,r){
 const b=st.f==='bag';
 return ['',`Trái chín · ${fm(r.cherry)}${NB}kg`,`${BEAN[st.bean].proc==='honey'?'Honey':'Natural'} · ${vn(r.green,1)}${NB}kg nhân`,`Rang City+ · ${g1(st.R)}${NB}kg`,'Xay thô',
  b?'Ngâm lạnh (chai)':`Ngâm ${st.T}${NB}°C · ${st.h} giờ`,b?'Lọc (chai)':`Lọc · TDS ${vn(r.tdsC,1)}${NB}%`,b?'Chiết rót (chai)':`${fm(r.n)} chai ${st.vol}${NB}ml`,
  b?`${fm(r.bags)} túi ${st.bag}${NB}g`:'Đóng túi (túi ủ)','Cold Brew MeDili',b?'Giao toàn quốc':'Giao lạnh trong ngày'][i]}
const CHIP=[null,{x:178,y:14},{x:262,y:64},{x:344,y:108},{x:418,y:150},{x:492,y:192},{x:566,y:240},{x:636,y:290},{x:704,y:330},{x:760,y:384},{x:842,y:436}];
function drawChips(r){let h='';
 for(let i=1;i<=10;i++){const C=CHIP[i],l=chipLabel(i,r),w=40+l.length*7,x=Math.min(C.x,1032-w-6),q=P(...ANCH[i]),off=!use(i);
  h+=`<polyline class="lead-l${i===st.sel?' on':''}" points="${f1(q[0])},${f1(q[1])} ${f1(x+20)},${C.y+13}"/><g class="chip${i===st.sel?' on':''}${off?' off':''}" data-c="${i}"><rect x="${f1(x+6)}" y="${C.y}" rx="8" width="${f1(w)}" height="26"/><circle cx="${f1(x+6)}" cy="${C.y+13}" r="13"/><text class="num" x="${f1(x+6)}" y="${C.y+18.5}" text-anchor="middle">${i}</text><text class="lab" x="${f1(x+26)}" y="${C.y+18}">${l}</text></g>`}
 const el=$('chips');el.innerHTML=h;el.querySelectorAll('.chip').forEach(g=>g.addEventListener('click',()=>select(+g.dataset.c)))}
function drawFlow(r){
 const rows=[['Trái chín Di Linh',fm(r.cherry)+NB+'kg','#B33A24'],['Nhân xanh, ẩm 10–12 %',vn(r.green,1)+NB+'kg','#D8C9A3'],['Cà phê rang City+',g1(st.R)+NB+'kg','#6B4226']];
 if(st.f==='bag')rows.push(['Bột thô trong túi lọc',fm(r.bags)+NB+'túi','#F6F0E4'],['Thành phẩm',fm(r.boxes)+NB+'hộp '+st.per+' túi','#9E3B26']);
 else{rows.push(['Nước ngâm '+st.T+NB+'°C',fm(r.W)+NB+'L','#E9D3AE'],['Cốt sau lọc',vn(r.Vc,1)+NB+'L','#7A4A23']);if(st.f==='rtd'&&!r.low)rows.push(['Pha tới TDS '+vn(st.tds,1)+NB+'%',vn(r.Vout,1)+NB+'L','#A06C45']);rows.push(['Thành phẩm',fm(r.n)+NB+'chai '+st.vol+NB+'ml','#9E3B26'])}
 const x=16,rh=28,h=50+rows.length*rh+22,y=712-h,w=320;
 let g=`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="10" class="pa" style="stroke:var(--ink);stroke-width:1.2"/><text x="${x+16}" y="${y+26}" class="lab12" style="letter-spacing:.08em">TỪ VƯỜN ĐẾN SẢN PHẨM</text>`;
 rows.forEach(([a,b,c],i)=>{const yy=y+48+i*rh;g+=(i<rows.length-1?`<line x1="${x+24}" y1="${yy+7}" x2="${x+24}" y2="${yy+rh-7}" style="stroke:var(--muted);stroke-width:1.2;stroke-dasharray:2 3"/>`:'')+`<circle cx="${x+24}" cy="${yy}" r="7" style="fill:${c};stroke:var(--ol);stroke-width:1"/><text class="flowT" x="${x+40}" y="${yy+4}">${a}</text><text x="${x+w-16}" y="${yy+4}" text-anchor="end" class="mono flowT">${b}</text>`});
 g+=`<text x="${x+16}" y="${y+h-12}" class="tiny mutedt">Bản vẽ khái niệm · số liệu ước tính theo mô hình</text>`;
 $('flow').innerHTML=g}
function renderScene(r){
 document.querySelectorAll('#scene .st').forEach(g=>{const i=+g.dataset.i;g.classList.toggle('off',!use(i));g.classList.toggle('on',i===st.sel)});
 $('kC').textContent=st.f==='bag'?'—':`${st.T} °C · ${st.h} giờ`;
 $('kS').textContent=st.f==='bag'?'—':vn(r.tdsC,1)+' %';
 $('kF').textContent=st.f==='bag'?'—':'2 °C';
 cherries();parcel();drawChips(r);drawFlow(r);
}

/* ====== BIỂU ĐỒ TDS THEO GIỜ ====== */
function drawCT(r){
 const bag=st.f==='bag',ratio=bag?8:st.ratio,dose=bag?st.bag:st.R*1000,water=bag?st.bag*8:st.R*st.ratio*1000,bev=water-RET*dose;
 const tds=(T,h)=>bev>0?EY(T,h,ratio)*dose/bev:0,Tm=bag?4:st.T,ref=24;
 const W=340,H=162,l=30,rr=48,t=18,b=22,ymax=Math.max(2,Math.ceil(Math.max(tds(ref,24),tds(Tm,24))*1.1));
 const X=h=>l+h/24*(W-l-rr),Y=v=>t+(1-v/ymax)*(H-t-b);
 let g=`<text class="ttl" x="${l}" y="11">TDS ${bag?'cốt trong ly của khách':'cốt sau lọc'} (%) · trục ngang: giờ</text>`;
 if(bag)g+=`<rect x="${f1(X(18))}" y="${t}" width="${f1(X(24)-X(18))}" height="${H-t-b}" style="fill:var(--good);fill-opacity:.14"/>`;
 [0,ymax/2,ymax].forEach(v=>g+=`<line x1="${l}" x2="${W-rr}" y1="${f1(Y(v))}" y2="${f1(Y(v))}" style="stroke:var(--rule);stroke-width:.7"/><text x="${l-5}" y="${f1(Y(v)+3.5)}" text-anchor="end">${g1(Math.round(v*10)/10)}</text>`);
 [0,6,12,18,24].forEach(hh=>g+=`<text x="${f1(X(hh))}" y="${H-5}" text-anchor="middle">${hh}</text>`);
 const path=T=>{const p=[];for(let i=0;i<=48;i++){const hh=i/2;p.push(f1(X(hh))+','+f1(Y(tds(T,hh))))}return p.join(' ')};
 g+=`<polyline points="${path(ref)}" fill="none" style="stroke:var(--muted);stroke-width:2;stroke-dasharray:5 4"/>`;
 g+=`<polyline points="${path(Tm)}" fill="none" style="stroke:var(--accent);stroke-width:2"/>`;
 const lab=[[ref,'24 °C'],[Tm,Tm+' °C']].map(([T,s])=>({y:Y(tds(T,24)),s})).sort((a,b)=>a.y-b.y);if(lab[1].y-lab[0].y<12)lab[1].y=lab[0].y+12;
 lab.forEach(o=>g+=`<text x="${W-rr+5}" y="${f1(o.y+3.5)}" style="fill:var(--ink)">${o.s}</text>`);
 const hm=bag?20:st.h;g+=`<line x1="${f1(X(hm))}" x2="${f1(X(hm))}" y1="${t}" y2="${H-b}" style="stroke:var(--ink);stroke-width:1"/><circle cx="${f1(X(hm))}" cy="${f1(Y(tds(Tm,hm)))}" r="4.5" style="fill:var(--accent);stroke:var(--panel);stroke-width:2"/>`;
 if(bag)g+=`<text x="${f1(X(21))}" y="${H-b-6}" text-anchor="middle" style="paint-order:stroke;stroke:var(--panel);stroke-width:3px;stroke-linejoin:round;fill:var(--ink)">18–24 giờ</text>`;
 $('cT').innerHTML=g;
 $('cLbl').textContent=bag?'Khách ủ trong ngăn mát: cốt đậm dần theo giờ':'Ngâm càng lạnh, cốt đậm càng chậm';
 $('lgT').innerHTML=`<span><i class="sw2" style="border-color:var(--accent)"></i>${bag?'Ngăn mát 4 °C':'Ngâm '+Tm+' °C'}</span><span><i class="sw2 d" style="border-color:var(--muted)"></i>Nhiệt độ phòng 24 °C, để so sánh</span>`;
 $('tip').textContent=`Ở ${Tm} °C, ${hm} giờ: TDS khoảng ${vn(tds(Tm,hm),1)} %. Ở 24 °C cùng thời gian: khoảng ${vn(tds(ref,hm),1)} %.`;
}

/* ====== CÔNG THỨC MẺ ====== */
function sop(r){
 const s=st,b=BEAN[s.bean],bag=s.f==='bag',rows=[],add=(t,d,a,c)=>rows.push([t,d,a,c]);
 add('Hái chín ở farm Di Linh','Chỉ hái trái chín đỏ, sơ chế trong ngày. Ghi mã vườn lên bao.',`${fm(r.cherry)}${NB}kg trái tươi`,'Đếm 100 trái trong rổ: từ 90 trái chín trở lên.');
 add(b.proc==='honey'?'Sơ chế honey, phơi giàn':'Phơi nguyên trái trên giàn',b.proc==='honey'?'Xát vỏ, giữ lớp nhớt, phơi trên giàn, đảo mỗi ngày, rồi xát khô ra nhân.':'Phơi nguyên trái trên giàn, đảo mỗi ngày, khô rồi xát lấy nhân.',`${vn(r.green,1)}${NB}kg nhân xanh`,'Ẩm nhân 10–12 %, không mốc.');
 add('Rang City+, nghỉ hạt','Rang riêng cho cold brew, ra mẻ 210–220 °C. Nghỉ 3–10 ngày trong thùng kín có van một chiều.',`${g1(s.R)}${NB}kg rang, hao khoảng 17,5${NB}%`,'Bẻ hạt đều màu, cupping mẫu.');
 add('Xay thô',`Thô như muối hạt, xay ngay trước khi ${bag?'đóng túi':'ngâm'}.`,`${vn(s.R*.99,1)}${NB}kg bột`,'Ít bụi mịn.');
 if(bag){
  add('Đóng túi lọc',`Định lượng ${s.bag}${NB}g bột vào túi lọc không dệt dùng cho thực phẩm, hàn kín, gắn dây và thẻ MeDili.`,`${fm(r.bags)} túi × ${s.bag}${NB}g`,`Cân 10 túi: lệch không quá 1${NB}g.`);
  add('Túi bạc thổi nitơ','Mỗi 5 túi lọc vào một túi bạc nhiều lớp có van một chiều, thổi nitơ rồi hàn.',`${fm(Math.ceil(r.bags/5))} túi bạc`,'Bóp nhẹ: không xì.');
  add('Đóng hộp, dán nhãn','Hộp kraft Cold Brew MeDili, hướng dẫn ủ in mặt sau, ghi ngày sản xuất, hạn dùng, mã lô.',`${fm(r.boxes)} hộp × ${s.per} túi`,'Nhãn khớp bản tự công bố.');
  add('Lưu kho khô','Kho khô, thoáng, tránh nắng, dưới 30 °C. Hạn dùng đề xuất 6 tháng, xác lập bằng kiểm nghiệm và thử cảm quan theo thời gian.','6 tháng, mốc đề xuất','Lô cũ xuất trước.');
  add('Giao toàn quốc qua sàn',`Thùng carton có chèn chống sốc. Hướng dẫn khách: 1 túi với ${s.bag*8}${NB}ml nước lọc, ngâm ngăn mát 18–24 giờ, nhấc túi, pha 1:1 với nước, sữa hoặc đá.`,`Khoảng ${fm(r.out)}${NB}ml cốt mỗi túi`,'Hỏi phản hồi của khách sau 2 tuần đầu.');
 }else{
  add('Ngâm lạnh',`Bột vào túi lọc vải thực phẩm, mỗi túi không quá 2,5${NB}kg, đặt vào bồn inox 304. Rót nước uống đạt chuẩn đã làm lạnh, ấn cho bột ngấm, đậy kín, ngâm ${s.h} giờ ở ${s.T}${NB}°C.`,`${fm(r.W)}${NB}L nước · 1:${vn(s.ratio,1)} · ${s.T}${NB}°C · ${s.h} giờ`,'Nhiệt kế kho 2–5 °C, ghi giờ vào phiếu lô.');
  add('Nhấc túi, lọc hai tầng','Để ráo 15–20 phút, không vắt mạnh. Lọc tinh qua giấy lọc hoặc vải lọc thực phẩm.',`${vn(r.Vc,1)}${NB}L cốt`,'Cốt trong, không cặn.');
  add(s.f==='rtd'?'Đo TDS, pha loãng':'Đo TDS, ghi lô',s.f==='rtd'?(r.low?`Cốt chỉ đạt TDS khoảng ${vn(r.tdsC,1)}${NB}%, chưa đủ để pha tới ${vn(s.tds,1)}${NB}%. Tăng lượng cà phê hoặc ngâm lâu hơn.`:`Đo TDS cốt bằng khúc xạ kế, thêm nước uống đạt chuẩn tới TDS ${vn(s.tds,1)}${NB}%: thêm ${vn(r.add,1)}${NB}L.`):'Đo TDS cốt bằng khúc xạ kế, ghi lên phiếu lô. Lệch quá 10 % so với mốc thì chỉnh mẻ sau.',s.f==='rtd'?`${vn(r.Vout,1)}${NB}L uống liền`:`TDS khoảng ${vn(r.tdsC,1)}${NB}%`,'Nếm so với mẫu chuẩn.');
  add('Chiết rót, đóng nắp',`Chai thủy tinh nâu ${s.vol}${NB}ml đã rửa, khử trùng, để khô. Đóng nắp có vòng niêm phong, dán nhãn có ngày sản xuất, hạn dùng, mã lô ngay khi chiết.`,`${fm(r.n)} chai ${s.vol}${NB}ml`,'Lật ngược 5 chai: không rỉ.');
  add('Kho lạnh 0–4 °C','Đưa vào kho lạnh ngay. Ghi nhiệt độ hai lần mỗi ngày. Lưu 2 chai mẫu mỗi lô đến hết hạn.','Hạn dùng 7 ngày','Chai dưới 5 °C khi xuất kho.');
  add('Giao lạnh trong ngày','Thùng xốp có đá gel, giao nội thành trong ngày, nhắc khách cất tủ lạnh ngay. Không gửi đi tỉnh bằng giao hàng thường.','Nội thành, trong ngày','Chai dưới 5 °C khi tới tay khách.');
 }
 $('sopH').textContent=`Hình 2: công thức mẻ ${g1(s.R)}${NB}kg · ${FMT[s.f].n.toLowerCase()}`;
 $('sop').innerHTML=rows.map(([t,d,a,c],i)=>`<li><span class="n">${i+1}</span><div><h3>${t}</h3><p>${d}</p></div><p><span class="lbl">Thông số</span>${a}</p><p><span class="lbl">Kiểm tra</span>${c}</p></li>`).join('');
}

/* ====== BAO BÌ ====== */
function bottleSvg(){
 const kind=st.f==='rtd'?'UỐNG LIỀN':'CÔ ĐẶC',vol=st.f==='bag'?250:st.vol,h=st.f==='bag'?18:st.h;
 const ridges=[0,1,2,3,4,5,6,7,8,9].map(i=>`<line x1="${81+i*4.2}" x2="${81+i*4.2}" y1="13" y2="37" stroke="#8D6A33" stroke-opacity=".45"/>`).join('');
 return `<svg viewBox="0 0 200 410" role="img" aria-label="Chai Cold Brew MeDili ${kind.toLowerCase()} ${vol} ml">
<defs><linearGradient id="pkG" x1="0" x2="1"><stop offset="0" stop-color="#3E2112"/><stop offset=".2" stop-color="#8B5226"/><stop offset=".55" stop-color="#5E3418"/><stop offset=".86" stop-color="#8B5226"/><stop offset="1" stop-color="#3A1E10"/></linearGradient>
<linearGradient id="pkC" x1="0" x2="1"><stop offset="0" stop-color="#8D6A33"/><stop offset=".5" stop-color="#E7C985"/><stop offset="1" stop-color="#8D6A33"/></linearGradient>
<linearGradient id="pkL" x1="0" x2="1"><stop offset="0" stop-color="#2E1A10" stop-opacity=".22"/><stop offset=".16" stop-color="#2E1A10" stop-opacity="0"/><stop offset=".84" stop-color="#2E1A10" stop-opacity="0"/><stop offset="1" stop-color="#2E1A10" stop-opacity=".24"/></linearGradient></defs>
<ellipse cx="100" cy="398" rx="72" ry="8" fill="#2E1A10" fill-opacity=".18"/>
<path d="M80 36h40v50c0 20 38 30 38 64v212a18 18 0 0 1-18 18H60a18 18 0 0 1-18-18V150c0-34 38-44 38-64z" fill="url(#pkG)" stroke="#3A1E10" stroke-width="1.5"/>
<path d="M53 165c-3 60-3 130 0 190" stroke="#F6E7CF" stroke-opacity=".3" stroke-width="5" fill="none" stroke-linecap="round"/>
<rect x="77" y="10" width="46" height="30" rx="5" fill="url(#pkC)" stroke="#6E4E22"/>${ridges}<rect x="78" y="38" width="44" height="5" rx="1.5" fill="#B08A4C" stroke="#6E4E22" stroke-width=".8"/>
<path d="M120 52c10 2 14 6 16 12" stroke="#C9A15B" stroke-width="1.2" fill="none"/>
<g transform="rotate(10 144 78)"><rect x="124" y="62" width="44" height="31" rx="3" fill="#F4E8D2" stroke="#9E3B26" stroke-width="1.2"/><circle cx="129" cy="67" r="1.6" fill="#9E3B26"/><text x="147" y="77" text-anchor="middle" class="pkTag" fill="#9E3B26">GIỮ LẠNH</text><text x="147" y="87" text-anchor="middle" class="pkTag" fill="#4A2C1A">0–4 °C</text></g>
<rect x="42" y="174" width="116" height="180" fill="#F4E8D2"/>
<image href="assets/logo-mau.png" x="58" y="184" width="84" height="27"/>
<text x="100" y="245" text-anchor="middle" class="pkT" fill="#4A2C1A">COLD BREW</text>
<text x="100" y="262" text-anchor="middle" class="pkS" fill="#9E3B26">Robusta Di Linh</text>
<line x1="70" x2="130" y1="270" y2="270" stroke="#C9A15B" stroke-width="1.2"/>
<text x="100" y="284" text-anchor="middle" class="pkS2" fill="#4A2C1A">Ủ lạnh ${h} giờ · rang mộc</text>
<path d="M42 318L60 303L80 309L102 296L124 307L144 299L158 305V332H42Z" fill="#D9B77E"/><path d="M42 326L68 313L96 321L122 311L158 319V332H42Z" fill="#B8894A"/>
${[[52,320],[60,317],[68,315],[76,318],[86,320],[96,322],[106,318],[116,314],[126,314],[136,317],[146,318]].map(([x,y])=>`<circle cx="${x}" cy="${y+4}" r="2.2" fill="#6B4226"/>`).join('')}
<rect x="42" y="332" width="116" height="22" fill="#9E3B26"/><text x="100" y="346.5" text-anchor="middle" class="pkB" fill="#F6EBD9">${kind} · ${vol} ml</text>
<rect x="42" y="174" width="116" height="180" fill="url(#pkL)"/>
</svg>`}
function boxSvg(){
 const per=st.per,g=st.bag;
 return `<svg viewBox="0 52 306 246" role="img" aria-label="Hộp Cold Brew MeDili túi ủ lạnh ${per} túi ${g} g">
<ellipse cx="160" cy="284" rx="140" ry="9" fill="#2E1A10" fill-opacity=".16"/>
<polygon points="28,96 96,70 232,96 164,122" fill="#E4C78E" stroke="#6E4E22" stroke-width="1.3"/>
<polygon points="28,96 164,122 164,284 28,258" fill="#D3AF6A" stroke="#6E4E22" stroke-width="1.3"/>
<polygon points="164,122 232,96 232,256 164,284" fill="#B38C48" stroke="#6E4E22" stroke-width="1.3"/>
<g transform="matrix(1 .1912 0 1 28 96)">
 <rect x="0" y="0" width="136" height="24" fill="#9E3B26"/><text x="68" y="16" text-anchor="middle" class="pkB" fill="#F6EBD9">TÚI Ủ LẠNH</text>
 <image href="assets/logo-mau.png" x="26" y="32" width="84" height="27"/>
 <text x="68" y="88" text-anchor="middle" class="pkT" fill="#4A2C1A" style="font-size:25px">COLD BREW</text>
 <text x="68" y="104" text-anchor="middle" class="pkS" fill="#9E3B26">Robusta Di Linh</text>
 <path d="M0 132L22 118L44 125L70 112L96 122L118 114L136 120V162H0Z" fill="#B8894A"/><path d="M0 140L30 128L60 136L92 126L136 134V162H0Z" fill="#8D5A32"/>
 <text x="68" y="154" text-anchor="middle" class="pkB" fill="#F6EBD9">${per} TÚI × ${g} G</text>
</g>
<g transform="matrix(1 -.3824 0 1 164 122)">
 <text x="34" y="30" text-anchor="middle" class="pkS2" fill="#3A2416">Ủ tại nhà</text>
 <text x="34" y="46" text-anchor="middle" class="pkS2" fill="#3A2416">1 túi + ${g*8} ml</text>
 <text x="34" y="60" text-anchor="middle" class="pkS2" fill="#3A2416">ngăn mát</text>
 <text x="34" y="74" text-anchor="middle" class="pkS2" fill="#3A2416">18–24 giờ</text>
 <text x="34" y="88" text-anchor="middle" class="pkS2" fill="#9E3B26">pha 1:1</text>
 <circle cx="34" cy="116" r="13" fill="none" stroke="#9E3B26" stroke-width="1.6"/><path d="M28.5 109h11l-1.4 13h-8.2z" fill="#4A2C1A"/>
</g>
<g transform="rotate(-6 268 238)">
 <path d="M266 206c2-12 4-22 3-34" stroke="#B9A274" stroke-width="1.2" fill="none"/>
 <rect x="255" y="150" width="28" height="22" rx="2" fill="#9E3B26"/><text x="269" y="164" text-anchor="middle" class="pkTag" fill="#F6EBD9">MeDili</text>
 <rect x="240" y="206" width="56" height="64" rx="6" fill="#F6F0E4" stroke="#B9A274" stroke-width="1.4" stroke-dasharray="3 2"/>
 <rect x="245" y="212" width="46" height="52" rx="4" fill="#E3D9C6"/>
 ${[[252,222],[263,230],[276,220],[284,234],[256,246],[268,254],[281,248],[285,258],[252,258]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="2.1" fill="#6B4226" fill-opacity=".55"/>`).join('')}
</g>
</svg>`}
function backLabel(r){
 const bag=st.f==='bag',d=today(),e=bag?addM(d,6):addD(d,r.life-1);
 const name=bag?'COLD BREW MEDILI – CÀ PHÊ TÚI Ủ LẠNH':st.f==='rtd'?'COLD BREW MEDILI – CÀ PHÊ Ủ LẠNH UỐNG LIỀN':'COLD BREW MEDILI – CÀ PHÊ Ủ LẠNH CÔ ĐẶC';
 const ing=bag?'Cà phê Robusta rang xay 100 % (Robusta Di Linh).':'Nước, cà phê Robusta rang xay (Robusta Di Linh).';
 const qty=bag?`Khối lượng tịnh: ${st.per*st.bag} g (${st.per} túi × ${st.bag} g)`:`Thể tích thực: ${st.vol} ml`;
 const how=bag?`Cho 1 túi vào bình với ${st.bag*8} ml nước lọc, đậy kín, ngâm ngăn mát 18–24 giờ, nhấc túi ra. Pha 1:1 với nước, sữa hoặc đá. Cốt đã ủ giữ ngăn mát, dùng trong 3 ngày.`:st.f==='rtd'?'Lắc đều trước khi dùng. Uống lạnh hoặc rót trên đá.':'Lắc đều. Pha 1 phần cốt với 2 phần nước, sữa hoặc đá.';
 const keep=bag?'Nơi khô ráo, thoáng mát, tránh ánh nắng. Sau khi mở túi bạc, đóng kín và dùng sớm.':'Bảo quản lạnh 0–4 °C. Đậy kín và giữ lạnh sau khi mở.';
 const warn=bag?'Sản phẩm có caffeine. Cân nhắc khi dùng cho trẻ em, phụ nữ mang thai và người nhạy cảm với caffeine.':'Không dùng khi chai phồng, rỉ hoặc có mùi lạ. Không để ngoài tủ lạnh quá 2 giờ. Sản phẩm có caffeine.';
 const html=`<h4>${name}</h4><p><b>Thành phần:</b> ${ing}</p><p><b>${qty}</b></p><p><b>Hướng dẫn sử dụng:</b> ${how}</p><p><b>Bảo quản:</b> <span class="${bag?'':'red'}">${keep}</span></p><p><b>Cảnh báo:</b> ${warn}</p>
<div class="dt"><div><span>NSX</span>${dmy(d)}</div><div><span>HSD</span>${dmy(e)}</div><div><span>Mã lô</span>${lot()}</div></div>
<p><b>Số tự công bố:</b> ……/DSUNFOOD/${d.getFullYear()}</p><p><b>Tổ chức chịu trách nhiệm:</b> Công ty TNHH DSunfood, ${ADDR}. ĐT ${PHONE}.</p><p><b>Xuất xứ:</b> Việt Nam. Nguyên liệu từ farm MeDili, ${ADDR_FARM}.</p>`;
 $('backlbl').innerHTML=html;
 st.label=$('backlbl').innerText.replace(/\n{2,}/g,'\n');
}
function listing(r){
 const bag=st.f==='bag',conc=st.f==='conc';
 const title=bag?`Cold Brew MeDili túi ủ lạnh · Hộp ${st.per} túi × ${st.bag} g · Robusta Di Linh rang mộc`:`Cold Brew MeDili ${conc?'cô đặc':'uống liền'} ${st.vol} ml · Robusta Di Linh ủ lạnh ${st.h} giờ · Giao lạnh trong ngày`;
 const L=bag?[`100 % cà phê Robusta từ farm MeDili, Di Linh, Lâm Đồng, rang mộc City+, xay thô.`,`Mỗi túi ${st.bag} g ủ với ${st.bag*8} ml nước lọc trong ngăn mát 18–24 giờ, được khoảng ${fm(r.out)} ml cốt.`,'Pha 1:1 với nước, sữa tươi hoặc đá, tuỳ gu.',`Hộp ${st.per} túi, đóng trong túi bạc thổi nitơ.`,'Hàng khô, giao toàn quốc.']
  :[`100 % cà phê Robusta từ farm MeDili, Di Linh, Lâm Đồng, rang mộc City+.`,`Ủ lạnh ${st.h} giờ ở ${st.T} °C, lọc hai lần. Không đường, không chất bảo quản.`,conc?'Pha 1 phần cốt với 2 phần nước, sữa hoặc đá.':'Lắc đều, uống lạnh hoặc rót trên đá.','Bảo quản 0–4 °C, dùng trong 7 ngày kể từ ngày sản xuất.','Giao nội thành TP.HCM trong ngày, thùng xốp có đá gel.'];
 st.lst=title+'\n\n'+L.map(x=>'• '+x).join('\n');$('lst').textContent=st.lst}

/* ====== DỤNG CỤ, PHIẾU LÔ ====== */
function equip(r){
 const s=st,rows=[];
 if(s.f==='bag'){
  rows.push(['Cân điện tử','Cân bột từng đợt xay','Kiểm cân định kỳ']);
  rows.push(['Máy đóng gói túi lọc định lượng',`${fm(r.bags)} túi × ${s.bag}${NB}g`,'Hoặc thuê xưởng gia công đã có giấy an toàn thực phẩm']);
  rows.push(['Túi lọc không dệt dùng cho thực phẩm',`${fm(Math.ceil(r.bags*1.03))} túi`,'Dư 3 % cho hao hụt máy']);
  rows.push(['Túi bạc nhiều lớp có van một chiều',`${fm(Math.ceil(r.bags/5))} túi`,'5 túi lọc mỗi túi bạc']);
  rows.push(['Máy hàn miệng túi có thổi nitơ','1 máy','Kiểm mối hàn đầu mỗi ca']);
  rows.push(['Hộp kraft in Cold Brew MeDili',`${fm(r.boxes)} hộp`,`${s.per} túi mỗi hộp`]);
 }else{
  const tank=Math.ceil(r.W*1.4/10)*10,nb=Math.ceil(r.n*1.05);
  rows.push(['Cân điện tử','Cân bột và nước','1 lít nước khoảng 1 kg']);
  rows.push(['Bồn inox 304 có nắp, van xả đáy',`Từ ${fm(tank)}${NB}L`,'Chừa chỗ cho bột nở']);
  rows.push(['Túi lọc vải hoặc lưới nylon dùng cho thực phẩm',`${Math.ceil(s.R/2.5)} túi`,'Mỗi túi không quá 2,5 kg bột']);
  rows.push(['Giấy lọc hoặc vải lọc tinh, phễu inox','Lọc tầng hai','Thay giấy mỗi mẻ']);
  rows.push(['Kho lạnh hoặc tủ mát 0–4 °C',`Chứa bồn và ${fm(r.n)} chai`,'Đặt nhiệt kế trong kho']);
  rows.push(['Nhiệt kế, khúc xạ kế đo TDS','1 bộ','Ghi số vào phiếu lô']);
  rows.push(['Chai thủy tinh nâu, nắp có vòng niêm phong',`${fm(nb)} bộ`,'Dư 5 % phòng vỡ']);
  rows.push(['Nhãn decal chống ẩm',`${fm(nb)} nhãn`,'In ngày sản xuất, hạn dùng, mã lô']);
  rows.push(['Thùng xốp, đá gel','Theo đơn giao','Giao trong ngày']);
 }
 $('eqT').innerHTML=rows.map(([a,b,c])=>`<tr><td><b>${a}</b></td><td>${b}</td><td>${c}</td></tr>`).join('');
}
function sheet(r){
 const s=st,d=today();
 const head=`Mã lô: ${lot()}   Ngày: ${dmy(d)}   Người làm: __________
Cà phê: ${BEAN[s.bean].full}, ngày rang ________ (nghỉ 3–10 ngày)`;
 const t=s.f==='bag'?`PHIẾU LÔ · COLD BREW MEDILI TÚI Ủ LẠNH
${head}
Bột thô: ${vn(s.R*.99,1)} kg · ${s.bag} g mỗi túi · dự kiến ${fm(r.bags)} túi
Cân kiểm 10 túi (g): ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
Túi bạc thổi nitơ: ______ túi · mối hàn: đạt / chưa đạt
Đóng hộp: ______ hộp × ${s.per} túi · HSD ${dmy(addM(d,6))}
Kho khô: ______ °C · ghi chú: ____________________`
 :`PHIẾU LÔ · COLD BREW MEDILI ${s.f==='rtd'?'UỐNG LIỀN':'CÔ ĐẶC'}
${head}
Bột thô: ${vn(s.R*.99,1)} kg · nước ${fm(r.W)} L (1:${vn(s.ratio,1)}) · mục tiêu ${s.T} °C, ${s.h} giờ
Bắt đầu ngâm: ______ giờ · nhấc túi: ______ giờ
Nhiệt độ kho: đầu mẻ ____ °C · giữa mẻ ____ °C · lúc lọc ____ °C
Cốt sau lọc: ______ L (mô hình ${vn(r.Vc,1)} L) · TDS đo ____ % (mô hình ${vn(r.tdsC,1)} %)${s.f==='rtd'?`
Nước pha thêm: ______ L (mô hình ${vn(r.add,1)} L) · TDS sau pha ____ % (mục tiêu ${vn(s.tds,1)} %)`:''}
Chiết rót: ______ chai ${s.vol} ml (mô hình ${fm(r.n)}) · HSD ${dmy(addD(d,FMT[s.f].life-1))}
Lưu 2 chai mẫu đến hết hạn · nếm so mẫu chuẩn: đạt / chưa đạt
Ghi chú: ____________________`;
 st.sheet=t;$('sheet').textContent=t;
}

/* ====== ĐIỀU KHIỂN ====== */
function pills(id,items,cur,cb){$(id).innerHTML=items.map(([k,n])=>`<button class="pill" type="button" data-k="${k}" aria-pressed="${String(cur)===String(k)}">${n}</button>`).join('');$(id).querySelectorAll('button').forEach(b=>b.onclick=()=>cb(b.dataset.k))}
const sym=k=>k==='good'?'✓':k==='warn'?'!':'✕';
function stats(r){const s=st,t=(a,b)=>`<div class="stat"><span>${a}</span><b>${b}</b></div>`;
 $('stats').innerHTML=s.f==='bag'?t('Số túi',fm(r.bags))+t('Số hộp',fm(r.boxes))+t('Cốt mỗi túi',fm(r.out)+NB+'ml')+t('Hạn dùng','6 tháng')
  :s.f==='rtd'?t('Uống liền',vn(r.Vout,1)+NB+'L')+t('TDS chai',vn(r.low?r.tdsC:s.tds,1)+NB+'%')+t('Số chai',fm(r.n))+t('Hạn dùng','7 ngày')
  :t('Cốt thu được',vn(r.Vc,1)+NB+'L')+t('TDS cốt',vn(r.tdsC,1)+NB+'%')+t('Số chai',fm(r.n))+t('Hạn dùng','7 ngày')}
function renderStation(){
 const s=ST[st.sel-1],r=calc(),x=st.sel===10?K10[st.f==='bag'?'dry':'cold']:s,off=!use(st.sel);
 document.querySelectorAll('#scene .st').forEach(g=>g.classList.toggle('on',+g.dataset.i===st.sel));
 document.querySelectorAll('#strip button').forEach((b,n)=>{b.classList.toggle('on',n+1===st.sel);b.classList.toggle('off',!use(n+1));b.setAttribute('aria-pressed',n+1===st.sel)});
 $('detail').innerHTML=`<div class="dh"><div class="dn">${st.sel}</div><h2>${s.n}<small>${s.sub()}${off?' · không dùng cho '+FMT[st.f].n.toLowerCase():''}</small></h2></div><div class="dgrid"><div><span class="lbl">Cách làm</span><p>${s.mech(r)}</p><span class="lbl">Kiểm tra thế nào</span><p>${x.check}</p></div><div><span class="lbl">Thông số mẻ này</span><dl class="kv">${(off?[['Dùng cho',st.sel===8?'Dạng túi ủ lạnh':'Dạng chai cô đặc và chai uống liền'],['Đang chọn',FMT[st.f].n]]:s.kv(r)).map(([a,b])=>`<dt>${a}</dt><dd>${b}</dd>`).join('')}</dl><p style="margin-top:8px"></p><span class="lbl">Lỗi hay gặp</span><p>${x.fail}</p><span class="lbl">Mẹo</span><p>${x.tip}</p></div></div>`;
}
function select(i){st.sel=i;renderStation();drawChips(calc());const sc=document.querySelector('.scroller'),q=P(...ANCH[i]);if(sc.scrollWidth>sc.clientWidth)sc.scrollLeft=q[0]/1040*sc.scrollWidth-sc.clientWidth/2}
function sliders(){const set=(id,v)=>{$(id).value=v};
 set('iR',st.R);set('iRa',st.ratio);set('iT',st.T);set('iH',st.h);set('iS',st.tds);set('iB',st.bag);
 $('oR').textContent=st.R+NB+'kg';$('oRa').textContent='1:'+vn(st.ratio,1);$('oT').textContent=st.T+NB+'°C';$('oH').textContent=st.h+' giờ';$('oS').textContent=vn(st.tds,1)+NB+'%';$('oB').textContent=st.bag+NB+'g';
 $('tNote').textContent=st.T<=5?'Kho lạnh hoặc tủ mát 2–5 °C, đúng mức khuyến nghị.':st.T<=8?'Hơi ấm cho kho lạnh, đưa về 2–5 °C.':'Nhiệt độ phòng: chỉ hợp quán pha dùng trong ngày.';
 $('bgNote').textContent=`Mỗi túi pha với ${st.bag*8}${NB}ml nước, tỷ lệ 1:8 như cold brew ở Quầy pha.`;
 $('grpC').hidden=st.f==='bag';$('grpB').hidden=st.f!=='bag';$('grpR').hidden=st.f!=='rtd';
}
function update(){
 const r=calc(),v=verdict(r);
 pills('fmts',Object.entries(FMT).map(([k,f])=>[k,f.n]),st.f,k=>{st.f=k;if(!use(st.sel))st.sel=k==='bag'?8:5;stopRun();update()});
 pills('beans',Object.entries(BEAN).map(([k,b])=>[k,b.n]),st.bean,k=>{st.bean=k;update()});
 pills('vols',[250,330,500].map(x=>[x,x+NB+'ml']),st.vol,k=>{st.vol=+k;update()});
 pills('pers',[5,10].map(x=>[x,x+' túi']),st.per,k=>{st.per=+k;update()});
 $('fNote').textContent=FMT[st.f].note;$('bNote').textContent=BEAN[st.bean].note;
 sliders();stats(r);
 $('verdict').className=v.k;$('verdict').innerHTML=`<b>${sym(v.k)} ${v.t}</b>${v.m}`;
 $('figsub').textContent=`dây chuyền 10 trạm, ${FMT[st.f].n.toLowerCase()}, mẻ ${g1(st.R)}${NB}kg cà phê rang`;
 renderScene(r);drawCT(r);sop(r);
 $('pkBottle').innerHTML=bottleSvg();$('pkBox').innerHTML=boxSvg();
 $('pkBc').textContent=`Chai Cold Brew MeDili ${st.f==='rtd'?'uống liền':'cô đặc'} ${st.f==='bag'?250:st.vol} ml, thủy tinh nâu, nhãn quấn thân`;
 $('pkXc').textContent=`Hộp túi ủ lạnh ${st.per} túi × ${st.bag} g, giấy kraft in hai màu`;
 backLabel(r);listing(r);equip(r);sheet(r);renderStation();
}

/* ====== CHẠY DÂY CHUYỀN ====== */
const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
let timer=0;
function stopRun(){clearTimeout(timer);timer=0;$('scene').classList.remove('running')}
function run(){
 stopRun();const seq=[1,2,3,4,5,6,7,8,9,10].filter(i=>use(i));
 if(still){select(seq[seq.length-1]);return}
 $('scene').classList.add('running');let k=0;
 const step=()=>{const i=seq[k],q=P(ANCH[i][0],ANCH[i][1],ANCH[i][2]-1.2),t=$('tok');t.setAttribute('cx',f1(q[0]));t.setAttribute('cy',f1(q[1]));select(i);k++;
  if(k<seq.length)timer=setTimeout(step,700);else timer=setTimeout(()=>$('scene').classList.remove('running'),900)};
 step();
}

/* ====== KHỞI ĐỘNG ====== */
$('strip').innerHTML=ST.map((s,i)=>`<button type="button" aria-pressed="false">${i+1} ${s.n}</button>`).join('');
$('strip').querySelectorAll('button').forEach((b,i)=>b.onclick=()=>select(i+1));
const onIn=(id,f)=>$(id).addEventListener('input',()=>{stopRun();f(+$(id).value);update()});
onIn('iR',v=>st.R=v);onIn('iRa',v=>st.ratio=v);onIn('iT',v=>st.T=v);onIn('iH',v=>st.h=v);onIn('iS',v=>st.tds=v);onIn('iB',v=>st.bag=v);
$('run').onclick=run;$('run2').onclick=run;$('reset').onclick=()=>{stopRun();const f=st.f;Object.assign(st,DEF,{f});update()};
const cp=async(txt,el)=>{try{await navigator.clipboard.writeText(txt);$(el).textContent='Đã sao chép.'}catch(e){$(el).textContent='Không sao chép được, hãy bôi đen để chép.'}setTimeout(()=>$(el).textContent='',2600)};
$('cpLbl').onclick=()=>cp(st.label,'cpLblS');$('cpLst').onclick=()=>cp(st.lst,'cpLstS');$('cpSh').onclick=()=>cp(st.sheet,'cpShS');
buildScene();update();
'''
