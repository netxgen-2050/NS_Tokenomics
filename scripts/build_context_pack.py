"""
Build a single-file context pack of this repo, for AI assistants that work best with one upload
(ChatGPT projects, Claude projects, Gemini). Standard library only.

Order: instructions for assistants and the README first, then the current design (docs 22–29 and
the simulation results), then everything else as background. Nothing from private/ is included.

Run from the repo root:  python3 scripts/build_context_pack.py
Output: context-pack/NS_Tokenomics - full context.md
"""
import glob
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "context-pack")
OUT = os.path.join(OUT_DIR, "NS_Tokenomics - full context.md")


def branch():
    try:
        return subprocess.check_output(["git", "-C", ROOT, "rev-parse", "--abbrev-ref", "HEAD"],
                                       text=True).strip()
    except Exception:
        return "unknown"


def commit():
    try:
        return subprocess.check_output(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"],
                                       text=True).strip()
    except Exception:
        return "unknown"


def main():
    docs = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "[0-9][0-9] - *.md")))
    current = [d for d in docs if "22" <= d[:2] <= "29"]
    background = [d for d in docs if d not in current and d != "00 - README.md"]
    order = (["AGENTS.md", "00 - README.md"] + current
             + ["sim/RESULTS_series_waterfall.md", "sim/RESULTS_series_montecarlo.md"]
             + background
             + ["prompt_legal.md", "prompt_gemini.md", "sim/RESULTS.md", "sim/RESULTS_value_model.md"])
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as out:
        out.write("# NS_Tokenomics — full context pack\n\n")
        out.write(f"Generated from `main` (built on top of commit `{commit()}`) by "
                  "`scripts/build_context_pack.py`. Each file below starts with a `=== FILE:` line.\n\n")
        out.write("**How to read this pack:** follow `AGENTS.md` (first file). The **current legal "
                  "design is design B** (docs 22–29). Docs 01–21 are earlier work: read them as inputs "
                  "and background, not as the current proposal. Nothing here is legal, tax or "
                  "investment advice.\n\n")
        for rel in order:
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                continue
            with open(path, encoding="utf-8") as f:
                out.write(f"\n\n=== FILE: {rel} ===\n\n")
                out.write(f.read())
    words = sum(len(open(os.path.join(ROOT, r), encoding="utf-8").read().split())
                for r in order if os.path.exists(os.path.join(ROOT, r)))
    print(f"Wrote {OUT} ({len(order)} files, ~{words:,} words)")


if __name__ == "__main__":
    main()
