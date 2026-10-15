# Week 1.3, Session 2: Print PGM image info

from pathlib import Path


def print_image_info(image_file):
    try:
        with open(image_file, 'r') as file:
            tokens = []
            for line in file:
                stripped = line.strip()
                if not stripped:
                    continue
                if stripped.startswith('#'):
                    continue
                tokens.extend(stripped.split())

        if len(tokens) < 4:
            raise ValueError("Invalid PGM file format")

        magic_number = tokens[0]
        if magic_number != 'P2':
            raise ValueError("This is not a text-based PGM file")

        width, height = map(int, tokens[1:3])
        max_gray_value = int(tokens[3])

        print(f"Dimensions: {width} x {height} pixels")
        print(f"Max Gray Value: {max_gray_value}")

    except FileNotFoundError:
        print(f"Error: {image_file} not found.")
    except ValueError as error:
        print(f"Error: {error}")


image_path = Path(__file__).resolve().parent.parent.parent / 'images' / 'feep.pgm'
print_image_info(image_path)
