# MeDili Café · web medili.vn

Kho này chứa toàn bộ web MeDili và bộ mã dựng web.

| Thư mục | Nội dung |
|---|---|
| `site-new4/` | **Web hoàn chỉnh**: các trang, ảnh, dữ liệu giá cà phê. Đây là thư mục được đưa lên medili.vn. |
| `art/` | Bộ mã dựng web (Python). Chạy `python3 art/build_manus.py` để dựng lại `site-new4/`. |
| `art/cuahang.py`, `art/data/manus-catalog.json` | Cửa hàng (dựng theo cấu trúc web medilinh.com): trang `cua-hang.html`, 20 trang sản phẩm `sp-*.html`, giỏ hàng `gio-hang.html`, tìm kiếm `tim-kiem.html` (chỉ mục `tim-kiem.json`), `sitemap.xml`, `robots.txt`. Giỏ lưu trên trình duyệt, khách gửi đơn qua Google Form, Zalo hoặc email. |
| `artifact-main/index.html` | Trang chủ dạng mảnh (không có phần đầu trang) để đăng bản xem trước trên Claude; khung của Claude tự thêm phần đầu. Bản đầy đủ cho medili.vn là `site-new4/index.html`. |
| `site-new3/`, `site-live/`, `artifact-files/`, `run-check/` | Dữ liệu đầu vào cho bộ dựng. |
| `hosting/sync.php` | Tác vụ chạy trên hosting: mỗi 30 phút đọc kho này, tải các file mới hoặc đã đổi trong `site-new4/` vào `public_html` của medili.vn. |

## Cập nhật web

- **Sửa web:** dựng lại `site-new4/`, đẩy lên nhánh `main`. Hosting tự lấy bản mới trong vòng 30 phút.
- **Giá cà phê:** tác vụ cập nhật hằng ngày ghi vào `site-new4/gia-ca-phe.json`.

## Kiểm tra

```
cd art && npm install
node t5.js        # toàn site: tràn khung, lỗi, link nội bộ
node nxtest.js    # trang Chọn nhân xanh
```
