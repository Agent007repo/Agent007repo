"""Build one animated, theme-aware project card for any repository README.

Same design language as the profile README (it reuses build_assets.py).
Usage:
    python3 repo_card.py spec.json OUT_DIR
writes OUT_DIR/readme-card-dark.svg and OUT_DIR/readme-card-light.svg.

spec.json fields (all text must be true for the repo; no em dashes):
{
  "title": "Project name",                      # <= 26 characters (font shrinks to fit)
  "eyebrow": "AI PRODUCT ENGINEERING",          # <= 30 characters, caps
  "tagline": ["first line", "second line"],     # each <= 48 characters
  "stats": [["40", "label", "detail"], ...],    # exactly 4; number <= 6 chars, label/detail <= 26 chars
  "chain": {"title": "Pipeline", "note": "short note",          # note <= 40 characters
            "nodes": [["1", "Ingest", "feedback"], ...]},       # 3 to 5 nodes; big <= 3 chars, lines <= 12 chars
  "panel": {"title": "...", "subtitle": "...",                  # title <= 55 chars, subtitle <= 70 chars
            "rows": [["label", "sub", 0.86, "0.86"], ...]}      # 2 to 4 bars; value in 0..1 of bar length
     OR   {"title": "Honest scope", "lines": ["...", "..."]}    # 2 to 4 lines, each <= 70 characters
  "stack": "Python · pandas · scikit-learn"     # <= 70 characters
}
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_assets as B  # noqa: E402


def card(spec: dict, c: dict) -> str:
    w, h = 1200, 440
    palette = [c["violet"], c["blue"], c["teal"], c["amber"], c["green"]]
    accents = [c["blue"], c["teal"], c["violet"], c["amber"]]
    stats = [(s[0], s[1], s[2], accents[i % 4]) for i, s in enumerate(spec["stats"][:4])]

    ch = spec["chain"]
    nodes = ch["nodes"][:5]
    n = len(nodes)
    x0, x1, ny = 560, 1128, 112
    dx = (x1 - x0) / max(n - 1, 1)
    parts = [
        f'<line x1="{x0}" y1="{ny}" x2="{x1}" y2="{ny}" stroke="{c["line"]}" stroke-width="2"/>',
        f'<line class="draw" x1="{x0}" y1="{ny}" x2="{x1}" y2="{ny}" stroke="url(#chaingrad)" stroke-width="3" stroke-linecap="round" pathLength="1"/>',
        f'<circle class="pulse" cx="{x0}" cy="{ny}" r="7" fill="{c["text"]}"/>',
        f'<g class="rise" style="animation-delay:.3s"><text x="{x0 - 30}" y="{ny - 50}" class="head" fill="{c["text"]}">{escape(ch["title"])}</text>'
        f'<text x="{x1 + 30}" y="{ny - 50}" text-anchor="end" class="monos" fill="{c["muted"]}">{escape(ch.get("note", ""))}</text></g>',
    ]
    for i, (big, l1, l2) in enumerate(nodes):
        cx = x0 + i * dx
        col = palette[i % 5]
        parts.append(
            f'<g class="pop" style="animation-delay:{0.4 + i * 0.18:.2f}s">'
            f'<circle class="lit" style="animation-delay:{i * 0.6:.1f}s" cx="{cx:.1f}" cy="{ny}" r="31" fill="{col}" fill-opacity="0.16" stroke="{col}" stroke-width="2"/>'
            f'<circle cx="{cx:.1f}" cy="{ny}" r="25" fill="{c["panel"]}"/>'
            f'<text x="{cx:.1f}" y="{ny + 6}" text-anchor="middle" class="mono" style="font-size:16px;font-weight:800" fill="{col}">{escape(str(big))}</text>'
            f'<text x="{cx:.1f}" y="{ny + 56}" text-anchor="middle" class="small" fill="{c["text"]}">{escape(l1)}</text>'
            f'<text x="{cx:.1f}" y="{ny + 72}" text-anchor="middle" class="small" fill="{c["muted"]}">{escape(l2)}</text></g>'
        )

    p = spec["panel"]
    px, py, pw, ph = 530, 222, 640, 186
    parts.append(
        f'<g class="rise" style="animation-delay:.6s">'
        f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="18" fill="{c["panel"]}" fill-opacity="0.85" stroke="{c["line"]}"/>'
        f'<text x="{px + 22}" y="{py + 32}" class="head" fill="{c["text"]}">{escape(p["title"])}</text>'
    )
    if "rows" in p:
        parts.append(f'<text x="{px + 22}" y="{py + 50}" class="monos" fill="{c["muted"]}">{escape(p.get("subtitle", ""))}</text>')
        bx, bw = px + 190, 330
        for i, (label, sub, v, shown) in enumerate(p["rows"][:4]):
            v = max(0.0, min(1.0, float(v)))
            y = py + 74 + i * 24
            col = [c["teal"], c["violet"], c["blue"], c["amber"]][i % 4]
            parts.append(
                f'<text x="{px + 22}" y="{y + 12}" class="monos" fill="{c["text"]}">{escape(label)}</text>'
                f'<text x="{bx - 10}" y="{y + 12}" text-anchor="end" class="monos" fill="{c["muted"]}">{escape(sub)}</text>'
                f'<rect x="{bx}" y="{y}" width="{bw}" height="15" rx="7.5" fill="{c["line"]}" fill-opacity="0.5"/>'
                f'<rect class="grow" style="animation-delay:{0.9 + i * 0.12:.2f}s" x="{bx}" y="{y}" width="{bw * v:.1f}" height="15" rx="7.5" fill="{col}"/>'
                f'<text x="{bx + bw * v + 8:.1f}" y="{y + 12}" class="mono" fill="{c["text"]}">{escape(str(shown))}</text>'
            )
    else:
        for i, line in enumerate(p["lines"][:4]):
            y = py + 66 + i * 28
            parts.append(
                f'<g class="rise" style="animation-delay:{0.9 + i * 0.15:.2f}s">'
                f'<circle cx="{px + 30}" cy="{y - 5}" r="4" fill="{[c["teal"], c["violet"], c["amber"], c["rose"]][i % 4]}"/>'
                f'<text x="{px + 44}" y="{y}" class="small" style="font-size:14.5px" fill="{c["text"]}">{escape(line)}</text></g>'
            )
    parts.append("</g>")

    css = f"""
{B.BLOB_CSS}{B.RISE_CSS}{B.CARD_CSS}
.eyebrow {{ letter-spacing: 2px; }}
.draw {{ stroke-dasharray: 1; animation: draw 1.6s .4s cubic-bezier(.4,0,.2,1) both; }}
@keyframes draw {{ from {{ stroke-dashoffset: 1; }} }}
.pulse {{ opacity: 0; animation: pulse 3s 2s cubic-bezier(.5,0,.5,1) infinite; }}
@keyframes pulse {{ 0% {{ transform: translateX(0); opacity: 0; }} 10% {{ opacity: .9; }} 90% {{ opacity: .9; }} 100% {{ transform: translateX({x1 - x0}px); opacity: 0; }} }}
.lit {{ animation: lit 3s 2s ease-out infinite; transform-box: fill-box; transform-origin: center; }}
@keyframes lit {{ 0%, 100% {{ transform: scale(1); }} 8% {{ transform: scale(1.18); fill-opacity: .45; }} 30% {{ transform: scale(1); }} }}
{B.REDUCED}
"""
    left = B.card_left(c, "", spec["title"], spec["tagline"][0], spec["tagline"][1] if len(spec["tagline"]) > 1 else "",
                       stats, spec["stack"], c["teal"])
    left = left.replace("FEATURED RESEARCH · ", escape(spec["eyebrow"]))
    size = min(46, int(430 / (0.58 * max(len(spec["title"]), 1))))
    left = left.replace('class="title"', f'class="title" style="font-size:{size}px"')
    desc = f'{spec["title"]}: ' + "; ".join(f"{s[0]} {s[1]}" for s in spec["stats"][:4])
    return (
        B.svg_open(w, h, spec["title"], desc)
        + f"<style>{css}</style>"
        + B.background(w, h, c, "rc")
        + f'<defs><linearGradient id="chaingrad" x1="0" x2="1"><stop offset="0" stop-color="{c["violet"]}"/><stop offset=".5" stop-color="{c["teal"]}"/><stop offset="1" stop-color="{c["green"]}"/></linearGradient></defs>'
        + left
        + "".join(parts)
        + "</svg>\n"
    )


def main() -> None:
    spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    blob = json.dumps(spec, ensure_ascii=False)
    limits = {"title": 26, "eyebrow": 30, "stack": 70}
    for k, n in limits.items():
        if len(spec.get(k, "")) > n:
            print(f"warning: {k} longer than {n} characters, may overflow")
    for line in spec.get("tagline", []):
        if len(line) > 48:
            print("warning: tagline line longer than 48 characters:", line)
    if "—" in blob:
        sys.exit("spec contains an em dash; replace it")
    for name, c in B.THEMES.items():
        (out / f"readme-card-{name}.svg").write_text(card(spec, c), encoding="utf-8")
    print("wrote", out / "readme-card-dark.svg", out / "readme-card-light.svg")


if __name__ == "__main__":
    main()
