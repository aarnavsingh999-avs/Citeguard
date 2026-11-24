import asyncio
import os
import edge_tts

SCRIPTS = {
    "vo1.mp3": "University students struggle to find accurate rules on fees, exams, and hostels across scattered PDFs, while generic AI hallucinates policies. CiteGuard AI solves this using a section-aware RAG pipeline with strict grounding and deterministic refusal.",
    "vo2.mp3": "In our prompt experiment, Version 1 gives a vague generic response without any policy source. Upgrading to Version 3 enforces inline section citations, verbatim policy excerpts, and a deterministic refusal protocol when out-of-scope questions like keeping pets in hostels are asked.",
    "vo3.mp3": "In this live demo, asking about 71% attendance with typhoid retrieves Section 1.1 with verbatim quotes and official citations. Querying tuition late fees returns the exact grace period and slab rules from Section 2.1, backed by four indexed institutional policy handbooks.",
    "vo4.mp3": "All five modules are working and verified against our 15-case evaluation suite with zero hallucinations. For Milestone 3, we will add multi-hop cross-section fine calculations and live PDF circular uploads."
}

async def generate():
    os.makedirs("temp_video", exist_ok=True)
    voice = "en-US-GuyNeural"
    for filename, text in SCRIPTS.items():
        out_path = os.path.join("temp_video", filename)
        print(f"Synthesizing {filename} with voice {voice}...")
        communicate = edge_tts.Communicate(text, voice=voice)
        await communicate.save(out_path)
        print(f"Saved {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    asyncio.run(generate())
