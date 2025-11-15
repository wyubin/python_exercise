#!/usr/bin/env python3
import argparse
import os
from yt_dlp import YoutubeDL

def sanitize_filename(name: str) -> str:
    """替換檔名非法字元與空白"""
    name = name.replace(" ", "_")
    invalid = r'\/:*?"<>|'
    for ch in invalid:
        name = name.replace(ch, "_")
    return name

def main():
    parser = argparse.ArgumentParser(description="Download videos or audio from a YouTube playlist.")
    parser.add_argument("--id", required=True, help="Playlist ID")
    parser.add_argument("--outDir", required=True, help="Output directory")
    parser.add_argument("--fromIndex", type=int, default=1, help="Start index (1-based)")
    parser.add_argument("--toIndex", type=int, default=None, help="End index (1-based)")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--audio-high", action="store_true", help="Download high quality audio (m4a)")
    group.add_argument("--audio-low", action="store_true", help="Download low quality audio (64 kbps mp3)")

    args = parser.parse_args()

    playlist_url = f"https://www.youtube.com/playlist?list={args.id}"
    os.makedirs(args.outDir, exist_ok=True)

    # 取得播放清單影片列表
    ydl_opts_list = {"extract_flat": True, "quiet": True}
    with YoutubeDL(ydl_opts_list) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        entries = info.get("entries", [])

    start = args.fromIndex - 1
    end = args.toIndex if args.toIndex else len(entries)
    selected_entries = entries[start:end]

    print(f"Total videos in playlist: {len(entries)}")
    print(f"Downloading index {args.fromIndex} to {args.toIndex or len(entries)}")
    print("===================================================")

    for index, entry in enumerate(selected_entries, start=args.fromIndex):
        video_id = entry["id"]
        title = sanitize_filename(entry["title"])
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        print(f"[{index}] Downloading: {entry['title']}")

        if args.audio_high:
            # 高音質：直接下載 m4a
            ydl_opts_download = {
                "outtmpl": os.path.join(args.outDir, f"{title}.%(ext)s"),
                "quiet": False,
                "format": "bestaudio[ext=m4a]/bestaudio",
            }
        elif args.audio_low:
            # 低音質：下載 64 kbps mp3
            ydl_opts_download = {
                "outtmpl": os.path.join(args.outDir, f"{title}.%(ext)s"),
                "quiet": False,
                "format": "bestaudio/best",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "64",
                }],
            }
        else:
            # 影片模式
            ydl_opts_download = {
                "outtmpl": os.path.join(args.outDir, f"{title}.%(ext)s"),
                "quiet": False,
                "format": "bestvideo+bestaudio/best",
                "merge_output_format": "mp4",
            }

        with YoutubeDL(ydl_opts_download) as ydl:
            ydl.download([video_url])

    print("\nAll done!")

if __name__ == "__main__":
    main()
