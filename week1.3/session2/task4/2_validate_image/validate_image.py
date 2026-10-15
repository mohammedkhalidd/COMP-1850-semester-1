# Week 1.3, Session 2: Validate image

from pathlib import Path


def validate_image(image_file):
    try:
        with open(image_file, 'r') as file:
            tokens = []
            for line in file:
                stripped = line.strip()
                if not stripped or stripped.startswith('#'):
                    continue
                tokens.extend(stripped.split())

        if len(tokens) < 4:
            raise ValueError("Invalid PGM file")

        if tokens[0] != 'P2':
            raise ValueError("This is not a valid PGM file")

        width, height = map(int, tokens[1:3])
        max_gray_value = int(tokens[3])
        pixels = list(map(int, tokens[4:]))

        expected_pixels = width * height

        if len(pixels) != expected_pixels:
            if len(pixels) % width == 0:
                print("Invalid height")
            else:
                print("Invalid width")
            return

        for pixel in pixels:
            if pixel < 0 or pixel > max_gray_value:
                print("Invalid pixel values")
                return

        print("Valid image")

    except FileNotFoundError:
        print(f"Error: {image_file} not found.")
    except ValueError as error:
        print(f"Error: {error}")


image_path = Path(__file__).resolve().parent.parent / 'images' / 'feep.pgm'
validate_image(image_path)
