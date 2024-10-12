import sys
import os
from PIL import Image
import numpy as np
from load_image import load_image

def zoom():

    image_path = sys.argv[1]

    assert image_path.endswith(("jpeg", "jpg")), "Image extension must be jpeg or jpg"
    assert os.path.exists(image_path), "Image not found"
    
    img = load_image(image_path)

    #CONVERT TO GREEN SCALE
    img_green_scale = img.convert("L")

    #IMAGE ZOOM
    img_zoom = img_green_scale.crop([400, 100, 800, 600])
    img_zoom_heigth, img_zoom_width = img_zoom.size
    print(f"({img_zoom_heigth}, {img_zoom_width}, {len(img_zoom.getbands())})")
    print(np.array(img_zoom))
    img_zoom.show()


if __name__ == "__main__":
    zoom()