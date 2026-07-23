# 🎬 KỊCH BẢN QUAY VIDEO — "Bộ Não Thứ 2" (Obsidian + Claude Code)

> Video hướng dẫn cài đặt & khởi tạo hệ thống wiki tri thức cá nhân.
> Dạng: **screen-recording (quay màn hình) + giọng thuyết minh (voice-over)**.

---

## 0. THÔNG TIN CHUNG (đọc trước khi quay)

| Mục | Nội dung |
|-----|----------|
| **Độ dài mục tiêu** | 12–16 phút |
| **Đối tượng** | Người không rành kỹ thuật, lần đầu nghe tới AI/Terminal |
| **Giọng điệu** | Gần gũi, chậm rãi, "cầm tay chỉ việc". Xưng **"mình" / gọi "bạn"** |
| **Định dạng quay** | Quay màn hình 1080p (hoặc 4K), thu tiếng qua micro rời |
| **Phần mềm gợi ý** | OBS / ScreenFlow / Camtasia để quay; CapCut/Premiere để dựng |
| **Con trỏ chuột** | Bật hiệu ứng highlight chuột + phóng to (zoom) khi bấm nút quan trọng |
| **Nhịp độ** | Mỗi thao tác quan trọng dừng 1–2 giây để người xem kịp làm theo |

### ✅ Chuẩn bị TRƯỚC khi bấm REC (rất quan trọng)
- [ ] Dọn màn hình desktop cho gọn, ẩn icon riêng tư.
- [ ] Phóng to cỡ chữ Terminal (dễ đọc trên điện thoại): Terminal → Settings → Font ~16–18pt.
- [ ] Chuẩn bị sẵn **1 máy CHƯA cài gì** (hoặc gỡ sẵn) để quay cảnh cài thật từ đầu — chân thực hơn.
- [ ] Mở sẵn các tab trình duyệt: `obsidian.md`, `nodejs.org`, `git-scm.com`.
- [ ] Copy sẵn câu lệnh setup dài (ở CẢNH 9) vào Notes để dán nhanh.
- [ ] Tắt thông báo (Do Not Disturb) để không lộ tin nhắn khi quay.
- [ ] Test âm thanh 10 giây trước khi quay chính thức.

---

## 1. BẢNG PHÂN CẢNH TỔNG QUAN

| # | Cảnh | Thời lượng | Kiểu hình |
|---|------|-----------|-----------|
| 1 | Hook mở đầu — 3 nỗi đau | 0:00–0:45 | Mặt người / slide |
| 2 | Bộ não thứ 2 là gì | 0:45–2:00 | Slide + sơ đồ |
| 3 | Hiểu `raw/` và `wiki/` | 2:00–3:30 | Slide 2 cột |
| 4 | Bước 1 — Cài Obsidian | 3:30–4:30 | Quay màn hình |
| 5 | Bước 2 — Cài Node.js | 4:30–5:30 | Quay màn hình |
| 6 | Bước 3 — Cài Claude Code | 5:30–7:00 | Quay Terminal |
| 7 | Bước 4 — Cài Git | 7:00–8:00 | Quay màn hình |
| 8 | Bước 5 + 6 — Tạo vault & mở Obsidian | 8:00–9:30 | Quay màn hình |
| 9 | Lần đầu mở Claude Code + dán lệnh setup | 9:30–13:00 | Quay Terminal (điểm nhấn) |
| 10 | Kết quả & quy trình mỗi ngày | 13:00–14:30 | Quay Obsidian + slide |
| 11 | Kêu gọi hành động (CTA) | 14:30–15:30 | Mặt người |

---

## 2. KỊCH BẢN CHI TIẾT TỪNG CẢNH

Mỗi cảnh gồm 3 phần:
- 🎥 **HÌNH** — quay/hiện gì trên màn hình
- 🎙️ **LỜI** — đọc nguyên văn (voice-over)
- 💬 **CHỮ HIỆN** — text overlay gợi ý

---

### 🎬 CẢNH 1 — HOOK MỞ ĐẦU (0:00–0:45)

🎥 **HÌNH:** Quay mặt bạn nói trực tiếp với camera (hoặc slide 3 icon 😵 📓 🤷 hiện lần lượt).

🎙️ **LỜI:**
> "Bạn có bao giờ học một khoá học, đọc một cuốn sách rất hay… nhưng chỉ hai tuần sau là quên sạch không?
> Hay ghi chú đầy vở, đầy điện thoại, mà không bao giờ mở lại?
> Biết lý thuyết đấy, nhưng tới lúc cần thì không biết áp dụng thế nào?
> Nếu bạn gật đầu với một trong ba điều đó — thì video này dành cho bạn.
> Hôm nay mình sẽ hướng dẫn bạn xây một thứ gọi là **BỘ NÃO THỨ HAI** — một kho tri thức cá nhân, tự động sắp xếp, và lúc nào cũng sẵn sàng trả lời bạn. Hoàn toàn **miễn phí**, chạy ngay trên máy bạn."

💬 **CHỮ HIỆN:** `BỘ NÃO THỨ 2` · `MIỄN PHÍ · CHẠY TRÊN MÁY BẠN`

> 📌 *Mẹo:* Nói 3 nỗi đau thật chậm, mỗi câu 1 nhịp gật đầu — để người xem "tự nhận ra mình".

---

### 🎬 CẢNH 2 — BỘ NÃO THỨ 2 LÀ GÌ (0:45–2:00)

🎥 **HÌNH:** Slide sơ đồ 3 khối:  📁 **Obsidian** → 🤖 **Claude Code** → ✨ **Wiki cá nhân** (mũi tên chạy lần lượt).

🎙️ **LỜI:**
> "Bộ não thứ hai không phải một app đơn lẻ. Nó là **ba thứ làm việc cùng nhau**.
> Thứ nhất — **Obsidian**: đây là nơi lưu ghi chú của bạn, nằm ngay trên máy, miễn phí.
> Thứ hai — **Claude Code**: đây là một AI. Nó sẽ tự đọc tài liệu bạn bỏ vào và sắp xếp lại thành kiến thức gọn gàng.
> Thứ ba — kết quả: một **wiki cá nhân**, giống như Wikipedia của riêng bạn, luôn cập nhật và tìm kiếm được.
> Nói đơn giản nhất: **bạn bỏ tài liệu vào — AI đọc và xử lý — bạn có ngay một kho tri thức gọn gàng.** Mỗi lần cần tìm lại, chỉ việc hỏi."

💬 **CHỮ HIỆN:** `Bỏ tài liệu vào → AI xử lý → Kho tri thức`

> 📌 *Mẹo:* Đến câu "giống Wikipedia của riêng bạn", chèn 1 ảnh minh hoạ wiki để người xem hình dung.

---

### 🎬 CẢNH 3 — HIỂU `raw/` VÀ `wiki/` (2:00–3:30)

🎥 **HÌNH:** Slide chia đôi. Trái: 📥 **raw/ — ĐẦU VÀO**. Phải: 📚 **wiki/ — KẾT QUẢ**.

🎙️ **LỜI:**
> "Trước khi cài, bạn chỉ cần hiểu đúng **hai thư mục** này thôi — hiểu hai cái này là hiểu 80% cách hệ thống hoạt động.
> Bên trái là **raw** — kho ĐẦU VÀO. Đây là chỗ bạn quăng tài liệu vào: ghi chú sau buổi học, bài viết hay, file PDF, ảnh chụp, ý tưởng chợt nảy ra, transcript video… **Không cần sắp xếp, không cần đặt tên đẹp.** Cứ bỏ vào là xong.
> Bên phải là **wiki** — kho KẾT QUẢ. Claude đọc thư mục raw xong sẽ **tự tạo** các file gọn gàng ở đây: trang tóm tắt khoá học, trang dự án, trang thông tin về người, về sức khoẻ, tài chính… **Bạn không phải tự viết gì cả.**
> Và đây là quy trình mỗi ngày, đơn giản tới mức này thôi: **bỏ tài liệu vào raw → bảo Claude 'nạp nguồn này cho mình' → Claude tự tạo wiki.** Hết."

💬 **CHỮ HIỆN:** `raw/ = bạn bỏ vào` · `wiki/ = Claude tự tạo` · `QUY TRÌNH: raw → "nạp nguồn" → wiki`

> 📌 *Mẹo:* Nhấn giọng vào chữ **"KHÔNG cần sắp xếp"** và **"KHÔNG phải tự viết"** — đây là điểm khiến người lười cũng dùng được.

---

### 🎬 CẢNH 4 — BƯỚC 1: CÀI OBSIDIAN (3:30–4:30)  ⏱ 3 phút thực tế

🎥 **HÌNH:** Quay màn hình thật. Mở trình duyệt → gõ `obsidian.md`.

🎙️ **LỜI + THAO TÁC (làm chậm, vừa làm vừa nói):**
> "Bắt đầu cài nhé. Sáu bước, mỗi bước chỉ là tải về và bấm Next như cài app bình thường.
> Bước một: **Obsidian**. Mình vào trang **obsidian.md**…" *(gõ địa chỉ, Enter)*
> "…bấm nút **Download** lớn ở giữa. Nó tự nhận máy mình là Mac hay Windows." *(bấm Download, zoom vào nút)*
> "Tải xong, mở file lên, bấm **Next** liên tục rồi **Finish**." *(mở file cài, tua nhanh phần Next-Next)*

🎥 **HÌNH (kết quả):** Mở app Obsidian → hiện màn hình "Create new vault / Open folder as vault".

🎙️ **LỜI:**
> "Cài xong, mở thử Obsidian, bạn sẽ thấy màn hình hỏi tạo vault hoặc mở folder. **Khoan** — mình đóng lại, chưa làm gì ở đây vội. Xong bước một."

💬 **CHỮ HIỆN:** `Bước 1/6 · obsidian.md · Download → Next → Finish`

> 📌 *Mẹo dựng phim:* Tua nhanh (×4) đoạn tải và bấm Next-Next để không làm người xem chán.

---

### 🎬 CẢNH 5 — BƯỚC 2: CÀI NODE.JS (4:30–5:30)  ⏱ 3 phút

🎥 **HÌNH:** Trình duyệt → `nodejs.org`. Zoom vào nút xanh có chữ **LTS**.

🎙️ **LỜI + THAO TÁC:**
> "Bước hai: **Node.js**. Bạn không cần biết nó là gì — cứ hiểu nó là cái nền để Claude Code chạy được. Cài một lần rồi quên đi.
> Vào **nodejs.org**, bấm nút xanh lớn có chữ **LTS**." *(zoom, bấm)*
> "Tải xong mở file, lại **Next** liên tục, **Install**, rồi **Finish**." *(tua nhanh)*

🎥 **HÌNH (kết quả):** Cửa sổ cài đóng lại, KHÔNG có icon mới.

🎙️ **LỜI:**
> "Cài xong sẽ **không** thấy icon app nào mới xuất hiện đâu — vì Node chạy ngầm. Hoàn toàn bình thường, đừng lo."

💬 **CHỮ HIỆN:** `Bước 2/6 · nodejs.org · chọn bản LTS` · `⚠️ Không có icon = bình thường`

> 📌 *Mẹo:* Câu "không có icon = bình thường" là câu người mới hay hoảng — nên nói rõ, để chữ to.

---

### 🎬 CẢNH 6 — BƯỚC 3: CÀI CLAUDE CODE (5:30–7:00)  ⏱ 5 phút  ⭐ điểm nhấn kỹ thuật

🎥 **HÌNH:** Quay cận cảnh việc mở Terminal.

🎙️ **LỜI (mở Terminal):**
> "Bước ba là cài chính chủ nhân vật của chúng ta — **Claude Code**. Đây là lần đầu ta dùng tới **Terminal**, nghe hơi 'ghê' nhưng thật ra rất dễ, mình chỉ gõ đúng một dòng thôi.
> **Trên máy Mac:** nhấn **Command + Space**, gõ chữ **Terminal**, Enter." *(quay đúng thao tác)*
> "**Trên Windows:** nhấn phím **Start**, gõ **cmd**, Enter."

🎥 **HÌNH:** Terminal mở ra. Dán lệnh và Enter.

🎙️ **LỜI:**
> "Bây giờ copy đúng dòng lệnh này, dán vào Terminal, nhấn Enter:"

🎥 **HÌNH (gõ/dán, quay rõ):**
```
npm install -g @anthropic-ai/claude-code
```
> Cho hiện dòng lệnh này TO trên màn hình vài giây để người xem chép/tạm dừng.

🎥 **HÌNH:** Chờ chạy, hiện dòng `added 47 packages in 8s`.

🎙️ **LỜI:**
> "Chờ vài giây… Khi thấy dòng **'added … packages'** hiện ra là cài xong.
> Để chắc ăn, gõ thêm: **claude gạch gạch version**." *(gõ `claude --version`)*
> "Thấy hiện ra một dãy số phiên bản như thế này là thành công rồi!"

🎥 **HÌNH:**
```
claude --version
1.x.x
```

💬 **CHỮ HIỆN:** `npm install -g @anthropic-ai/claude-code` · `Kiểm tra: claude --version`

🎙️ **LỜI (chốt, chuyển ý quan trọng):**
> "Và đây là điều tuyệt nhất: **từ giây phút này, bất kỳ bước nào phía sau mà bạn thấy khó — bạn cứ hỏi thẳng Claude, nó sẽ làm giúp bạn.** Bạn không còn phải làm một mình nữa."

> 📌 *Mẹo:* Đây là câu "bán được cả hệ thống". Nói chậm, nhìn thẳng camera nếu có chèn mặt người.
> 📌 *Lưu ý quay:* Nếu Terminal báo lỗi quyền (permission) trên Mac, người xem có thể cần thêm `sudo`. Nên quay sẵn phương án dự phòng, hoặc nhắc: "nếu báo lỗi quyền, thêm chữ `sudo` phía trước và nhập mật khẩu máy."

---

### 🎬 CẢNH 7 — BƯỚC 4: CÀI GIT (7:00–8:00)  ⏱ 3 phút

🎥 **HÌNH:** Trình duyệt → `git-scm.com` → nút **Download**.

🎙️ **LỜI:**
> "Bước bốn: **Git**. Cái này giúp Claude **tự lưu lại lịch sử mọi thay đổi** trong kho ghi chú của bạn. Nhờ vậy lỡ có gì sai, bạn quay về bản cũ được, không sợ mất bài. Không bắt buộc, nhưng rất nên có.
> Vào **git-scm.com**, bấm **Download**, chọn đúng hệ điều hành, mở file, **Next** liên tục, **Install**, **Finish**." *(tua nhanh)*

🎥 **HÌNH (kiểm tra):** Terminal gõ `git --version`.

🎙️ **LỜI:**
> "Kiểm tra: mở Terminal, gõ **git gạch gạch version**. Thấy dòng **git version 2 chấm gì đó** là xong.
> **Riêng máy Mac:** lần đầu gõ có thể hiện popup hỏi cài 'Command Line Tools' — cứ bấm **Install** là được, đó cũng là cách cài Git nhanh nhất trên Mac."

💬 **CHỮ HIỆN:** `Bước 4/6 · git-scm.com` · `Kiểm tra: git --version` · `Mac: bấm Install "Command Line Tools"`

---

### 🎬 CẢNH 8 — BƯỚC 5 & 6: TẠO VAULT & MỞ OBSIDIAN (8:00–9:30)

🎥 **HÌNH:** Quay Desktop → chuột phải → New Folder → đặt tên.

🎙️ **LỜI (Bước 5):**
> "Bước năm, siêu nhanh — **tạo thư mục vault**. Vault là thư mục gốc chứa toàn bộ bộ não của bạn.
> Ra ngoài **Desktop**, tạo một thư mục mới, đặt tên gì cũng được, ví dụ mình đặt **'Bộ não của Minh'**." *(gõ tên, Enter)*
> "Chỉ vậy thôi! **Không** cần tạo gì bên trong, **không** cần tải file nào cả. Để trống hoàn toàn. Lát nữa Claude sẽ tự dựng mọi thứ bên trong."

🎥 **HÌNH (Bước 6):** Mở Obsidian → "Open folder as vault" → chọn thư mục → Open.

🎙️ **LỜI:**
> "Bước sáu, bước cuối của phần cài: **kết nối Obsidian với thư mục vừa tạo**.
> Mở app **Obsidian**, chọn **'Open folder as vault'**, tìm tới thư mục 'Bộ não của Minh', bấm **Open**." *(thao tác chậm, zoom nút)*
> "Obsidian mở ra giao diện hai cột. Lúc này vault còn **trống trơn** — hoàn toàn bình thường, vì ta chưa chạy setup mà."

💬 **CHỮ HIỆN:** `Bước 5: tạo folder RỖNG trên Desktop` · `Bước 6: Obsidian → Open folder as vault`

🎥 **HÌNH chốt:** Slide 🎉 `CÀI ĐẶT HOÀN TẤT!`

🎙️ **LỜI:**
> "Xong! Sáu bước cài đặt hoàn tất. Giờ tới phần hay nhất: đánh thức bộ não thứ hai dậy."

---

### 🎬 CẢNH 9 — LẦN ĐẦU MỞ CLAUDE CODE + DÁN LỆNH SETUP (9:30–13:00)  ⭐⭐ điểm nhấn chính

🎥 **HÌNH:** Quay Finder/Explorer, chuột phải vào thư mục vault.

🎙️ **LỜI (mở Claude đúng thư mục):**
> "Điều quan trọng nhất ở đây: phải mở Claude Code **ngay bên trong thư mục vault**. Nghe phức tạp nhưng mẹo cực dễ:
> **Trên Mac:** chuột phải vào thư mục 'Bộ não của Minh', chọn **'New Terminal at Folder'**.
> **Trên Windows:** mở thư mục đó ra, chuột phải vào khoảng trống bên trong, chọn **'Open in Terminal'**.
> Cửa sổ Terminal hiện ra và **đã ở sẵn đúng thư mục** cho bạn rồi." *(quay rõ tên thư mục trên dòng Terminal)*

🎙️ **LỜI (nếu Mac thiếu tuỳ chọn):**
> "Máy Mac nếu chuột phải chưa thấy 'New Terminal at Folder', bật một lần thôi: vào **System Settings → Keyboard → Keyboard Shortcuts → Services → Files and Folders**, tích ô **'New Terminal at Folder'**. Từ đó về sau folder nào cũng có."

🎥 **HÌNH:** Gõ `claude` trong Terminal.

🎙️ **LỜI:**
> "Giờ chỉ cần gõ đúng một chữ: **claude** — rồi Enter." *(gõ, Enter)*
> "Cửa sổ chat của Claude Code hiện ra. Lần đầu nó có thể hỏi bạn đăng nhập tài khoản — cứ làm theo hướng dẫn trên màn hình là được."

🎥 **HÌNH:** Dán câu lệnh setup dài (đã copy sẵn) vào Claude Code → Enter.

🎙️ **LỜI (điểm nhấn cao trào):**
> "Và đây là câu 'thần chú' biến thư mục rỗng thành một bộ não thật sự. Mình đã để **nguyên văn câu lệnh này trong phần mô tả video / trong file đính kèm** — bạn chỉ cần copy **toàn bộ**, dán vào Claude Code, rồi Enter." *(dán, Enter)*
> "Xong. Giờ ngồi xem Claude làm việc thôi."

🎥 **HÌNH:** Claude Code chạy — tạo thư mục, viết file, cuối cùng in cây thư mục.

🎙️ **LỜI (thuyết minh trong lúc Claude chạy):**
> "Nhìn nè — Claude đang tự tạo các thư mục **wiki**, **raw**, **production**… đang tự viết file **CLAUDE.md** — đây là 'bộ quy tắc' để nó làm việc — rồi các file khởi tạo như index, log, tổng quan.
> Bạn **không gõ thêm bất cứ dòng lệnh nào**. Nó tự làm hết.
> Và khi xong, nó in ra cả cây thư mục để xác nhận." *(zoom vào cây thư mục kết quả)*

🎥 **HÌNH:** Quay sang Obsidian — các thư mục `raw`, `wiki`, `production` và file `CLAUDE.md` hiện ra ở cột trái.

🎙️ **LỜI:**
> "Quay lại Obsidian — thấy chưa? Cột trái vừa nãy trống trơn, giờ đã có đầy đủ **raw**, **wiki**, **production** và file **CLAUDE.md**. Bộ não thứ hai của bạn **chính thức sống rồi.**"

💬 **CHỮ HIỆN:** `Gõ: claude` · `Dán câu lệnh setup (xem mô tả) → Enter` · `Claude tự dựng toàn bộ hệ thống`

> 📌 *Mẹo quay:* Đoạn Claude chạy có thể lâu — **tua nhanh** phần giữa, giữ nguyên tốc độ ở đầu (lúc dán lệnh) và cuối (lúc in cây thư mục).
> 📌 *Cẩn trọng:* Trước khi quay, **chạy thử một lần** để chắc câu lệnh cho ra kết quả đẹp, rồi mới quay lần thật.

---

### 🎬 CẢNH 10 — KẾT QUẢ & QUY TRÌNH MỖI NGÀY (13:00–14:30)

🎥 **HÌNH:** Kéo một file PDF/ghi chú thả vào thư mục `raw/` trong Obsidian.

🎙️ **LỜI (demo dùng thật — rất nên có):**
> "Vậy dùng hằng ngày thế nào? Đơn giản đúng ba nhịp.
> Một — mình kéo một tài liệu bất kỳ, ví dụ file ghi chú buổi học này, **thả vào thư mục raw**." *(kéo thả)*
> "Hai — quay sang Claude Code, gõ: **'nạp nguồn này cho mình'** (hoặc 'ingest file này')." *(gõ)*
> "Ba — ngồi xem. Claude đọc tài liệu, tóm tắt, tạo trang wiki, liên kết chéo với những gì đã có, và ghi vào nhật ký." *(tua nhanh, rồi mở 1 trang wiki mới cho xem)*

🎙️ **LỜI:**
> "Từ nay mỗi lần cần tìm lại kiến thức, bạn **không phải lục lại đống tài liệu** nữa — chỉ cần hỏi Claude, nó đọc wiki và trả lời bạn kèm trích dẫn nguồn. Càng bỏ nhiều vào, bộ não càng thông minh và càng hiểu bạn."

💬 **CHỮ HIỆN:** `1. Thả vào raw/` · `2. "nạp nguồn này"` · `3. Claude tạo wiki`

---

### 🎬 CẢNH 11 — KÊU GỌI HÀNH ĐỘNG / CTA (14:30–15:30)

🎥 **HÌNH:** Mặt bạn nói với camera. Hạ chữ đăng ký / link.

🎙️ **LỜI:**
> "Vậy là chỉ với sáu bước cài đặt và một câu lệnh, bạn đã có một bộ não thứ hai — miễn phí, riêng tư, chạy ngay trên máy bạn, và lớn dần theo thời gian.
> Câu lệnh setup, đường link các phần mềm, và bản hướng dẫn chi tiết mình để hết **trong phần mô tả bên dưới**.
> Nếu video giúp ích cho bạn, cho mình một **like** và **đăng ký kênh** để đón những video tiếp theo — mình sẽ hướng dẫn cách 'dạy' bộ não này viết blog, lên kịch bản, tóm tắt sách cho bạn.
> Có gì chưa rõ, cứ để lại **bình luận** — mình đọc hết. Cảm ơn bạn đã xem, hẹn gặp lại!"

💬 **CHỮ HIỆN:** `👍 LIKE · 🔔 ĐĂNG KÝ` · `Link + câu lệnh ở mô tả 👇`

---

## 3. PHỤ LỤC A — CÂU LỆNH SETUP (dán vào phần mô tả video)

> Người xem sẽ copy nguyên khối này. Nhớ dán **đầy đủ, không cắt xén**.

```text
Bạn là người bảo trì (maintainer) một "Bộ não thứ hai - wiki tri thức bền vững" cho dự án này. Hãy THIẾT LẬP TOÀN BỘ hệ thống ngay bây giờ theo mô tả dưới đây: tạo cấu trúc thư mục, file schema CLAUDE.md, và các file khởi tạo. Làm thật (dùng công cụ tạo file/thư mục), không chỉ mô tả. Sau khi xong, liệt kê những gì đã tạo.

NGÔN NGỮ
Toàn bộ vault và schema viết bằng TIẾNG VIỆT. Nếu buộc phải dùng thuật ngữ nước ngoài, luôn kèm chú thích tiếng Việt trong ngoặc ngay lần đầu xuất hiện. Ví dụ: "embedding (vector nhúng)".

TRIẾT LÝ (để bạn hiểu, đưa vào phần đầu CLAUDE.md)
Thay vì mỗi lần hỏi lại đi truy xuất tài liệu thô từ đầu (kiểu RAG), hệ thống này DUY TRÌ MỘT WIKI liên kết chéo, tích lũy dần. Mỗi khi nạp nguồn mới, bạn ĐỌC nó, trích thông tin then chốt, rồi TÍCH HỢP vào wiki hiện có (cập nhật trang thực thể, chỉnh tóm tắt chủ đề, ghi chú mâu thuẫn với dữ liệu cũ). Kiến thức được biên dịch MỘT LẦN rồi giữ cập nhật, không suy lại mỗi lần hỏi. Wiki là tài sản bền vững, lớn dần theo thời gian.

BA TẦNG
raw/ — Nguồn thô, BẤT BIẾN. Chỉ đọc, KHÔNG BAO GIỜ sửa. Đây là nguồn chân lý.
wiki/ — Các file markdown do bạn (LLM) sinh ra và sở hữu hoàn toàn: trang tóm tắt, trang thực thể, trang khái niệm, bảng so sánh, tổng quan, tổng hợp. Bạn tạo, cập nhật, giữ liên kết chéo nhất quán.
CLAUDE.md — Schema: quy tắc tổ chức wiki, quy ước, và quy trình làm việc. Đây là file cấu hình then chốt.
production/ — Các file markdown do quá trình làm việc sinh ra sau này, khi người dùng ra lệnh, ví dụ như blog, bài đăng facebook, kịch bản video, file PDF, hoặc các tài liệu được tạo ra khác.

CÁC THƯ MỤC / FILE CẦN TẠO NGAY
Thư mục: wiki/, wiki/thuc-the/, wiki/khai-niem/, wiki/tom-tat-nguon/, wiki/so-sanh/, raw/assets/, production/
File: CLAUDE.md, wiki/index.md, wiki/log.md, wiki/tong-quan.md

NỘI DUNG CLAUDE.md CẦN CÓ (viết đầy đủ, cụ thể, dạng cẩm nang cho phiên sau)
- Triết lý + mô tả ba tầng (ở trên).
- Quy ước ngôn ngữ (ở trên).
- QUY ƯỚC TRANG WIKI:
  + Tên file: chữ thường, không dấu, nối bằng gạch ngang (ví dụ pham-thanh-long.md).
  + Mỗi trang mở đầu bằng frontmatter YAML: tieu_de, loai (thuc-the | khai-niem | tom-tat-nguon | so-sanh | tong-quan | tong-hop), ngay_tao, ngay_cap_nhat, nguon (danh sách file nguồn tham chiếu), tags.
  + Liên kết chéo giữa các trang bằng cú pháp [[ten-file-khong-duoi]].
  + Mọi khẳng định rút ra từ nguồn phải TRÍCH DẪN theo dạng (nguồn: tên-file, mốc thời gian nếu có).
- QUY TRÌNH "NẠP NGUỒN" (Ingest) — checklist đánh số:
  1. Đọc file nguồn trong raw/.
  2. Trao đổi với người dùng vài ý chính.
  3. Viết trang tóm tắt trong wiki/tom-tat-nguon/.
  4. Cập nhật wiki/index.md.
  5. Cập nhật / tạo các trang thực thể và khái niệm liên quan khắp wiki.
  6. Ghi chú nếu nguồn mới mâu thuẫn nguồn cũ.
  7. Thêm 1 dòng vào wiki/log.md.
  (Một nguồn có thể chạm 10–15 trang. Mặc định nạp TỪNG nguồn một, có giám sát; hỗ trợ nạp hàng loạt nếu người dùng yêu cầu.)
- QUY TRÌNH "TRUY VẤN" (Query) — đọc index.md trước để tìm trang liên quan → đọc các trang đó → tổng hợp câu trả lời CÓ TRÍCH DẪN. Nếu câu trả lời có giá trị (so sánh, phân tích, phát hiện mối liên hệ), đề nghị lưu ngược lại thành trang wiki mới để tích lũy.
- QUY TRÌNH "RÀ SOÁT" (Lint) — kiểm tra: mâu thuẫn giữa các trang; khẳng định lỗi thời; trang mồ côi (không có liên kết trỏ đến); khái niệm quan trọng chưa có trang riêng; thiếu liên kết chéo; khoảng trống dữ liệu. Đề xuất câu hỏi mới và nguồn cần tìm.
- Giải thích vai trò index.md và log.md.

NỘI DUNG wiki/index.md (khởi tạo)
Danh mục MỌI trang trong wiki, tổ chức theo hạng mục (Thực thể / Khái niệm / Tóm tắt nguồn / So sánh / Khác). Mỗi trang một dòng: - [[ten-file]] — tóm tắt một dòng. Cập nhật MỖI lần nạp nguồn. Ban đầu để khung rỗng với các tiêu đề hạng mục.

NỘI DUNG wiki/log.md (khởi tạo)
Nhật ký CHỈ-THÊM (append-only), theo thời gian. Mỗi mục bắt đầu bằng tiền tố nhất quán để grep được: ## [YYYY-MM-DD] ingest | Tên nguồn, hoặc ## [YYYY-MM-DD] query | ..., hoặc ## [YYYY-MM-DD] lint | ... Thêm ngay mục đầu tiên ghi lại việc "khởi tạo hệ thống hôm nay".

NỘI DUNG wiki/tong-quan.md (khởi tạo)
Trang tổng quan mô tả wiki này nói về gì, hiện có bao nhiêu nguồn trong raw/, và trỏ tới index.md. Cập nhật dần khi wiki lớn lên.

Bắt đầu tạo ngay. Khi xong, in cây thư mục và xác nhận từng file đã tạo.
```

---

## 4. PHỤ LỤC B — CÂU LỆNH & LINK CẦN NHỚ KHI QUAY

| Việc | Gõ / vào đâu |
|------|-------------|
| Tải Obsidian | `obsidian.md` → Download |
| Tải Node.js | `nodejs.org` → bản **LTS** |
| Tải Git | `git-scm.com` → Download |
| Cài Claude Code | `npm install -g @anthropic-ai/claude-code` |
| Kiểm tra Claude | `claude --version` |
| Kiểm tra Git | `git --version` |
| Mở Claude Code | `claude` (gõ trong thư mục vault) |
| Nạp tài liệu | thả file vào `raw/` → nói *"nạp nguồn này cho mình"* |

---

## 5. PHỤ LỤC C — GỢI Ý TIÊU ĐỀ & MÔ TẢ VIDEO

**Tiêu đề gợi ý (chọn 1):**
- "Xây BỘ NÃO THỨ 2 bằng AI — Miễn phí, chạy trên máy bạn (Obsidian + Claude Code)"
- "Không bao giờ quên kiến thức nữa: Hướng dẫn tạo Wiki cá nhân với AI từ A-Z"
- "Tôi để AI tự sắp xếp toàn bộ kiến thức của mình — đây là cách làm"

**Khung mô tả (description):**
```
⏱️ Trong video này bạn sẽ học cách xây "Bộ não thứ 2" — kho tri thức cá nhân tự động sắp xếp bằng AI, hoàn toàn miễn phí.

🔗 LINK CẦN TẢI:
• Obsidian: https://obsidian.md
• Node.js (bản LTS): https://nodejs.org
• Git: https://git-scm.com

⌨️ LỆNH CÀI CLAUDE CODE:
npm install -g @anthropic-ai/claude-code

📋 CÂU LỆNH SETUP (copy toàn bộ, dán vào Claude Code):
[dán khối lệnh ở Phụ lục A vào đây]

⏲️ MỐC THỜI GIAN:
00:00 Bạn có 3 nỗi đau này không?
00:45 Bộ não thứ 2 là gì
02:00 Hiểu raw/ và wiki/
03:30 Bước 1: Cài Obsidian
04:30 Bước 2: Cài Node.js
05:30 Bước 3: Cài Claude Code
07:00 Bước 4: Cài Git
08:00 Bước 5-6: Tạo vault & mở Obsidian
09:30 Khởi tạo hệ thống (dán lệnh setup)
13:00 Dùng hằng ngày thế nào
14:30 Lời kết

#BoNaoThu2 #Obsidian #ClaudeAI #NangSuat #SecondBrain
```

---

## 6. CHECKLIST HẬU KỲ (dựng phim)

- [ ] Chèn **thanh tiến độ "Bước X/6"** ở góc cho các cảnh cài đặt.
- [ ] **Zoom + highlight** mọi nút bấm và mọi dòng lệnh quan trọng.
- [ ] Tua nhanh (×4–×8) các đoạn tải/cài Next-Next và đoạn Claude chạy dài.
- [ ] Nhạc nền nhẹ, hạ âm lượng khi có lời thoại.
- [ ] Kiểm tra: mọi câu lệnh trên hình **khớp** với Phụ lục B.
- [ ] Che/blur mọi thông tin cá nhân lỡ lọt vào khung hình (email, tên máy…).
- [ ] Thêm phụ đề (caption) — nhiều người xem không bật tiếng.
```
