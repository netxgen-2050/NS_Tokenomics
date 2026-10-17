---
title: Gemini deep research review — what it confirms, what it adds, what it gets wrong
created: 2026-10-17
status: v0.1 — review by Claude for Gus; not legal advice. Every legal point here is [verify] until counsel reviews it
audience: Gus first, then the team (Franz, Gabriel, Vagner, Juanpi)
---

# Gemini deep research review (2026-10-17)

Back to [[00 - README]] · Input: `prompt_gemini.md` · Builds on [[20 - Land structure after Próspera and reply to Franz]], [[17 - Lighthouse Constitution and Rights of Nature (draft)]], [[06 - Legal Friction Map]]

---

## 🌱 In one breath

We ran Gemini Deep Research on our prompt and got two reports[^gem1][^gem2]. **The skeleton matches ours**: land in an Argentine trust that can't sell or mortgage it, the Guardian as final owner and holder of perpetual easements and a golden share, BioPueblo paid in holding equity, three pots, a capital ladder from SAFE to regulated tokenisation, one person one vote for residents. That is not independent confirmation: Gemini read our files and mostly gave them back in legal prose. **What is genuinely new**: (1) the Supreme Court did restore the rural land law on 2026-10-09 (we checked), so "foreign holding, Argentine land" moves from fallback to base case; (2) the timeshare risk for passes that promise fixed nights; (3) useful ideas for the term sheet (equity released by milestones), the fallbacks (sale zone *outside* the 1,000 ha; run the land as one unsubdivided rural unit) and provincial permits (DIA, DPA, riverbank line, private nature reserve). **What it gets wrong or invents**: 50% wild as a day-one minimum (ours is a 10%→50% ratchet); "revocable licences" with "immediate eviction" for families who build houses; a resale fee on passes it also calls non-transferable; MiCA "ART" and a "Swiss purpose trust"; wrong ordinance number and article; and it never asks the question that decides the whole structure: **is Macrolote 7 rural land in law at all?**

---

## 1. How to read a deep research report (functional, not legal)

Think of Gemini as a fast junior who read our three files plus some web pages. Every sentence falls into one of four boxes:

| Box | What it is | How much to trust it |
|---|---|---|
| **Echo** | Our own design, rewritten (cites `2_estructura…` or `3_constitucion…`) | Zero new evidence. Agreement here is the model repeating us |
| **Web fact** | A law, ruling or resolution with an external link | Check the link; good when it points to official text or several outlets |
| **Inference** | Gemini combining facts into a recommendation | Useful as a hypothesis; often confident beyond the evidence |
| **Invention** | Numbers or article numbers with no source, or a source that doesn't say it | Discard or verify |

Most of both reports is **echo** (footnotes 2 and 3 everywhere). The value is in the few web facts and inferences below.

## 2. Aligned with our work ✅

| Topic | Gemini says | Our doc |
|---|---|---|
| Land off the market | Argentine trust, no sale, no mortgage; Guardian is fideicomisario at year 30 | [[20 - Land structure after Próspera and reply to Franz]] §2 |
| Perpetual protection | Guardian owns a small dominant parcel; real easements (CCyC 2162–2165) over the 1,000 ha | [[17 - Lighthouse Constitution and Rights of Nature (draft)]] layer 1 |
| Purpose lock in the company | Golden share with no dividends, veto on land, Constitution, Commons Fund | 20 §2 |
| Three pots | Company (SAFE) · Commons (passes, Guardian) · Land (trust units) | Design rule 2 |
| Capital ladder 0–5 | Foundations → SAFE → Founding Pass → trust units → clusters → CNV tokenised trust | 20 §2b |
| Stewardship | Council of Regeneration, Voice of the Land, two chambers, clusters of ~16, Fibonacci, Ledger C | 20 §2b, 17 |
| Reply to Franz | Keep his easements, towpath, DIA and DPA points; correct lot sales, conversion credits, fixed nights, internal resale market, ticket-weighted votes | 20 §4 |
| Pessimistic cases | Same P1–P10, same mitigations | 20 §3 |

## 3. Genuinely new, and worth adopting 🆕

1. **The rural land law is back** [C, web]. On 2026-10-09 the Supreme Court suspended, as an interim measure, art. 154 of DNU 70/2023, so Ley 26.737 applies again while a Bariloche case is decided[^csjn]. Limits: 15% foreign ownership of rural land per country, province and department; 30% of that for one nationality; foreigners can't own land containing or bordering large permanent water bodies. **Consequence**: what doc 20 called P2 (a fallback) is now the base case. The land trust and the Guardian must be Argentine-controlled; foreign capital stays in the holding. Update: 06 L8, L30, L38 and 07 H-2.
2. **Timeshare** 🧨 [S, verify]. A pass that promises *N fixed nights a year for N years* may fall under the timeshare regime (CCyC 2087–2102, Ley 26.356), which needs a deed and a tourism registry first. Passes should give **consumable credits subject to availability**, never fixed nights. New: 06 L42.
3. **Equity released by milestones** (term sheet, P8) [criterio]. BioPueblo's shares vest in tranches tied to verifiable steps (trust deed; easements registered; DIA and water permit). The 30/30/40 split is Gemini's, not a proposal yet. It answers "how much is the land worth": part of the price is paid when the land is *protected and permitted*, not on day one.
4. **Sale zone outside the 1,000 ha** (P6) [criterio]. If BioPueblo needs liquidity from lot sales, the cleanest answer is a bounded zone **in BioPueblo's other ~9,000 ha**, with easements in every deed, not inside Lighthouse. This keeps the diode whole and is a cleaner option than the ones in [[18 - Hybrid model (selling some lots) - options and trade-offs]].
5. **Run the land as one unsubdivided rural unit** (P4) [criterio, verify]. If municipal approval is slow, the trust can keep the land as one parcel used for conservation and production, with passes and company capital paying for the first hectare. That keeps the land clock running without needing the subdivision approved.
6. **Provincial checklist** [S, verify]: DIA under Ley M 3266 before moving soil; DPA water permits under Ley Q 2952 and the riverbank line (15 m towpath, CCyC 1974); optional **private nature reserve** for the riverside under Ley M 2669 (extra public protection on top of our easements); a **binding tax ruling** from Río Negro's revenue agency on stamp tax for the land contribution.
7. **Precedents**: Edith Maryon Foundation (Switzerland: buys land to take it off the market forever, grants surface rights), Terre de Liens and Kulturland (citizen capital buying farmland with capped returns), CLTs (tripartite board). Good references for the Guardian and the land units. The Tamera/OASA row mostly cites *our* doc 17, so it is an echo.

## 4. Misaligned, wrong or invented ⚠️

| # | Gemini says | Problem | Our position |
|---|---|---|---|
| M1 | "At least 50% of the surface wild or agroecological" as a Constitution minimum; "max 5% built per parcel" | Takes OASA's numbers as ours. Doc 17 says they are a point of comparison only | Ecological ratchet: **start at 10%, grow by stages to 50%, never back** (Gus, 2026-10-15) |
| M2 | Families get a **revocable use licence**; "immediate eviction" after breaches | A family won't build a house on a licence that can be revoked; what gets built on someone else's land belongs to the landowner unless there is a surface right; and in Argentina eviction always goes through a court [verify]. It also reads as punishment-first | For homes: a **surface right (DRS)** over the house, land stays in the trust; graduated responses, help before sanction (17 art. 8). Short licences for hospitality and uses |
| M3 | Passes are "non-transferable in v0" **and** a 3% fee on resales of passes | Self-contradictory. The 3%/5% figures come from Franz's report, not ours | v0 passes non-transferable; any regeneration share in flows is set by the team, not copied |
| M4 | Commons funds "unseizable" (*inembargables*) | A contract can't make money unseizable. What protects it is a **separate patrimony** (trust or the Guardian's own account), away from the company's creditors | Commons money sits with the Guardian, never on NetX's balance sheet (rule 2) |
| M5 | Funders' chamber "approves Commons Fund investments" by weighted vote | Lets capital steer commons money | Commons spending: Guardian + Council of Regeneration; funders advise ❓ to settle in the governance doc |
| M6 | MiCA "utility tokens **or ART**"; "Swiss Purpose Trust" under FINMA | ART is the stablecoin-like category, wrong for a pass. Swiss law has no purpose trust of its own (Liechtenstein does) | RAIZ v2 rails: open, to research (07 C) |
| M7 | "Ordenanza 173/04", "art. 41" | The ordinance is 173/2026; our doc cites arts. 23, 42 and 43 | Keep 06 L28 and L41 |
| M8 | CNV resolution numbers (1069, 1081, 1087, 1137, 1150, "1058" for PSAV) and the sandbox "to 2027/2028" | Mixed: some are real and linked (RG 1150/2026), others have no source | Counsel to confirm; our working date for the sandbox end stays 31-12-2027 [verify] |
| M9 | Guardian buys its 1 ha dominant parcel "on days 61–90" | That parcel has to be surveyed and split first, which needs the survey and the municipality. The two reports even disagree on timing | Easements after the survey (realistic: H2 2027) [criterio] |
| M10 | Tamera/OASA "land in a trust, no private lots" | Cites our own file; not checked | Treat as unverified |

## 5. The question nobody asked: is it "rural land" in law?

Ley 26.737 applies only to **rural land: any parcel outside an urban *ejido*, whatever its use** (art. 2 [verify]). So everything in §3.1 hinges on one fact: **is Macrolote 7 inside Mainqué's urban ejido, or will Ord. 173 approval make it urban?**

- **If it is urban**: the foreign-ownership limits don't apply to it, and the holding has more freedom (even so, we keep the land in an Argentine trust for purpose reasons).
- **If it is rural**: the trust and Guardian must be Argentine-controlled, and the riverside strip can never pass to foreign hands, even as a final step.
- **Also check**: is BioPueblo's owner (Lavima S.A.) itself foreign-controlled? If it is, the law already constrains what it can hold or transfer.

Doc 06 L38 raised this in passing; Gemini only lists an "ejido certificate" as an admin step on day 31–60. It is actually **the first legal question**. New: 07 H-11.

## 5b. Can foreign capital still come in? Yes, if control of the land never flips upwards

Ley 26.737 doesn't ban foreign **investment**. It limits foreign **ownership, possession or tenure** of rural land and **control** of it through companies. Our structure separates exactly those two things: money can come from abroad, control of the land stays Argentine [criterio, verify].

| Door | Can a foreigner come in? | Why |
|---|---|---|
| **SAFE in the holding** (company pot) | ✅ Yes | The holding doesn't own the land; BioPueblo is paid in company shares, not land |
| **Founding Pass / RAIZ** (commons pot) | ✅ Yes | A right to use services; no ownership or possession of land |
| **Land trust units** (land pot) | ⚠️ With care | Point 2 below |
| **Living there** (surface right or long licence) | ⚠️ With care | Point 3 below |

Conditions, each a question for counsel (07 H-13):

1. **Control flows bottom-up, never top-down.** The law treats a company as foreign above 51% foreign capital, or from 25% if that is enough to form its will (art. 3 [verify]). If the foreign holding controlled the trust or the Guardian, the land would be foreign-held through that chain. Our design is the reverse: the Argentine Guardian is the trust's final beneficiary and holds the golden share **over** the holding. Counsel must confirm that no clause gives the holding power over the trust: appointing or removing the trustee, changing beneficiaries, amending the trust deed.
2. **Foreign holders of trust units.** If units carry rights to **income** (licence fees, hospitality, services) and none to the land, the risk looks low. We don't know whether the law or Decree 274/2012 counts them as indirect ownership [verify]. Prudent default: cap the foreign share of step 3 until counsel answers.
3. **Foreign residents.** The law also speaks of possession and tenure: a 70-year surface right granted to a foreigner might count [verify]. On the river strip, never: foreigners can't hold land that contains or borders large permanent water bodies (art. 10). That strip is already planned as conservation and commons (06 L30).
4. **Quotas, not only bans.** Something that counts as foreign isn't automatically forbidden: the caps are 15% of the department and 1,000 ha of core zone, or its provincial equivalent, per foreign holder [verify the Río Negro equivalent]. A certificate from the National Rural Land Registry shows the remaining quota.

All of this matters only if 7A is rural land in law (§5).

## 6. Did Gabriel's vault file bias the research?

Gus asked whether Gabriel's internal file was used as dogma. Honest answer:

- **What we took from it** (doc 06 footnote [^gv]): law texts and their limits: the name of the provincial registry (IGPJ), the private-offer limits of RG 1088, the 5-year cap on a pre-emption right, the need for a dominant parcel for a perpetual easement, mortgage of surface units, and that the land law was in dispute. These are **readings of public law**, each marked [verify]. The prompt told Gemini *not* to use internal material and to verify the land law itself; it did, and found the ruling.
- **Where it shaped the design**: the dominant parcel for the Guardian, and the 30-year trust limit. Both are plain Civil Code (arts. 2162–2165, 1668), not Gabriel's opinion, and Gemini found them independently.
- **What it did not decide**: the optimistic structure (ownership in a purpose trust, Guardian, golden share) came from Gus's correction of 2026-10-16, and Gabriel's file had nothing on it. The ladder came from docs 13–15 and 20.
- **One real distortion, already fixed**: an earlier draft of doc 20 treated "the trust holds only a surface right" as fact; that came from a verbal account, not from the law. Gus caught it, and it became fallback P1.

Rule going forward [criterio]: Gabriel's file is a **source list**, not a set of conclusions. Any point from it that changes the design needs the cited text read by our own counsel (07 H-1).

## 7. What to do now

1. Update 06 (L8, L30, L38: land law in force on an interim basis since 2026-10-09; new L42 timeshare) and 20 (P2 becomes the base case).
2. First question to counsel: **rural or urban** (§5), plus whether BioPueblo's owner is foreign-controlled.
3. Term sheet: add milestone vesting (§3.3) and "sale zone outside Lighthouse" (§3.4) as options.
4. Fix in our own texts before sharing the Gemini reports: M1 (ratchet), M2 (DRS for homes), M3–M5.
5. Share with Franz: the reports plus this page, so the team doesn't take the echo as independent proof.

---

## Sources & logic used

[^gem1]: Gemini Deep Research, "Estructura Legal Lighthouse VRN", Google Doc shared by Gus, 2026-10-17 (run on `prompt_gemini.md` with Franz's report, doc 20 and doc 17 as attachments). [S]
[^gem2]: Gemini Deep Research, "Lighthouse VRN Legal Architecture", Google Doc shared by Gus, 2026-10-17 (same run, longer version following the deliverable list of the prompt). [S]
[^csjn]: CSJN interim suspension of art. 154 DNU 70/2023, 2026-10-09, reported by [Palabras del Derecho](https://www.palabrasdelderecho.com.ar/articulo/7050/La-Corte-Suprema-suspendio-la-derogacion-de-la-Ley-de-Tierras-dispuesta-por-el-DNU-70/2023), [Diario Judicial](https://www.diariojudicial.com/news-104625-los-arboles-mueren-de-pie), [ANB](https://www.anbariloche.com.ar/amp/noticias/2026/10/09/119592-la-corte-suprema-restablecio-los-limites-a-la-compra-de-tierras-por-extranjeros-por-un-reclamo-de-bariloche) and [Noticias NQN](https://www.noticiasnqn.com.ar/noticias/2026/10/09/355956-la-corte-freno-la-derogacion-de-la-ley-de-tierras-que-limites-vuelven-a-regir-y-que-falta-resolver). [S] (several outlets agree; the ruling text itself not yet read [verify])
[^gv]: Gabriel, inventory of his vault for the legal deep research, 2026-10-13 (internal working file, kept out of the repo).

- **Method**: each claim in both reports was sorted into echo / web fact / inference / invention (§1) by checking its footnote against our files, then compared with docs 06, 17, 18 and 20.
- **Checked by search**: the Supreme Court ruling only. All other Gemini legal claims stay [verify].
- **Our judgement** [criterio]: M2 (surface right for homes), §5 (rural/urban as the first question) and the reading of Gabriel's role in §6.
