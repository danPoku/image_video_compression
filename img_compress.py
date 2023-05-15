"""
Author: Dan G. Poku (dan.gyinaye@gmail.com)
Date: April 15, 2023
Description: This script compresses (at 50%) all image files in a 
folder and its subfolders and saves them in a separate folder. 
It avoids recompressing previously compressed files.
"""

import os
import logging
from typing import List
import numpy as np
import cv2
from destination_path import PY_SCRIPT

# Set up logging
logging.basicConfig(filename='image_compression.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# Define the compression parameters
compress_params: List[int] = [cv2.IMWRITE_JPEG_QUALITY, 50]


def get_folder_path() -> str:
    """Returns the folder path of the Python script"""
    return os.path.dirname(os.path.abspath(PY_SCRIPT))


def create_destination_folder(folder_path: str) -> str:
    """Creates a new folder within the given folder path"""
    destination_folder = os.path.join(folder_path, "compressed_images")
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    return destination_folder


def get_compressed_files(destination_folder: str) -> List[str]:
    """Keep track of previously compressed files to avoid recompression"""
    return [os.path.splitext(f)[0] for f in os.listdir(destination_folder)]


def compress_image(img_path: str, compressed_files: List[str], destination_folder: str) -> None:
    """Compress an image and save in another folder within the same folder"""
    # Load the image
    with open(img_path, 'rb') as f:
        img = cv2.imdecode(np.frombuffer(f.read(), np.uint8), cv2.IMREAD_COLOR)

    # Get the basename of the image file without the extension
    img_name = os.path.splitext(os.path.basename(img_path))[0]

    # Compress the image and save it in another folder with "_compressed" appended to the filename
    compressed_path = os.path.join(
        destination_folder, f"{img_name}_compressed.jpg")
    with open(compressed_path, 'wb') as f:
        f.write(cv2.imencode('.jpg', img, compress_params)[1])

    # Add the compressed filename to the list of compressed files
    compressed_files.append(img_name)


def compress_images() -> None:
    """Compress all image files in the folder and its subfolders."""
    # Get and set the current folder path of the Python script
    folder_path = get_folder_path()

    # Loop through all image files in the folder and compress them
    for root, dirs, files in os.walk(folder_path):
        destination_folder = create_destination_folder(root)
        compressed_files = get_compressed_files(destination_folder)
        for filename in files:
            if filename.lower().endswith((".jpg", "png")) or filename.lower().endswith((".JPG", "PNG")):
                img_path = os.path.join(root, filename)
                if os.path.splitext(filename)[0] not in compressed_files:
                    compress_image(img_path, compressed_files, destination_folder)


if __name__ == "__main__":
    compress_images()
