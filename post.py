#!/usr/bin/env python3
"""VUTEX — Đăng bài tự động lên GoHighLevel (Blog + Social Planner).

Cách dùng:
  python post.py            # đăng mọi bài MỚI/ĐÃ SỬA trong thư mục content/
  python post.py --list     # in ra danh sách blog / tác giả / danh mục / tài khoản MXH
  python post.py --dry-run  # thử chạy, KHÔNG gọi API thật (kiểm tra file)
"""
import argparse
import glob
import hashlib
import json
import os
import sys

import frontmatter
import markdown

from ghl.blog import (create_blog_post, list_authors, list_blogs,
                      list_categories)
from ghl.client import GHLClient
from ghl.config import Config
from ghl.social import create_social_post, list_accounts

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER_PATH = os.path.join(ROOT, ".ghl_posted.json")


# ---------- Sổ ghi nhận bài đã đăng (tránh đăng trùng) ----------
def load_ledger():
    if os.path.exists(LEDGER_PATH):
        with open(LEDGER_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_ledger(ledger):
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, ensure_ascii=False, indent=2)


def file_hash(path, content):
    h = hashlib.sha256()
    h.update(content.encode("utf-8"))
    return h.hexdigest()[:16]


# ---------- Đăng 1 file ----------
def post_blog_file(client, post, path, dry_run):
    meta = post.metadata
    html = markdown.markdown(post.content, extensions=["extra"])
    title = meta.get("title") or os.path.basename(path)
    print(f"  📝 BLOG: {title}")
    if dry_run:
        return {"dry_run": True}
    return create_blog_post(
        client,
        title=title,
        html=html,
        slug=meta.get("slug"),
        description=meta.get("description", ""),
        image_url=meta.get("image", ""),
        image_alt=meta.get("image_alt", ""),
        categories=meta.get("categories") or [],
        tags=meta.get("tags") or [],
        author=meta.get("author"),
        status=meta.get("status", "PUBLISHED"),
        published_at=meta.get("published_at"),
    )


def post_social_file(client, post, path, dry_run):
    meta = post.metadata
    accounts = meta.get("accounts") or []
    print(f"  📣 SOCIAL: {os.path.basename(path)} -> {len(accounts)} tài khoản")
    if dry_run:
        if not accounts:
            print("     ⚠️  (mẫu) chưa điền 'accounts' — nhớ điền trước khi đăng thật")
        return {"dry_run": True}
    if not accounts:
        raise ValueError("Thiếu 'accounts' trong frontmatter của bài social")
    return create_social_post(
        client,
        summary=post.content.strip(),
        account_ids=accounts,
        media=meta.get("media") or [],
        schedule_date=meta.get("schedule"),
    )


def run_post(dry_run=False):
    if not dry_run:
        Config.require("TOKEN", "LOCATION_ID")
    client = GHLClient()
    ledger = load_ledger()

    blog_files = sorted(glob.glob(os.path.join(ROOT, "content", "blog", "*.md")))
    social_files = sorted(glob.glob(os.path.join(ROOT, "content", "social", "*.md")))

    todo = [("blog", p) for p in blog_files] + [("social", p) for p in social_files]
    if not todo:
        print("Không tìm thấy bài nào trong content/blog hoặc content/social.")
        return

    posted, skipped, failed = 0, 0, 0
    for kind, path in todo:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        post = frontmatter.loads(raw)
        h = file_hash(path, raw)
        rel = os.path.relpath(path, ROOT)

        if ledger.get(rel, {}).get("hash") == h:
            skipped += 1
            continue

        try:
            if kind == "blog":
                resp = post_blog_file(client, post, path, dry_run)
            else:
                resp = post_social_file(client, post, path, dry_run)
            if not dry_run:
                ledger[rel] = {"hash": h, "response_id": _extract_id(resp)}
            posted += 1
            print("     ✅ Xong")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"     ❌ Lỗi: {e}", file=sys.stderr)

    if not dry_run:
        save_ledger(ledger)

    print(f"\nKết quả: đăng {posted} | bỏ qua (đã đăng) {skipped} | lỗi {failed}")
    if failed:
        sys.exit(1)


def _extract_id(resp):
    if not isinstance(resp, dict):
        return None
    for key in ("id", "_id"):
        if key in resp:
            return resp[key]
    for v in resp.values():
        if isinstance(v, dict):
            for key in ("id", "_id"):
                if key in v:
                    return v[key]
    return None


def run_list():
    Config.require("TOKEN", "LOCATION_ID")
    client = GHLClient()
    print("== BLOGS ==")
    _dump(list_blogs(client))
    print("\n== TÁC GIẢ (authors) ==")
    _dump(list_authors(client))
    print("\n== DANH MỤC (categories) ==")
    _dump(list_categories(client))
    print("\n== TÀI KHOẢN MẠNG XÃ HỘI ==")
    _dump(list_accounts(client))


def _dump(data):
    print(json.dumps(data, ensure_ascii=False, indent=2)[:4000])


def main():
    parser = argparse.ArgumentParser(description="Đăng bài GHL")
    parser.add_argument("--list", action="store_true",
                        help="Liệt kê blog/author/category/tài khoản MXH")
    parser.add_argument("--dry-run", action="store_true",
                        help="Thử chạy, không gọi API thật")
    args = parser.parse_args()

    if args.list:
        run_list()
    else:
        run_post(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
