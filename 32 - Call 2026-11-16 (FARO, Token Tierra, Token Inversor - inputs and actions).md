---
title: Call 2026-11-16 — FARO, Token Tierra, Token Inversor (inputs and actions)
created: 2026-11-19
status: v0.1 — sanitised notes of a private call; positions are reported, not agreed, unless marked ✅; legal points [verify]
audience: Gus, Juanpi, Franz; then the whole core team
---

# 32 · Call 2026-11-16: FARO, Token Tierra, Token Inversor

Back to [[00 - README]] · Proposal that follows from it: [[34 - Propuesta para Juanpi y Franz (FARO, Token Tierra y Token Inversor)]] · Earlier: [[31 - Lot sales for phase 1 (CEO decision 2026-11-02)]], [[11 - Review of $NETX v2 tokenomics (2025)]]

## 🌱 In one breath

Gus showed the platform selling lots and a commons token called **FARO**. Juanpi showed the strategy with Tether and Hadron and three instruments: **Token Tierra** (a lot paid in instalments), **Token Inversor** (money lent to a project, bought back with a premium) and tokenised equity. Juanpi warned against funding the project with a freely traded token, because the team ends up defending its price. One thing was agreed: **one trust per neighbourhood**. Both said their models can live together, and Franz asked for one shared document where the two are crossed [^call].

> **Priority (Gus, 2026-11-19):** what was said in this call comes before decisions recorded earlier in this repo. Hard law still binds both. Section 4 lists what that changes.

## 1. What was agreed

| # | Point | Status |
|---|---|---|
| 1 | **One trust (fideicomiso) per neighbourhood**, to isolate legal and administrative risk | ✅ agreed in the call [^call] |
| 2 | The two models (FARO; Token Tierra and Token Inversor) aren't exclusive and can be worked in parallel | ✅ said by Gus, accepted by Juanpi |
| 3 | One shared document for the three, in the "Plataforma y Tokenomics" folder, holding the Hadron studies, the 2025 $NETX work and Gus's material | ✅ Franz organises it |
| 4 | Nothing is signed with Tether before the agreements are reviewed in depth | ✅ all three |
| 5 | The token needs as much real use as possible | ✅ Gus and Juanpi |

## 2. Positions

| Topic | Gus | Juanpi | Franz |
|---|---|---|---|
| The commons | FARO: one fungible token for everything held in common (access, rights, duties, voice). A non-fungible record per private lot. Ostrom's principles as the base | FARO is "a utility by nature", and that is good | Wants Bauwens added to the bibliography |
| How FARO is sold | Tranches at rising prices, by quantity sold or by time; early buyers pay less. Could also prepay yearly dues | Not in favour of a project token as a funding tool: it needs liquidity and a reserve from day one, early buyers want out, and the team spends its time answering for the price | Sees potential if value grows with the project over 15–20 years |
| Price control | Burns tied to use; bonding curves; a closed primary market; release little by little; simulate first (cadCAD, Monte Carlo). Said the land could act as the reserve | Use and market makers help, but "once everything is released you can't control it" | — |
| Lots | A buyer of a resold lot should hold staked FARO, so private resales also feed the commons | **Token Tierra**: buy a lot in tokenised instalments (ERC-20 or ERC-3643). In Argentina the token gives economic rights; the deed follows its own legal path; an NFT can be a certificate when the plan is completed | Each area of the masterplan clickable on the platform |
| Project funding | — | **Token Inversor**: a pre-sale for defined projects; buyers are micro-funders; the developer or trust buys the token back at a higher value (his example: USD 100 back at USD 110 after a year). It can cover a part (his example: 2 of 10 million) next to traditional funding. Tickets from USD 100 | A window of about six months, July to December 2027, to raise with tokens; the legal side ready by July |
| Tether and Hadron | Reputation risk: Tether's priority is its own currency; "careful" | Tether could buy equity in NetX State LLC with land brought into the company (Adecoagro precedent), and Hadron as the tokenisation tool. Hadron has no compliance layer of its own: NetX resolves it | Likes Tether; agrees to check before signing |
| Secondary market | — | A closed, private trust can resell inside the platform (the trust buys and sells again) without becoming a public offer [verify] | — |

## 3. Facts and claims to check

- The regulatory sandbox for tokenisation ends on **2027-12-31**, and national elections come just before; after that "anything can happen" (Juanpi) [S]. The repo already held the same date for the CNV regime (RG 1069/2025 and 1150/2026) [^hadron].
- A token resold inside the platform by a private trust is "a utility or asset token", not a negotiable security (Juanpi) **[verify]**: who runs the resale may need to be a registered virtual-asset provider, and a buy-back with a premium looks like debt [^tetherdoc].
- Tickets from USD 100 to the public don't fit a private offer to a few investors **[verify]**: the route for retail has to be named (public-offer trust under the CNV regime, or a crowdfunding platform).
- Land brought into NetX State LLC with a foreign shareholder meets Ley 26.737 (rural land) **[verify]**; the team's own Tether draft already says equity must not be described as ownership of land [^tetherdoc].
- FARO per lot shown in the platform: about 10 per m² (21,650 for a lot of 2,165 m²), a sample value [^slides].
- Vagner sent cost data as a PDF; it isn't in the slides or in this repo yet ❓.

## 4. Where the call departs from this repo

`AGENTS.md` asks for this to be said out loud. With Gus's priority note above, the call wins where it's a choice of ours; law doesn't move.

| Rule or earlier decision | What the call does | Kind |
|---|---|---|
| Rule 1, the diode (no instrument sells the land) | Token Tierra sells lots in instalments; already opened by doc 31 | Our choice, under review |
| Rule 2, three pots (company, commons, land) | Tether equity with land inside the company would join two pots | Our choice; and Ley 26.737 [verify] |
| Rule 3 (the membership token never carries price or return language) | Rising-price tranches and "the price should rise" were said about FARO, inside the team | Our choice; and Ley 26.831 art. 2 [verify] |
| Rule 4 (no lots, priority or reservations before municipal approval) | Token Tierra is a reservation with payments if it starts before approval | **Law** (Ord. 173/2026) |
| Rule 6 (residents' matters, one person one vote) | Voice by FARO held, with a cap per person | Our choice |
| A2 (the mother token is RAIZ) | The commons token is called FARO | Our choice |
| F-3 (platform chosen after the design, for pot 3 only) | Hadron is discussed for lots, project funding and equity | Our choice |
| Doc 11 (drop burns, public sale and market making) | Burns tied to use are back; public sale and market making stay out by Juanpi's own warning | Our choice |

## 5. Action items

| Who | What |
|---|---|
| Gus + Juanpi | A shared document crossing both models and naming the synergies → [[34 - Propuesta para Juanpi y Franz (FARO, Token Tierra y Token Inversor)]] is Gus's draft for it |
| Gus | Update the platform document with Vagner's costs |
| Franz | Organise the shared document and folder; send the Bauwens bibliography (received 2026-11-16 → [[33 - Bauwens bibliography (P2P and the commons) - reading notes]]) |
| Juanpi | Send the Hadron email and access to the documents |
| Team | Read the slides of 2026-11-09 and answer their questions |

## Sources & logic used

- Private call "Plataforma | Tokenomics y MicroFunding", 2026-11-16 (Google Meet transcript and automatic notes, kept outside the repo). The automatic transcript garbles names and terms; where a term was unclear it was left out.
- Slides "El bien común de Lighthouse VRN", team meeting of 2026-11-09 (Google Drive).
- Shared working document "Tokenomics & Plataforma | Trimestre de Fuego" (Google Doc; sections on the platform comparison, the Tether proposal, the Hadron preparation and the 2025 $NETX tokenomics), read 2026-11-19.
- Logic: separate what was agreed from what was only said; mark which departures are choices and which are law [criterio].

[^call]: Private call "Plataforma | Tokenomics y MicroFunding", 2026-11-16.
[^slides]: Slides "El bien común de Lighthouse VRN", 2026-11-09, and the platform demo in the call.
[^hadron]: Section "Blindaje Legal | Gus" of the shared working document (prepared 2026-10-27).
[^tetherdoc]: Section "Propuesta para Tether" of the shared working document, §1 and §4.
