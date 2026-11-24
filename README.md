# MeDili Café · web medili.vn

Kho này chứa toàn bộ web MeDili và bộ mã dựng web.

| Thư mục | Nội dung |
|---|---|
| `site-new4/` | **Web hoàn chỉnh**: các trang, ảnh, dữ liệu giá cà phê. Đây là thư mục được đưa lên medili.vn. |
| `art/` | Bộ mã dựng web (Python). Chạy `python3 art/build_manus.py` để dựng lại `site-new4/`. |
| `art/cuahang.py`, `art/data/manus-catalog.json` | Cửa hàng (dựng theo cấu trúc web medilinh.com): trang `cua-hang.html`, 20 trang sản phẩm `sp-*.html`, giỏ hàng `gio-hang.html`, tìm kiếm `tim-kiem.html` (chỉ mục `tim-kiem.json`), `sitemap.xml`, `robots.txt`. Giỏ lưu trên trình duyệt, khách gửi đơn qua Google Form, Zalo hoặc email. |
| `art/make_photos.py`, `art/make_gallery.py`, `art/anhvuon.py` | Ảnh thật: cắt, nén, bỏ EXIF/GPS và đóng logo chìm MeDili lên **mọi ảnh dùng trên web**. `anhvuon.py` giữ danh sách ảnh trang Ảnh vườn (`anh-vuon.html`, 4 nhóm Vườn · Hái · Thu hoạch · Phơi & xay) và ảnh nền toàn khung `bg-*.jpg` (bản máy tính và bản điện thoại `-m`, logo chìm ở góc dưới phải, web neo ảnh nền ở góc đó). |
| `art/huongdan.py`, `art/hd3d.js`, `art/hdshot.js` | Trang **Hướng dẫn pha** (`huong-dan-pha.html`): bốn cách pha phin, pour-over, espresso, cold brew với mô hình 3D dựng bằng code (three.js r160, giấy phép MIT). Bộ dựng gộp `hd3d.js` với three.js thành `site-new4/assets/hd3d.js` (cần `npm install` để có esbuild). Máy không chạy được 3D thì hiện ảnh dự phòng `assets/hd-*.webp`; sửa mô hình xong thì chụp lại ảnh bằng `node hdshot.js`. |
| `art/donghanh.py` | Trang **Đồng hành cùng quán** (`dong-hanh-cung-quan.html`) cho khách quán: chọn theo ưu tiên (tối ưu giá vốn, cân bằng, chất lượng) → ba dòng Classic, Premium, Arabica & Specialty kèm giá sỉ cấp 1 (lấy từ Phòng chọn mua) → các bước đồng hành → phiếu liên hệ (mở Google Form hoặc dán vào Zalo). Cam kết chị Ngân chốt 23/11/2026: mẫu thử 50 g miễn phí, phản hồi Zalo trong 60 phút (6:30–22:30), có hướng dẫn công thức, chỉnh cối xay, bảo trì máy. |
| `art/chinhsach.py` | Trang **Chính sách MeDili** (`chinh-sach.html`) có 4 thẻ: Khách sỉ, Đổi trả, Kiểm hàng, Hoàn tiền (mở thẳng một thẻ bằng `chinh-sach.html#khach-si`, `#doi-tra`, `#kiem-hang`, `#hoan-tien`). Chị Ngân chốt 23/11/2026: thanh toán chuyển khoản hoặc tiền mặt, linh hoạt; hoàn tiền trong 5 ngày; miễn phí giao từ 10 kg; hóa đơn VAT do Công ty TNHH DSunfood xuất. |
| `art/thanhtoan.py` | Trang **Thanh toán** (`thanh-toan.html`, chị Ngân yêu cầu 24/11/2026): mã VietQR chuyển khoản vào tài khoản công ty (hằng số `BANK` trong `kit.py`), quét được bằng app ngân hàng, MoMo, ZaloPay; số tiền và nội dung (mã đơn) tự điền. Link thanh toán: `thanh-toan.html?ma=MD24113520&tien=475200`; `&pt=cod` (tiền mặt khi nhận), `&pt=sau` (Phòng chọn mua, thanh toán sau), `&pt=bg` (chờ báo giá). Cuối trang có ô để MeDili tự tạo link gửi khách. Mã QR dựng trên trình duyệt bằng `assets/qrcode.js` (qrcode-generator, MIT). Trên điện thoại, khách chọn app ngân hàng: link qua dịch vụ deeplink của VietQR (`https://dl.vietqr.io/pay?app=…&ba=STK@vcb&am=…&tn=mã đơn&bn=…&url=…`, Casso); MB, VietinBank, BIDV, ACB, OCB tự điền số tiền và nội dung, app khác chỉ mở app (danh sách: vietqr.io/deeplink/bank-apps, cập nhật mã app trong `thanhtoan.py`). Giỏ hàng và Phòng chọn mua gửi đơn thẳng vào Google Form (chỉ trên medili.vn; bản xem trước không gửi thật) rồi chuyển sang trang này. |
| `kit.float_links()` | Nút **Zalo** và **FB** nổi ở góc trái bên dưới mọi trang (gắn sau chân trang). Link Facebook ở hằng số `FACEBOOK` trong `kit.py`. |
| `artifact-main/index.html` | Trang chủ dạng mảnh (không có phần đầu trang) để đăng bản xem trước trên Claude; khung của Claude tự thêm phần đầu. Bản đầy đủ cho medili.vn là `site-new4/index.html`. |
| `site-new3/`, `site-live/`, `artifact-files/`, `run-check/` | Dữ liệu đầu vào cho bộ dựng. |
| `art/i18n.py`, `art/i18n/` | **Bản tiếng Anh, Nhật, Trung** (`site-new4/en`, `ja`, `zh`, chị Ngân yêu cầu 24/11/2026): dịch theo từ điển `i18n/en.json`, `ja.json`, `zh.json` (khóa là câu tiếng Việt), thuật ngữ ở `i18n/GLOSSARY.md`. `build_manus.py` tự ráp ba bản này, thêm nút chọn ngôn ngữ, hreflang, phông chữ Nhật/Trung, số và ngày theo từng ngôn ngữ. |
| `hosting/sync.php` | Tác vụ chạy trên hosting: mỗi 30 phút đọc kho này, tải các file mới hoặc đã đổi trong `site-new4/` vào `public_html` của medili.vn. |

## Cập nhật web

- **Sửa web:** dựng lại `site-new4/`, đẩy lên nhánh `main`. Hosting tự lấy bản mới trong vòng 30 phút.
- **Giá cà phê:** tác vụ theo lịch "Cập nhật giá cà phê MeDili" chạy 13:38 và 19:38 (giờ Việt Nam). Mỗi lần: tra giá (Báo Lâm Đồng; dự phòng VietNamNet và bài báo giá trong ngày, cần ít nhất 2 báo khớp nhau), ghi `site-new4/gia-ca-phe.json` và bản sao `run-check/gia-ca-phe.json`, đẩy lên `main` với thông điệp "Giá cà phê dd/mm" (cách chính: công cụ GitHub `push_files`; dự phòng: `git push`), rồi cập nhật bản xem trước trên Claude kèm nhật ký `nhat-ky-gia.txt`. Lần 19:38 là lần kiểm tra lại, đủ dữ liệu thì dừng sớm.
- **Đăng bản xem trước bằng tay:** không gửi `gia-ca-phe.json` (để tác vụ giá quản lý), tránh các khung 13:30–13:45 và 19:30–19:45.
- **Sửa chữ tiếng Việt:** dựng lại rồi chạy `python3 art/i18n.py extract` và `python3 art/i18n.py status`; câu mới hoặc câu đã sửa phải được dịch (xem `art/i18n/GLOSSARY.md`) trước khi đẩy lên, nếu không bản EN/JA/ZH sẽ hiện câu tiếng Việt ở chỗ đó.
- **Chữ của các trang cũ** (`gia-ca-phe`, `vuon`, `trai-ca-phe`, `len-men-*`, `rang`, `quay-pha`, `suc-khoe`, `tu-vuon-den-ly`, `mua-hang`) sửa thẳng trong `site-new3/*.html`; các bộ dựng cũ (`build_site.py`, `build_f2c.py`, `build_gia.py`) không còn dùng.

## Quy ước câu chữ (chị Ngân chốt 23/11/2026)

- **Dấu thanh** kiểu phổ biến: hóa, khỏe, tòa, thủy, ủy (không viết hoá, khoẻ, toà, thuỷ, uỷ).
- **Tiếng Anh:** chỉ giữ 3 câu khẩu hiệu "A little coffee, a lot of connection", "Di Linh origin · Saigon soul", "Farm to cup". Phần mô tả viết tiếng Việt. Giữ tên riêng và tên dòng sản phẩm (Robusta, Arabica, Culi, Catimor, Moka, Fine Robusta, Classic, Premium, Specialty, Signature, Blend, Ngũ Hành), tên đồ uống (espresso, cappuccino, latte, Americano, cold brew), tên cách sơ chế viết hoa: Natural, Honey, Washed. Tên vườn là **MeDili Coffee Farm**; trong câu văn dùng "vườn MeDili".
- **Thuật ngữ thống nhất:** cà phê (không viết cafe trừ tên MeDili Café), nhân xanh, lớp nhớt, độ ẩm 10–12%, chua thanh (không viết "chua sáng"), acid, socola, ca cao, phân ủ (compost), thực đơn (không viết menu trong câu văn), thử nếm (cupping), hồ sơ rang, đường cong nhiệt, chiết xuất thiếu / quá mức, sao chép, trực tuyến, phù hợp với (không mở câu bằng "Hợp …"), ép Pháp, pour-over, tỷ lệ.
- **Trình bày:** 8% (không cách trước %), 24 °C (có cách trước °C), 0966 770 788, ngoặc kép “ ”, dấu ba chấm …, tiêu đề viết hoa chữ đầu câu (Câu chuyện MeDili, không viết Câu Chuyện MeDili), gọi khách là "bạn".

## Kiểm tra

```
cd art && npm install
node t5.js        # toàn site: tràn khung, lỗi, link nội bộ
node nxtest.js    # trang Chọn nhân xanh
node hdshot.js    # chụp lại ảnh dự phòng của trang Hướng dẫn pha (sau khi dựng web)
```
