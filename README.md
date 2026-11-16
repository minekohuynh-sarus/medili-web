# MeDili Café · web medili.vn

Kho này chứa toàn bộ web MeDili và bộ mã dựng web.

| Thư mục | Nội dung |
|---|---|
| `site-new4/` | **Web hoàn chỉnh**: các trang, ảnh, dữ liệu giá cà phê. Đây là thư mục được đưa lên medili.vn. |
| `art/` | Bộ mã dựng web (Python). Chạy `python3 art/build_manus.py` để dựng lại `site-new4/`. |
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
