# MeDili Café · web medili.vn

Kho này chứa toàn bộ web MeDili và bộ mã dựng web.

| Thư mục | Nội dung |
|---|---|
| `site-new4/` | **Web hoàn chỉnh**: các trang, ảnh, dữ liệu giá cà phê. Đây là thư mục được đưa lên medili.vn. |
| `art/` | Bộ mã dựng web (Python). Chạy `python3 art/build_manus.py` để dựng lại `site-new4/`. |
| `art/cuahang.py`, `art/data/manus-catalog.json` | Cửa hàng (dựng theo cấu trúc web medilinh.com): trang `cua-hang.html`, 20 trang sản phẩm `sp-*.html`, giỏ hàng `gio-hang.html`, tìm kiếm `tim-kiem.html` (chỉ mục `tim-kiem.json`), `sitemap.xml`, `robots.txt`. Giỏ lưu trên trình duyệt, khách gửi đơn qua Google Form, Zalo hoặc email. |
| `art/make_photos.py`, `art/make_gallery.py`, `art/anhvuon.py` | Ảnh thật: cắt, nén, bỏ EXIF/GPS và đóng logo chìm MeDili lên **mọi ảnh dùng trên web**. `anhvuon.py` giữ danh sách ảnh trang Ảnh vườn (`anh-vuon.html`, 4 nhóm Vườn · Hái · Thu hoạch · Phơi & xay) và ảnh nền toàn khung `bg-*.jpg` (bản máy tính và bản điện thoại `-m`, logo chìm ở góc dưới phải, web neo ảnh nền ở góc đó). |
| `artifact-main/index.html` | Trang chủ dạng mảnh (không có phần đầu trang) để đăng bản xem trước trên Claude; khung của Claude tự thêm phần đầu. Bản đầy đủ cho medili.vn là `site-new4/index.html`. |
| `site-new3/`, `site-live/`, `artifact-files/`, `run-check/` | Dữ liệu đầu vào cho bộ dựng. |
| `hosting/sync.php` | Tác vụ chạy trên hosting: mỗi 30 phút đọc kho này, tải các file mới hoặc đã đổi trong `site-new4/` vào `public_html` của medili.vn. |

## Cập nhật web

- **Sửa web:** dựng lại `site-new4/`, đẩy lên nhánh `main`. Hosting tự lấy bản mới trong vòng 30 phút.
- **Giá cà phê:** tác vụ theo lịch "Cập nhật giá cà phê MeDili" chạy 13:38 và 19:38 (giờ Việt Nam). Mỗi lần: tra giá (Báo Lâm Đồng; dự phòng VietNamNet và bài báo giá trong ngày, cần ít nhất 2 báo khớp nhau), ghi `site-new4/gia-ca-phe.json` và bản sao `run-check/gia-ca-phe.json`, đẩy lên `main` với thông điệp "Giá cà phê dd/mm" (cách chính: công cụ GitHub `push_files`; dự phòng: `git push`), rồi cập nhật bản xem trước trên Claude kèm nhật ký `nhat-ky-gia.txt`. Lần 19:38 là lần kiểm tra lại, đủ dữ liệu thì dừng sớm.
- **Đăng bản xem trước bằng tay:** không gửi `gia-ca-phe.json` (để tác vụ giá quản lý), tránh các khung 13:30–13:45 và 19:30–19:45.

## Kiểm tra

```
cd art && npm install
node t5.js        # toàn site: tràn khung, lỗi, link nội bộ
node nxtest.js    # trang Chọn nhân xanh
```
