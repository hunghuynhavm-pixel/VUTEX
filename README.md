# VUTEX — Đăng bài tự động lên GoHighLevel (GHL)

Tự động đăng **Blog** và bài **Mạng xã hội (Social Planner)** lên GHL.
Anh chỉ cần bỏ file bài viết vào thư mục `content/`, GitHub Actions sẽ tự đăng.

---

## 🚀 Cần chuẩn bị gì? (3 bước)

### Bước 1 — Lấy thông tin từ GHL
Vào tài khoản GHL của anh, lấy 4 thứ sau:

| Thông tin | Lấy ở đâu |
|-----------|-----------|
| **Token** | Settings → Private Integrations → tạo token mới (chọn quyền: blogs, social planner) |
| **Location ID** | Settings → Business Info, hoặc trong URL sub-account |
| **Blog ID** | Chạy `python post.py --list` sau khi có Token + Location ID |
| **Author ID** | Cũng lấy từ lệnh `--list` ở trên |

> ⚠️ **KHÔNG dán các thông tin này thẳng vào file rồi upload GitHub.** Chúng là bí mật.

### Bước 2 — Nạp bí mật vào GitHub Secrets
Trên GitHub: **repo → Settings → Secrets and variables → Actions → New repository secret**.
Thêm lần lượt:

- `GHL_TOKEN`
- `GHL_LOCATION_ID`
- `GHL_BLOG_ID`
- `GHL_AUTHOR_ID`

### Bước 3 — Đăng bài
- **Đăng blog:** tạo file `.md` mới trong `content/blog/` (xem file mẫu).
- **Đăng MXH:** tạo file `.md` mới trong `content/social/` (xem file mẫu).
- **Commit + push lên nhánh `main`** → GitHub Actions tự động chạy và đăng.

Xem tiến trình ở tab **Actions** trên GitHub.

---

## 🖥️ Chạy tay ở máy (để thử nghiệm)

```bash
pip install -r requirements.txt
cp .env.example .env      # rồi điền thông tin vào .env
python post.py --list     # xem ID blog / tác giả / danh mục / tài khoản MXH
python post.py --dry-run  # thử, không gọi API thật
python post.py            # đăng thật
```

---

## 📁 Cấu trúc

```
content/blog/     → mỗi file .md là 1 bài blog
content/social/   → mỗi file .md là 1 bài mạng xã hội
ghl/              → mã nguồn gọi API GHL
post.py           → script chính
.ghl_posted.json  → sổ ghi bài đã đăng (tự sinh, tránh đăng trùng)
.github/workflows → cấu hình tự động chạy
```

## ❓ Chống đăng trùng
Mỗi bài đã đăng được ghi vào `.ghl_posted.json` kèm mã băm nội dung.
Chạy lại sẽ **bỏ qua** bài không đổi, và **đăng lại** nếu anh sửa nội dung file.

## ⏰ Đăng theo lịch (tuỳ chọn)
Mở `.github/workflows/post-to-ghl.yml`, bỏ dấu `#` ở phần `schedule` để bật.
