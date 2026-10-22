# Translation and extraction notes

## Source type — a web page, not a paper

- **There is no paper for Dream-1.** The source document is the official Dream Labs web page **“Zero-Shot to New Robots: Introducing Dream-1”** (<https://dreamlabs.ai/research/dream-1/>; page label “Research . October 2026 · 10 min read”; byline “The Dream Labs team”). It is a product-launch / technical blog post, so there are no numbered sections, figures, tables, equations, appendices or a bibliography in the usual paper sense.
- `detailed_paper.md` is the main file. `paper.md` is a byte-identical copy.
- Context only, not translated here: `/workspace/dream1_research/src/wam.html` (the page’s WAM diagram embed), `dreamzero.pdf` / `dreamzero.txt` (DreamZero paper, which has its own reader in `World Action Models are Zero-shot Policies/`).

## Canonical source

- Saved HTML: `/workspace/dream1_research/src/dream1.html`, SHA256 `dc264c99de004796e0c1dd7fa5c682e6099dcb4df25d67ddfbff03fcfa63a5b8`.
- Live refetch on 2026-10-21 (UTC+8): HTTP 200, byte-identical to the saved copy.
- Embedded iframe pages fetched from the live site: `assets/chicken-and-egg.html`, `assets/robot-price-ladder.html`, `assets/wam.html`.
- Chart values come from the page’s inline `data-chart` JSON (5 charts: zero-shot Simulation / Real robots, capability YAM / YAM + UMI gripper, FaaS 12-robot chart). They are exact values, not read from pixels.

## Structure and anchors

- Reader order follows the page: Lead → 01 → 02 → 03 → 04 (04.1–04.5) → 05 → Notes and references (fn 1–6) → Cite this post.
- Each section links to its original page anchor (`#chicken-and-egg`, `#cambrian-explosion`, `#the-result`, `#introducing-dream-1`, `#get-started`, `#zero-shot`, `#how-it-works`, `#can-and-cant`, `#one-shot`, `#looking-forward`, `#footnotes`).
- The floating table of contents on the page uses shorter labels for three sections; the reader uses the in-body headings and notes the difference.
- Figure numbers 1–14 and table numbers 1–11 are **assigned by the reader**. The page does not number them.
- Paragraph labels restart in each major section. Footnotes use `Para. fn1` … `Para. fn6`.

## Figures, charts and videos

| Reader figure | Page element | Asset(s) | Form |
|---|---|---|---|
| Fig 1 | Launch video (01:59) | `assets/launch-still.webp` | video → poster still only |
| Fig 2 | Chicken-and-egg animated diagram (iframe) | `assets/render/chicken-and-egg.png` | rendered final frame; embedded text transcribed in caption |
| Fig 3 + Table 1 | Robot price ladder, 24 robots (iframe carousel) | `assets/render/robot-price-ladder.png`, `assets/price-ladder/*.webp` (24) | partial carousel snapshot; all 24 cards transcribed; card images decoded from embed |
| Fig 4a–b + Tables 2–3 | Unseen-task video wall (Beta testers 12 / In-house 18) | `assets/render/wall-*.png`, `assets/beta/*.jpg` (12), `assets/demo/*.jpg` (18) | videos → poster stills; instructions transcribed |
| Fig 5a–b + Tables 4–5 | Unseen-robot gallery (Simulation 27 / Real 21) | `assets/render/zs-gallery-*.png`, `assets/zero-shot/picks/*.jpg` (27), `assets/zero-shot/real_*.jpg` (21) | videos → poster stills; carousel snapshots |
| Fig 6a–b + Tables 6–7 | Zero-shot relative-to-YAM bar charts | `assets/render/zs-chart-*.png`, `assets/embodiments/rollouts/*.jpg` (28), real-chart previews | interactive chart rendered; values from `data-chart` |
| Fig 7 | “How a World Action Model works” animated diagram (iframe) | `assets/render/wam.png` | rendered mid-cycle frame; embedded text transcribed in caption |
| Fig 8 + Table 8 | Robocurve report (3 charts) | `assets/robocurve.webp` | **image only**; values read from the image |
| Fig 9a–b + Tables 9–10 | Unseen task generalization (YAM / YAM + UMI) | `assets/render/capability-*.png` | values ± se from `data-chart`; bucket counts computed from clip lists; **no caption on the page** (reader caption marked) |
| Fig 10 | Data-collection timelapse video (00:38) | `assets/dc-timelapse-poster.webp` | video → poster still |
| Fig 11a–d | Zero-shot vs. after-FaaS paired videos | `assets/faas/pair-*.jpg`, `assets/faas/real-makermods-*.jpg` | videos → poster stills |
| Fig 12a–b | After-FaaS far embodiments (Dexmate/Sharpa, YAM knife gripper) | `assets/faas/real-sharpa-ft.jpg`, `assets/faas/real-yam-strawberry-ft.jpg` | videos → poster stills |
| Fig 13 + Table 11 | Zero-shot vs. after FaaS, 12 robots | `assets/render/faas-chart.png`, `assets/faas/ft-*.jpg` (12) | interactive chart rendered; values from `data-chart` |
| Fig 14 | Dream-1 MicroDuck control video (00:16) | `assets/microduck-control-poster.jpg` | video → poster still |
| Code listing 1 | “Condensed client side code” | — | transcribed verbatim |

- 22 embedded image cards with bilingual captions; 165 files in `assets/` (129 page images, 12 renders, 24 price-ladder cards). Every image and local link resolves relative to `detailed_paper.md`.
- `assets/render/*` were captured with headless Chrome from the live page on 2026-10-21. Site navigation was hidden for the captures.
- There are no equations on the page. The two display formulas in the reader are reader-added arithmetic checks, marked “not in source”.

## Could not be extracted / limitations

- **Video content is not viewable in this reader.** None of the MP4s were downloaded or transcribed. This covers the launch video, 12 beta clips, 18 in-house clips, 27×(up to 5) simulation clips, 21 real-robot clips, chart-preview clips, about 450 capability rollout clips, the data-collection timelapse, the FaaS pairs/far-embodiment clips, and the Microduck video. The launch video’s narration/speech is not captured.
- Simulation gallery cards cycle through up to 5 picked rollouts; only the first pick’s poster is in the static HTML.
- The Robocurve figure is image-only. Labelled values (59, 48, 48, 47, 42, 36, 19, 10; $0.15; 1.4 min; 1.2×/16×; 1.3×/1.7×) were read from the image, and unlabelled scatter points cannot be identified.
- Animated diagrams (Figs 2, 7) are single frames of a looping animation. Their full text strings were extracted from the embed source.
- The price ladder is a scrolling carousel, so the render shows only part of it. Table 1 is complete.
- The page gives no model size, architecture details, training data, simulator name, full task lists for the 50/150-task simulated evaluations, or statistical protocol. None of this was inferred or added.

## Source inconsistencies preserved (not harmonized)

- The beta wall pager reads “1–13 of 13”, but the wall has 12 partner cards (“12 sites”).
- Capability chart titles vs. listed clips: YAM Push & slide 58/57; YAM + UMI Pour & scoop 52/51 and Open & close 57/56.
- Names vary across the page: “Franka Research 3, two arms” (gallery) vs. “Franka FR3, two arms” (chart); “Trossen” (FaaS chart) vs. “Trossen Workbench”; price-ladder names such as “reBot Arm B601-DM”, “ARX-5”, “YAM 7”, “R1-A5” vs. “reBot B601-DM”, “ARX X5”, “YAM-7”, “Unitree R1”.
- ROBO-T1 is in the FaaS chart but not in the 27-robot simulation list.
- The caption says “4 real robots”. The real-robot gallery also shows YAM + UMI, YAM + Enpire grippers and Vega 1 Pro + YAM Gripper.
- The FaaS chart’s y-axis is unlabeled beyond %. The text calls the metric the “language-following score”. Two of the 12 robots decrease (Bracket Bot 32→31, Unitree R1 42→31), which matches “ten of them”.
- Per-call cost: the page says “$0.0013 an action”, but the arithmetic is per call (1.6 s of actions). The reader keeps the page wording and notes the arithmetic.

## Translation policy

- Model, product, robot, company, dataset/benchmark and metric names stay in English (Dream-1, Dream-1-flash, FaaS, YAM, UMI, RoboDojo-RC Tier 1, Opus 5.5, Gemini 4 Argon, GPT-6 Astra, etc.). Robot task instructions are quoted verbatim in English. Chinese glosses are given for the in-house tasks and beta tasks.
- Claims, hedges (“may”, “early signs”, “one of the first”), numbers, prices, durations and speed-ups are kept exactly.
- Footnote bibliographic titles and URLs stay in English for searchability. The annotation text is translated.
- Omitted site chrome: navigation/menu, floating Contents widget, player controls, “Join us / We’re hiring / Come build with us” footer, copyright/location line.

## Quantitative coverage

- 50 bilingual pairs: Lead 7, 01 6, 02 3, 03 2, 04 1, 04.1 2, 04.2 3, 04.3 4, 04.4 7, 04.5 6, 05 3, footnotes 6.
- 22 caption pairs; 11 transcribed tables; 1 verbatim code listing; 1 verbatim BibTeX block.
