# Hi, I'm Ameyanagi

I build scientific software, developer tools, and AI-assisted products across Rust, TypeScript, Python, and WebAssembly.

My work spans scientific computing and X-ray spectroscopy, multilingual search, Rust developer tools, and AI-assisted safety and compliance products.

## Current public work

| Project | Stack | What it is | Links |
|---------|-------|------------|-------|
| [ruviz](https://github.com/Ameyanagi/ruviz) | Rust, Python, TypeScript | High-performance 2D and 3D plotting with matplotlib-style ergonomics and a `wgpu` renderer | [Demo](https://youtu.be/6MT_hu8xpjo) · [Rust](https://crates.io/crates/ruviz) · [Python](https://pypi.org/project/ruviz/) · [npm](https://www.npmjs.com/package/ruviz) |
| [Yuru](https://github.com/Ameyanagi/yuru) | Rust | Fast CJK-aware fuzzy finder with Japanese romaji, Chinese pinyin, Korean phonetic search, and fzf-style shell integration | [Demo](https://youtu.be/_RyVr3VLULo) · [Releases](https://github.com/Ameyanagi/yuru/releases/latest) |
| [refeff](https://github.com/Ameyanagi/refeff) | Rust | From-scratch, safe-Rust FEFF10-compatible engine and CLI for EXAFS, XANES, RIXS, EELS, and related spectra | [Library](https://crates.io/crates/refeff) · [CLI](https://crates.io/crates/refeff-cli) |
| [aibo](https://github.com/Ameyanagi/aibo) | Rust | Hotkey-summoned, context-aware AI panel for macOS and Windows, with provider routing, dictation, file search, and agent runs | [Releases](https://github.com/Ameyanagi/aibo/releases/latest) |
| [xraytsubaki](https://github.com/Ameyanagi/xraytsubaki) | Rust | Fast XAS/XAFS analysis for large datasets, with parallel processing, fitting, plotting, and a desktop application | [Repository](https://github.com/Ameyanagi/xraytsubaki) |
| [ondotori-ble](https://github.com/Ameyanagi/ondotori-ble) | Python | Typed APIs for receiving selected T&D Ondotori sensor advertisements over Bluetooth Low Energy | [Documentation](https://ameyanagi.github.io/ondotori-ble/) · [PyPI](https://pypi.org/project/ondotori-ble/) |

## Project demos

<table>
  <tr>
    <td width="33%" align="center">
      <a href="https://youtu.be/_RyVr3VLULo">
        <img src="https://raw.githubusercontent.com/Ameyanagi/yuru/main/docs/assets/yuru-demo.gif" alt="Animated Yuru terminal demo" width="260" />
      </a>
      <br /><strong><a href="https://github.com/Ameyanagi/yuru">Yuru</a></strong><br />CJK phonetic fuzzy search in the terminal
    </td>
    <td width="33%" align="center">
      <a href="https://youtu.be/6MT_hu8xpjo">
        <img src="https://raw.githubusercontent.com/Ameyanagi/ruviz/main/docs/assets/gallery/rust/3d/surface3d_orbit.gif" alt="Animated ruviz 3D surface demo" width="260" />
      </a>
      <br /><strong><a href="https://github.com/Ameyanagi/ruviz">ruviz</a></strong><br />Publication-grade plotting in Rust
    </td>
    <td width="33%" align="center">
      <a href="https://youtu.be/kGLp1Vifssc">
        <img src="https://img.youtube.com/vi/kGLp1Vifssc/hqdefault.jpg" alt="Watch the KYTLab demo" width="260" />
      </a>
      <br /><strong><a href="https://github.com/Ameyanagi/KYTLab">KYTLab</a></strong><br />AI-assisted hazard prediction training
    </td>
  </tr>
</table>

## Products and applications

| Project | What it is | Links |
|---------|------------|-------|
| [Morphous](https://github.com/Ameyanagi/morphos) | Catalog of nature-inspired design systems, generated motif assets, and shadcn/tweakcn theme exports | [Live catalog](https://morphos.ameyanagi.com/) |
| [WebXrayDB](https://github.com/Ameyanagi/webxraydb-rs) | Browser and desktop X-ray reference database with attenuation, scattering, optics, and sample-preparation calculators | [Web app](https://webxraydb-rs.ameyanagi.com/) · [Desktop releases](https://github.com/Ameyanagi/webxraydb-rs/releases/latest) |
| [KYTLab](https://github.com/Ameyanagi/KYTLab) | Collaborative hazard prediction training with GPT-assisted coaching and generated training scenes | [Demo](https://youtu.be/kGLp1Vifssc) |
| [TagRune](https://tagrune.rxx.jp/) | AI tagging workflow built around a Rust API, queue workers, object storage, and a TanStack Start UI | [Product](https://tagrune.rxx.jp/) |
| [Cadence Note](https://cadence.rxx.jp/) | Personal-first task manager built with TanStack Start, Elysia, Drizzle, PostgreSQL, and worker queues | [Product](https://cadence.rxx.jp/) |

## Packages and project families

<details>
<summary><strong>refeff</strong> — pure-Rust FEFF10-compatible spectroscopy stack</summary>

| Published crate | Role |
|-----------------|------|
| [`refeff`](https://crates.io/crates/refeff) | Typed application-facing facade |
| [`refeff-cli`](https://crates.io/crates/refeff-cli) | CLI and FEFF-compatible executables |
| [`refeff-engine`](https://crates.io/crates/refeff-engine) | Embeddable computation pipeline without CLI dependencies |
| [`refeff-core`](https://crates.io/crates/refeff-core) | Numerical kernels |
| [`refeff-io`](https://crates.io/crates/refeff-io) | FEFF input, output, and handoff file formats |
| [`refeff-linalg`](https://crates.io/crates/refeff-linalg) | `faer`-backed linear algebra bridge |

</details>

<details>
<summary><strong>ruviz</strong> — plotting across Rust, Python, browsers, and native GUIs</summary>

- Core distributions: [crates.io](https://crates.io/crates/ruviz), [PyPI](https://pypi.org/project/ruviz/), and [npm](https://www.npmjs.com/package/ruviz).
- Browser runtime: [`ruviz-web`](https://crates.io/crates/ruviz-web).
- Native adapters: [`ruviz-gpui`](https://crates.io/crates/ruviz-gpui), [`ruviz-egui`](https://crates.io/crates/ruviz-egui), [`ruviz-iced`](https://crates.io/crates/ruviz-iced), and [`ruviz-slint`](https://crates.io/crates/ruviz-slint).

</details>

<details>
<summary><strong>Yuru</strong> — phonetic fuzzy search as composable Rust crates</summary>

| Published crate | Role |
|-----------------|------|
| [`yuru`](https://crates.io/crates/yuru) | Shell-facing fuzzy finder |
| [`yuru-core`](https://crates.io/crates/yuru-core) | Matching and ranking engine |
| [`yuru-ja`](https://crates.io/crates/yuru-ja) | Japanese romaji and kana support |
| [`yuru-zh`](https://crates.io/crates/yuru-zh) | Chinese pinyin support |
| [`yuru-ko`](https://crates.io/crates/yuru-ko) | Korean Hangul support |
| [`yuru-tui`](https://crates.io/crates/yuru-tui) | Terminal interface |

</details>

<details>
<summary><strong>Aibo</strong> — desktop AI application workspace</summary>

Aibo is distributed as [macOS and Windows releases](https://github.com/Ameyanagi/aibo/releases/latest). Its internal Rust crates are intentionally unpublished and separate the domain model, model providers, platform integrations, session orchestration, storage, tools, agent loop, and `iced` UI.

</details>

<details>
<summary><strong>X-ray and scientific Rust ecosystem</strong></summary>

| Project | Packages and role |
|---------|-------------------|
| [xraytsubaki](https://github.com/Ameyanagi/xraytsubaki) | Source workspace for XAS analysis, desktop UI, and in-development Python bindings; optionally uses `refeff`, `feff10`, and `ruviz` |
| [feff10-rs](https://github.com/Ameyanagi/feff10-rs) | Fortran-backed FEFF10 integration: [`feff10`](https://crates.io/crates/feff10), [`feff10-cli`](https://crates.io/crates/feff10-cli), [`feff10-sys`](https://crates.io/crates/feff10-sys), and [Python bindings](https://pypi.org/project/feff10-rs/) |
| [xraydb-rs](https://github.com/Ameyanagi/xraydb-rs) | Elemental X-ray data: [`xraydb`](https://crates.io/crates/xraydb) and [`xraydb-data`](https://crates.io/crates/xraydb-data) |
| [chemical-formula-rs](https://github.com/Ameyanagi/chemical-formula-rs) | Formula and composition parsing for [Rust](https://crates.io/crates/chemical-formula), [Python](https://pypi.org/project/chemical-formula-rs/), and [npm](https://www.npmjs.com/package/@ameyanagi/chemical-formula) |
| [baselines](https://github.com/Ameyanagi/baselines) | 1D and 2D baseline correction with pybaselines parity and optional GPU kernels; [published crate](https://crates.io/crates/baselines) |
| [lmopt](https://github.com/Ameyanagi/lmopt) | Source workspace for Levenberg-Marquardt nonlinear least-squares optimization using `faer` |
| [RSpin](https://github.com/Ameyanagi/RSpin) | Unpublished NMR workspace: facade, core, IO, processing, analysis, simulation, prediction, and WebAssembly bindings |

`feff10-rs` wraps the original FEFF10 Fortran implementation; `refeff` is a separate from-scratch Rust implementation. RSpin and `lmopt` are not currently published on crates.io.

</details>

<details>
<summary><strong>Safety, risk assessment, and regulatory data</strong></summary>

| Project | Published artifact | Focus |
|---------|--------------------|-------|
| [ra-library](https://github.com/Ameyanagi/ra-library) | [PyPI](https://pypi.org/project/ra-library/) | Explainable chemical risk calculations and recommendations |
| [ra-law-db](https://github.com/Ameyanagi/ra-law-db) | [PyPI](https://pypi.org/project/ra-law-db/) · bundled SQLite | Japanese chemical-law screening and public regulatory data |
| [ra-bio](https://github.com/Ameyanagi/ra-bio) | [PyPI](https://pypi.org/project/ra-bio/) · bundled SQLite | Microorganism, biosafety, and regulatory references |
| [risk_assessment_list](https://github.com/Ameyanagi/risk_assessment_list) | Source and SQLite data | Experimental obligation-list, GHS, and mixture screening |

</details>

<details>
<summary><strong>Earlier XAS tools and datasets</strong></summary>

[mucaljs](https://github.com/Ameyanagi/mucaljs) ·
[xasanalysis](https://github.com/Ameyanagi/xasanalysis) ·
[xasalign](https://github.com/Ameyanagi/xasalign) ·
[xasref](https://github.com/Ameyanagi/xasref) ·
[IBR-AIC](https://github.com/Ameyanagi/IBR-AIC) ·
[DecomNano](https://github.com/Ameyanagi/DecomNano) ·
[crowpeas](https://github.com/Ameyanagi/crowpeas) ·
[cif-parser](https://github.com/Ameyanagi/cif-parser)

</details>

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
