# A python script that automates image conversion
# How to run:
# In termnial, type "source venv/bin/activate" and "python convert_images.py images converted"
# images is the input folder, converted is the output folder. Can be directory or file

from PIL import Image
import os
import sys

# Get arguments: input folder, output folder
if len(sys.argv) != 3:
    print("Usage: python convert_images.py <input_folder> <output_folder>")
    sys.exit(1)

input_folder = sys.argv[1]
output_folder = sys.argv[2]

# Set format to PNG
output_format = "png"
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    path = os.path.join(input_folder, file)
    try:
        with Image.open(path) as img:
            # PNG supports transparency, no need to convert to RGB
            new_name = os.path.splitext(file)[0] + f".{output_format}"
            img.save(os.path.join(output_folder, new_name), "PNG")
            print(f"Converted {file} → {new_name}")
    except Exception as e:
        print(f"Skipped {file} ({e})")