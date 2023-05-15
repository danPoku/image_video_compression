# Image and Video Compression Script
**Author:** Dan G. Poku (dan.gyinaye@gmail.com)  
**Date:** April 15, 2023

## Image Compression Script (img_compress.py)
## Description

This script compresses (at 50%) all image files in a folder and its subfolders, saving them in a separate folder. It avoids recompressing previously compressed files.

## Requirements

- Python 3.x
- OpenCV (cv2) library

## Usage

1. Place the script in the root folder containing the images you want to compress.

2. Ensure the `destination_path.py` file is present in the same directory as the script.

3. Open a terminal or command prompt and navigate to the root folder.

4. Run the following command:

```
python img_compress.py
```

The script will recursively compress all image files (`.jpg` and `.png`) in the root folder and its subfolders, saving the compressed images in a "compressed_images" folder within each folder containing the original images.

5. Once the script completes, the compressed images will be available in their respective "compressed_images" folders.

## Logging

The script logs its progress and any errors encountered during execution to the `image_compression.log` file.

## Functionality

The script provides the following functions:

### `get_folder_path() -> str`

Returns the folder path of the Python script.

### `create_destination_folder(folder_path: str) -> str`

Creates a new folder within the given folder path to store the compressed images.

### `get_compressed_files(destination_folder: str) -> List[str]`

Retrieves a list of previously compressed file names in the destination folder to avoid recompression.

### `compress_image(img_path: str, compressed_files: List[str], destination_folder: str) -> None`

Compresses an image and saves it in another folder within the same folder.

### `compress_images() -> None`

Compresses all image files in the root folder and its subfolders.

Note: The script uses OpenCV's `cv2` library to read and compress images.


## Video Compression Script (vid_compress.py)
## Description

This script compresses all `.mp4` files in a folder and its subfolders, saving them in a separate folder. It avoids recompressing previously compressed files.

## Requirements

- `ffmpeg` and `ffprobe` should be installed on your system. Ensure they are accessible from the command line.

## Usage

1. Place the `videocomp.py` script in the root folder containing the videos you want to compress.

2. Open a terminal or command prompt and navigate to the root folder.

3. Run the following command:

```
python vid_compress.py
```

The script will recursively compress all `.mp4` files in the root folder and its subfolders, saving the compressed files in a "compressed" folder within each folder containing the original videos.

4. Once the script completes, the compressed videos will be available in their respective "compressed" folders.

## Functionality

The script provides the following functions:

### `get_video_info(video_path: str) -> dict`

Returns a dictionary containing video information using `ffprobe`.

### `get_bitrate(video_path: str) -> int`

Returns the current bitrate of a video file.

### `is_video_compressed(video_path: str) -> bool`

Checks if a video file has already been compressed.

### `compress_video(video_path: str, output_dir: str) -> str`

Compresses a video file and returns the path of the compressed file.

### `compress_videos(root_folder: str)`

Recursively compresses all `.mp4` files in a root folder and saves them to a "compressed" folder within each folder containing the original videos.

Note: The script applies different compression settings based on the bitrate of the video file.

## Contact

For any questions or feedback, please contact Dan at dan.gyinaye@gmail.com.
