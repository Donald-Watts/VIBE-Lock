# VIBE‑Lock

**Vast Intelligence‑Based Extraction — Containment & Cognitive Sovereignty Toolkit**



**License**: MIT  
**Status**: Alpha Preview — Stable Roadmap in Progress



Welcome to **VIBE‑Lock**, the open-source implementation of the [VIBE Protocol](./VIBE-PROTOCOL.md), a framework that defends your creative signal against silent AI extraction.

Think of VIBE‑Lock as a developer shield — a CLI toolchain, modular library, and protocol spec that watermark, timestamp, and obfuscate your code, text, and designs so they **stay yours**, even in collaborative AI-driven workflows.

> ⚠️ This project is experimental and under active development. Use at your own risk. Contributions are welcome.



##  Why VIBE‑Lock?
Modern AI systems memorize fragments of everything they ingest — source code, business logic, UI screenshots, and even debugging sessions. Your proprietary edge can resurface in someone else's model output.

**VIBE‑Lock counters this with practical, battle-tested defenses:**

- 🧠 **Cognitive Fingerprint Watermarking** — Embed stylistic n-grams or zero-width glyphs.
- ⏱ **Temporal Proof-of-Origin (TPO)** — Timestamp & log your artifact hashes.
- 🔀 **Obfuscation Layer** — Use AST transforms and entropy to confuse scrapers.
- 🖼 **Screenshot Poisoning** — Add SVG/CSS noise to block screenshot-to-code models.
- 🚫 **Consent-Aware Prompt Wrappers** — “Do Not Train” flags for CLI/IDE systems.
- 🧾 **Distributed Cognitive Ledger** — Append-only log (SQLite/IPFS/blockchain-ready).



##  Project Structure

vibe-lock/

├── vibe_stamp.py            # Watermarking logic

├── vibe_scan.py             # Fingerprint and TPO validator

├── vibe_init.py             # Ledger and project bootstrap

├── .vibe/                   # Proof-of-origin ledger

├── vibe_protocol.md         # Full protocol spec

├── setup.py                 # Installation entry point

└── README.md




## 🛠️ Installation
### Clone and Install Locally

git clone https://github.com/Donald-Watts/VIBE-Lock.git
cd VIBE-Lock
python -m pip install -e .


> Requires: Python ≥ 3.9, Git, OpenSSL



##  Quick Start
1. **Initialize a project ledger**  

vibe-init  # creates .vibe/ + ledger log


2. **Watermark a file**  

vibe-stamp src/main.py  # embeds fingerprint + hashes


3. **Verify later**  

vibe-scan build/output.txt  # confidence check + TPO match


> 🧪 Optionally enable screenshot noise with `vibe-css-cloak` (Node ≥18 required).



## 🔐 Agent-Compatible by Design
VIBE-Lock won’t interfere with AI workflows — it’s designed to:
- Enhance traceability of original logic
- Work in live environments like **Cursor**, **Replit**, or **Codespaces**
- Avoid adding unnecessary entropy to agentic AI indexing systems

Use VIBE-Lock *with* agents, not against them.



## ✅ Features
| Feature | Status | Notes |
|--------|--------|-------|
| `vibe-stamp` | ✅ | Code & text watermarks à la Kirchenbauer et al. (2023) |
| `vibe-init` | ✅ | Git-hook ready ledger bootstrap |
| Screenshot Poisoner | 🟡 | Tailwind JIT class cloaking (Beta) |
| `vibe-guard` | 🟡 | Drift auditor & prompt monitor (Q3 2025) |
| Chain-Agnostic TPO | 🔜 | Ethereum/Solana/Filecoin support |

Legend: ✅ Stable 🟡 Beta 🔜 Planned



##  Roadmap
| Version | Milestone | Target |
|---------|-----------|--------|
| 0.1     | CLI Core (`stamp`, `scan`, `init`) | Q3 2025 |
| 0.2     | Blockchain TPO & SQL backend       | Q4 2025 |
| 0.5     | Community red-team spec audit      | Q1 2026 |
| 1.0     | VS Code/Cursor SDK release         | 2026    |



##  Who This Is For
- Indie developers protecting project originality
- AI teams needing traceable builds
- Researchers embedding authorship metadata
- Creators who want public collaboration without silent replication



##  Contributing
1. Fork and create your feature branch:
  
   git checkout -b feat/your-feature
   
2. Sign the Developer Certificate of Origin (see `DCO.txt`)
3. Submit PRs with signed-off commits:
   
   git commit -s -m "feat: add fingerprint masking"
  
4. Pass `vibe-scan` and ≥90% unit test coverage to merge.



##  License
MIT License, with attribution-preservation clause on watermark schema.
See `LICENSE` for full details.



## 🪶 Acknowledgements
- **Kirchenbauer et al.** – A Watermark for LLMs (2023)
- **Edwardsson & Al-Saqaf** – Content Provenance via Blockchain (2024)
- **University of Chicago** – Glaze Artist Cloak (2023)
- **Plaintiffs** in Doe v. GitHub and Getty v. Stability AI

> _The vibe is mutual. The extraction is not._
> **Build your own shield.**

