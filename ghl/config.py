"""Đọc cấu hình từ biến môi trường (hoặc file .env khi chạy tay)."""
import os


def _load_dotenv():
    """Nạp file .env nếu có (chỉ dùng khi chạy tay ở máy local)."""
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


_load_dotenv()


class Config:
    TOKEN = os.environ.get("GHL_TOKEN", "")
    LOCATION_ID = os.environ.get("GHL_LOCATION_ID", "")
    BLOG_ID = os.environ.get("GHL_BLOG_ID", "")
    AUTHOR_ID = os.environ.get("GHL_AUTHOR_ID", "")
    API_VERSION = os.environ.get("GHL_API_VERSION", "2021-07-28")
    BASE_URL = "https://services.leadconnectorhq.com"

    @classmethod
    def require(cls, *fields):
        missing = [f for f in fields if not getattr(cls, f)]
        if missing:
            raise SystemExit(
                "❌ Thiếu cấu hình: "
                + ", ".join("GHL_" + f for f in missing)
                + "\n   -> Thêm vào GitHub Secrets (hoặc file .env khi chạy tay)."
            )
