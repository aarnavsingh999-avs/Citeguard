# Changelog — CiteGuard AI (Campus Helpdesk Assistant)

All notable changes to the **Campus Helpdesk Assistant** project for **SCSE4041 Mini Project** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-11-22 (Milestone 2 Final Delivery)

### Added
- **Production RAG Engine (`code/rag_engine.py`)**:
  - Implemented `PolicyCorpusParser` with hierarchical regex section splitting across all 4 policy handbooks.
  - Implemented `HybridRetriever` combining sublinear TF-IDF vectorization with domain keyword/entity overlap boosting.
  - Implemented Confidence Score Gate ($\tau = 0.15$) intercepting ungrounded queries before generation.
  - Implemented dual generation backend: native Google Gemini 1.5 Flash API with deterministic offline fallback ensuring 100% test reliability in sandboxed environments.
  - Implemented regex citation extractor verifying `[Doc: <doc>, Section: <sec>]` syntax.
- **Production Prompt (`prompts/final/P1_campus_helpdesk_final.txt`)**:
  - Enforced 4-part structured response schema: Direct Summary, Key Policy Provisions, Official Citations, Administrative Point of Contact.
  - Hardened adversarial prompt injection defense rejecting simulated administrative overrides (e.g., Dean roleplay).
- **Automated Evaluation Test Suite (`code/run_tests.py` & `test-data/test_inputs.json`)**:
  - 15 diverse benchmark test cases covering academic thresholds, financial penalties, UGC refund tiers, hostel curfews, IT quotas, out-of-scope queries, and jailbreaks.
  - Automated evaluation harness generating comprehensive report at `test-data/test_results.md`.
  - Achieved **100.0% Pass Rate (15/15)**, **100.0% Retrieval Recall**, **100.0% Refusal Accuracy**, **100.0% Citation Precision**, and **2.90 ms mean latency**.
- **Streamlit Web Application (`code/app.py`)**:
  - Interactive multi-tab web portal: Campus Q&A Assistant, Prompt Engineering Comparison Lab, Policy Corpus Explorer, Benchmark Runner, and Architecture Explorer.
  - Deployable on Streamlit Community Cloud and Hugging Face Spaces.
- **Architecture Diagram (`docs/architecture_diagram.png`)**:
  - Programmatically generated publication-quality vector schematic using `matplotlib`.
- **Programmatic PDF Builder (`code/generate_pdfs.py`)**:
  - Built using ReportLab with custom page-numbering canvas, professional typography, tables, and embedded architecture diagram.
  - Produced `docs/CiteGuardAI_TechnicalReport.pdf`.
  - Produced `docs/M2_[TEAM_ID]_CampusHelpdeskAssistant.pdf` and `docs/M2_T14_CampusHelpdeskAssistant.pdf`.

---

## [0.3.0] - 2026-11-12 (Milestone 2 Prompt Iterations)

### Added
- **Prompt Iteration `v2` (`prompts/v2/P1_grounded_citations.txt`)**:
  - Introduced explicit grounding instructions and citation tags `[Source: <Doc> §<Section>]`.
  - Drastically reduced factual hallucinations on known topics.
- **Prompt Iteration `v3` (`prompts/v3/P1_strict_refusal_format.txt`)**:
  - Enforced zero-tolerance hallucination rules.
  - Mandated exact standardized refusal string: `"I cannot answer this question based on official campus policies. Please contact the Campus Administration Desk at helpdesk@campus.edu or visit the Student Affairs Office."`
  - Eliminated polite speculative guessing on out-of-scope inquiries.

---

## [0.2.0] - 2026-11-05 (Milestone 2 Corpus & Parser Architecture)

### Added
- **Institutional Policy Handbooks (`code/policies/`)**:
  - `01_academic_and_exam_rules.md` (Code: `ACAD-REG-2024-V2`, Sections 1.1–1.5).
  - `02_fee_and_refund_policy.md` (Code: `FIN-REF-2024-V3`, Sections 2.1–2.4).
  - `03_hostel_and_mess_regulations.md` (Code: `HOST-REG-2024-V4`, Sections 3.1–3.5).
  - `04_library_and_it_services.md` (Code: `LIB-IT-2024-V2`, Sections 4.1–4.4).
- **Semantic Section Chunking**:
  - Replaced naive 500-token sliding windows with header-aware regex boundary extraction.
  - Bound metadata (document name, section ID, section title) permanently to text chunks.

---

## [0.1.0] - 2026-10-15 (Milestone 1 Baseline Prototype)

### Added
- Project ideation, problem formulation, and university regulatory audit.
- Baseline conversational prompt (`prompts/v1/P1_baseline.txt`).
- Initial exploratory retrieval tests with unconstrained LLM responses.
- Observed high hallucination rate on ungrounded queries, motivating Milestone 2 architecture.
