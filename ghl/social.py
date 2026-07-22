"""Đăng bài lên Social Planner của GHL (Facebook, Instagram, TikTok...)."""
from .client import GHLClient
from .config import Config


def create_social_post(client: GHLClient, *, summary, account_ids,
                       media=None, schedule_date=None, status=None):
    """Tạo bài social planner.

    account_ids: list ID tài khoản mạng xã hội đã kết nối trong GHL.
    media: list URL ảnh/video (hoặc list dict {"url":..,"type":..}).
    schedule_date: ISO string -> hẹn giờ đăng. Bỏ trống -> đăng ngay.
    """
    path = f"/social-media-posting/{Config.LOCATION_ID}/posts"
    body = {
        "accountIds": account_ids,
        "summary": summary,
        "type": "post",
    }
    if media:
        body["media"] = [
            m if isinstance(m, dict) else {"url": m} for m in media
        ]
    if schedule_date:
        body["scheduleDate"] = schedule_date
        body["status"] = status or "scheduled"
    else:
        body["status"] = status or "published"
    return client.post(path, json=body)


def list_accounts(client: GHLClient):
    """Liệt kê các tài khoản mạng xã hội đã kết nối trong location."""
    path = f"/social-media-posting/{Config.LOCATION_ID}/accounts"
    return client.get(path)
