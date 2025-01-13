from toDot import *
import os
import time

def main():
    BASE_DIR = "frames"
    for i in range(1, 6572):
        img_path = f"{BASE_DIR}/output_{str(i).zfill(4)}.jpg"
        binary_pixels = process_image(img_path)
        print(text_preview(binary_pixels), flush=True)
        time.sleep(1.0/30.0)
        os.system("clear")

if __name__ == "__main__":
    main()

