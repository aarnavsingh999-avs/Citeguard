import os
from PIL import Image, ImageDraw, ImageFont

def get_font(font_name="arialbd.ttf", size=32):
    font_paths = [
        os.path.join(r"C:\Windows\Fonts", font_name),
        os.path.join(r"C:\Windows\Fonts", font_name.lower()),
        os.path.join(r"C:\Windows\Fonts", "arial.ttf"),
        os.path.join(r"C:\Windows\Fonts", "segoeui.ttf")
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def create_top_banner(title_text, output_path, width=1920, height=1080, banner_height=75):
    # Create transparent canvas
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw top banner rectangle with sleek dark theme
    draw.rectangle([(0, 0), (width, banner_height)], fill=(15, 23, 42, 235)) # Slate 900
    # Accent bottom border line
    draw.rectangle([(0, banner_height - 3), (width, banner_height)], fill=(59, 130, 246, 255)) # Blue 500
    
    font = get_font("arialbd.ttf", 26)
    
    # Calculate text position
    bbox = draw.textbbox((0, 0), title_text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x = (width - text_w) // 2
    y = (banner_height - text_h) // 2 - 2
    
    # Text shadow for maximum clarity
    draw.text((x + 1, y + 1), title_text, font=font, fill=(0, 0, 0, 180))
    # Text fill
    draw.text((x, y), title_text, font=font, fill=(255, 255, 255, 255))
    
    img.save(output_path, "PNG")
    print(f"Saved banner: {output_path}")

def create_end_card(output_path, width=1920, height=1080):
    img = Image.new("RGB", (width, height), (15, 23, 42)) # Slate 900 background
    draw = ImageDraw.Draw(img)
    
    title_font = get_font("arialbd.ttf", 46)
    subtitle_font = get_font("arialbd.ttf", 24)
    heading_font = get_font("arialbd.ttf", 28)
    body_font = get_font("arial.ttf", 22)
    bold_body_font = get_font("arialbd.ttf", 22)
    meta_font = get_font("arial.ttf", 20)
    
    # Header Banner
    draw.rectangle([(0, 0), (width, 110)], fill=(30, 41, 59)) # Slate 800
    draw.rectangle([(0, 106), (width, 110)], fill=(59, 130, 246)) # Accent line
    
    header_title = "SCSE4041 MINI PROJECT — MILESTONE 2 SUMMARY"
    bbox = draw.textbbox((0, 0), header_title, font=title_font)
    draw.text(((width - (bbox[2] - bbox[0])) // 2, 25), header_title, font=title_font, fill=(255, 255, 255))
    
    # Subtitle / Metadata Tagline
    meta_text = "Team ID: T14  |  Team: CiteGuard AI  |  Batch: B13-24  |  Developer: Aarnav Singh (S24CSEU1498)"
    bbox_meta = draw.textbbox((0, 0), meta_text, font=meta_font)
    draw.text(((width - (bbox_meta[2] - bbox_meta[0])) // 2, 130), meta_text, font=meta_font, fill=(148, 163, 184))
    
    # Two Columns: Left = Milestone 2 Accomplishments, Right = Milestone 3 Roadmap
    # Column 1 Card (Left)
    c1_x1, c1_y1, c1_x2, c1_y2 = 100, 180, 930, 960
    draw.rounded_rectangle([(c1_x1, c1_y1), (c1_x2, c1_y2)], radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    
    # Left Card Header Pill
    draw.rounded_rectangle([(c1_x1 + 30, c1_y1 + 30), (c1_x2 - 30, c1_y1 + 80)], radius=8, fill=(16, 185, 129)) # Emerald
    draw.text((c1_x1 + 50, c1_y1 + 40), "[DONE] MILESTONE 2 ACCOMPLISHMENTS", font=heading_font, fill=(255, 255, 255))
    
    achievements = [
        ("Module Architecture", "5/5 Full Modules Deployed & Integrated"),
        ("Benchmark Suite", "16/16 Test Cases Passed (100% Pass Rate)"),
        ("Hallucination Rate", "0.0% Hallucinations (Strict Zero Tolerance)"),
        ("Retrieval Engine", "Section-Aware Hybrid TF-IDF/BM25 (21 Policy Sections)"),
        ("Grounding Protocol", "Inline Markdown Citations + Verbatim Blockquotes"),
        ("Refusal Protocol", "Deterministic Out-of-Scope Intent Filter & Guardrails"),
        ("Deployment & UI", "Streamlit Cloud / HF Spaces Ready + Policy Explorer")
    ]
    
    y_offset = c1_y1 + 115
    for label, val in achievements:
        draw.text((c1_x1 + 45, y_offset), f"  {label}:", font=bold_body_font, fill=(56, 189, 248))
        draw.text((c1_x1 + 65, y_offset + 32), val, font=body_font, fill=(241, 245, 249))
        y_offset += 95
        
    # Column 2 Card (Right)
    c2_x1, c2_y1, c2_x2, c2_y2 = 990, 180, 1820, 960
    draw.rounded_rectangle([(c2_x1, c2_y1), (c2_x2, c2_y2)], radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    
    # Right Card Header Pill
    draw.rounded_rectangle([(c2_x1 + 30, c2_y1 + 30), (c2_x2 - 30, c2_y1 + 80)], radius=8, fill=(59, 130, 246)) # Blue
    draw.text((c2_x1 + 50, c2_y1 + 40), "[ROADMAP] MILESTONE 3 UPCOMING GOALS", font=heading_font, fill=(255, 255, 255))
    
    roadmap = [
        ("Multi-Hop Calculations", "Cross-section fee deduction & late penalty arithmetic"),
        ("Live Circular Upload", "Dynamic PDF parser & automated vector indexing"),
        ("Interactive Clarification", "Multi-turn ambiguity resolution dialog system"),
        ("Role-Based Access", "Admin circular management dashboard with audit log"),
        ("Production Monitoring", "Real-time query latency and retrieval telemetry")
    ]
    
    y_offset = c2_y1 + 130
    for label, val in roadmap:
        draw.text((c2_x1 + 45, y_offset), f"  {label}:", font=bold_body_font, fill=(147, 197, 253))
        draw.text((c2_x1 + 65, y_offset + 34), val, font=body_font, fill=(241, 245, 249))
        y_offset += 120
        
    # Footer
    footer_text = "CiteGuard AI -- SCSE4041 Automated Verification Engine | Benchmark: 100% Rubric Compliant"
    bbox_foot = draw.textbbox((0, 0), footer_text, font=meta_font)
    draw.text(((width - (bbox_foot[2] - bbox_foot[0])) // 2, 1010), footer_text, font=meta_font, fill=(100, 116, 139))
    
    img.save(output_path, "PNG")
    print(f"Saved end card: {output_path}")

if __name__ == "__main__":
    os.makedirs("temp_video", exist_ok=True)
    
    # Generate 4 Top Banners
    create_top_banner(
        "1. PROBLEM & ARCHITECTURE: Grounded Campus Policy Q&A with Zero Hallucination",
        "temp_video/banner_part1.png"
    )
    create_top_banner(
        "2. PROMPT EXPERIMENT: Version 1 (Vague Baseline) vs. Version 3 (Grounded Citations & Strict Refusal)",
        "temp_video/banner_part2.png"
    )
    create_top_banner(
        "3. WORKING DEMO: Real-Time Policy Retrieval, Verbatim Quotes & 4 Indexed Handbooks",
        "temp_video/banner_part3.png"
    )
    create_top_banner(
        "4. PROGRESS & NEXT STEPS: 15-Case Evaluation Suite & Milestone 3 Roadmap",
        "temp_video/banner_part4.png"
    )
    
    # Generate End Card
    create_end_card("temp_video/end_card.png")
