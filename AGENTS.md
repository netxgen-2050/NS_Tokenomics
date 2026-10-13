# Instructions for AI assistants working in this repository

(Read by Claude Code via `CLAUDE.md`, and by other assistants via `AGENTS.md`. Humans: see `00 - README.md`.)

## What this repo is

Token and capital design for the **Lighthouse** (~1,000 ha, Macrolote 7, Mainqué, Río Negro, Argentina) of NetX Gen: the **RAIZ** utility token, the Commons Fund, the community token templates, and the investor capital stack (company SAFE / commons RAIZ / land fideicomiso). Start with `00 - README.md`, then read the file your task touches. Every doc opens with a 🌱 "In one breath" summary.

Team: Gus (design), Gabriel (COO, legal), Vagner (CFO, financial model), Franz (BioPueblo relationship, investor pipeline), Martín (masterplan), Juanpi (tokenisation platforms). Working language: **English** (Spanish quotes from Argentine sources are fine).

## Non-negotiable design rules (don't propose things that break them)

1. **The diode**: no token, fund, community or investor instrument may encumber, collateralise or sell the land. Rights flow up the layers; recourse and debt never flow down. (A bounded sale zone inside Lighthouse is under discussion since 2026-10-12, see doc 18; until the team amends this rule in writing, it stands.)
2. **Three pots, never mixed**: company (SAFE), commons (RAIZ / Guardian), land (fideicomiso units). Commons money is never NetX revenue.
3. **RAIZ is a utility.** Never write price forecasts, "appreciation", "yield", "return" or "investment" language about RAIZ. Returns live only in the SAFE and fideicomiso units.
4. **No lots, no priority, no reservations** of Mainqué parcels before municipal approval (Ordenanza 173/2026).
5. **No gating by beliefs or values** (Ley 23.592): gate by conduct and contribution only.
6. Residents' matters are **one person, one vote**; money never buys that voice.

## Writing conventions (mandatory)

- **Cite sources.** Every factual claim gets a footnote `[^x]`, and every document ends with a **"Sources & logic used"** section (documents, data and reasoning used). Mark claims **[C]** confirmed, **[S]** secondary, **[NC]** not confirmed, **[criterio]** our judgement, **[verify]** check with counsel.
- **Emoji legend**: ✅ doable · 🧨 legal challenge · 🏴‍☠️ legal hack (only if substance matches form) · ❓ open question · 🔒 private.
- Keep the 🌱 plain-language summary at the top of each doc. Readers include people new to crypto-economics.
- Numbers are **"what must be true"** models, not forecasts. If you change a number, change the model in `sim/` and regenerate the RESULTS file; don't hand-edit results.
- Use Obsidian `[[wikilinks]]` between docs; keep file names stable (other docs link to them).
- When you add a decision or open question, update `07 - Open Questions and Research Backlog.md`.

## Privacy

- `private/` is git-ignored (call transcripts, the financial model original, third-party decks). **Never add, quote at length or summarise personal content from it**, and never commit it. Cite it as e.g. *"Private call Gus–Gabriel, 2026-10-02"*.
- Paths starting with `../NS_platform/` point to a sibling folder on Gus's machine that is not in this repo. Cite them; don't assume you can read them.
- Don't paste personal data (IDs, bank details, contact lists) into docs.

## Git workflow

- Team repo: `https://github.com/netxgen-2050/NS_Tokenomics`; its `main` holds agreed content. Gus's working copy is `sepu85/NS_Tokenomics`, merged into the team repo by pull request.
- Never commit to `main` directly. Work on your person's branch, named after them (`gustavo`, `gabriel`, `vagner` exist; otherwise create e.g. `cambios_franz`), and open a pull request to `main` with a short summary and the sources you used. Merges follow team agreements.
- Commit messages: what changed and why, in one or two lines.

## Running the models

```
python3 sim/hatch_sim.py           # Founding Pass raise vs credits promised
python3 sim/value_model_sim.py     # RAIZ use-value and fideicomiso IRR scenarios
```
Standard library only.

## Legal caveat

Nothing here is legal, tax or investment advice. Legal statements come from the 2026-09-29 research (in NS_platform) or are marked [verify]; counsel decides.
