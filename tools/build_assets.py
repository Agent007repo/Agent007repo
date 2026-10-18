"""Generate the animated SVG assets for the GitHub profile README.

Every number shown in the project cards is copied from the generated
results blocks of the two public repositories (Agent007repo/trusttrace and
Agent007repo/continuum-bench) as of 18 Oct 2026. Edit DATA below if those
results are regenerated.

Animations are pure CSS inside the SVG, so they play when GitHub renders the
file through an <img> tag, and they switch off under prefers-reduced-motion,
leaving every element in its final, readable state.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', monospace"

THEMES = {
    "dark": dict(
        bg="#0A0F1E", bg2="#0F1630", panel="#121A36", line="#26304F",
        text="#EEF1FA", muted="#98A2BD", faint="#5B6683",
        teal="#2DD4BF", violet="#A78BFA", amber="#FBBF24", blue="#60A5FA",
        rose="#F472B6", green="#34D399", red="#F87171",
        blob1="#4F46E5", blob2="#0EA5E9", blob3="#14B8A6", blob_op="0.38",
        grid_op="0.07",
    ),
    "light": dict(
        bg="#F8FAFF", bg2="#EEF2FB", panel="#FFFFFF", line="#DCE2F0",
        text="#0B1222", muted="#4F5A73", faint="#8A93A8",
        teal="#0D9488", violet="#7C3AED", amber="#B45309", blue="#2563EB",
        rose="#DB2777", green="#059669", red="#DC2626",
        blob1="#A5B4FC", blob2="#7DD3FC", blob3="#99F6E4", blob_op="0.55",
        grid_op="0.09",
    ),
}

REDUCED = """
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; }
}"""


def svg_open(w: int, h: int, title: str, desc: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">\n'
        f'<title id="t">{escape(title)}</title>\n<desc id="d">{escape(desc)}</desc>\n'
    )


def background(w: int, h: int, c: dict, uid: str) -> str:
    """Rounded panel with drifting aurora blobs and a faint grid."""
    return f"""
<defs>
  <clipPath id="clip-{uid}"><rect width="{w}" height="{h}" rx="28"/></clipPath>
  <filter id="blur-{uid}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
  <pattern id="grid-{uid}" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="{c['text']}" stroke-width="1" opacity="{c['grid_op']}"/>
  </pattern>
  <linearGradient id="fade-{uid}" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0.15"/>
  </linearGradient>
  <mask id="gridmask-{uid}"><rect width="{w}" height="{h}" fill="url(#fade-{uid})"/></mask>
</defs>
<g clip-path="url(#clip-{uid})">
  <rect width="{w}" height="{h}" fill="{c['bg']}"/>
  <g filter="url(#blur-{uid})" opacity="{c['blob_op']}">
    <circle class="b1" cx="{int(w*0.82)}" cy="{int(h*0.15)}" r="230" fill="{c['blob1']}"/>
    <circle class="b2" cx="{int(w*0.18)}" cy="{int(h*0.95)}" r="250" fill="{c['blob2']}"/>
    <circle class="b3" cx="{int(w*0.55)}" cy="{int(h*0.55)}" r="170" fill="{c['blob3']}"/>
  </g>
  <rect width="{w}" height="{h}" fill="url(#grid-{uid})" mask="url(#gridmask-{uid})"/>
</g>
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="28" fill="none" stroke="{c['line']}"/>
"""


BLOB_CSS = """
.b1 { animation: drift1 22s ease-in-out infinite alternate; }
.b2 { animation: drift2 26s ease-in-out infinite alternate; }
.b3 { animation: drift3 18s ease-in-out infinite alternate; }
@keyframes drift1 { to { transform: translate(-140px, 90px); } }
@keyframes drift2 { to { transform: translate(180px, -110px); } }
@keyframes drift3 { to { transform: translate(-90px, -60px) scale(1.25); } }
"""

RISE_CSS = """
.rise { animation: rise .9s cubic-bezier(.2,.7,.2,1) both; }
@keyframes rise { from { opacity: 0; transform: translateY(14px); } }
.pop { animation: pop .6s cubic-bezier(.2,.9,.3,1.3) both; transform-box: fill-box; transform-origin: center; }
@keyframes pop { from { opacity: 0; transform: scale(.6); } }
.grow { animation: grow 1.4s cubic-bezier(.2,.7,.2,1) both; transform-box: fill-box; transform-origin: left center; }
@keyframes grow { from { transform: scaleX(0); } }
"""


# --------------------------------------------------------------------------
# Hero
# --------------------------------------------------------------------------

PHRASES = [
    "Trustworthy LLM systems",
    "Measured energy, not guesses",
    "Pre-registered, reproducible",
    "AI product engineering",
]
TYPE, HOLD, ERASE, GAP = 0.075, 2.4, 0.03, 0.45
FS, CW = 26, 15.6  # mono font size and fixed advance per character
SUB_X, SUB_Y = 96, 222


def typing_block(c: dict) -> tuple[str, str]:
    """Per-character typing and backspacing, driven by CSS keyframes."""
    t = 0.0
    events: list[tuple[float, int]] = []  # (time, visible chars) for the cursor
    spans: list[tuple[int, int, float, float]] = []
    for k, phrase in enumerate(PHRASES):
        n = len(phrase)
        start = t
        for i in range(n):
            events.append((start + i * TYPE, i + 1))
        typed_end = start + n * TYPE
        erase_start = typed_end + HOLD
        for i in range(n):
            spans.append((k, i, start + i * TYPE, erase_start + (n - 1 - i) * ERASE + ERASE))
        for j in range(n):
            events.append((erase_start + j * ERASE + ERASE, n - 1 - j))
        t = erase_start + n * ERASE + GAP
    total = t

    def pct(x: float) -> str:
        return f"{100 * x / total:.3f}%"

    css, tsp = [], []
    for k, phrase in enumerate(PHRASES):
        chars = []
        for i, ch in enumerate(phrase):
            _, _, a, b = next(s for s in spans if s[0] == k and s[1] == i)
            name = f"c{k}_{i}"
            css.append(
                f"@keyframes {name}{{0%,{pct(a)}{{opacity:0}}{pct(a + 0.001)},{pct(b)}{{opacity:1}}"
                f"{pct(b + 0.001)},100%{{opacity:0}}}}"
            )
            base = 1 if k == 0 else 0
            chars.append(
                f'<tspan x="{SUB_X + i * CW:.1f}" style="opacity:{base};animation:{name} {total:.2f}s linear infinite">'
                f"{escape(ch) if ch != ' ' else '&#160;'}</tspan>"
            )
        tsp.append(f'<text y="{SUB_Y}" class="sub">{"".join(chars)}</text>')

    stops = [f"0%{{transform:translateX(0px)}}"]
    for time, count in sorted(events):
        stops.append(f"{pct(time)}{{transform:translateX({count * CW:.1f}px)}}")
    css.append("@keyframes cur{" + "".join(stops) + "}")
    css.append(
        f".cur {{ animation: cur {total:.2f}s steps(1,end) infinite; "
        f"transform: translateX({len(PHRASES[0]) * CW:.1f}px); }}"
    )
    css.append(".blink { animation: blink 1s steps(1,end) infinite; } @keyframes blink { 50% { opacity: 0; } }")
    body = (
        f'<text x="64" y="{SUB_Y}" class="sub" fill="{c["teal"]}">&gt;</text>'
        + "".join(tsp)
        + f'<g class="cur"><rect class="blink" x="{SUB_X + 2}" y="{SUB_Y - 22}" width="3" height="28" rx="1.5" fill="{c["teal"]}"/></g>'
    )
    return body, "\n".join(css)


def hero(c: dict) -> str:
    w, h = 1200, 440
    typing, typing_css = typing_block(c)
    chips = [
        ("2 public repos, v0.1.0", c["teal"]),
        ("Protocols frozen first", c["violet"]),
        ("Energy measured, not modelled", c["amber"]),
        ("Every number traced to code", c["blue"]),
    ]
    chip_svg, x = [], 64
    for i, (label, col) in enumerate(chips):
        cw = int(len(label) * 7.1 + 42)
        chip_svg.append(
            f'<g class="rise" style="animation-delay:{1.3 + i * 0.15:.2f}s">'
            f'<rect x="{x}" y="318" width="{cw}" height="34" rx="17" fill="{c["panel"]}" fill-opacity="0.75" stroke="{c["line"]}"/>'
            f'<circle cx="{x + 18}" cy="335" r="4" fill="{col}"><animate attributeName="opacity" values="1;.35;1" dur="2.4s" begin="{i * 0.6}s" repeatCount="indefinite"/></circle>'
            f'<text x="{x + 30}" y="340" class="chip">{escape(label)}</text></g>'
        )
        x += cw + 12

    # Orbit motif on the right: trace, measure, verify.
    ox, oy = 1010, 205
    orbit = [
        f'<g class="pop" style="animation-delay:.5s">',
        f'<circle cx="{ox}" cy="{oy}" r="150" fill="none" stroke="{c["line"]}" stroke-dasharray="2 7"/>',
        f'<circle cx="{ox}" cy="{oy}" r="104" fill="none" stroke="{c["line"]}"/>',
        f'<circle cx="{ox}" cy="{oy}" r="58" fill="none" stroke="{c["line"]}" stroke-dasharray="4 4"/>',
        f'<g class="spin1"><circle cx="{ox + 150}" cy="{oy}" r="5" fill="{c["violet"]}"/><circle cx="{ox - 150}" cy="{oy}" r="3" fill="{c["blue"]}"/></g>',
        f'<g class="spin2"><circle cx="{ox}" cy="{oy - 104}" r="6" fill="{c["teal"]}"/><circle cx="{ox}" cy="{oy + 104}" r="3.5" fill="{c["amber"]}"/></g>',
        f'<g class="spin3"><circle cx="{ox + 58}" cy="{oy}" r="4" fill="{c["rose"]}"/></g>',
        f'<circle class="core" cx="{ox}" cy="{oy}" r="22" fill="{c["teal"]}" fill-opacity="0.18" stroke="{c["teal"]}"/>',
        f'<circle cx="{ox}" cy="{oy}" r="7" fill="{c["teal"]}"/>',
        "</g>",
    ]
    for i, (label, ang_x, ang_y, col) in enumerate(
        [("trace", -128, -92, c["violet"]), ("measure", 118, -78, c["amber"]), ("verify", 118, 86, c["teal"])]
    ):
        orbit.append(
            f'<g class="rise" style="animation-delay:{0.9 + i * 0.2:.1f}s">'
            f'<rect x="{ox + ang_x - 38}" y="{oy + ang_y - 15}" width="76" height="26" rx="13" fill="{c["panel"]}" stroke="{col}" stroke-opacity="0.7"/>'
            f'<text x="{ox + ang_x}" y="{oy + ang_y + 3}" text-anchor="middle" class="tag" fill="{col}">{label}</text></g>'
        )

    css = f"""
{BLOB_CSS}{RISE_CSS}
.prompt {{ font: 500 15px {MONO}; fill: {c['muted']}; }}
.name {{ font: 800 66px {SANS}; letter-spacing: -1.5px; }}
.sub {{ font: 600 {FS}px {MONO}; fill: {c['text']}; }}
.lead {{ font: 450 18px {SANS}; fill: {c['muted']}; }}
.chip {{ font: 600 13.5px {SANS}; fill: {c['text']}; }}
.tag {{ font: 600 12.5px {MONO}; }}
.s1 {{ animation: hue1 9s ease-in-out infinite alternate; }}
.s2 {{ animation: hue2 9s ease-in-out infinite alternate; }}
@keyframes hue1 {{ 0% {{ stop-color: {c['teal']}; }} 50% {{ stop-color: {c['blue']}; }} 100% {{ stop-color: {c['violet']}; }} }}
@keyframes hue2 {{ 0% {{ stop-color: {c['violet']}; }} 50% {{ stop-color: {c['teal']}; }} 100% {{ stop-color: {c['amber']}; }} }}
.spin1, .spin2, .spin3 {{ transform-origin: {ox}px {oy}px; }}
.spin1 {{ animation: spin 28s linear infinite; }}
.spin2 {{ animation: spin 18s linear infinite reverse; }}
.spin3 {{ animation: spin 9s linear infinite; }}
@keyframes spin {{ to {{ transform: rotate(360deg); }} }}
.core {{ animation: core 3s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
@keyframes core {{ 50% {{ transform: scale(1.35); opacity: .5; }} }}
{typing_css}
{REDUCED}
"""
    return (
        svg_open(w, h, "Samarth Annigeri", "Animated profile banner: Samarth Annigeri. Trustworthy LLM systems, measured energy, pre-registered and reproducible studies, AI product engineering.")
        + f"<style>{css}</style>"
        + background(w, h, c, "hero")
        + f"""
<defs><linearGradient id="namegrad" x1="0" y1="0" x2="1" y2="0">
  <stop class="s1" offset="0" stop-color="{c['teal']}"/>
  <stop offset="0.55" stop-color="{c['text']}"/>
  <stop class="s2" offset="1" stop-color="{c['violet']}"/>
</linearGradient></defs>
<g class="rise" style="animation-delay:.1s"><text x="64" y="78" class="prompt"><tspan fill="{c['teal']}">~/agent007repo</tspan> $ whoami</text></g>
<g class="rise" style="animation-delay:.25s"><text x="62" y="152" class="name" fill="url(#namegrad)">Samarth Annigeri</text></g>
<g>{typing}</g>
<g class="rise" style="animation-delay:.9s">
  <text x="64" y="268" class="lead">I build LLM systems and the evidence around them: traced requirements,</text>
  <text x="64" y="294" class="lead">measured joules, blinded audits, and limits stated before anyone asks.</text>
</g>
{''.join(chip_svg)}
{''.join(orbit)}
</svg>
"""
    )


# --------------------------------------------------------------------------
# Shared card scaffolding
# --------------------------------------------------------------------------

CARD_CSS = """
.eyebrow { font: 700 12.5px MONO; letter-spacing: 2px; }
.title { font: 800 46px SANS; letter-spacing: -1px; }
.tagline { font: 450 17px SANS; }
.big { font: 800 34px SANS; letter-spacing: -0.5px; }
.small { font: 500 13px SANS; }
.mono { font: 600 13px MONO; }
.monos { font: 500 12px MONO; }
.head { font: 700 14px SANS; }
""".replace("MONO", MONO).replace("SANS", SANS)


def stat_grid(c: dict, stats: list[tuple[str, str, str, str]], x0: int, y0: int) -> str:
    out = []
    for i, (num, l1, l2, col) in enumerate(stats):
        x = x0 + (i % 2) * 222
        y = y0 + (i // 2) * 92
        out.append(
            f'<g class="rise" style="animation-delay:{0.5 + i * 0.12:.2f}s">'
            f'<rect x="{x}" y="{y}" width="206" height="80" rx="16" fill="{c["panel"]}" fill-opacity="0.8" stroke="{c["line"]}"/>'
            f'<rect x="{x}" y="{y + 18}" width="3" height="44" rx="1.5" fill="{col}"/>'
            f'<text x="{x + 18}" y="{y + 38}" class="big" fill="{col}">{escape(num)}</text>'
            f'<text x="{x + 18}" y="{y + 56}" class="small" fill="{c["text"]}">{escape(l1)}</text>'
            f'<text x="{x + 18}" y="{y + 71}" class="small" fill="{c["muted"]}">{escape(l2)}</text></g>'
        )
    return "".join(out)


def card_left(c: dict, n: str, title: str, tag1: str, tag2: str, stats, stack: str, accent: str) -> str:
    return f"""
<g class="rise"><text x="56" y="62" class="eyebrow" fill="{accent}">FEATURED RESEARCH · {n}</text></g>
<g class="rise" style="animation-delay:.1s"><text x="54" y="114" class="title" fill="{c['text']}">{escape(title)}</text></g>
<g class="rise" style="animation-delay:.2s">
  <text x="56" y="146" class="tagline" fill="{c['muted']}">{escape(tag1)}</text>
  <text x="56" y="168" class="tagline" fill="{c['muted']}">{escape(tag2)}</text>
</g>
{stat_grid(c, stats, 56, 196)}
<g class="rise" style="animation-delay:1.1s"><text x="56" y="404" class="monos" fill="{c['faint']}">{escape(stack)}</text></g>
"""


# --------------------------------------------------------------------------
# TrustTrace card
# --------------------------------------------------------------------------

def trusttrace(c: dict) -> str:
    w, h = 1200, 440
    nodes = [
        ("8", "Stakeholder", "roles", c["violet"]),
        ("40", "Require-", "ments", c["blue"]),
        ("15", "Decision", "records", c["teal"]),
        ("C4", "Compo-", "nents", c["amber"]),
        ("38", "Reach a", "passing test", c["green"]),
    ]
    x0, dx, ny = 560, 142, 112
    chain = [
        f'<line x1="{x0}" y1="{ny}" x2="{x0 + dx * 4}" y2="{ny}" stroke="{c["line"]}" stroke-width="2"/>',
        f'<line class="draw" x1="{x0}" y1="{ny}" x2="{x0 + dx * 4}" y2="{ny}" stroke="url(#chaingrad)" stroke-width="3" stroke-linecap="round" pathLength="1"/>',
        f'<circle class="pulse" cx="{x0}" cy="{ny}" r="7" fill="{c["text"]}"/>',
    ]
    for i, (big, l1, l2, col) in enumerate(nodes):
        cx = x0 + i * dx
        chain.append(
            f'<g class="pop" style="animation-delay:{0.4 + i * 0.18:.2f}s">'
            f'<circle class="lit" style="animation-delay:{i * 0.6:.1f}s" cx="{cx}" cy="{ny}" r="31" fill="{col}" fill-opacity="0.16" stroke="{col}" stroke-width="2"/>'
            f'<circle cx="{cx}" cy="{ny}" r="25" fill="{c["panel"]}"/>'
            f'<text x="{cx}" y="{ny + 6}" text-anchor="middle" class="mono" style="font-size:16px;font-weight:800" fill="{col}">{big}</text>'
            f'<text x="{cx}" y="{ny + 56}" text-anchor="middle" class="small" fill="{c["text"]}">{l1}</text>'
            f'<text x="{cx}" y="{ny + 72}" text-anchor="middle" class="small" fill="{c["muted"]}">{l2}</text></g>'
        )
    chain.append(
        f'<g class="rise" style="animation-delay:.3s"><text x="{x0 - 30}" y="{ny - 50}" class="head" fill="{c["text"]}">Trace chain</text>'
        f'<text x="{x0 + dx * 4 + 30}" y="{ny - 50}" text-anchor="end" class="monos" fill="{c["muted"]}">a verifier fails on any dangling link</text></g>'
    )

    # F1 panel
    px, py, pw, ph = 530, 222, 640, 186
    rows = [
        ("Mistral-7B", "naive", 0.86, c["faint"]),
        ("Mistral-7B", "guided", 0.91, c["teal"]),
        ("Qwen2.5-1.5B", "naive", 0.73, c["faint"]),
        ("Qwen2.5-1.5B", "guided", 0.72, c["violet"]),
    ]
    bx, bw = px + 190, 300
    f1 = [
        f'<g class="rise" style="animation-delay:.6s">'
        f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="18" fill="{c["panel"]}" fill-opacity="0.85" stroke="{c["line"]}"/>'
        f'<text x="{px + 22}" y="{py + 32}" class="head" fill="{c["text"]}">B10 pilot · macro F1 against hand-written gold labels</text>'
        f'<text x="{px + 22}" y="{py + 50}" class="monos" fill="{c["muted"]}">10 texts × 2 models × 2 prompts × 3 seeds = 120 generations</text>'
    ]
    for i, (model, arm, v, col) in enumerate(rows):
        y = py + 74 + i * 24
        f1.append(
            f'<text x="{px + 22}" y="{y + 12}" class="monos" fill="{c["text"] if i % 2 == 0 else c["muted"]}">{model if i % 2 == 0 else ""}</text>'
            f'<text x="{bx - 10}" y="{y + 12}" text-anchor="end" class="monos" fill="{c["muted"]}">{arm}</text>'
            f'<rect x="{bx}" y="{y}" width="{bw}" height="15" rx="7.5" fill="{c["line"]}" fill-opacity="0.5"/>'
            f'<rect class="grow" style="animation-delay:{0.9 + i * 0.12:.2f}s" x="{bx}" y="{y}" width="{bw * v:.1f}" height="15" rx="7.5" fill="{col}"/>'
            f'<text x="{bx + bw * v + 8:.1f}" y="{y + 12}" class="mono" fill="{c["text"]}">{v:.2f}</text>'
        )
    kx = px + pw - 104
    f1.append(
        f'<g class="pop" style="animation-delay:1.6s">'
        f'<circle cx="{kx + 46}" cy="{py + 110}" r="40" fill="none" stroke="{c["line"]}" stroke-width="7"/>'
        f'<circle class="ring" cx="{kx + 46}" cy="{py + 110}" r="40" fill="none" stroke="{c["teal"]}" stroke-width="7" stroke-linecap="round" pathLength="100" stroke-dasharray="73 100" transform="rotate(-90 {kx + 46} {py + 110})"/>'
        f'<text x="{kx + 46}" y="{py + 108}" text-anchor="middle" class="mono" style="font-size:19px;font-weight:800" fill="{c["text"]}">κ .73</text>'
        f'<text x="{kx + 46}" y="{py + 124}" text-anchor="middle" class="monos" style="font-size:10px" fill="{c["muted"]}">≥ .60 req.</text>'
        f'<text x="{kx + 46}" y="{py + 168}" text-anchor="middle" class="monos" style="font-size:11px" fill="{c["muted"]}">blinded audit</text></g>'
    )
    f1.append("</g>")

    css = f"""
{BLOB_CSS}{RISE_CSS}{CARD_CSS}
.draw {{ stroke-dasharray: 1; stroke-dashoffset: 0; animation: draw 1.6s .4s cubic-bezier(.4,0,.2,1) both; }}
@keyframes draw {{ from {{ stroke-dashoffset: 1; }} }}
.pulse {{ opacity: 0; animation: pulse 3s 2s cubic-bezier(.5,0,.5,1) infinite; }}
@keyframes pulse {{ 0% {{ transform: translateX(0); opacity: 0; }} 10% {{ opacity: .9; }} 90% {{ opacity: .9; }} 100% {{ transform: translateX({dx * 4}px); opacity: 0; }} }}
.lit {{ animation: lit 3s 2s ease-out infinite; transform-box: fill-box; transform-origin: center; }}
@keyframes lit {{ 0%, 100% {{ transform: scale(1); }} 8% {{ transform: scale(1.18); fill-opacity: .45; }} 30% {{ transform: scale(1); }} }}
.ring {{ animation: ring 1.6s 1.7s cubic-bezier(.2,.7,.2,1) both; }}
@keyframes ring {{ from {{ stroke-dasharray: 0 100; }} }}
{REDUCED}
"""
    stats = [
        ("40", "requirements", "38 traced to passing tests", c["blue"]),
        ("15", "decision records", "each with a reflection", c["teal"]),
        ("120", "pilot generations", "protocol frozen first", c["violet"]),
        ("41", "references", "each resolved by script", c["amber"]),
    ]
    return (
        svg_open(w, h, "TrustTrace", "TrustTrace project card: traces stakeholder concerns through 40 requirements and 15 decision records to passing tests; B10 extraction pilot with macro F1 0.86 to 0.91 for Mistral-7B and a blinded matcher audit at kappa 0.73.")
        + f"<style>{css}</style>"
        + background(w, h, c, "tt")
        + f"""<defs><linearGradient id="chaingrad" x1="0" x2="1"><stop offset="0" stop-color="{c['violet']}"/><stop offset=".5" stop-color="{c['teal']}"/><stop offset="1" stop-color="{c['green']}"/></linearGradient></defs>"""
        + card_left(c, "01", "TrustTrace", "Can a team show why a design choice answers", "a trust concern, and where the evidence stops?", stats, "Python 3.12 · Pydantic metamodel · FastAPI · llama.cpp · LaTeX", c["teal"])
        + "".join(chain)
        + "".join(f1)
        + "</svg>\n"
    )


# --------------------------------------------------------------------------
# ContinuumBench card
# --------------------------------------------------------------------------

ENERGY = [  # config, joules per request, accuracy (device tier, M1 Max GPU)
    ("mistral7b-q4", 19.1, 65.3),
    ("qwen7b-q4", 18.3, 74.7),
    ("qwen1.5b-q4", 3.8, 65.8),
    ("qwen1.5b-q8", 3.4, 64.4),
    ("qwen0.5b-q4", 1.1, 37.3),
    ("qwen0.5b-q8", 1.0, 41.3),
]


def continuum(c: dict) -> str:
    w, h = 1200, 440
    px, py, pw = 530, 40, 640
    bx, bw, jmax = px + 140, 300, 20.0
    chart = [
        f'<g class="rise" style="animation-delay:.3s">'
        f'<rect x="{px}" y="{py}" width="{pw}" height="226" rx="18" fill="{c["panel"]}" fill-opacity="0.85" stroke="{c["line"]}"/>'
        f'<text x="{px + 22}" y="{py + 32}" class="head" fill="{c["text"]}">Joules per request, measured on the M1 Max GPU</text>'
        f'<text x="{px + pw - 22}" y="{py + 32}" text-anchor="end" class="monos" fill="{c["muted"]}">accuracy, 450 items</text>'
    ]
    for i, (cfg, j, acc) in enumerate(ENERGY):
        y = py + 52 + i * 27
        col = c["amber"] if j > 10 else (c["teal"] if j > 2 else c["blue"])
        chart.append(
            f'<text x="{bx - 12}" y="{y + 13}" text-anchor="end" class="monos" fill="{c["text"]}">{cfg}</text>'
            f'<rect x="{bx}" y="{y}" width="{bw}" height="17" rx="5" fill="{c["line"]}" fill-opacity="0.45"/>'
            f'<rect class="grow" style="animation-delay:{0.7 + i * 0.12:.2f}s" x="{bx}" y="{y}" width="{bw * j / jmax:.1f}" height="17" rx="5" fill="{col}"/>'
            f'<text x="{bx + bw * j / jmax + 8:.1f}" y="{y + 13}" class="mono" fill="{c["text"]}">{j:.1f} J</text>'
            f'<rect x="{px + pw - 82}" y="{y}" width="60" height="18" rx="9" fill="{col}" fill-opacity="0.14"/>'
            f'<text x="{px + pw - 52}" y="{y + 13}" text-anchor="middle" class="monos" fill="{col}">{acc:.1f}%</text>'
        )
    chart.append("</g>")

    # Routing panel: estimate vs live measurement vs pre-registered bar
    ry = 282
    sx, sw, smax = px + 190, 300, 40.0
    thr = sx + sw * 25 / smax
    route = [
        f'<g class="rise" style="animation-delay:.6s">'
        f'<rect x="{px}" y="{ry}" width="{pw}" height="126" rx="18" fill="{c["panel"]}" fill-opacity="0.85" stroke="{c["line"]}"/>'
        f'<text x="{px + 22}" y="{ry + 30}" class="head" fill="{c["text"]}">Routing cascade vs always-7B: energy saved</text>',
        f'<text x="{sx - 12}" y="{ry + 60}" text-anchor="end" class="monos" fill="{c["muted"]}">offline estimate</text>'
        f'<rect x="{sx}" y="{ry + 48}" width="{sw}" height="16" rx="5" fill="{c["line"]}" fill-opacity="0.45"/>'
        f'<rect class="grow" style="animation-delay:1.2s" x="{sx}" y="{ry + 48}" width="{sw * 29 / smax:.1f}" height="16" rx="5" fill="{c["faint"]}"/>'
        f'<text x="{sx + sw * 29 / smax + 8:.1f}" y="{ry + 61}" class="mono" fill="{c["muted"]}">29%</text>',
        f'<text x="{sx - 12}" y="{ry + 90}" text-anchor="end" class="monos" fill="{c["text"]}">measured live</text>'
        f'<rect x="{sx}" y="{ry + 78}" width="{sw}" height="16" rx="5" fill="{c["line"]}" fill-opacity="0.45"/>'
        f'<rect class="grow" style="animation-delay:1.4s" x="{sx}" y="{ry + 78}" width="{sw * 23.8 / smax:.1f}" height="16" rx="5" fill="{c["teal"]}"/>'
        f'<text x="{sx + sw * 29 / smax + 8:.1f}" y="{ry + 91}" class="mono" fill="{c["text"]}">23.8%</text>',
        f'<line class="thr" x1="{thr:.1f}" y1="{ry + 40}" x2="{thr:.1f}" y2="{ry + 102}" stroke="{c["rose"]}" stroke-width="2" stroke-dasharray="4 4"/>'
        f'<text x="{thr:.1f}" y="{ry + 116}" text-anchor="middle" class="monos" style="font-size:11px" fill="{c["rose"]}">pre-set bar 25%</text>',
        f'<g class="pop" style="animation-delay:2s"><rect x="{px + pw - 128}" y="{ry + 58}" width="106" height="44" rx="12" fill="{c["rose"]}" fill-opacity="0.12" stroke="{c["rose"]}" stroke-opacity="0.6"/>'
        f'<text x="{px + pw - 75}" y="{ry + 77}" text-anchor="middle" class="mono" style="font-size:12px" fill="{c["rose"]}">H3 not</text>'
        f'<text x="{px + pw - 75}" y="{ry + 93}" text-anchor="middle" class="mono" style="font-size:12px" fill="{c["rose"]}">supported</text></g>',
        "</g>",
    ]
    css = f"""
{BLOB_CSS}{RISE_CSS}{CARD_CSS}
.thr {{ animation: dash 1.2s linear infinite; }}
@keyframes dash {{ to {{ stroke-dashoffset: -16; }} }}
{REDUCED}
"""
    stats = [
        ("4,050", "measured requests", "450 items × 9 configs", c["teal"]),
        ("8,338", "power samples", "powermetrics, every 200 ms", c["amber"]),
        ("19×", "energy spread", "1.0 to 19.1 J per request", c["blue"]),
        ("24%", "energy saved live", "below the 25% bar, reported", c["violet"]),
    ]
    return (
        svg_open(w, h, "ContinuumBench", "ContinuumBench project card: six quantised models on an Apple M1 Max, energy per request from 1.0 to 19.1 joules measured with powermetrics; a routing cascade estimated at 29% savings measured 23.8% live, below the pre-registered 25% bar.")
        + f"<style>{css}</style>"
        + background(w, h, c, "cb")
        + card_left(c, "02", "ContinuumBench", "What does running an LLM under your own control", "really cost in accuracy, latency and joules?", stats, "llama.cpp Metal · powermetrics · bootstrap CIs · MkDocs", c["amber"])
        + "".join(chart)
        + "".join(route)
        + "</svg>\n"
    )


# --------------------------------------------------------------------------
# Principles strip
# --------------------------------------------------------------------------

def principles(c: dict) -> str:
    w, h = 1200, 210
    steps = [
        ("01", "Freeze the protocol", "before any data exists", c["violet"]),
        ("02", "Measure, don't estimate", "and label what was assumed", c["amber"]),
        ("03", "Audit the instrument", "blinded checks on my own scorer", c["teal"]),
        ("04", "Publish the limits", "including the results that failed", c["rose"]),
    ]
    x0, dx, y = 150, 300, 84
    parts = [
        f'<line x1="{x0}" y1="{y}" x2="{x0 + dx * 3}" y2="{y}" stroke="{c["line"]}" stroke-width="2"/>',
        f'<line class="flow" x1="{x0}" y1="{y}" x2="{x0 + dx * 3}" y2="{y}" stroke="url(#pgrad)" stroke-width="2.5" stroke-dasharray="6 10"/>',
    ]
    for i, (n, t1, t2, col) in enumerate(steps):
        x = x0 + i * dx
        parts.append(
            f'<g class="pop" style="animation-delay:{0.2 + i * 0.25:.2f}s">'
            f'<circle class="halo" style="animation-delay:{i * 0.75:.2f}s" cx="{x}" cy="{y}" r="30" fill="{col}" fill-opacity="0.15"/>'
            f'<circle cx="{x}" cy="{y}" r="22" fill="{c["panel"]}" stroke="{col}" stroke-width="2"/>'
            f'<text x="{x}" y="{y + 5}" text-anchor="middle" class="mono" fill="{col}">{n}</text></g>'
            f'<g class="rise" style="animation-delay:{0.4 + i * 0.25:.2f}s">'
            f'<text x="{x}" y="{y + 64}" text-anchor="middle" class="head" style="font-size:16px" fill="{c["text"]}">{escape(t1)}</text>'
            f'<text x="{x}" y="{y + 86}" text-anchor="middle" class="small" fill="{c["muted"]}">{escape(t2)}</text></g>'
        )
    css = f"""
{BLOB_CSS}{RISE_CSS}{CARD_CSS}
.flow {{ animation: flow 1.6s linear infinite; }}
@keyframes flow {{ to {{ stroke-dashoffset: -32; }} }}
.halo {{ animation: halo 3s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
@keyframes halo {{ 0%, 100% {{ transform: scale(1); opacity: 1; }} 20% {{ transform: scale(1.4); opacity: .3; }} 40% {{ transform: scale(1); opacity: 1; }} }}
{REDUCED}
"""
    return (
        svg_open(w, h, "How I work", "Four working rules: freeze the protocol before data, measure rather than estimate, audit the instrument with blinded checks, publish the limits including failed results.")
        + f"<style>{css}</style>"
        + background(w, h, c, "pr")
        + f"""<defs><linearGradient id="pgrad" x1="0" x2="1"><stop offset="0" stop-color="{c['violet']}"/><stop offset=".33" stop-color="{c['amber']}"/><stop offset=".66" stop-color="{c['teal']}"/><stop offset="1" stop-color="{c['rose']}"/></linearGradient></defs>"""
        + "".join(parts)
        + "</svg>\n"
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, c in THEMES.items():
        for stem, fn in [("hero", hero), ("trusttrace", trusttrace), ("continuumbench", continuum), ("principles", principles)]:
            (OUT / f"{stem}-{name}.svg").write_text(fn(c), encoding="utf-8")
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))


if __name__ == "__main__":
    main()
