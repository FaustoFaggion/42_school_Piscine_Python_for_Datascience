from PIL import Image, UnidentifiedImageError
import numpy as np

def load_image(image: str):
    try:
        img = Image.open(image)
        if img is None:
            raise AssertionError("Image fail to load")
        
        #PRINT SIZE AND CHANNELS
        img_channels = len(img.getbands())
        img_height, img_width = img.size
        print(f"({img_height}, {img_width}, {img_channels})")

        #PRINT PIXEL ARRAY
        print(np.array(img))

        #SHOW IMAGE
        img.show()  

        return img
    except FileNotFoundError as e:
        print(f"Error: The file was not found - {e}")
    except UnidentifiedImageError as e:
        print(f"Error: The file could not be identified as an image - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

