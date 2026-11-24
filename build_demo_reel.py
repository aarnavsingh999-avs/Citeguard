import os
import subprocess
import imageio_ffmpeg

def run_cmd(cmd):
    print("Running command:\n" + " ".join(cmd))
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print("ERROR stderr:\n", result.stderr)
        raise RuntimeError(f"Command failed with code {result.returncode}")
    return result

def main():
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    os.makedirs("temp_video", exist_ok=True)
    os.makedirs("campus-helpdesk-assistant/docs", exist_ok=True)
    
    src_video = "campus-helpdesk-assistant/video_1.mp4"
    if not os.path.exists(src_video):
        src_video = "video_1.mp4"
    print(f"Using source video: {src_video}")
    
    # -------------------------------------------------------------------------
    # PART 1: Problem & System Architecture (16.5s)
    # Source: 01:12 (72.0s) to 01:28.5 (88.5s)
    # Audio: vo1.mp3 (16.13s)
    # -------------------------------------------------------------------------
    print("\n=== Building Part 1 (16.5s) ===")
    part1_out = "temp_video/part1.mp4"
    cmd_part1 = [
        ffmpeg, "-y",
        "-ss", "72.0", "-to", "88.5", "-i", src_video,
        "-i", "temp_video/overlay_part1.png",
        "-i", "temp_video/vo1.mp3",
        "-filter_complex",
        "[0:v]scale=1920:920,pad=1920:1080:0:80:color=0x0f172a,setsar=1,fps=30[bg];"
        "[bg][1:v]overlay=0:0,setsar=1[v];"
        "[2:a]apad=pad_dur=2[a]",
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-t", "16.5",
        part1_out
    ]
    run_cmd(cmd_part1)
    
    # -------------------------------------------------------------------------
    # PART 2: Prompt Experiment: Before vs. After (36.0s)
    # 2A: 02:20 to 02:27 (140.0s to 147.0s, 7.0s) - V1 baseline
    # 2B: 02:02 to 02:20 (122.0s to 140.0s, 18.0s) - V2 & V3 grounded citations
    # 2C: 01:36 to 01:47 (96.0s to 107.0s, 11.0s) - Refusal protocol on pet trap
    # Total: 7 + 18 + 11 = 36.0s
    # Audio: vo2.mp3 (17.18s)
    # -------------------------------------------------------------------------
    print("\n=== Building Part 2 (36.0s) ===")
    part2_out = "temp_video/part2.mp4"
    cmd_part2 = [
        ffmpeg, "-y",
        "-ss", "140.0", "-to", "147.0", "-i", src_video,
        "-ss", "122.0", "-to", "140.0", "-i", src_video,
        "-ss", "96.0", "-to", "107.0", "-i", src_video,
        "-i", "temp_video/overlay_part2.png",
        "-i", "temp_video/vo2.mp3",
        "-filter_complex",
        "[0:v]scale=1920:920,pad=1920:1080:0:80:color=0x0f172a,setsar=1,fps=30[v0];"
        "[1:v]scale=1920:920,pad=1920:1080:0:80:color=0x0f172a,setsar=1,fps=30[v1];"
        "[2:v]scale=1920:920,pad=1920:1080:0:80:color=0x0f172a,setsar=1,fps=30[v2];"
        "[v0][v1][v2]concat=n=3:v=1:a=0[vcat];"
        "[vcat][3:v]overlay=0:0,setsar=1[v];"
        "[4:a]apad=pad_dur=20[a]",
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-t", "36.0",
        part2_out
    ]
    run_cmd(cmd_part2)
    
    # -------------------------------------------------------------------------
    # PART 3: Live Working Demo (48.0s)
    # 3A: 00:02 to 00:15 (2.0s to 15.0s, 13.0s) - 71% attendance typhoid
    # 3B: 00:24 to 00:39 (24.0s to 39.0s, 15.0s) - Late tuition fee 4 days
    # 3C: 00:38 to 00:58 (38.0s to 58.0s, 20.0s) - Policy Corpus Explorer
    # Total: 13 + 15 + 20 = 48.0s
    # Audio: vo3.mp3 (17.69s)
    # -------------------------------------------------------------------------
    print("\n=== Building Part 3 (48.0s) ===")
    part3_out = "temp_video/part3.mp4"
    cmd_part3 = [
        ffmpeg, "-y",
        "-ss", "2.0", "-to", "15.0", "-i", src_video,
        "-ss", "24.0", "-to", "39.0", "-i", src_video,
        "-ss", "38.0", "-to", "58.0", "-i", src_video,
        "-i", "temp_video/overlay_part3.png",
        "-i", "temp_video/vo3.mp3",
        "-filter_complex",
        "[0:v]scale=1920:920,pad=1920:1080:0:80:color=0x0f172a,setsar=1,fps=30[v0];"
        "[1:v]scale=1920:920,pad=1920:1080:0:80:color=0x0f172a,setsar=1,fps=30[v1];"
        "[2:v]scale=1920:920,pad=1920:1080:0:80:color=0x0f172a,setsar=1,fps=30[v2];"
        "[v0][v1][v2]concat=n=3:v=1:a=0[vcat];"
        "[vcat][3:v]overlay=0:0,setsar=1[v];"
        "[4:a]apad=pad_dur=32[a]",
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-t", "48.0",
        part3_out
    ]
    run_cmd(cmd_part3)
    
    # -------------------------------------------------------------------------
    # PART 4: Progress & Milestone 3 Next Steps (18.0s)
    # 4A: 01:02 to 01:10 (62.0s to 70.0s, 8.0s) - Benchmark suite (16 tests)
    # 4B: End Card Graphic (10.0s) - High-res Milestone 2 accomplishments & M3 roadmap
    # Total: 8 + 10 = 18.0s
    # Audio: vo4.mp3 (13.49s)
    # -------------------------------------------------------------------------
    print("\n=== Building Part 4 (18.0s) ===")
    part4_out = "temp_video/part4.mp4"
    cmd_part4 = [
        ffmpeg, "-y",
        "-ss", "62.0", "-to", "70.0", "-i", src_video,
        "-i", "temp_video/overlay_part4.png",
        "-loop", "1", "-framerate", "30", "-t", "10.0", "-i", "temp_video/end_card.png",
        "-i", "temp_video/vo4.mp3",
        "-filter_complex",
        "[0:v]scale=1920:920,pad=1920:1080:0:80:color=0x0f172a,setsar=1,fps=30[v0_bg];"
        "[v0_bg][1:v]overlay=0:0,setsar=1[v0];"
        "[2:v]scale=1920:1080,setsar=1,fps=30[v1];"
        "[v0][v1]concat=n=2:v=1:a=0[vcat];"
        "[3:a]apad=pad_dur=6[a]",
        "-map", "[vcat]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-t", "18.0",
        part4_out
    ]
    run_cmd(cmd_part4)
    
    # -------------------------------------------------------------------------
    # FINAL CONCATENATION (118.5s total)
    # Output to docs/CiteGuardAI_DemoReel.mp4
    # -------------------------------------------------------------------------
    print("\n=== Concatenating all 4 parts into Final Demo Reel ===")
    concat_list_file = "temp_video/concat_list.txt"
    with open(concat_list_file, "w") as f:
        f.write("file 'part1.mp4'\n")
        f.write("file 'part2.mp4'\n")
        f.write("file 'part3.mp4'\n")
        f.write("file 'part4.mp4'\n")
        
    final_output = "campus-helpdesk-assistant/docs/CiteGuardAI_DemoReel.mp4"
    cmd_final = [
        ffmpeg, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list_file,
        "-c", "copy",
        final_output
    ]
    run_cmd(cmd_final)
    print(f"\nSUCCESS! Demo reel generated at: {final_output}")
    print(f"File size: {os.path.getsize(final_output) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    main()
