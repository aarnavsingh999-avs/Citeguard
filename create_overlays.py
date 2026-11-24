import os
from PIL import Image, ImageDraw, ImageFont

def get_font(font_name="arialbd.ttf", size=26):
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

def create_part_overlay(title_text, output_path, width=1920, height=1080):
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Top Banner (0 to 80 px)
    draw.rectangle([(0, 0), (width, 80)], fill=(15, 23, 42, 245)) # Slate 900
    draw.rectangle([(0, 77), (width, 80)], fill=(59, 130, 246, 255)) # Blue accent line
    
    font_banner = get_font("arialbd.ttf", 25)
    bbox = draw.textbbox((0, 0), title_text, font=font_banner)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (width - text_w) // 2
    y = (80 - text_h) // 2 - 2
    
    draw.text((x + 1, y + 1), title_text, font=font_banner, fill=(0, 0, 0, 180))
    draw.text((x, y), title_text, font=font_banner, fill=(255, 255, 255, 255))
    
    # Bottom Footer Bar (1000 to 1080 px)
    draw.rectangle([(0, 1000), (width, 1080)], fill=(15, 23, 42, 245))
    draw.rectangle([(0, 1000), (width, 1003)], fill=(51, 65, 85, 255)) # Divider
    
    font_footer = get_font("arial.ttf", 19)
    footer_text = "CiteGuard AI  |  Team ID: T14  |  Developer: Aarnav Singh (S24CSEU1498)  |  SCSE4041 Milestone 2"
    bbox_f = draw.textbbox((0, 0), footer_text, font=font_footer)
    fx = (width - (bbox_f[2] - bbox_f[0])) // 2
    draw.text((fx, 1030), footer_text, font=font_footer, fill=(148, 163, 184, 255))
    
    img.save(output_path, "PNG")
    print(f"Generated overlay: {output_path}")

if __name__ == "__main__":
    os.makedirs("temp_video", exist_ok=True)
    create_part_overlay(
        "1. PROBLEM & ARCHITECTURE: Grounded Campus Policy Q&A with Zero Hallucination",
        "temp_video/overlay_part1.png"
    )
    create_part_overlay(
        "2. PROMPT EXPERIMENT: Version 1 (Vague Baseline) vs. Version 3 (Grounded Citations & Strict Refusal)",
        "temp_video/overlay_part2.png"
    )
    create_part_overlay(
        "3. WORKING DEMO: Real-Time Policy Retrieval, Verbatim Quotes & 4 Indexed Handbooks",
        "temp_video/overlay_part3.png"
    )
    create_part_overlay(
        "4. PROGRESS & NEXT STEPS: 15-Case Evaluation Suite & Milestone 3 Roadmap",
        "temp_video/overlay_part4.png"
    )
