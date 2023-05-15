import os
import subprocess
import json

def get_video_info(video_path: str) -> dict:
    """
    Returns a dictionary containing video information using ffprobe.
    """
    result = subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", video_path], capture_output=True)
    info = json.loads(result.stdout)
    return info

def get_bitrate(video_path: str) -> int:
    """
    Returns the current bitrate of a video file.
    """
    info = get_video_info(video_path)
    bitrate = int(info['format']['bit_rate'])
    return bitrate

def is_video_compressed(video_path: str) -> bool:
    """
    Checks if a video file has already been compressed.
    """
    filename = os.path.basename(video_path)
    compressed_path = os.path.join(os.path.dirname(video_path), "compressed", os.path.splitext(filename)[0] + "_compressed.mp4")
    return os.path.exists(compressed_path)

def compress_video(video_path: str, output_dir: str) -> str:
    """
    Compresses a video file and returns the path of the compressed file.
    """
    bitrate = get_bitrate(video_path)
    if bitrate > 3000000:
        crf = 30
    elif bitrate > 1000000:
        crf = 26
    else:
        crf = 25

    filename = os.path.basename(video_path)
    compressed_path = os.path.join(output_dir, os.path.splitext(filename)[0] + "_compressed.mp4")

    subprocess.run(["ffmpeg", "-i", video_path, "-vcodec", "libx264", "-crf", str(crf), compressed_path], capture_output=True)
    return compressed_path

def compress_videos(root_folder: str):
    """
    Recursively compresses all .mp4 files in a root folder and saves them to a "compressed" folder
    within each folder containing the original videos.
    """
    for subdirs, dirs, files in os.walk(root_folder):
        if 'compressed' in dirs:
            dirs.remove('compressed') # exclude compressed folder from processing
        for filename in files:
            if filename.lower().endswith(".mp4") and not is_video_compressed(os.path.join(subdirs, filename)):
                video_path = os.path.join(subdirs, filename)
                output_dir = os.path.join(subdirs, "compressed")
                os.makedirs(output_dir, exist_ok=True)
                compressed_path = compress_video(video_path, output_dir)
                print(f"Compressed {video_path} to {compressed_path}")

if __name__ == '__main__':
    root_folder = os.path.dirname(os.path.abspath("videocomp.py"))
    compress_videos(root_folder)