from PIL import Image, UnidentifiedImageError

def load_image(image: str):
    try:
        img = Image.open(image)
        
        if img.mode == "RGB":
            img_mode = 3
        img_height, img_width = img.size
        print(f"({img_height}, {img_width}, {img_mode})")

        # Print the RGB values of the pixels
        pixels = img.load()  # Load pixel data
        width, height = img.size
        for y in range(height):

            for x in range(width):
                r, g, b = pixels[x, y]
                print(f"[{r}, {g}, {b}]", end="")
        # img.show()  # Optional: display the image
    
    except FileNotFoundError as e:
        print(f"Error: The file was not found - {e}")
    except UnidentifiedImageError as e:
        print(f"Error: The file could not be identified as an image - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ensure to run the main function as described earlier
