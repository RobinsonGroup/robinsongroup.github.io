import csv
import os
import sys
from collections import defaultdict
from datetime import datetime

"""
Generate the News page and the home-page teaser from data/news.tsv.

Columns: date (YYYY-MM-DD), title, text, image (optional), link (optional).
Images are paths relative to docs/, e.g. img/news/foo.jpg
"""

N_TEASER = 3   # number of items shown on the home page

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_dir = os.path.join(script_dir, "..")
tsv_path = os.path.join(repo_dir, "data", "news.tsv")
docs_dir = os.path.join(repo_dir, "docs")
news_md = os.path.join(docs_dir, "news.md")
snippet_dir = os.path.join(repo_dir, "snippets")
teaser_md = os.path.join(snippet_dir, "news_teaser.md")


def load_items():
    items = []
    with open(tsv_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for line_no, row in enumerate(reader, start=2):
            date = (row.get("date") or "").strip()
            title = (row.get("title") or "").strip()
            if not date or not title:
                print(f"[WARNING] line {line_no}: missing date or title, skipped", file=sys.stderr)
                continue
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print(f"[WARNING] line {line_no}: date '{date}' is not YYYY-MM-DD, skipped", file=sys.stderr)
                continue
            image = (row.get("image") or "").strip()
            if image and not os.path.exists(os.path.join(docs_dir, image)):
                print(f"[WARNING] line {line_no}: image '{image}' not found under docs/", file=sys.stderr)
            items.append({
                "date": date,
                "title": title,
                "text": (row.get("text") or "").strip(),
                "image": image,
                "link": (row.get("link") or "").strip(),
            })
    items.sort(key=lambda r: r["date"], reverse=True)
    return items


def write_news_page(items):
    by_year = defaultdict(list)
    for it in items:
        by_year[it["date"][:4]].append(it)
    with open(news_md, "w", encoding="utf-8") as fh:
        fh.write("# News\n\n")
        for year in sorted(by_year, reverse=True):
            fh.write(f"## {year}\n\n")
            for it in by_year[year]:
                fh.write(f"**{it['date']} – {it['title']}**\n\n")
                if it["image"]:
                    fh.write(f"![{it['title']}]({it['image']}){{ width=\"300\" align=right }}\n\n")
                if it["text"]:
                    fh.write(it["text"])
                if it["link"]:
                    fh.write(f" [More]({it['link']}){{:target=\"_blank\"}}")
                fh.write("\n\n")


def write_teaser(items):
    os.makedirs(snippet_dir, exist_ok=True)
    with open(teaser_md, "w", encoding="utf-8") as fh:
        for it in items[:N_TEASER]:
            fh.write(f"- **{it['date']}** – {it['title']}\n")
        fh.write("\n[All news](news.md)\n")


if __name__ == "__main__":
    items = load_items()
    write_news_page(items)
    write_teaser(items)
    print(f"Wrote {len(items)} news items to {news_md} and teaser to {teaser_md}")