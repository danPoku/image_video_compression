# Image and Video Compression Script

## img_compress.py
This script compresses all image files (.jpg and .png only) in a 
folder and its subfolders and saves them in a separate folder. 
It avoids recompressing previously compressed files.

## Video Compression Script (vid_compress.py)
###Description
This script compresses all .mp4 files in a folder and its subfolders, saving them in a separate folder. It avoids recompressing previously compressed files.

### Requirements
**'ffmpeg'** and **'ffprobe'** should be installed on your system. Ensure they are accessible from the command line.
### Usage
Place the videocomp.py script in the root folder containing the videos you want to compress.

Open a terminal or command prompt and navigate to the root folder.

Run the following command:
'''console
python videocomp.py
'''
The script will recursively compress all **'.mp4'** files in the root folder and its subfolders, saving the compressed files in a "compressed" folder within each folder containing the original videos.

Once the script completes, the compressed videos will be available in their respective "compressed" folders.
### Functionality
The script provides the following functions:

**'get_video_info(video_path: str) -> dict'**
Returns a dictionary containing video information using ffprobe.

**'get_bitrate(video_path: str) -> int'**
Returns the current bitrate of a video file.

**'is_video_compressed(video_path: str) -> bool'**
Checks if a video file has already been compressed.

**'compress_video(video_path: str, output_dir: str) -> str'**
Compresses a video file and returns the path of the compressed file.

**'compress_videos(root_folder: str)'**
Recursively compresses all .mp4 files in a root folder and saves them to a "compressed" folder within each folder containing the original videos.

Note: The script applies different compression settings based on the bitrate of the video file.

Contact
For any questions or feedback, please contact Dan G. Poku at dan.gyinaye@gmail.com.
