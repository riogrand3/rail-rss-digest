from __future__ import annotations

import argparse
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

import feedparser

# Allow importing config/feeds.py from the project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from config.feeds import RSS_FEEDS  # noqa: E402


USER_AGENT = "rail-rss-project-feed-tester/1.0"


def fetch_url(url: str, timeout: int = 20) -> tuple[int | None, bytes | None, str | None]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = getattr(response, "status", None)
            data = response.read()
            return status, data, None
    except urllib.error.HTTPError as exc:
        return exc.code, None, f"HTTP error: {exc}"
    except urllib.error.URLError as exc:
        return None, None, f"URL error: {exc}"
    except Exception as exc:
        return None, None, f"Unexpected error: {exc}"


def entry_datetime(entry) -> datetime | None:
    # Prefer parsed timestamps from feedparser
    for attr in ("published_parsed", "updated_parsed", "created_parsed"):
        parsed = entry.get(attr)
        if parsed:
            try:
                return datetime.fromtimestamp(time.mktime(parsed), tz=timezone.utc)
            except Exception:
                pass

    # Fallback to string timestamps
    for attr in ("published", "updated", "created"):
        value = entry.get(attr)
        if value:
            try:
                dt = parsedate_to_datetime(value)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return dt.astimezone(timezone.utc)
            except Exception:
                pass

    return None


def truncate(text: str, length: int = 90) -> str:
    text = " ".join((text or "").split())
    if len(text) <= length:
        return text
    return text[: length - 3] + "..."


def test_feed(name: str, url: str, recent_days: int, timeout: int) -> dict:
    status, data, fetch_error = fetch_url(url, timeout=timeout)

    result = {
        "name": name,
        "url": url,
        "status": status,
        "fetch_error": fetch_error,
        "bozo": None,
        "bozo_exception": None,
        "feed_title": None,
        "entry_count": 0,
        "recent_count": 0,
        "latest_date": None,
        "latest_title": None,
        "ok": False,
    }

    if data is None:
        return result

    parsed_feed = feedparser.parse(data)

    result["bozo"] = bool(parsed_feed.get("bozo"))
    if parsed_feed.get("bozo_exception"):
        result["bozo_exception"] = str(parsed_feed.get("bozo_exception"))

    result["feed_title"] = parsed_feed.feed.get("title", "")
    entries = parsed_feed.entries or []
    result["entry_count"] = len(entries)

    cutoff = datetime.now(timezone.utc) - timedelta(days=recent_days)

    latest_dt = None
    latest_title = None
    recent_count = 0

    for entry in entries:
        dt = entry_datetime(entry)

        if dt:
            if latest_dt is None or dt > latest_dt:
                latest_dt = dt
                latest_title = entry.get("title", "")

            if dt >= cutoff:
                recent_count += 1
        else:
            # If there is no parseable date, count it as unknown, not recent.
            pass

    result["recent_count"] = recent_count

    if latest_dt:
        result["latest_date"] = latest_dt.strftime("%Y-%m-%d")
    result["latest_title"] = latest_title

    # A feed is "ok" if it fetched successfully and has at least one entry.
    # Recent entries are reported separately because some feeds publish irregularly.
    result["ok"] = status is not None and 200 <= status < 400 and len(entries) > 0

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Test RSS/Atom feeds from config/feeds.py")
    parser.add_argument("--recent-days", type=int, default=14, help="Window for recent article count")
    parser.add_argument("--timeout", type=int, default=20, help="HTTP timeout per feed in seconds")
    parser.add_argument(
        "--fail-on-zero",
        action="store_true",
        help="Fail if any feed returns zero entries",
    )
    parser.add_argument(
        "--fail-on-no-recent",
        action="store_true",
        help="Fail if any feed has no entries within recent-days",
    )

    args = parser.parse_args()

    print("=" * 90)
    print("RSS / Atom feed test")
    print("=" * 90)
    print(f"Feeds configured: {len(RSS_FEEDS)}")
    print(f"Recent window: last {args.recent_days} days")
    print()

    results = []

    for name, url in RSS_FEEDS.items():
        print(f"Testing: {name}")
        print(f"URL:     {url}")

        result = test_feed(name, url, args.recent_days, args.timeout)
        results.append(result)

        if result["ok"]:
            print("Result:  OK")
        else:
            print("Result:  PROBLEM")

        print(f"HTTP:    {result['status']}")
        print(f"Entries: {result['entry_count']}")
        print(f"Recent:  {result['recent_count']}")

        if result["feed_title"]:
            print(f"Title:   {result['feed_title']}")

        if result["latest_date"]:
            print(f"Latest:  {result['latest_date']} — {truncate(result['latest_title'])}")
        else:
            print("Latest:  No parseable article date found")

        if result["fetch_error"]:
            print(f"Error:   {result['fetch_error']}")

        if result["bozo"]:
            print(f"Warning: Feedparser marked this feed as malformed: {result['bozo_exception']}")

        print("-" * 90)

    ok_feeds = [r for r in results if r["ok"]]
    zero_entry_feeds = [r for r in results if r["entry_count"] == 0]
    no_recent_feeds = [r for r in results if r["entry_count"] > 0 and r["recent_count"] == 0]
    broken_feeds = [r for r in results if not r["ok"]]

    print()
    print("=" * 90)
    print("SUMMARY")
    print("=" * 90)
    print(f"Total feeds:              {len(results)}")
    print(f"Feeds returning entries:  {len(ok_feeds)}")
    print(f"Broken / zero-entry:      {len(broken_feeds)}")
    print(f"No recent entries:        {len(no_recent_feeds)}")
    print()

    if broken_feeds:
        print("Broken or zero-entry feeds:")
        for r in broken_feeds:
            print(f"- {r['name']} | entries={r['entry_count']} | status={r['status']} | {r['url']}")

    if no_recent_feeds:
        print()
        print(f"Feeds with entries, but none in the last {args.recent_days} days:")
        for r in no_recent_feeds:
            print(f"- {r['name']} | latest={r['latest_date']} | entries={r['entry_count']} | {r['url']}")

    should_fail = False

    if args.fail_on_zero and zero_entry_feeds:
        should_fail = True

    if args.fail_on_no_recent and no_recent_feeds:
        should_fail = True

    if should_fail:
        print()
        print("Feed test failed based on selected failure rules.")
        return 1

    print()
    print("Feed test completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
