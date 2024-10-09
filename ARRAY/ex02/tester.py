import sys
from load_image import load_image

def main():
    image_path = sys.argv[1]

    load_image(image_path)

if __name__ == "__main__":
    main()