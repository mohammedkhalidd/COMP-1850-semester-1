# Week 1.3, Session 2: Invert PGM image

from pathlib import Path


def invert_image(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
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
            raise ValueError("Image data does not match the declared dimensions")

        inverted_pixels = [max_gray_value - pixel for pixel in pixels]

        with open(output_file, 'w') as out:
            out.write("P2\n")
            out.write(f"{width} {height}\n")
            out.write(f"{max_gray_value}\n")

            for row_index in range(height):
                row = inverted_pixels[row_index * width:(row_index + 1) * width]
                out.write(" ".join(str(pixel) for pixel in row) + "\n")

        print(f"Inverted image saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except ValueError as error:
        print(f"Error: {error}")


input_path = Path(__file__).resolve().parent.parent / 'images' / 'feep.pgm'
output_path = Path(__file__).resolve().parent / 'inverted_feep.pgm'
invert_image(input_path, output_path)
