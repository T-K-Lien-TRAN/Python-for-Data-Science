from PIL import Image
import numpy as np
from numpy import array


def ft_load(path: str) -> array:
    """Loads an image, prints its format, and its pixels
content in RGB format"""
    try:
        if not isinstance(path, str):
            raise TypeError("The path must be a string")
        with Image.open(path) as image:
            if (image.format != "JPEG"):
                raise ValueError("The format of image must be JPG or JPEG")
            pixels = np.array(image.convert("RGB"))
        print("The shape of image is:", pixels.shape)
        return pixels
    except (OSError, ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None


def main():
    """Load landscape.jpg and print its pixel data."""

    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
