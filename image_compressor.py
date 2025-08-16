from PIL import Image
import os

def compress_image(input_path, output_path, quality=85, max_width=None):
    img = Image.open(input_path)

    if max_width and img.width > max_width:
        height = int((max_width / img.width) * img.height)
        img = img.resize((max_width, height), Image.ANTIALIAS)

    img.save(output_path, optimize=True, quality=quality)
    print(f"Compressed image saved to: {output_path}")

input_image = 'backremover1.jpg'
output_image = 'compressed.jpg'
compress_image(input_image, output_image, quality=80, max_width=1080)
