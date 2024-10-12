import sys
from PIL import Image, ImageOps
import os

def ft_invert(img: any):
    img_invert = ImageOps.invert(img)
    img_invert.show()


def ft_red(img: any):

    # Convert the image to RGB (if not already in that mode)
    img = img.convert("RGB")

    # Split the image into its color channels
    r, g, b = img.split()

    # Create a new image with only the red channel
    img_filtered = Image.merge("RGB", (r, Image.new("L", img.size), Image.new("L", img.size)))
    img_filtered.show()


def ft_green(img: any):
    # Convert the image to RGB (if not already in that mode)
    img = img.convert("RGB")

    # Split the image into its color channels
    r, g, b = img.split()

    # Create a new image with only the red channel
    img_filtered = Image.merge("RGB", (Image.new("L", img.size), g, Image.new("L", img.size)))
    img_filtered.show()

def ft_blue(img: any):
    # Convert the image to RGB (if not already in that mode)
    img = img.convert("RGB")

    # Split the image into its color channels
    r, g, b = img.split()

    # Create a new image with only the red channel
    img_filtered = Image.merge("RGB", (Image.new("L", img.size), Image.new("L", img.size), b))
    img_filtered.show()

def ft_grey(img: any):
    img_filtered = img.convert("L")
    img_filtered.show()

def pimp_image():
    
    try:
        image_path = sys.argv[1]
        img = Image.open(image_path)
        assert image_path.endswith(("jpeg", "jpg")), "Image extension must be jpeg or jpg"
        assert os.path.exists(image_path), "Image not found"

        ft_invert(img)
        ft_red(img)
        ft_green(img)
        ft_blue(img)
        ft_grey(img)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    pimp_image()