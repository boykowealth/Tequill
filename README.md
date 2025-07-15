# Welcome To Tequill

**Tequill** is a desktop-based markdown notebook engineered for professionals in quantitative finance, academia, and technical fields. Built with PySide6 and QtWebEngine, it combines structured writing, math rendering, and clean exporting, all in one local-first interface. With full Markdown and LaTeX support, Tequill is ideal for research notes, whitepaper drafting, strategy documentation, and reproducible thought capture.

---

## Core Features

### Structured Markdown Editing
A clean, distraction-free editor built on `QTextEdit`, optimized for Markdown syntax. Write faster with formatting flexibility and immediate rendering support.

### Live Preview with MathJax
Render content in real time with a built-in `QWebEngineView`. Full LaTeX integration via MathJax enables inline and block equations, no external compilation required.

### Session Management
Each notebook is a self-contained session. Sessions can be created, renamed, deleted, or quickly reopened from a persistent sidebar manager.

### Multi-Format Exporting
Export notebooks to:
- **HTML** (with MathJax embedding)
- **PDF** (print-quality via Qt’s native rendering)
- **Markdown (.md)** (raw content for Git workflows or future automation)

All exports retain mathematical fidelity and formatting consistency.

### Customizable UI Panels
- Hide or reveal the **notebook manager** with a single toggle  
- Adjustable **split panels** allow flexible focus on editing vs. rendered view  
- Clean light-mode stylesheet designed for technical clarity and typographic comfort

---

## Built for Professionals

Tequill is not a note-taking toy. It's designed for:

- **Academics & Researchers**: Draft research notes, literature reviews, and papers with real math support.
- **Quantitative Analysts**: Document model assumptions, derivations, and results.
- **Engineers & Developers**: Maintain internal documentation, technical design notes, or blog-ready content.
- **Knowledge Architects**: Structure thoughts, export to clean formats, and retain control over content lifecycle.

---

## Under the Hood

- **Framework**: PySide6 (Qt for Python)  
- **Rendering Engine**: QtWebEngine (Chromium-based)  
- **Markdown Parser**: `markdown2`  
- **Math Typesetting**: MathJax v3 (LaTeX)  
- **Export Engine**: Native Qt PDF and HTML output  

---

## Local-First, Offline-Ready

Tequill is fully offline. Your content remains local and private — ideal for secure environments, finance institutions, or research workflows where data compliance and intellectual property control matter.

---

## Philosophy

*"Clarity precedes mastery."*  

Tequill is designed around the principle that structured thought is the foundation of high-leverage work. Whether you're modeling derivatives or composing a thesis, your tools should respect your process, not get in the way of it.
