from PIL import Image
import numpy as np
import sys

def process_image(path, target_width=120, target_height=50):
    img = Image.open(path)
    img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

    if img.mode != "L": img = img.convert("L")

    pixels = np.array(img)
    binary_pixels = (pixels < 10).astype(int) # 1 for dark, 0 for light
    return binary_pixels

def text_preview(binary_pixels):
    chars = {0: ".", 1: "#"}

    return "\n".join("".join(chars[px] for px in row) for row in binary_pixels)


if __name__ == "__main__":
    img_path = "frames/output_0099.jpg"
    binary_pixels = process_image(img_path)
    sys.stdout.write(text_preview(binary_pixels))
