# Hi, I'm Ameyanagi

I build scientific software, developer tools, and AI-assisted products in Rust, Python, TypeScript, WebAssembly, and Mojo.

[Projects](#projects) · [npm](#npm) · [PyPI](#pypi) · [Rust crates](#rust-crates) · [Demos](#project-demos) · [All repositories](https://github.com/Ameyanagi?tab=repositories)

## Projects

### Scientific software

| Project | Stack | What it is | Links |
| --- | --- | --- | --- |
| <img src="https://raw.githubusercontent.com/Ameyanagi/rexafs/main/assets/brand/rexafs-icon.png" alt="" width="20" /> [rexafs](https://github.com/Ameyanagi/rexafs) | Rust, Python, TypeScript | XAS/EXAFS analysis with normalization, background removal, Fourier transforms, path fitting, and a desktop application | [Website](https://rexafs.com/) · [Docs](https://rexafs.com/docs/getting-started/) · [Desktop releases](https://github.com/Ameyanagi/rexafs/releases/latest) |
| <img src="https://raw.githubusercontent.com/Ameyanagi/refeff/main/assets/refeff-icon.png" alt="" width="20" /> [refeff](https://github.com/Ameyanagi/refeff) | Rust, WebAssembly | Safe-Rust port of FEFF10 for EXAFS, XANES, and related X-ray spectra, with a CLI and embeddable computation engine | [v0.3.0](https://github.com/Ameyanagi/refeff/releases/tag/v0.3.0) · [crates.io](https://crates.io/crates/refeff) · [Docs](https://docs.rs/refeff) |
| [feff10-rs](https://github.com/Ameyanagi/feff10-rs) | Rust, Python, Fortran | FEFF10 integration with Rust and Python APIs, a CLI, and a C interface | [crates.io](https://crates.io/crates/feff10) · [PyPI](https://pypi.org/project/feff10-rs/) · [Releases](https://github.com/Ameyanagi/feff10-rs/releases/latest) |
| <img src="https://raw.githubusercontent.com/Ameyanagi/ruviz/main/docs/assets/logo/ruviz-logo-32.png" alt="" width="20" /> [ruviz](https://github.com/Ameyanagi/ruviz) | Rust, Python, TypeScript | 2D and 3D plotting with 29 core plot types, publication figures, notebook widgets, and interactive browser controls | [Demo](https://youtu.be/6MT_hu8xpjo) · [v0.14.1](https://github.com/Ameyanagi/ruviz/releases/tag/v0.14.1) · [Rust](https://crates.io/crates/ruviz) · [Python](https://pypi.org/project/ruviz/) · [npm](https://www.npmjs.com/package/ruviz) |
| <img src="https://raw.githubusercontent.com/Ameyanagi/baselines/main/docs/assets/branding/baselines-icon-midnight-hex-v2.png" alt="" width="20" /> [baselines](https://github.com/Ameyanagi/baselines) | Rust, Python, WebAssembly | Baseline correction for signals, spectra, and 2D surfaces, with optional GPU kernels | [crates.io](https://crates.io/crates/baselines) · [PyPI](https://pypi.org/project/baselines-rs/) · [npm](https://www.npmjs.com/package/baselines-rs) · [Demo](https://youtu.be/nAsXHbcthLA) |
| <img src="https://raw.githubusercontent.com/Ameyanagi/webxraydb-rs/main/assets/icon-512.png" alt="" width="20" /> [WebXrayDB](https://github.com/Ameyanagi/webxraydb-rs) | Rust, TypeScript | Browser and desktop X-ray reference tools for attenuation, scattering, optics, and XAS sample preparation | [Web app](https://webxraydb-rs.ameyanagi.com/) · [Demo](https://youtu.be/tt1Y-5KL51Q) · [Desktop releases](https://github.com/Ameyanagi/webxraydb-rs/releases/latest) |
| <img src="https://raw.githubusercontent.com/Ameyanagi/xraydb-rs/main/assets/icon-512.png" alt="" width="20" /> [xraydb-rs](https://github.com/Ameyanagi/xraydb-rs) | Rust, WebAssembly | Elemental X-ray reference data: absorption edges, emission lines, and cross-sections | [crates.io](https://crates.io/crates/xraydb) · [npm](https://www.npmjs.com/package/xraydb-wasm) |
| [chemical-formula-rs](https://github.com/Ameyanagi/chemical-formula-rs) | Rust, Python, WebAssembly | Chemical formula and composition parsing, including nested formulas and weight percentages | [crates.io](https://crates.io/crates/chemical-formula) · [PyPI](https://pypi.org/project/chemical-formula-rs/) · [npm](https://www.npmjs.com/package/@ameyanagi/chemical-formula) |
| [DiCE](https://github.com/Ameyanagi/DiCE) | Rust, Python | Differentiable reaction kinetics, reactor simulation, global fitting, and uncertainty analysis; in development | [Source](https://github.com/Ameyanagi/DiCE) |
| [RSpin](https://github.com/Ameyanagi/RSpin) | Rust, WebAssembly | NMR library workspace for spectrum IO, processing, analysis, simulation, and prediction | [Source](https://github.com/Ameyanagi/RSpin) |
| [lmopt](https://github.com/Ameyanagi/lmopt) | Rust | Levenberg-Marquardt nonlinear least-squares optimization using faer | [Source](https://github.com/Ameyanagi/lmopt) |
| [ondotori-ble](https://github.com/Ameyanagi/ondotori-ble) | Python | Typed BLE advertisement APIs for selected T&amp;D Ondotori sensors | [PyPI](https://pypi.org/project/ondotori-ble/) · [Docs](https://ameyanagi.github.io/ondotori-ble/) |
| [spdist](https://github.com/Ameyanagi/spdist) | Rust, Python | Distance metrics for comparing curves and measured spectra | [PyPI](https://pypi.org/project/spdist/) |

`feff10-rs` wraps the original FEFF10 Fortran implementation; `refeff` translates and adapts that implementation into safe Rust. rexafs supports fitting in Rust and the desktop application; its Python and JavaScript/Wasm bindings expose spectrum processing.

### Developer and document tools

| Project | Stack | What it is | Links |
| --- | --- | --- | --- |
| <img src="https://raw.githubusercontent.com/Ameyanagi/yuru/main/docs/assets/yuru-icon.svg" alt="" width="20" /> [Yuru](https://github.com/Ameyanagi/yuru) | Rust | Fast CJK-aware fuzzy finder with Japanese, Chinese, and Korean phonetic search plus Bash, Zsh, Fish, PowerShell, and Clink integration | [Demo](https://youtu.be/_RyVr3VLULo) · [v0.2.3](https://github.com/Ameyanagi/yuru/releases/tag/v0.2.3) · [crates.io](https://crates.io/crates/yuru) |
| <img src="https://raw.githubusercontent.com/Ameyanagi/aibo/main/assets-src/aibo-icon-1024.png" alt="" width="20" /> [aibo](https://github.com/Ameyanagi/aibo) | Rust | Hotkey-summoned, context-aware AI panel for macOS and Windows, with provider routing, dictation, file search, and agent runs | [Releases](https://github.com/Ameyanagi/aibo/releases/latest) |
| [EasyPPTX](https://github.com/Ameyanagi/easypptx) | Python | AI-friendly PowerPoint generation with grid and Deck builders, Markdown conversion, auto-pagination, themes, and table style presets | [Demo](https://github.com/user-attachments/assets/84bd2754-854c-41f9-a21c-9e096971a6d4) · [v0.11.0](https://github.com/Ameyanagi/easypptx/releases/tag/0.11.0) · [PyPI](https://pypi.org/project/EasyPPTX/) |
| [ClaudeSlide](https://github.com/Ameyanagi/ClaudeSlide) | TypeScript | CLI and library for editing PowerPoint files through OOXML | [npm](https://www.npmjs.com/package/claudeslide) · [Examples](https://github.com/Ameyanagi/claudeslide_example) |
| [LLMRateLimiter](https://github.com/Ameyanagi/LLMRateLimiter) | Python | Distributed LLM API rate limiting with Redis-backed FIFO queues and token/request budgets | [PyPI](https://pypi.org/project/LLMRateLimiter/) · [Docs](https://ameyanagi.github.io/LLMRateLimiter/) |
| [agenting](https://github.com/Ameyanagi/agenting) | TypeScript | CLI for generating managed AGENTS.md and CLAUDE.md instructions | [Source](https://github.com/Ameyanagi/agenting) |

### Safety and risk data

| Project | What it is | Links |
| --- | --- | --- |
| <img src="https://raw.githubusercontent.com/Ameyanagi/phoenix-chem/main/assets/logo.png" alt="" width="20" /> [PHOENIX](https://github.com/Ameyanagi/phoenix-chem) | Reactive chemical hazard screening with thermodynamic estimation, CHETAH-style screening, and decomposition analysis | [PyPI](https://pypi.org/project/phoenix-chem/) · [Docs](https://ameyanagi.github.io/phoenix-chem/) |
| <img src="https://raw.githubusercontent.com/Ameyanagi/ra-library/main/assets/logo.png" alt="" width="20" /> [ra-library](https://github.com/Ameyanagi/ra-library) | Explainable chemical risk calculations and recommendations | [PyPI](https://pypi.org/project/ra-library/) |
| <img src="https://raw.githubusercontent.com/Ameyanagi/ra-law-db/main/assets/logo.png" alt="" width="20" /> [ra-law-db](https://github.com/Ameyanagi/ra-law-db) | Japanese chemical-law screening with a bundled public regulatory dataset | [PyPI](https://pypi.org/project/ra-law-db/) |
| <img src="https://raw.githubusercontent.com/Ameyanagi/ra-bio/main/assets/logo.png" alt="" width="20" /> [ra-bio](https://github.com/Ameyanagi/ra-bio) | Microorganism risk, biosafety, and regulatory reference data | [PyPI](https://pypi.org/project/ra-bio/) |
| [safety-tool-contracts](https://github.com/Ameyanagi/safety-tool-contracts) | Shared response envelopes, tool manifests, audit sanitization, and comparison contracts for safety tools | [Source](https://github.com/Ameyanagi/safety-tool-contracts) |
| [risk_assessment_list](https://github.com/Ameyanagi/risk_assessment_list) | Experimental Japanese obligation-list, GHS, and mixture screening tools | [Source](https://github.com/Ameyanagi/risk_assessment_list) |

PHOENIX supports screening; experimental validation is required for safety decisions.

### Applications

| Project | What it is | Links |
| --- | --- | --- |
| <img src="https://raw.githubusercontent.com/Ameyanagi/morphos/main/src/logo.svg" alt="" width="20" /> [Morphous](https://github.com/Ameyanagi/morphos) | Catalog of nature-inspired design systems, generated motif assets, and shadcn/tweakcn theme exports | [Live catalog](https://morphos.ameyanagi.com/) |
| [Asaborake](https://github.com/Ameyanagi/Asaborake) | Commercial detection, cutting, and transcoding for Japanese broadcast recordings, with a web UI and EPGStation integration | [Source](https://github.com/Ameyanagi/Asaborake) |
| [KYTLab](https://github.com/Ameyanagi/KYTLab) | Collaborative hazard prediction training with guided sessions, AI coaching, and generated training scenes | [Source](https://github.com/Ameyanagi/KYTLab) · [Demo](https://youtu.be/kGLp1Vifssc) |
| [Yoshikosan](https://github.com/Ameyanagi/Yoshikosan) | Workplace safety application for digital pointing-and-calling checks and SOP workflows | [Source](https://github.com/Ameyanagi/Yoshikosan) |
| [Yoshitomo](https://github.com/Ameyanagi/Yoshitomo) | Workplace safety application built with the T3 Stack and Bun | [Source](https://github.com/Ameyanagi/Yoshitomo) |
| <img src="https://tagrune.rxx.jp/logo.svg" alt="" width="20" /> [TagRune](https://tagrune.rxx.jp/) | AI tagging workflow built around a Rust API, queue workers, object storage, and a TanStack Start UI | [Product](https://tagrune.rxx.jp/) |
| <img src="https://cadence.rxx.jp/favicon.svg" alt="" width="20" /> [Cadence Note](https://cadence.rxx.jp/) | Personal-first task manager built with TanStack Start, Elysia, Drizzle, PostgreSQL, and worker queues | [Product](https://cadence.rxx.jp/) |

### Templates and agent skills

| Project | Type | Focus |
| --- | --- | --- |
| [cobalt-stack](https://github.com/Ameyanagi/cobalt-stack) | Application template | Rust Axum backend and Next.js frontend |
| [tanstack-start-fastapi-template](https://github.com/Ameyanagi/tanstack-start-fastapi-template) | Application template | TanStack Start and shadcn/ui frontend with a FastAPI backend |
| [tanstack-start-elysia](https://github.com/Ameyanagi/tanstack-start-elysia) | Agent skill | Scaffolds TanStack Start, shadcn/ui, and ElysiaJS applications |
| [tanstack-start-fastapi](https://github.com/Ameyanagi/tanstack-start-fastapi) | Agent skill | Scaffolds TanStack Start, shadcn/ui, and FastAPI applications |
| [ameyanagi-template](https://github.com/Ameyanagi/ameyanagi-template) | Repository template | Rust project template |

### Experimental Mojo libraries

Libraries for CJK search, text, graphics, and scientific computing, distributed through the [Mojo package channel](https://ameyanagi.github.io/mojo-channel/).

| Project | Focus |
|---------|-------|
| [yuragi](https://github.com/Ameyanagi/yuragi) | CJK-aware fuzzy finder |
| [yomi](https://github.com/Ameyanagi/yomi) | CJK phonetic representations and readings |
| [sen](https://github.com/Ameyanagi/sen) | Scientific plotting |
| [nerai](https://github.com/Ameyanagi/nerai) | Optimization and nonlinear least squares |
| [shuhafft](https://github.com/Ameyanagi/shuhafft) | Production-quality fast Fourier transforms |
| [mojotui](https://github.com/Ameyanagi/mojotui) | Composable terminal user interfaces |
| [akari](https://github.com/Ameyanagi/akari) | Color science, palettes, and scientific colormaps |
| [nagare](https://github.com/Ameyanagi/nagare) | Interpolation and spline algorithms |
| [kagerou](https://github.com/Ameyanagi/kagerou) | Low-level native 2D rendering |
| [hibana](https://github.com/Ameyanagi/hibana) | High-performance fuzzy matching |
| [nami](https://github.com/Ameyanagi/nami) | Scientific signal processing |
| [moji](https://github.com/Ameyanagi/moji) | Unicode text, search, and layout primitives |
| [kumihan](https://github.com/Ameyanagi/kumihan) | Validated OpenType parsing and renderer-neutral text shaping foundations |
| [mojo-channel](https://github.com/Ameyanagi/mojo-channel) | Interim package channel for the experimental Mojo ecosystem |

## Published packages

Published versions checked on **2026-09-13**. npm and PyPI entries link to the published package and its source repository.

### npm

| Package | Version | Purpose | Repository |
| --- | --- | --- | --- |
| [@ameyanagi/chemical-formula](https://www.npmjs.com/package/@ameyanagi/chemical-formula) | 0.1.3 | Chemical formula and composition parsing | [Source](https://github.com/Ameyanagi/chemical-formula-rs) |
| [baselines-rs](https://www.npmjs.com/package/baselines-rs) | 0.1.2 | Baseline correction for signals and surfaces | [Source](https://github.com/Ameyanagi/baselines) |
| [claudeslide](https://www.npmjs.com/package/claudeslide) | 1.4.1 | PowerPoint editing CLI | [Source](https://github.com/Ameyanagi/ClaudeSlide) |
| [rexafs](https://www.npmjs.com/package/rexafs) | 0.2.4 | XAS spectrum processing | [Source](https://github.com/Ameyanagi/rexafs) |
| [ruviz](https://www.npmjs.com/package/ruviz) | 0.14.1 | Plotting and interactive visualization | [Source](https://github.com/Ameyanagi/ruviz) |
| [xraydb-wasm](https://www.npmjs.com/package/xraydb-wasm) | 0.4.1 | X-ray reference database | [Source](https://github.com/Ameyanagi/xraydb-rs) |

### PyPI

| Package | Version | Purpose | Repository |
| --- | --- | --- | --- |
| [baselines-rs](https://pypi.org/project/baselines-rs/) | 0.1.1 | Baseline correction for signals and surfaces | [Source](https://github.com/Ameyanagi/baselines) |
| [chemical-formula-rs](https://pypi.org/project/chemical-formula-rs/) | 0.1.3 | Chemical formula and composition parsing | [Source](https://github.com/Ameyanagi/chemical-formula-rs) |
| [EasyPPTX](https://pypi.org/project/EasyPPTX/) | 0.11.0 | PowerPoint generation | [Source](https://github.com/Ameyanagi/easypptx) |
| [feff10-rs](https://pypi.org/project/feff10-rs/) | 0.2.3 | FEFF10 calculation bindings | [Source](https://github.com/Ameyanagi/feff10-rs) |
| [LLMRateLimiter](https://pypi.org/project/LLMRateLimiter/) | 0.3.2 | Distributed LLM API rate limiting | [Source](https://github.com/Ameyanagi/LLMRateLimiter) |
| [ondotori-ble](https://pypi.org/project/ondotori-ble/) | 0.1.0 | Ondotori BLE readings | [Source](https://github.com/Ameyanagi/ondotori-ble) |
| [phoenix-chem](https://pypi.org/project/phoenix-chem/) | 0.2.0 | Reactive chemical hazard screening | [Source](https://github.com/Ameyanagi/phoenix-chem) |
| [pptemp](https://pypi.org/project/pptemp/) | 0.1.0 | Simple PowerPoint helpers | [Source](https://github.com/Ameyanagi/pptemp) |
| [ra-bio](https://pypi.org/project/ra-bio/) | 0.2.1 | Microorganism risk-reference data | [Source](https://github.com/Ameyanagi/ra-bio) |
| [ra-law-db](https://pypi.org/project/ra-law-db/) | 0.5.2 | Japanese chemical-law screening data | [Source](https://github.com/Ameyanagi/ra-law-db) |
| [ra-library](https://pypi.org/project/ra-library/) | 0.4.1 | Chemical risk calculations | [Source](https://github.com/Ameyanagi/ra-library) |
| [rexafs](https://pypi.org/project/rexafs/) | 0.2.4 | XAS spectrum processing | [Source](https://github.com/Ameyanagi/rexafs) |
| [ruviz](https://pypi.org/project/ruviz/) | 0.14.1 | Plotting and interactive visualization | [Source](https://github.com/Ameyanagi/ruviz) |
| [spdist](https://pypi.org/project/spdist/) | 0.1.3 | Distance metrics for curves | [Source](https://github.com/Ameyanagi/spdist) |

### Rust crates

| Primary crate | Version | Companion crates |
| --- | --- | --- |
| [rexafs](https://crates.io/crates/rexafs) | 0.2.4 | — |
| [refeff](https://crates.io/crates/refeff) | 0.3.0 | [refeff-cli](https://crates.io/crates/refeff-cli) · [refeff-engine](https://crates.io/crates/refeff-engine) · [refeff-core](https://crates.io/crates/refeff-core) · [refeff-io](https://crates.io/crates/refeff-io) · [refeff-linalg](https://crates.io/crates/refeff-linalg) |
| [feff10](https://crates.io/crates/feff10) | 0.2.3 | [feff10-cli](https://crates.io/crates/feff10-cli) · [feff10-sys](https://crates.io/crates/feff10-sys) |
| [ruviz](https://crates.io/crates/ruviz) | 0.14.1 | [ruviz-web](https://crates.io/crates/ruviz-web) · [ruviz-gpui](https://crates.io/crates/ruviz-gpui) · [ruviz-egui](https://crates.io/crates/ruviz-egui) · [ruviz-iced](https://crates.io/crates/ruviz-iced) · [ruviz-slint](https://crates.io/crates/ruviz-slint) |
| [baselines](https://crates.io/crates/baselines) | 0.1.1 | — |
| [xraydb](https://crates.io/crates/xraydb) | 0.4.1 | [xraydb-data](https://crates.io/crates/xraydb-data) |
| [chemical-formula](https://crates.io/crates/chemical-formula) | 0.1.3 | — |
| [yuru](https://crates.io/crates/yuru) | 0.2.3 | [yuru-core](https://crates.io/crates/yuru-core) · [yuru-ja](https://crates.io/crates/yuru-ja) · [yuru-zh](https://crates.io/crates/yuru-zh) · [yuru-ko](https://crates.io/crates/yuru-ko) · [yuru-tui](https://crates.io/crates/yuru-tui) |

Versions in this table apply to the primary crate. Companion crates have their own release histories.

## Project demos

<div align="center">

<table width="100%">
  <tr>
    <td width="50%" align="center">
      <a href="https://github.com/Ameyanagi/yuru"><img src="https://raw.githubusercontent.com/Ameyanagi/yuru/main/docs/assets/yuru-icon.svg" alt="Yuru" width="32" /></a><br>
      <video src="https://github.com/user-attachments/assets/37f9643f-0ed1-4cca-8a15-c4a8bd78cf34" width="100%" controls></video>
    </td>
    <td width="50%" align="center">
      <a href="https://github.com/Ameyanagi/ruviz"><img src="https://raw.githubusercontent.com/Ameyanagi/ruviz/main/docs/assets/logo/ruviz-logo-32.png" alt="ruviz" width="32" /></a><br>
      <video src="https://github.com/user-attachments/assets/bce842b5-50d8-43e4-893d-074bf6738975" width="100%" controls></video>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <strong><a href="https://github.com/Ameyanagi/easypptx">EasyPPTX</a></strong><br>
      <video src="https://github.com/user-attachments/assets/84bd2754-854c-41f9-a21c-9e096971a6d4" width="100%" controls></video>
    </td>
    <td width="50%" align="center">
      <a href="https://github.com/Ameyanagi/webxraydb-rs"><img src="https://raw.githubusercontent.com/Ameyanagi/webxraydb-rs/main/assets/icon-512.png" alt="WebXrayDB" width="32" /></a><br>
      <video src="https://github.com/user-attachments/assets/6b8caac1-5e22-44de-bc75-cb99ba2d8a89" width="100%" controls></video>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <a href="https://github.com/Ameyanagi/baselines"><img src="https://raw.githubusercontent.com/Ameyanagi/baselines/main/docs/assets/branding/baselines-icon-midnight-hex-v2.png" alt="baselines" width="40" /></a><br>
      <video src="https://github.com/user-attachments/assets/2b3c97ec-e395-4c75-aa7f-aebec5f9a3f3" width="50%" controls></video>
    </td>
  </tr>
</table>

</div>

## Earlier projects and reference material

| Area | Repositories |
| --- | --- |
| XAS analysis and data | [xasanalysis](https://github.com/Ameyanagi/xasanalysis) · [xasalign](https://github.com/Ameyanagi/xasalign) · [xasrebin](https://github.com/Ameyanagi/xasrebin) · [xasref](https://github.com/Ameyanagi/xasref) · [IBR-AIC](https://github.com/Ameyanagi/IBR-AIC) |
| X-ray models and structures | [DecomNano](https://github.com/Ameyanagi/DecomNano) · [crowpeas](https://github.com/Ameyanagi/crowpeas) · [cif-parser](https://github.com/Ameyanagi/cif-parser) · [mucaljs](https://github.com/Ameyanagi/mucaljs) · [xraydb-api](https://github.com/Ameyanagi/xraydb-api) · [structure2feff](https://github.com/Ameyanagi/structure2feff) · [xafsutil](https://github.com/Ameyanagi/xafsutil) · [Webatoms-js](https://github.com/Ameyanagi/Webatoms-js) |
| Beamline workflows | [QASXRD](https://github.com/Ameyanagi/QASXRD) · [larchppt](https://github.com/Ameyanagi/larchppt) |
| Numerical experiments | [lmopt-rs](https://github.com/Ameyanagi/lmopt-rs) · [T-number](https://github.com/Ameyanagi/T-number) · [Gaussian_processes](https://github.com/Ameyanagi/Gaussian_processes) · [nngauss](https://github.com/Ameyanagi/nngauss) |
| Presentation tools and examples | [pptemp](https://github.com/Ameyanagi/pptemp) · [pptx-claude](https://github.com/Ameyanagi/pptx-claude) · [claudeslide_example](https://github.com/Ameyanagi/claudeslide_example) |
| Tutorials and reference material | [python-tutorial](https://github.com/Ameyanagi/python-tutorial) · [StructuredPy](https://github.com/Ameyanagi/StructuredPy) · [StructuredPy-code](https://github.com/Ameyanagi/StructuredPy-code) · [Install_Demeter](https://github.com/Ameyanagi/Install_Demeter) · [Aozora_bunko_list](https://github.com/Ameyanagi/Aozora_bunko_list) |

More experiments and source repositories are on [GitHub](https://github.com/Ameyanagi?tab=repositories).

## GitHub stats

<details>
<summary>Open metrics</summary>

<p align="center">
  <img src="/metrics-general.svg" alt="General metrics" />
</p>

<p align="center">
  <img src="/metrics-languages.svg" alt="Top languages" />
</p>

</details>
