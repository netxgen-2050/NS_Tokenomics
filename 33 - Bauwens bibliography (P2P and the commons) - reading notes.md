---
title: Bauwens bibliography (P2P and the commons) — reading notes
created: 2026-11-19
status: v0.1 — notes built from structured digests of each text, not from a line-by-line reading; check the full text before quoting
audience: Franz, Gus, Juanpi; then the whole core team
---

# 33 · Bauwens bibliography (P2P and the commons): reading notes

Back to [[00 - README]] · Used in: [[34 - Propuesta para Juanpi y Franz (FARO, Token Tierra y Token Inversor)]] · Call where it was asked for: [[32 - Call 2026-11-16 (FARO, Token Tierra, Token Inversor - inputs and actions)]]

## 🌱 In one breath

Franz sent eight texts by Michel Bauwens and co-authors of the P2P Foundation [^mail]. Their shared argument: put the commons at the centre, let the market serve it, and let capital come in and be paid as long as what grows is the commons. Bauwens calls that last move **transvestment**: "we need to translate capital into commons" [^seeds]. The texts back the split proposed in doc 34 (capital in one lane, the commons token in another, a membrane between them). They question two things we had on the table: a token designed to be scarce and get more expensive, and a community that only looks inward. They don't contain a token design, numbers or anything on land law.

The link to Doughnut Economics that came up in the call: one of the files lists Kate Raworth's doughnut as a figure, next to a figure on contributing within social and ecological limits [^figs]. Both are images and weren't read.

## 1. The eight texts

| # | Text | What it is | Licence | Markdown copy |
|---|---|---|---|---|
| 1 | Manski & Bauwens, "Reimagining New Socio-Technical Economics Through the Application of Distributed Ledger Technologies", *Frontiers in Blockchain* 2:29 (2020) | Review article, 17 pages. The most useful one for token design | CC BY [C] | `sources/bauwens/` (in the repo) |
| 2 | Its corrigendum, *Frontiers in Blockchain* 3:14 (2020) | Fixes a name, two citations and one term; conclusions unchanged | CC BY [C] | `sources/bauwens/` (in the repo) |
| 3 | Bauwens, Kostakis & Pazaitis, *Peer to Peer: The Commons Manifesto*, University of Westminster Press (2019) | Short book, 103 pages. The general theory | CC BY-NC-ND 4.0 [C] | `private/bauwens/` |
| 4 | Kostakis & Bauwens, *Network Society and Future Scenarios for a Collaborative Economy*, Palgrave Macmillan (2014) | Short book, 98 pages. The four scenarios and the partner state | All rights reserved [C] | `private/bauwens/` |
| 5 | Bauwens & Jandrić, "The Seeds of the Commons", *Postdigital Science and Education* 3 (2021) | Interview, 17 pages | Springer, exclusive licence [C] | `private/bauwens/` |
| 6 | Bauwens, "The Blockchain Revolution", GTI Forum (February 2022) | Short essay. **The file is Franz's annotated copy**: his notes in Spanish, then the full text | Not stated | `private/bauwens/` |
| 7 | "P2P Accountability Figures" | A working list of figures and boxes for a P2P Foundation report on accounting. 12 figures are images | Not stated | `private/bauwens/` |
| 8 | Kostakis, Roos & Bauwens, "Towards a political ecology of the digital economy" (2015) | Only the wiki page with abstract and conclusions, 2 pages, recovered by OCR | Not stated | `private/bauwens/` |

Only the two CC BY files are committed. The other six stay in `private/`, which is git-ignored: each person keeps the files Franz sent. The file names differ from the dates of two texts: 1 and 2 are from 2020, not 2021.

## 2. The ideas, in plain words

| Idea | What it means | Where |
|---|---|---|
| **Commons** | Three things together: a shared resource, the people who create and look after it, and the rules they set themselves | [^m20] Part 1 |
| **Seed forms** | Small new patterns that grow into systems, as double-entry bookkeeping did for capitalism | [^seeds] |
| **Transvestment** | Bringing outside capital in and paying it, while what it builds stays in common. A "membrane" keeps commons flows and market flows apart. Their own example is land held in a land trust | [^m20] Part 1; [^man] §1.3 |
| **Three institutions** | Around any commons: the community that produces it, the businesses that live from it, and a for-benefit association that protects it and owns no business | [^man] §2.3.2 |
| **Generative or extractive** | Whether an owner adds to the shared resource or only takes from it | [^man] §§3.1–3.3 |
| **Four scenarios** | Platforms that own everything; "everyone a small capitalist" (where they place Bitcoin); local resilient communities; a global commons | [^k14] ch. 3–8 |
| **Partner state** | A public authority that enables and protects commons instead of running or selling them | [^k14] ch. 9 |
| **Cosmo-local** | Knowledge and designs are shared worldwide; heavy things are made locally | [^m20] Part 2 |
| **Value sovereignty** | The community decides what counts as a contribution and keeps its own accounts of it | [^man] §2.3.1 |
| **Three kinds of accounting** | Contributory (who gave what, including unpaid work), flow (each exchange seen in its whole chain) and thermodynamic (matter and energy counted directly, not through prices) | [^m20] Part 3; [^gti] |
| **Mutual credit** | Money that only exists when one member gives credit to another; all balances add up to zero and the community sets the limits | [^m20] Part 4 |
| **Money tied to a limit** | A currency whose amount follows what the resource can give, as in their fishing example | [^m20] Part 3; [^figs] Box 6 |
| **Reciprocity licence** | Anyone may use the commons; businesses that take without contributing pay a fee | [^k14] ch. 9; [^man] §5.2 |
| **Thresholds and allocations** | A body that says how much of a resource can be used and shares it out; the doughnut is the picture of it | [^m20] Part 5; [^figs] |

## 3. What it backs and what it questions in our design

The mapping is ours [criterio]; the texts never discuss a project like Lighthouse.

| Bauwens | Piece of doc 34 | Effect | What to do |
|---|---|---|---|
| Transvestment and the membrane | Two lanes and three bridges | ✅ Backs it. The bridges are the membrane | Use the word with Franz: capital is paid in lane A, the commons grows in lane B |
| The investor in their Enspiral example had no say over how the commons spent the money [^seeds] | Token Inversor and Tether get no voice over the commons | ✅ Backs 07 K-7 | Write it into the trust and the commons rules |
| Three institutions | The slides' Consorcio and Fundación; NetX, lot owners and producers as the businesses around the commons | ✅ Backs it | Keep the Foundation free of business interests |
| Their criticism of Bitcoin: built to get scarcer, early holders gain by selling to latecomers [^man] §3.3 | Rising-price tranches for FARO; the fixed supply of $NETX 2025 | 🧨 Questions both | Supports 07 K-2 and Juanpi's warning: FARO isn't sold on the promise of costing more later |
| Contributory accounting: people log their work and peers review it [^man] §2.4.2 | FARO earned by contributing (Semillas, 07 J-2) | ✅ Backs it | Same design; keep the collusion defences of doc 29 K11 |
| Mutual credit; money tied to a limit | FARO issued against real capacity (beds, meals, hours) | ✅ Backs it, and opens an option | ❓ Study FARO as mutual credit between members, issued when a service is given |
| A fifth of each venture's revenue to a foundation; rent that depends on how much a tenant serves the common good; fees for those who take without contributing [^m20] Part 3; [^man] §2.4.1 | Bridge 1, the share of every payment; yearly dues | ✅ Backs it, and suggests more | ❓ Dues that fall with contribution: who lives and works there pays less than an absent owner |
| Thermodynamic accounting; thresholds and allocations | The public record of what is measured on the land (the slides' "Libro C"); the Constitution's limits (07 G-11) | ✅ Backs it | Measure water, soil and energy directly; don't turn them into a price first |
| Local resilient communities fail without wider structures [^k14] ch. 7 | A neighbourhood of lot owners that only looks inward | 🧨 Questions it | Share designs and rules with other nodes; ❓ a reciprocity licence for the kit (doc 25) |
| Small-scale ownership of land as a step in the transition; community land trusts [^k14] ch. 9 | Private lots next to the commons (doc 31) | 🟡 Mild support | Their weight is on the trust, not on the lots |
| Partner state | The municipality recognising the Foundation and the consortium | ✅ Backs it | Take it to the conversation with Mainqué |
| Warning that elites capture ledgers unless they are designed for the commons [^m20] Conclusion | Hadron as the rail; Tether as investor | 🟡 Caution | Supports "no exclusivity, two separate conversations" |

## 4. What the texts don't give

- No token design: no supply, no price rule, no burn, no investor return.
- Almost nothing on land or on financing a physical commons, beyond the land-trust example.
- Nothing on Argentine law.
- The figures weren't read: they are images, including the doughnut, the four-quadrant model and the tables of the Manifesto.

## 5. Questions it leaves (07 K-11)

1. Do we write "funders have no voice over the commons" as a rule?
2. Dues and tolls that fall with contribution: yes or no?
3. Is mutual credit worth a model next to the prepaid FARO?
4. A reciprocity licence for the kit we give other nodes?
5. Which limits (water, built area, native cover) go into the public record, and who sets them?

## Sources & logic used

- The eight files attached to Franz's email "Bibliografia de Bauwens", 2026-11-16, converted to Markdown on 2026-11-19 with scripts (pandoc, poppler, one OCR pass), word counts checked against the originals. Full citations in the table of §1 and in each file's header.
- **How these notes were made:** each text was summarised into a structured digest during conversion; these notes are built from the digests. Section references point to where the digest places each idea. Nobody has yet read the eight texts line by line against these notes.
- Design pieces referred to: docs 25, 29, 31, 32, 34 and 07 (G-11, J-2, K).
- Logic: take each idea, find the piece of our design it touches, and say whether it supports it or argues against it [criterio].

[^mail]: Email from Franz, "Bibliografia de Bauwens", 2026-11-16.
[^seeds]: Bauwens & Jandrić (2021), "The Seeds of the Commons", *Postdigital Science and Education* 3:575–591, doi 10.1007/s42438-021-00218-8.
[^m20]: Manski & Bauwens (2020), *Frontiers in Blockchain* 2:29, doi 10.3389/fbloc.2019.00029 (CC BY). Copy in `sources/bauwens/`.
[^man]: Bauwens, Kostakis & Pazaitis (2019), *Peer to Peer: The Commons Manifesto*, University of Westminster Press, doi 10.16997/book33.
[^k14]: Kostakis & Bauwens (2014), *Network Society and Future Scenarios for a Collaborative Economy*, Palgrave Macmillan, doi 10.1057/9781137406897.
[^gti]: Bauwens (2022), "The Blockchain Revolution", GTI Forum "Technology and the Future", Great Transition Initiative.
[^figs]: "P2P Accountability Figures", working file of figures and boxes (author and year not stated in the file).
