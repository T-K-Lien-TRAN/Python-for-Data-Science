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
    """Provide an entry point; tests are in tester.py."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
