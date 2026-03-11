# Image Converter

A simple Python script to batch convert images to PNG, preserving transparency.  
Works with any folder and can process multiple image types.

## Features
- Converts JPEG, BMP, WebP, GIF, and more to PNG
- Preserves transparency
- Skips unsupported or corrupted files
- Creates output folder if it doesn’t exist

## Requirements
- Python 3.x
- Pillow (`pip install pillow`)

# Installing Python
Linux (Debian/Ubuntu)
  sudo apt update
  sudo apt install python3 python3-venv python3-pip -y

Linux (Fedora/CentOS/RHEL)
  sudo dnf install python3 python3-venv python3-pip -y

Windows
  Download python from official website: https://www.python.org/downloads/windows/

Verify Installation
  python --version
  pip --version

# Setting up the project
cd image_converter

Linux/macOS
  python3 -m venv venv
  source venv/bin/activate

Windows (Command Prompt)
  python -m venv venv
  venv\Scripts\activate

Windows (PowerShell)
  python -m venv venv
  venv\Scripts\Activate.ps1

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run the converter
python convert_images.py <input_folder> <output_folder>