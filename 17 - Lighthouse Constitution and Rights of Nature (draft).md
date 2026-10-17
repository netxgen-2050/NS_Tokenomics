---
title: Lighthouse Constitution and Rights of Nature — how we hardcode them (draft)
created: 2026-10-13
status: v0.1 — design draft by a non-lawyer; every anchoring instrument is [verify] with counsel
audience: Gus, Gabriel, Council of Regeneration (when it exists), counsel
---

# 17 · Lighthouse Constitution and Rights of Nature (draft)

Back to [[00 - README]] · Vision: [[03 - Long-Term Vision]] · Governance: [[10 - Governance Primitives (options)]] · Hybrid question: [[18 - Hybrid model (selling some lots) - options and trade-offs]]

## 🌱 In one breath

We want the land to have rights that nobody can vote away or buy. Getting a court to recognise a river or a forest as a legal person is a battle outside our scope. What we can do is write those rights into **every document that gives anyone power over the land**: the deed, the trust contract, the easements, the Guardian's statute, each community's licence. Inside our boundary, that works like a constitution: every lower rule has to respect it, and breaking it has consequences. This page looks at how OASA did it, lists the rights we take from the Rights of Nature movement, and drafts the articles.

## 1. What we learn from OASA

**Principles of Regeneration and Land Stewardship (v1.0, 2022)** [^oasa-p]
- Seven areas, each with operative rules: soil, water, air, waste, rewilding and biodiversity, resources, community. Many rules are measurable: no synthetic fertilisers or pesticides; at least 50% of the land kept or made wild; at most 5% of the surface built; at least 30% of trimmed biomass left on the ground; 20 species per hectare in cultivated fields.
- Access to land is conditional: guardian organisations and their members enjoy the land "as long as they uphold" the principles.
- A **Council of Regeneration** of three, elected yearly, interprets the principles, proposes changes and settles disputes about breaches.
- **Monitoring and graduated responses**: yearly reporting on soil, water and biodiversity; a remediation plan when something degrades; mistakes in good faith are not punished; three consecutive years of degradation can lead to removal of the guardian organisation. Persistent breach can end the right of use.

**OASA Constitution (2025)** [^oasa-c]
- Each project's land sits in a single-purpose vehicle or trust controlled by the association, which "may not sell or encumber the land except as explicitly permitted".
- Membership gives "no ownership of land or profit rights", only use rights and a voice. Surpluses are reinvested.
- **Guardians of Nature** represent soil, water, air, flora and fauna; they can flag or veto decisions that threaten ecological integrity, and their consent is needed to amend the constitution.
- Decisions are weighed against their effect on at least seven future generations.
- Projects may be stricter than the principles, never laxer.
- AI agents assist; they do not decide.

**What we take:** conditional access, measurable rules, a double key for amendments (assembly + guardians of nature), graduated responses, "stricter yes, laxer no". **What we adapt:** OASA weights governance by tokens modulated by presence; our residents' matters stay one person, one vote (design rule 6). OASA's thresholds (50% wild, 5% built) are a point of comparison only, not a target or a guide for us; ours come from the masterplan and the land itself ❓ (the RTMM brief asks for more than 50% ecological and productive landscape [^rtmm]).

## 2. The rights we hardcode

From the Universal Declaration of the Rights of Mother Earth (Cochabamba, 22 April 2010), promoted by the Global Alliance for the Rights of Nature [^garn]. Article 2 lists, in substance [S]:

| # | Right of the land and its living systems | Our operative rule (examples) | Measured by |
|---|---|---|---|
| a | To exist | The land is never sold as a commodity nor used as collateral (diode, I1) | Deed, trust contract |
| b | To be respected | The Constitution binds every instrument below it | Annex to every contract |
| c | To regenerate and continue its vital cycles | Minimum ecological share per zone; no net loss of living cover; the river strip stays in conservation (06 L30) | Ledger C, masterplan zones |
| d | To keep its identity and integrity | Development limited to planned zones; ecological corridors left open | Masterplan, GIS |
| e | To water as a source of life | Water budget per community; rain harvesting first; biological treatment of greywater and blackwater; no discharge to the river | Water KPIs |
| f | To clean air | No burning of toxic materials; controlled burns only where planned | Incidents |
| g | To integral health | Soil organic matter and biodiversity may not decline two periods in a row (I6) | Baseline + yearly MRV |
| h | To be free from contamination and toxic waste | No synthetic biocides or fertilisers; no hazardous materials | Audits |
| i | Not to have its genetic structure disrupted | Native and adapted species first; no invasive species ❓ scope to be defined by the Council | Planting register |
| j | To full and prompt restoration | Whoever harms, repairs: remediation plan, cost on the responsible party, graduated up to loss of the licence | Remediation log |

We do **not** claim that the land is a legal person or that these rights are enforceable as such by anyone in court. We claim that every party who holds a right over this land has **agreed** to these duties, and that the instruments below make that agreement enforceable 🏴‍☠️ (substance: real contractual and property-law duties, not a label).

## 3. Where the rights are anchored (the norm stack)

Gus called this "fractal jurisdictions" [^t]: each layer is free inside the layer above it.

| Layer | Instrument | What it can do for the rights of the land | Strength | Check |
|---|---|---|---|---|
| 0 | Argentine, provincial and municipal law | Sets the outer limits; environmental law already limits property rights | Public law | CCyC arts. 14 and 240; Ley 25.675 [verify] |
| 1 | **Easements** registered on the parcel, held by the Guardian | Negative duties that follow the land whoever holds it | Real right | A **real** easement is presumed perpetual (CCyC 2165) but needs a dominant parcel, so the Guardian must own one; a personal easement for an entity lasts ≤50 y (2182). Granted by the land owner; registration needs a cadastral certificate (RN Ley 3483) [C] [^gv] |
| 2 | **DRS deed** and **fideicomiso contract** | Purpose clause; forbidden acts (sale, mortgage); who receives the assets at the end; Guardian consent for reserved matters | Contract + registered real right | DRS ≤70 y to build, ≤50 y to forest; trust ≤30 y (CCyC 2117, 1668) [C]: what carries the rights after that? 🧨 (06 L37). A bare "no sale" clause is void in onerous acts (1972); resolutory conditions are capped at 10 y (1965) [C] [^gv] |
| 3 | **Lighthouse Constitution** (§4) | The single text all others refer to | By incorporation into 1, 2, 4, 5 | — |
| 4 | **Guardian statute** | Guardians of Nature seat, Council of Regeneration, double key for amendments, asset lock | Association / foundation law | IGPJ Río Negro (Ley K 3827); minimum members per Res. IGPJ 461/03 [C] [^gv] |
| 5 | **Community licence** and plug-in agreement ([[05 - Community Token Templates]]) | Conditional use: the licence lives while the principles are kept; graduated sanctions; step-in and termination | Contract | Enforceability of termination where people live 🧨 [verify] |
| 6 | Community charters, household and space agreements | Local rules, stricter if they want | Contract / internal rules | — |
| 7 | Platform rules and records | Makes compliance visible; flags | Evidence only (I8: the legal record wins) | Ley 25.326 |

**Other anchors, and their limits** [C] [^gv]: the regulation of a *conjunto inmobiliario* (CCyC 2078, 2080, 2085, 2086) can protect ecological values, is transcribed into every deed, gives the consortium a preference on resale and allows sanctions for serious or repeated breaches; it can limit transfers but not prevent them. A **charge** (*cargo*, art. 356) in each title, with a penalty clause (art. 794), travels with the right, though a judge can reduce a disproportionate penalty. There is no private expropriation: on owned land the strongest sanctions are fines, suspension of community rights and the community's preference when someone sells. No Argentine trust with an enforceable ecological sanctions regulation has been found [NC].

**Why licences matter here:** on licensed land we hold three remedies (repair, sanction, end of the licence). On a **sold lot** we keep only layer 1 and whatever regulation binds owners. That is the core of the trade-off in [[18 - Hybrid model (selling some lots) - options and trade-offs]].

## 4. Draft articles (v0.1, for discussion)

**Preamble.** We are stewards of this land for a time. It was here before us and will be here after us. We organise so that its living systems grow richer because we are here.

1. **The land is not a commodity.** Lighthouse land is never sold, mortgaged or pledged, and no token, fund, community or investor instrument may cause that. Rights flow up the layers; debt and recourse never flow down.
2. **Rights of the land.** The land and its living systems hold the rights listed in §2 (a–j). Every person and organisation with a right over the land accepts the duties that follow from them.
3. **Thresholds.** Each zone has measurable minimums (ecological share, built share, water, soil, biodiversity) set in the masterplan and reviewed by the Council. ❓ numbers pending Martín's masterplan.
4. **Stricter, never laxer.** Communities govern themselves and may adopt stricter rules. No community rule, contract or vote can lower a right in this Constitution.
5. **Subsidiarity.** Decisions are taken at the smallest circle able to carry them. A higher circle acts only on what affects more than one community or the land as a whole.
6. **Voice of the Land.** Guardians of Nature sit in the Guardian entity with the power to pause any decision that threatens the rights in article 2 until the Council has ruled.
7. **Council of Regeneration.** An independent council interprets this Constitution, gates the use of the Commons Fund against it (I5) and settles disputes about breaches. Its reasons are published.
8. **Monitoring and graduated responses.** Each community reports on soil, water and biodiversity. Degradation triggers, in order: explanation, remediation plan, support, sanction, and as a last resort the end of the licence. Good-faith mistakes are met with help first.
9. **People.** Residents' matters are decided one person, one vote. Nobody is admitted or excluded for their beliefs; admission and permanence depend on conduct and contribution, including the duties of article 2.
10. **Money.** Company, commons and land money are kept apart. Commons money is never company revenue. Surpluses of the commons are reinvested in the land and its communities.
11. **Succession.** If NetX, the Guardian or any steward ceases to exist or fails, stewardship passes to an organisation with the same purpose, chosen by the Council and the residents. The land never returns to the market through our failure.
12. **Machines.** Automated agents may monitor, inform and flag. They do not decide; a flag pauses and people rule.
13. **Entrenchment.** Articles 1, 2, 4 and 11 cannot be amended. The rest needs a qualified majority of residents and the consent of the Guardians of Nature.

Notes on the draft:
- Article 9 keeps us inside Ley 23.592: we ask people to **do** things (no biocides, repair what you harm), we don't ask them to **believe** things. OASA's devotional language fits a preamble that people may share, not an admission test [criterio].
- Article 1: whoever holds a surface right may mortgage what is built on it by law (CCyC 2120). "Never mortgaged" has to be agreed in the DRS deed, and whether that pact binds third parties is [verify] (06 L40).
- Article 11 is a wish until the land owner agrees: the fideicomiso holds a surface right from Lavima / BioPueblo, not ownership. What happens at the end of the surface right is theirs to grant 🧨 (06 L37).
- Article 13: "cannot be amended" has to be mirrored in instruments that last (easements, the DRS deed). A statute alone can be changed by those who control the entity [verify].

## 5. Open questions

1. Which numbers go into article 3, and per which zones? (Martín, Council)
2. Who are the Guardians of Nature: people named by the Council, partner organisations, a rotating seat? (ties to 10)
3. Can the Constitution be made an annex of the BioPueblo term sheet now, so the DRS deed carries it from day one? (Franz, Gabriel; 06 L39)
4. Legal anchoring of §3, layer by layer: block J of [[prompt_legal]].

## Sources & logic used

- Logic: rights that are not justiciable as "rights of nature" become enforceable when rewritten as duties in property and contract instruments; the stack follows the repo's layers and invariants ([[03 - Long-Term Vision]] §1, §7).
- The rights table in §2 paraphrases Article 2 of the Declaration from memory of the text; the GARN page only links to PDFs, so compare with the PDF before quoting [S].
- Drafting choices in §4 are ours [criterio].

[^oasa-p]: Oasa Association, *Principles of Regeneration and Land Stewardship*, v1.0, created 28 Apr 2022 (Google Doc shared by Gus, read 2026-10-13).
[^oasa-c]: *OASA Constitution 2025*: https://oasa.earth/papers/oasa-constitution-2025/ (read 2026-10-13, through an automated summary; verify wording before quoting) [S].
[^garn]: Global Alliance for the Rights of Nature, Universal Declaration of the Rights of Mother Earth: https://www.garn.org/universal-declaration-for-the-rights-of-mother-earth/ (adoption date and place confirmed on the page, 2026-10-13).
[^rtmm]: `sources/NetX_Lighthouse_Regenerative_Territorial_Model_AI.md`, as summarised in [[01 - Context and Constraints]] §1.
[^t]: Call 2026-10-12 (private Fathom transcript); see [[16 - Call 2026-10-12 (hybrid model, inputs and actions)]].
[^gv]: Gabriel, inventory of his vault for the legal deep research, 2026-10-13 (internal working file, kept out of the repo; only its shareable parts are used here: law texts and general criteria). Not reviewed by a licensed lawyer.
