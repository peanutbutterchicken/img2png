# Image Converter

A simple Python script to batch convert images to **PNG**, preserving transparency.  
Works with any folder and can process multiple image types.

## Features
- Converts JPEG, BMP, WebP, GIF, and more to PNG
- Preserves transparency
- Skips unsupported or corrupted files
- Creates output folder if it doesn’t exist

## Requirements
- Python 3.x
- Pillow (`pip install pillow`)

## Usage
```bash
# Activate virtual environment
source venv/bin/activate

# Run the converter
python convert_images.py <input_folder> <output_folder>