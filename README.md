# VIBE‑Lock

> **Vast Intelligence‑Based Extraction — Containment & Cognitive Sovereignty Toolkit**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) 
[![Stable Roadmap](https://img.shields.io/badge/roadmap-Q3_2025-orange.svg)](#roadmap)

Welcome to **VIBE‑Lock**, an open‑source implementation of the **VIBE Protocol** (see [`VIBE‑PROTOCOL.md`](./VIBE-PROTOCOL.md)) that defends your creative signal against silent AI extraction.  Think of VIBE‑Lock as a *developer shield*—CLI tools, libraries, and workflow recipes that watermark, timestamp, and obfuscate your code, text, and designs so they stay **yours**.



##  Why VIBE‑Lock?

Modern AI systems memorize fragments of everything they ingest—source code, business logic, UI screenshots, even your debugging sessions.  Without protection, your proprietary edge can resurface in somebody else’s model output.  VIBE‑Lock gives you practical, battle‑tested counter‑measures:

* **Cognitive Fingerprint Watermarking** – Embed stylistic n‑grams or zero‑width glyphs detectable with `vibe_scan`.
* **Temporal Proof‑of‑Origin (TPO)** – Create cryptographic timestamps & ledger entries for every artifact.
* **Obfuscation Layer** – AST transforms + entropy injection to confuse code‑scraping bots.
* **Screenshot Poisoning** – Invisible SVG & CSS noise to break “screenshot‑to‑HTML” reconstructions.
* **Consent‑Aware Prompt Wrappers** – Machine‑readable *Do Not Train* flags for IDE/CLI queries.
* **Distributed Cognitive Ledger** – Append‑only proof log (SQLite/IPFS/chain‑agnostic) for authorship audits.



##  Full Protocol Spec

For the philosophical underpinnings, threat model, and detailed component breakdown, read **[`VIBE‑PROTOCOL.md`](./VIBE-PROTOCOL.md)**.



##  Quick Start


# 1 Install the CLI
sed -i 's/pip install vibe-lock/python -m pip install -e ./g' README.md

# 2 Initialize a project ledger
vibe‑init  # creates .vibe/ with default config & TPO ledger

# 3 Watermark a source file
vibe‑stamp src/main.py  # embeds cognitive fingerprint & logs hash

# 4 Verify an artifact later
vibe‑scan build/output.txt  # reports watermark confidence & TPO match


> **Prerequisites:** Python ≥3.9, Git, OpenSSL.  Optional: Node ≥18 for the JIT CSS poisoning plugin.



##  Features

| Feature                                | Status | Notes                                                  |
| -------------------------------------- | ------ | ------------------------------------------------------ |
| `vibe‑stamp` Watermarker               | ✅      | Text & code watermarks à la Kirchenbauer et al. 2023   |
| `vibe‑init` Ledger bootstrap           | ✅      | Generates `.vibe/tpo_ledger.log` with Git commit hooks |
| Screenshot Poisoner (`vibe‑css‑cloak`) | 🟡     | Tailwind JIT noise generator (beta)                    |
| `vibe‑guard` Prompt Auditor            | 🟡     | Calculates drift score on export (due Q3 2025)         |
| Blockchain‑agnostic TPO plug‑in        | 🔜     | Pluggable driver for Ethereum, Solana, Filecoin        |

Legend: ✅  Stable 🟡 Beta 🔜 Planned



##  Roadmap

| Version | Milestone                                          | Target Date |
| ------- | -------------------------------------------------- | ----------- |
| **0.1** | CLI core (`vibe‑stamp`, `vibe‑scan`, ledger hooks) | **Q3 2025** |
| **0.2** | Chain‑agnostic TPO & on‑prem SQL backend           | Q4 2025     |
| **0.5** | Community red‑team audit & spec hardening          | Q1 2026     |
| **1.0** | Multi‑lang SDK, VS Code/Cursor plug‑ins            | 2026        |



##  Contributing

1. **Fork** the repo & create your feature branch (`git checkout -b feat/your‑feature`).
2. **Sign** the Developer Certificate of Origin (see `DCO.txt`).
3. **Commit** with signed‑off messages (`git commit -s -m "feat: ..."`).
4. **Open** a pull request describing your change & threat scenario.

All PRs must pass the `vibe‑scan` watermark integrity test and include unit tests ≥90% coverage.



##  License

MIT License with an *attribution‑preservation* clause covering cognitive fingerprint schemas.  See [`LICENSE`](./LICENSE) for details.



##  Acknowledgements

This project stands on the shoulders of:

* **Kirchenbauer et al.** – *A Watermark for Large Language Models* (2023)
* **Edwardsson & Al‑Saqaf** – *Content Provenance via Blockchain* (2024)
* **University of Chicago Glaze** – Artist style cloaking (2023)
* Community plaintiffs in **Doe v. GitHub** and **Getty v. Stability AI** – shining a light on vector echoes.



> **The vibe is mutual. The extraction is not.  Build your own shield.**
