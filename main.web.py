import time
from pyscript import document


from PIL import Image
import numpy as np

def process_image(path, target_width=120, target_height=25):
    img = Image.open(path)
    img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

    if img.mode != "L": img = img.convert("L")

    pixels = np.array(img)
    binary_pixels = (pixels < 10).astype(int) # 1 for dark, 0 for light
    return binary_pixels

def text_preview(binary_pixels):
    chars = {0: ".", 1: "#"}

    return "\n".join("".join(chars[px] for px in row) for row in binary_pixels)


def main():
    # output_div = document.querySelector("#output")

    for i in range(1, 6573):
        img_path = f"output_{str(i).zfill(4)}.jpg"
        binary_pixels = process_image(img_path)
        print(text_preview(binary_pixels), flush=True)
        time.sleep(1.0/30.0)
        print("\033c")


if __name__ == "__main__":
    main()

