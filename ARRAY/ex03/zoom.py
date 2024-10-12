import sys
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import load_image

def zoom():

    try:
        image_path = sys.argv[1]

        assert image_path.endswith(("jpeg", "jpg")), "Image extension must be jpeg or jpg"
        assert os.path.exists(image_path), "Image not found"
        
        img = load_image(image_path)

        #CONVERT TO GREEN SCALE
        img_green_scale = img.convert("L")

        #IMAGE ZOOM
        img_zoom = img_green_scale.crop([400, 100, 800, 00])
        img_zoom_heigth, img_zoom_width = img_zoom.size
        print(f"New shapw after slicing: ({img_zoom_heigth}, {img_zoom_width}, {len(img_zoom.getbands())})")
        print(np.array(img_zoom))
        
        # img_zoom.show()

        plt.imshow(img_zoom, cmap="grey")
        plt.axis('on')
        plt.show()
        
    except Exception as e:
        print(e)


if __name__ == "__main__":
    zoom()