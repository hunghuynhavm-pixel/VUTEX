---
tai_lieu: Bàn giao — công thức làm content VUTEX (nén từ phiên làm việc 18-20/07/2026)
muc_dich: Đọc file này là làm tiếp được, không cần lịch sử chat
page: Hưng Huỳnh - Chuyên gia Video Marketing
ngay: 2026-07-20
---

# Bàn giao content VUTEX

File này nén toàn bộ cách làm để **phiên sau (hoặc bản web) đọc là làm tiếp được ngay**,
không cần lịch sử trò chuyện.

---

## 1. Bối cảnh

- **VUTEX** = vault tự động soạn & đăng bài Facebook cho page **Hưng Huỳnh - Chuyên gia Video Marketing**
  qua **GoHighLevel / FunnelTex Social Planner API**.
- Chủ đề đang chạy: **Claude Code / dùng AI** — sếp Hưng giao "đăng bài giá trị về code, có CTA thu lead".
- Page đích: `.env` trỏ sẵn page "Chuyên gia Video Marketing" (accountId `...110353061977026_page`).

## 2. Giọng & luật nội dung (KHÓA CỨNG)

- Ngôi thứ 3, xưng **"Hưng"**, gọi khán giả **"anh chị"**.
- Mỗi bài ≥ 1 ví dụ cụ thể thật; **KHÔNG bịa số**; **KHÔNG nhắc tên thầy** (Phạm Thành Long).
- **KHÔNG markdown** trong thân bài (`*`, `#`, `>`).
- Trình bày **thoáng**: khối ngắn, có dòng trống giữa các ý; bước/mục đánh số mỗi cái một dòng.
- **CTA thu lead**: trao giá trị trọn vẹn trước, cuối bài mời comment từ khoá **CLAUDE** để nhận
  [bản hướng dẫn](huong-dan-bo-nao-thu-hai.md). ⚠️ Chỉ hứa gửi thứ **đã có thật**.
- **Bàn giao phải SẠCH**: file bài chỉ chứa thân bài (copy dán là đăng). Ghi chú nội bộ để **frontmatter**.

## 3. Độ dài theo ĐÚNG phong cách page (đo từ bài đã đăng thật)

| Loại bài | Thân bài | Comment đầu |
|---|---|---|
| **Nền màu** (quote, kêu gọi) | ~80 ký tự | **~90 ký tự — MỘT câu mời tương tác, hết** |
| **Kèm ảnh / video** | 400–700 ký tự | **KHÔNG CÓ** (mọi thứ trong thân bài) |

Trước khi viết: soi bài page đã đăng bằng `python3 scripts/quan-ly-bai.py --xem <id>`, bắt chước số liệu thật.

## 4. Màu nền (KHÓA CỨNG)

Bài chữ nền màu **LUÔN nền ĐỎ chữ trắng** (`--nen do`, mặc định). Nền đen trông như bài lỗi.
Đừng đổi màu chỉ để "cho khác" — khác chỉ đáng khi ĐẸP HƠN. Thêm màu phải hỏi anh Hửu.

---

## 5. CÔNG THỨC 5 BÀI — 5 ĐỊNH DẠNG KHÁC NHAU

Nguyên tắc: **5 bài/ngày = 5 ĐỊNH DẠNG khác nhau**, không phải 5 chủ đề trùng khuôn.
Khung giờ VN: **07:00 · 11:00 · 14:00 · 18:00 · 20:30**.

| # | Định dạng | Script | Ghi chú |
|---|---|---|---|
| 1 | 🎬 Video + caption | `reel-video.py` | b-roll + tiêu đề đè + nhạc; nội dung ở caption 400-700 ký tự |
| 2 | ☑️ Video checklist | `checklist-video.py` | tiêu đề đỏ 2 dòng + tối đa 10 mục "đã… chưa?" |
| 3 | 💬 Câu quote | `background-post.py --nen do` | thân ~80 ký tự + comment MỘT câu |
| 4 | 🖼️ Bài kèm hình | `photo-post.py --nhom <nhóm>` | caption dài 400-700, ảnh xoay vòng theo nhóm |
| 5 | 📣 Kêu gọi comment | `background-post.py --nen do` | tiêu đề kết 👇 + comment MỘT câu mời kể chuyện |

**Cách rải nhóm ảnh** (photo-post `--nhom`): whiteboard · lop-hoc · quay-phim · chan-dung · san-khau
· 1-1 · ngoai-troi · an-uong. Mỗi bài một nhóm khác nhau để không lặp mặt.

### Ví dụ 5 bài đã chạy (chủ đề Claude Code)

1. **Video** — "3 mẹo dùng AI đỡ tốn lượt" (đổi việc mở cuộc mới · nói cụ thể · việc nhẹ dùng chế độ nhẹ)
2. **Checklist** — "5 điều cần check trước khi giao việc cho AI"
3. **Quote** — "AI không làm thay anh chị. Nó chỉ gánh giúp mấy việc lặp đi lặp lại."
4. **Bài+hình** — "Bộ não thứ hai — kho kiến thức AI tra được"
5. **Kêu gọi** — "Việc nào anh chị làm đi làm lại hoài mà vẫn phải làm bằng tay? 👇"

Bài viết đầy đủ: xem `production/claude-code/*.md`.

### Kho chủ đề Claude Code (đã kiểm chứng bằng tài liệu Anthropic)

- Tiết kiệm token: `/clear` khi đổi việc · nói cụ thể · `/model` chọn máy nhẹ · `/usage` tự xem
- File `CLAUDE.md` — dặn một lần khỏi lặp
- Kéo ảnh chụp màn hình vào cho AI xem
- `@tên-file` trỏ đúng file
- Shift+Tab bật chế độ kế hoạch, duyệt xong mới cho sửa
- Esc dừng khi thấy đi sai hướng
- Skill riêng — đóng gói quy trình thành lệnh tắt
- Memory — AI nhớ mình qua các phiên

---

## 6. Lệnh chạy

```bash
# Bài chữ nền đỏ + comment ngắn
python3 scripts/background-post.py --text "..." --comment "..." --nen do

# Bài kèm hình, ảnh xoay vòng theo nhóm
python3 scripts/photo-post.py --nhom quay-phim --text "..."

# Reel video (b-roll + tiêu đề + nhạc)
python3 scripts/reel-video.py --t1 "dòng trên" --t2 "dòng dưới" --caption "..."

# Video checklist
python3 scripts/checklist-video.py --t1 "..." --t2 "..." --muc "mục 1" --muc "mục 2" --caption "..."

# Quản lý bài: liệt kê / xem / xoá
python3 scripts/quan-ly-bai.py --liet-ke
python3 scripts/quan-ly-bai.py --xem <id>
python3 scripts/quan-ly-bai.py --xoa <id> [<id>...]
```

**Lên lịch**: thêm `--status scheduled --schedule "2026-07-21T00:00:00Z"` (00:00 UTC = 07:00 VN, +7h).
**Mặc định là nháp (draft)** — chỉ `scheduled`/`published` mới đăng thật.
**Đăng qua GHL KHÔNG giới hạn số bài** — con số 5/ngày là chọn theo nhịp, không phải trần kỹ thuật.

Đổi giờ VN → UTC: 07:00→00:00Z · 11:00→04:00Z · 14:00→07:00Z · 18:00→11:00Z · 20:30→13:30Z.

---

## 7. Chất liệu content Hưng Huỳnh (cho bài nghe THẬT)

Chân dung thật ở vault khác: `Anh Hưng Huỳnh/wiki/thuc-the/huynh-duy-hung.md`.
Bản chắt an toàn: `wiki/analyses/Chất liệu content Hưng Huỳnh.md`.

**⛔ Lọc cứng — chỉ để hiểu, KHÔNG lên bài:** PII, tên thầy Phạm Thành Long, chuyện riêng
(vợ chồng, tự ti, sức khoẻ, tài chính cá nhân).

**✅ Dùng được:** cung chuyện "bình thường → học tập → thay đổi → truyền cảm hứng"; giá trị
(kỷ luật, gia đình, sức khoẻ, tự do, cho đi); ví dụ thật (phở khô Hưng Huỳnh + quỹ "lo cho em",
làm cha, chạy bộ/gym, làm YouTube, mê Arsenal); câu "hành động ngay cả khi không có cảm hứng".

---

## 8. Video "Bộ não thứ hai" (đang làm dở)

- Bản v1 đã dựng: `production/video-bo-nao/BO-NAO-THU-HAI_v1_chua-quay-man-hinh.mp4` (85s).
  Có giọng AI + phụ đề vàng + thẻ chữ + b-roll + CTA. **Còn chừa ĐEN** chỗ quay màn hình.
- Có sẵn 18 clip anh Hưng ngồi laptop: `production/video-bo-nao/clip-may-tinh/` (đã lọc từ 101 clip)
  → có thể lấp mấy khoảng đen bằng clip thật thay vì chờ quay màn hình.
- **Bẫy kỹ thuật:** clip gốc quay 59.94fps, ráp phải xuất **60fps** kẻo giật.
- **Còn lấn cấn:** giọng AI đọc "Claude Code" nghe như "Cờ-lô-cô" — cần nghe lại, sửa EverAI thành
  phiên âm "Clốt Cốt" nếu đúng.
- Prompt b-roll AI + prompt nhân vật anh Hưng: `production/video-bo-nao/PROMPT-*.md`.

---

## 9. Việc còn treo

- [ ] **Bật Share công khai** cho trang hướng dẫn (quà CTA), không thì người comment nhận link trắng:
  https://claude.ai/code/artifact/670ac78f-a695-4691-88a9-5fa870fd0be0
- [ ] Nghe lại giọng AI 3 mốc "Cờ-lô-cô", sửa nếu cần
- [ ] Quyết: lấp khoảng đen video bằng clip anh Hưng ngồi laptop, hay chờ quay màn hình
- [ ] Gen b-roll AI qua Google Flow (723 credits) — prompt sẵn ở `PROMPT-DAN-VAO-FLOW.md`

## 10. 5 bài đang lên lịch 21/07 (kiểm bằng quan-ly-bai.py --liet-ke)

| Giờ VN | Định dạng | Nội dung |
|---|---|---|
| 07:00 | Video | 3 mẹo dùng AI đỡ tốn lượt |
| 11:00 | Checklist | 5 điều cần check trước khi giao việc cho AI |
| 14:00 | Quote (đỏ) | AI không làm thay anh chị... |
| 18:00 | Bài+hình | Bộ não thứ hai |
| 20:30 | Kêu gọi (đỏ) | Việc nào anh chị làm đi làm lại hoài... 👇 |
