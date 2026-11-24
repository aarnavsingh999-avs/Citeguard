"""
CiteGuard AI - Architecture Diagram Generator
============================================
Generates high-resolution architecture diagram using matplotlib.
Output: docs/architecture_diagram.png

Developer: Aarnav Singh (S24CSEU1498)
Project: Campus Helpdesk Assistant (Milestone 2)
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

def draw_architecture_diagram():
    output_dir = Path(__file__).resolve().parent.parent / "docs"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "architecture_diagram.png"

    fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Background canvas
    fig.patch.set_facecolor("#0F172A") # Deep slate navy
    ax.set_facecolor("#0F172A")

    # Title Banner
    ax.text(50, 96, "CiteGuard AI — Campus Helpdesk Assistant Architecture", 
            fontsize=20, fontweight="bold", color="#F8FAFC", ha="center", va="center", fontfamily="sans-serif")
    ax.text(50, 92.5, "SCSE4041 Milestone 2 | Solo Developer: Aarnav Singh (S24CSEU1498) | Team: CiteGuard AI (T14)", 
            fontsize=11, color="#94A3B8", ha="center", va="center", fontfamily="sans-serif")

    # Layer Color Palette
    c_ingest = "#1E293B"      # Dark slate
    c_retrieve = "#0369A1"    # Cyan blue
    c_prompt = "#4338CA"      # Indigo
    c_llm = "#0D9488"         # Teal
    c_ui = "#B45309"          # Amber
    
    border_color = "#38BDF8"
    card_bg = "#1E293B"
    text_main = "#F1F5F9"
    text_sub = "#94A3B8"
    accent_green = "#10B981"
    accent_purple = "#818CF8"

    def draw_box(x, y, w, h, title, subtitle, details, bg_color="#1E293B", border="#38BDF8", title_color="#38BDF8"):
        # Shadow
        rect_shadow = patches.FancyBboxPatch((x+0.4, y-0.4), w, h, boxstyle="round,pad=0.6,rounding_size=1.2",
                                             facecolor="#020617", edgecolor="none", alpha=0.5)
        ax.add_patch(rect_shadow)
        
        # Main box
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6,rounding_size=1.2",
                                      facecolor=bg_color, edgecolor=border, linewidth=1.8)
        ax.add_patch(rect)
        
        # Content
        ax.text(x + w/2, y + h - 2.2, title, fontsize=11, fontweight="bold", color=title_color, ha="center", va="center")
        if subtitle:
            ax.text(x + w/2, y + h - 4.5, subtitle, fontsize=8.5, fontstyle="italic", color=text_sub, ha="center", va="center")
        
        # Details bullets
        line_y = y + h - 7.5
        for item in details:
            ax.text(x + 1.2, line_y, f"- {item}", fontsize=8.0, color=text_main, ha="left", va="center")
            line_y -= 2.6

    def draw_arrow(x1, y1, x2, y2, label="", color="#38BDF8"):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6",
                                    color=color, lw=2.2, shrinkA=3, shrinkB=3))
        if label:
            mx, my = (x1 + x2)/2, (y1 + y2)/2
            ax.text(mx, my + 1.2, label, fontsize=8, fontweight="bold", color=color, ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.2", facecolor="#0F172A", edgecolor="none", alpha=0.85))

    # --- ROW 1: INGESTION & DATASET (y ~ 68 to 86) ---
    draw_box(4, 68, 26, 19, "1. Policy Handbooks", "University Regulation Handbooks",
             ["01_academic_and_exam_rules.md", "02_fee_and_refund_policy.md", "03_hostel_and_mess_regulations.md", "04_library_and_it_services.md", "20 Structured Policy Sections"],
             bg_color="#1E293B", border="#38BDF8", title_color="#38BDF8")

    draw_box(37, 68, 26, 19, "2. Section-Aware Parser", "Hierarchical Regex Chunker",
             ["Header-Preserving Semantic Split", "Document Code & Section ID Bind", "Metadata Extraction (Doc, Title)", "Eliminates Cross-Section Drift", "Preserves Policy Continuity"],
             bg_color="#1E293B", border="#06B6D4", title_color="#06B6D4")

    draw_box(70, 68, 26, 19, "3. Hybrid Indexing", "Sparse TF-IDF + Keyword Booster",
             ["Sublinear Term Frequency TF-IDF", "Domain Keyword Overlap Boost", "Confidence Score Normalization", "Fast In-Memory Cosine Similarity", "< 3ms Index Lookup Speed"],
             bg_color="#1E293B", border="#10B981", title_color="#10B981")

    # Arrows for Row 1
    draw_arrow(30, 77.5, 37, 77.5, "Raw Markdown", color="#38BDF8")
    draw_arrow(63, 77.5, 70, 77.5, "Parsed Chunks", color="#06B6D4")

    # Arrow from Row 1 to Row 2
    draw_arrow(83, 68, 83, 58, "Top-3 Chunks", color="#10B981")

    # --- ROW 2: RETRIEVAL, PROMPTING & GUARDRAILS (y ~ 38 to 58) ---
    draw_box(70, 38, 26, 20, "4. Verification & Filter", "Confidence & Guardrail Gate",
             ["Score >= 0.15: In-Scope Route", "Score < 0.15: Refusal Trigger", "Injection / Jailbreak Detection", "Entity Consistency Audit", "Zero Hallucination Guarantee"],
             bg_color="#1E293B", border="#F59E0B", title_color="#F59E0B")

    draw_box(37, 38, 26, 20, "5. Prompt Orchestration", "Prompt Evolution v1 -> Final",
             ["v1: Baseline Conversational", "v2: Grounded Citations [Source]", "v3: Strict Refusal String Mandate", "final: CiteGuard Production Schema", "4-Part Structured Response"],
             bg_color="#1E293B", border="#818CF8", title_color="#818CF8")

    draw_box(4, 38, 26, 20, "6. User Query & Input", "Student Interface Ingestion",
             ["Natural Language Question", "Prompt Version Selector (v1-Final)", "Adversarial & Edge Query Ingest", "Interactive ERP Inquiries", "15 Benchmark Test Suites"],
             bg_color="#1E293B", border="#EC4899", title_color="#EC4899")

    # Arrows for Row 2
    draw_arrow(30, 48, 37, 48, "Prompt Template", color="#818CF8")
    draw_arrow(70, 48, 63, 48, "Filtered Context", color="#F59E0B")
    draw_arrow(17, 38, 17, 28, "User Request", color="#EC4899")

    # --- ROW 3: GENERATION & PRESENTATION (y ~ 8 to 28) ---
    draw_box(4, 8, 26, 20, "7. Dual Generation Engine", "Gemini API & Resilient Local",
             ["Google Gemini 1.5 Flash API", "Deterministic Grounding Fallback", "Strict Schema Formatting", "Sub-5ms Sandbox Execution", "100% Reliable Offline Tests"],
             bg_color="#1E293B", border="#14B8A6", title_color="#14B8A6")

    draw_box(37, 8, 26, 20, "8. Citation Auditor", "Grounding & Traceability",
             ["Regex Citation Extractor", "Format: [Doc, Section: X.Y]", "Reference Grounding Verification", "Strict Refusal Fallback Gate", "100% Verifiable Source Trace"],
             bg_color="#1E293B", border="#6366F1", title_color="#6366F1")

    draw_box(70, 8, 26, 20, "9. Delivery & Evaluation", "Streamlit UI & Evaluation Suite",
             ["Streamlit Multi-Tab Web App", "15 Benchmark Evaluation Suite", "Citation Badges & Chunk Explorer", "Automated PDF Generation (docs/)", "SCSE4041 Milestone 2 Reports"],
             bg_color="#1E293B", border="#E11D48", title_color="#E11D48")

    # Arrows for Row 3
    draw_arrow(37, 38, 17, 28, "Context + Prompt", color="#818CF8")
    draw_arrow(30, 18, 37, 18, "Raw Output", color="#14B8A6")
    draw_arrow(63, 18, 70, 18, "Audited Output", color="#6366F1")

    # Footer Metadata Banner
    footer_text = (
        "CiteGuard AI Pipeline: Section-Aware Parsing -> TF-IDF/BM25 Hybrid Retrieval -> "
        "Strict Out-of-Scope Refusal Gate -> Prompt v1-final -> Audited Citations -> Streamlit UI & Evaluation"
    )
    ax.text(50, 3.0, footer_text, fontsize=9.5, color="#64748B", ha="center", va="center", style="italic")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"[OK] Architecture diagram successfully generated at: {output_path}")

if __name__ == "__main__":
    draw_architecture_diagram()
