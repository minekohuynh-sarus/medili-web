# Trang Lên men tự thân trái cà phê (chị Ngân yêu cầu 25/11/2026, đặt trong mục Vùng trồng & sản xuất).
# Clip 3D 62 giây dựng bằng three.js: không cấy men, không thêm trái cây, ủ kín có van, dừng theo pH, phơi Natural, Honey, Washed.
# Nội dung clip theo Cỗ máy Vi sinh và Cỗ máy Lên men cùng trái cây (bản thùng đối chứng không trái cây, không cấy men).
# Video: assets/len-men-tu-than.mp4 (720×1280, H.264, không tiếng), ảnh chờ assets/len-men-tu-than.jpg (khung có logo MeDili).
from kit import *
from pages_a import head

FILE = 'len-men-tu-than.html'
VIDEO, POSTER = 'len-men-tu-than.mp4', 'len-men-tu-than.jpg'

STEPS = [
    ('trai', 'Thu hái trong ngày', 'Trái chín từ 90%, Brix 18–22. Trái hái về để trong bao qua đêm đã bắt đầu lên men, nên MeDili sơ chế ngay trong ngày.'),
    ('kinh', 'Tuyển nổi', 'Thả trái vào bể nước: trái chín đặc chìm xuống, trái lép và sâu nhẹ nổi lên, được gạt bỏ trước khi mang mốc vào thùng.'),
    ('visinh', 'Vi sinh tự thân', 'Không cấy men. Nấm men và vi khuẩn lactic sống sẵn trên vỏ, cuống trái tự làm việc. Mỗi vườn một hệ vi sinh riêng.'),
    ('soi', 'Ba cách sơ chế', 'Natural giữ nguyên trái, vỏ còn nguyên nên đường khuếch tán chậm. Honey và Washed xát tươi, giữ lớp nhớt làm thức ăn cho vi sinh.'),
    ('lanh', 'Ủ kín có van', 'Thùng nhựa thực phẩm, nắp gioăng, van một chiều, chừa 20% khoảng trống. Ủ 48–96 giờ tùy mẻ, thùng 22–24 °C, để nơi mát, che nắng.'),
    ('phantu', 'Ba nhóm vi sinh', 'Nấm men tạo cồn, CO₂ và hương trái cây. Vi khuẩn lactic hạ pH đều, chua dịu. Vi khuẩn acetic cần oxy nên bị thùng kín chặn.'),
    ('so', 'Đo và dừng ủ', 'Mỗi 6 giờ đo pH, Brix, nhiệt độ và ngửi mùi. Dừng khi chạm pH 4,0–4,4, không để dưới 4,0. Mốc, mùi thối, mùi sơn: bỏ mẻ.'),
    ('soche', 'Rửa hay chỉ lọc', 'Washed rửa sạch lớp nhớt tới khi hạt nhám như sỏi. Honey và Natural không rửa, chỉ lọc xác trái, đưa lên giàn trong ngày.'),
    ('phoi', 'Giàn sấy', 'Giàn cao có mái, rải mỏng, đảo bằng cào nhiều lần trong ngày, tới độ ẩm 10,5–11,5%. Phơi dày không đảo dễ mốc.'),
    ('tui', 'Ủ và thử nếm', 'Đóng bao kín khí, ghi mã mẻ, để nơi mát, tối, kê cao khỏi sàn. Thử nếm mù mỗi 2 tuần, mẻ nào hơn hẳn đối chứng mới làm lớn.'),
]

CSS = r'''
/* Trang Lên men tự thân: clip dọc 9:16 bên trái, các bước bên phải; điện thoại xếp chồng. */
.vclip{display:grid;grid-template-columns:minmax(0,400px) minmax(0,1fr);gap:22px 34px;align-items:start}
.vf{margin:0;display:grid;gap:8px;position:sticky;top:calc(76px + env(safe-area-inset-top,0px))}
.vf video{display:block;width:100%;height:auto;aspect-ratio:9/16;max-height:calc(100vh - 140px);border-radius:16px;border:1px solid var(--rule);background:#231812;object-fit:contain}
.vf figcaption{font:400 .84rem/1.45 var(--body);color:var(--muted)}
.vclip .pst h3 small{display:block;margin:0 0 2px}
@media (max-width:860px){.vclip{grid-template-columns:minmax(0,1fr)}.vf{position:static;width:100%;max-width:420px;justify-self:center}.vf video{max-height:none}}
'''


def page():
    steps = ''.join(f'<li><span class="n">{icon(k)}</span><h3><small>Bước {i:02d}</small>{t}</h3><p>{d}</p></li>'
                    for i, (k, t, d) in enumerate(STEPS, 1))
    body = head('Vùng trồng & sản xuất · Clip 3D', 'Lên men tự thân <em>trái cà phê.</em>',
                'Không cấy men, không thêm trái cây. Vi sinh có sẵn trên chính trái cà phê của vườn MeDili làm việc trong thùng kín, '
                'rồi hạt được phơi theo Natural, Honey hoặc Washed.',
                '<a class="btn main" href="#clip">Xem clip</a><a class="btn" href="vi-sinh.html">Cỗ máy Vi sinh</a>')
    body += f'''
<section class="facts" aria-label="Lên men tự thân qua các con số">
 <div><b>48–96 giờ</b><span>ủ kín, tùy mẻ</span></div>
 <div><b>pH 4,0–4,4</b><span>vùng dừng ủ</span></div>
 <div><b>10,5–11,5%</b><span>độ ẩm đích khi phơi</span></div>
 <div><b>3 cách</b><span>Natural, Honey, Washed</span></div>
</section>

<section class="vclip" id="clip" aria-label="Clip quy trình lên men tự thân">
 <figure class="vf">
  <video controls playsinline preload="metadata" poster="assets/{POSTER}" width="720" height="1280" aria-label="Clip 3D quy trình lên men tự thân trái cà phê MeDili">
   <source src="assets/{VIDEO}" type="video/mp4">
  </video>
  <figcaption>Clip 3D 62 giây, 10 bước, không có tiếng. Đường pH trong phiếu theo dõi và số ngày phơi là mốc từ mô hình minh họa, cần đo thực tế từng mẻ.</figcaption>
 </figure>
 <div class="p-sec">
  <p class="eye">Trong clip</p>
  <h2 class="p-h2" style="margin:0">Mười bước <em>từ trái chín đến bao kín.</em></h2>
  <ol class="pst">{steps}</ol>
  <div class="lnks"><a class="lnk" href="vi-sinh.html">Cỗ máy Vi sinh</a><a class="lnk" href="len-men-trai-cay.html">Lên men cùng trái cây</a><a class="lnk" href="len-men-men-bia.html">Lên men bằng men bia</a><a class="lnk" href="anh-vuon.html">Ảnh vườn MeDili</a></div>
 </div>
</section>
'''
    return doc(FILE, 'Lên men tự thân trái cà phê · MeDili',
               'Clip 3D quy trình lên men tự thân trái cà phê ở vườn MeDili Di Linh: không cấy men, không thêm trái cây, ủ kín có van, '
               'dừng theo pH, phơi Natural, Honey, Washed.',
               body, css=CSS, wrap_cls='wrap pg')
