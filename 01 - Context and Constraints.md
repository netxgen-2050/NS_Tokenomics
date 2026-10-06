---
title: Context and Constraints
created: 2026-10-02
status: v0.1
sources: ../NS_platform/Documentation (00, 03, 10, 11, 13, 16, Desarrollo/02-03, requisitos-legales, Investigacion DRS), sources/NetX_Lighthouse_Regenerative_Territorial_Model_AI.md
---

# 01 · Context and Constraints

Back to [[00 - README]]

## 🌱 In one breath

We have a big, beautiful piece of land that we cannot yet legally sell in pieces, a legal research that says "money goes to a trustee, never through the platform, and no tradable tokens", and a hard date (February 2027 Gathering at BioPueblo). The tokenomics has to create value **inside** those walls now and be **ready to grow** when the walls move.

## 1. The territory

| Item | What we know | Source |
|---|---|---|
| Land | **Macrolote 7, ~969 ha** in **Mainqué, Río Negro**, part of BioPueblo's ~10,000 ha. Lot **7A** is NetX's. Soluna (Parcel 5, 110 ha, 50 chacras) is the first BioPueblo barrio, a sibling not our land | Investigación DRS §2; Producto v2 §2 |
| Owner | Mother parcel 05-7-880580 (matrícula 05-22352) owned by **Lavima S.A.**; sale to BioPueblo in progress | Legal brief §0.a |
| Proposed structure | Lavima grants a **derecho real de superficie (DRS)** per macrolote (≤70 y) to a **fideicomiso de desarrollo** (≤30 y) with adhering fiduciantes; **perpetual negative easements** in favour of a **guardian entity** as the ecological anchor | Investigación DRS §2, §5 |
| Planning model | RTMM: ~1,000 residents, 10–12 intentional communities, >50% ecological/productive landscape, 180–250 ha food, shared metabolic infrastructure, three ledgers (cash / commons / ecological) | Lighthouse brief |
| Hard question the brief leaves us | **"What finances the commons after land-sale/appreciation capture matures?"** (Challenge 5) | Lighthouse brief §10 |

The tokenomics is, in large part, our answer to that last question.

## 2. Legal walls (as of 2026-09-29 research — context, not a legal opinion)

| Wall | Consequence for token design | Emoji |
|---|---|---|
| **Ordenanza 173/2026 Mainqué** arts. 41–46: no offering, advertising, reserving lots of unapproved subdivisions; 7A only "vision + non-binding interest, no money, no lot, no priority" until preliminary approval (target Feb 2027) | The mother token **cannot** carry lot priority, lot reservation, or be marketed with lots | 🧨 |
| **Transferable token = "activo virtual"** (Ley 25.246 art. 4 bis); offering it through a platform = **PSAV** registration (CNV, SA/SRL) | v0 must be **non-transferable** in Argentina | 🧨 |
| **If it carries profit expectation and is in series** → valor negociable → public offering without authorization (Ley 26.831 art. 2; CP art. 310) | No yield, no "appreciation" narrative, no buy-back promise | 🧨 |
| **Private-offer safe harbour** (RG CNV 1016/2024 mod. 1088/2025): ≤35 buyers per issue, ≤15 non-qualified, no mass media | Financial participation (fideicomiso) stays a **separate, invitation-only circle** | ✅/🧨 |
| **Money never passes through the platform or NetX Gen**; goes to the fiduciary / receiving entity | Pass revenue must land in a **legal recipient** (Commons association or fideicomiso), not NetX | ✅ |
| **Timeshare** ("7 tokens = 7 nights") needs property affectation + Tourism registry before promotion (CCyC 2087–2102; Ley 26.356) | TDF-style perpetual night rights are **out for Feb**; consumable stay credits are OK | 🧨 |
| **One foreign beneficiary** in the fideicomiso makes the whole fideicomiso taxable (25–35%); foreigners cannot take ownership of **riverside rural land** (Ley 26.737) | Foreign supporters are a natural audience for the **Commons/mother layer**, not for the fideicomiso | 🧨 → 🏴‍☠️ opportunity |
| **Anti-discrimination** (Ley 23.592): no admission by ideas/values | Token gating must be by **conduct and contribution**, never by belief | 🧨 |
| **Asociación civil** cannot distribute profits | Value from associations must circulate as **use-value / services / in-kind**, not dividends | design driver |
| **CNV tokenization sandbox** (RG 1069/2025 → RG 1150/2026) open **until 31-12-2027**; real-estate precedents (Illa Belgrano, Espacio Añelo, Landtoken) | A regulated, tradable real-estate token is possible **later** via fideicomiso financiero + PSAV | ✅ (2028) |
| **Personal data** (Ley 25.326) not yet researched | Presence/sweat/values data needs a privacy design | ❓ |

## 3. What the product team has already decided (we build on it, not around it)

- **No wallets or smart contracts in this phase**; "the platform may break, the investment contracts never" (Producto v2 §1).
- Non-transferable **Semillas** (ex Project Points) as internal value accounting, Collabberry-style agreement → peer review → allocation (doc 16).
- **Pase de estadías**: non-transferable lodging credits as a service contract.
- **Sumarte** = adhesion to the macrolote fideicomiso, invitation-only, KYC by the fiduciary.
- Community templates: **asociación civil** (non-profit) or **SAS** (with returns).
- UI vocabulary avoids "token", "inversión con retorno", "reservá" (Glosario UX-Legal).

**Implication:** the tokenomics should add **one new piece** for February (the mother/Founding Pass and the Commons Fund it feeds) and **re-use** Semillas, Pase de estadías and Sumarte as the other "organs".

## 4. Timeline anchors

| Date | Event |
|---|---|
| Oct 2026 – Jan 2027 | 4 monthly product iterations (doc 14) |
| **Feb 2027** | **Gathering/Congress at BioPueblo**: genesis event, first sales of the Pass, 7A preliminary approval hoped for |
| 2nd third of 2027 | Definitive approval (escrituración) per BioPueblo |
| **31-12-2027** | CNV tokenization sandbox ends (may be extended or replaced) |

## 5. What the RTMM brief adds to token design

- **Barrett's seven levels** become the *coverage test* for which needs the token ecosystem serves (survival goods → service/meaning).
- **Three ledgers** map one-to-one to token families:
  - Ledger A (cash) → fideicomiso units, sales, tariffs, Pass revenue.
  - Ledger B (internal provisioning / commons) → stay credits, commons credits, community vouchers, Semillas.
  - Ledger C (ecological capital) → **non-tradable** attestations that *gate* fund releases (never sold as credits in v0).
- The 12-community ecology gives us the **producers** whose commitments back the mother token's access utility.

## 6. Updates from the 2026-10-02 call (Gus–Gabriel) [^call]

| Topic | Update | Consequence |
|---|---|---|
| Land | **Lighthouse hectares will not be sold**; one fideicomiso for Lote 7 holds the DRS | Value must come from licences, tariffs, services, RAIZ: see [[09 - Investor Value Model (win-win-win)]] |
| Rights to communities | A DRS can't be granted on a DRS (CCyC art. 2118 [^drs]); communities get **use rights / licences** | Template in [[05 - Community Token Templates]] §0 |
| Structure (Gabriel's sketch) | Uruguay holding → Argentine SA/SAS → **fiduciary**; BioPueblo fiduciante (land) + beneficiary; investors beneficiaries | 🧨 fiduciary = developer conflicts with research recommendation (L21 in 06) |
| Scale | Lote 7 fits **~20 barrios**; land value mentioned **~USD 4M** [NC] | Input to the value model |
| Money | Cash runs out around **March 2027**; SAFE round USD 375–500k, 5k tickets | [[12 - Round Inputs (costs and use of funds)]] |
| Jurisdiction | Leave Próspera for the round (Uruguay or Wyoming) | Issuer choice in 06 §2 |
| Name | Mother token = **RAIZ** | All docs |
| Land law politics | Gabriel mentioned a bill to relax limits on foreign land ownership (Ley de Tierras) in Congress; the 29-09 research records the Senate approving the property bill **without** the land chapter on 6/7-08-2026 [^drs] | Re-verify before any foreign-buyer flow ❓ |

## 7. Updates from the 2026-10-05 team meeting [^team]

| Topic | Update |
|---|---|
| Scope | NetX's focus is **Lighthouse, "our barrio"**, inside a BioPueblo town of ~10 barrios; platform could later serve other barrios |
| Masterplan | Preliminary masterplan **15 Oct**; anteproyecto end of October → surveyor → municipality (Martín). GIS base includes topography, hydrology and historical flood levels |
| Flood strip | Part of the land next to the river may be unbuildable → keep as conservation commons (06 L30) |
| Land signature | LOI with BioPueblo expected **mid-October** |
| Micro-investors | Demand for USD 2–5k tickets; see [[15 - Micro-investor offer (USD 2-5k tickets)]] |

## Sources & logic used

- `../NS_platform/Documentation/` files 00, 03, 10, 11, 13, 16, `Desarrollo/02–03`, `requisitos-legales-plataforma-2026-09-29.md`, `Investigacion — DRS, fideicomisos y tokenizacion (Lighthouse VRN) 2026-09-29.md` (read 2026-10-02).
- `sources/NetX_Lighthouse_Regenerative_Territorial_Model_AI.md` (RTMM brief v0.1).
- Logic: constraints first, then design ("requirements before mechanisms", see 02).

[^call]: Private call Gus–Gabriel, 2026-10-02 (private transcript); sanitised in [[13 - Call 2026-10-02 (decisions and actions)]].
[^drs]: `../NS_platform/Documentation/Investigacion — DRS, fideicomisos y tokenizacion (Lighthouse VRN) 2026-09-29.md` §3 A.1, §3 A.5.
[^team]: Core team monthly, 2026-10-05 (Fathom transcript in `../NS_platform/Documentation/transcripts/Octubre/`); see [[14 - Team meeting 2026-10-05 (inputs and actions)]].
