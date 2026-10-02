#!/usr/bin/env python3
"""Builds roomread/privacy/index.html from privacy.md (a copy of the app's
app/src/main/assets/privacy.md with the contact email filled in). Handles the
small Markdown subset the policy uses: #, ##, paragraphs, "- " lists, **bold**,
[text](url) links and bare email addresses. Run: python3 build.py"""
import html, re
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "roomreadthecaller@gmail.com"

def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+|mailto:[^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"(?<![\w/:\">])([\w.+-]+@[\w-]+\.[\w.-]+\w)", r'<a href="mailto:\1">\1</a>', s)
    return s

def convert(md: str):
    lines = md.splitlines(); out = []; title = ""; meta = ""; para = []; in_list = False
    def flush():
        nonlocal para
        if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
    for ln in lines:
        if ln.startswith("# "):
            flush(); title = ln[2:].strip(); continue
        if ln.startswith("## "):
            flush()
            if in_list: out.append("</ul>"); in_list = False
            out.append(f"<h2>{inline(ln[3:].strip())}</h2>"); continue
        if ln.startswith("- "):
            flush()
            if not in_list: out.append("<ul>"); in_list = True
            out.append(f"<li>{inline(ln[2:].strip())}</li>"); continue
        if not ln.strip():
            flush()
            if in_list: out.append("</ul>"); in_list = False
            continue
        if not meta and not out and not para and ln.startswith("Effective"):
            meta = ln.strip(); continue
        para.append(ln.strip())
    flush()
    if in_list: out.append("</ul>")
    return title, meta, "\n".join(out)

PAGE = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Privacy policy for Room Read, the dance caller for Android.">
<link rel="icon" href="/roomread/icon-512.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="band"><div class="wrap">
  <a href="/roomread/"><img src="/roomread/icon-cream.png" alt=""></a>
  <div><div class="name"><a href="/roomread/">Room Read</a></div><div class="sub">dance caller for Android</div></div>
</div></header>
<main class="wrap">
<h1>Privacy policy</h1>
<p class="meta">{meta}</p>
{body}
<footer>Room Read is a personal project by Pascoe Harvey. Contact: <a href="mailto:{email}">{email}</a></footer>
</main>
</body>
</html>
"""

md = (ROOT / "privacy.md").read_text(encoding="utf-8")
title, meta, body = convert(md)
dst = ROOT / "roomread" / "privacy" / "index.html"
dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_text(PAGE.format(title=html.escape(title), meta=inline(meta), body=body, email=EMAIL), encoding="utf-8")
print("wrote", dst.relative_to(ROOT))
