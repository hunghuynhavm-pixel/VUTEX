"""Đăng bài Blog lên GHL."""
from datetime import datetime, timezone

from .client import GHLClient
from .config import Config


def create_blog_post(client: GHLClient, *, title, html, slug=None, description="",
                     image_url="", image_alt="", categories=None, tags=None,
                     author=None, status="PUBLISHED", published_at=None):
    """Tạo một bài blog. Trả về response JSON của GHL."""
    body = {
        "title": title,
        "locationId": Config.LOCATION_ID,
        "blogId": Config.BLOG_ID,
        "rawHTML": html,
        "status": status,
        "author": author or Config.AUTHOR_ID,
        "categories": categories or [],
        "tags": tags or [],
        "description": description,
        "imageUrl": image_url,
        "imageAltText": image_alt or title,
        "urlSlug": slug or _slugify(title),
        "publishedAt": published_at or datetime.now(timezone.utc).isoformat(),
    }
    return client.post("/blogs/posts", json=body)


def list_blogs(client: GHLClient):
    return client.get("/blogs/site/all", params={"locationId": Config.LOCATION_ID,
                                                  "skip": 0, "limit": 50})


def list_authors(client: GHLClient):
    return client.get("/blogs/authors", params={"locationId": Config.LOCATION_ID,
                                                 "skip": 0, "limit": 50})


def list_categories(client: GHLClient):
    return client.get("/blogs/categories", params={"locationId": Config.LOCATION_ID,
                                                    "skip": 0, "limit": 50})


def _slugify(text):
    import re
    import unicodedata
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)
