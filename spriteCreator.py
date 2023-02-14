import math
import os
import re
from pathlib import Path

from PIL import Image
from StatArray import add_to_json_file


def convert_to_camel_case(s):
    # Split the string into words based on the '-' character
    words = s.split('-')

    # Capitalize the first letter of each word after the first one
    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]

    # Join the words together and remove the extension
    camel_case_string = ''.join(camel_case_words)

    return camel_case_string


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def load_images_from_directory(directory):
    images = []
    for filename in natural_sort(os.listdir(directory)):
        try:
            image = Image.open(os.path.join(directory, filename))
            images.append(image)
        except Exception as e:
            print("Failed to load image:", filename)
            print("Error:", e)
    return images


def create_image_sheet(images, cell_width, cell_height):
    n = len(images)

    rows = math.ceil(math.sqrt(n))
    cols = math.ceil(rows)
    sheet_width = cell_width * cols
    sheet_height = cell_height * rows

    sheet = Image.new("RGBA", (sheet_width, sheet_height), (255, 255, 255, 0))
    for i, image in enumerate(images):
        x = (i % cols) * cell_width
        y = (i // cols) * cell_height
        image = image.resize((cell_width, cell_height), Image.ANTIALIAS)
        sheet.paste(image, (x, y))
    return sheet


def save_image_sheet(sheet, filename):
    sheet.save(filename, "PNG")


def pack_images_into_sheet(source_dir, destination_dir, effect_name):
    source_path = Path(source_dir) / effect_name
    sheet_filename = Path(destination_dir) / effect_name
    if (load_images_from_directory(source_path)):
        images = load_images_from_directory(source_path)
    widths, heights = zip(*(i.size for i in images))
    max_width, max_height = max(widths), max(heights)
    sprite_sheet_url = str(sheet_filename) + "-" + str(max_width) + "x" + str(max_height) + ".png"
    add_to_json_file(max_width, max_height, sprite_sheet_url, len(images), convert_to_camel_case(effect_name))
    sheet = create_image_sheet(images, max_width, max_height)
    save_image_sheet(sheet, sprite_sheet_url)

# if __name__ == "__main__":
#     # pack_images_into_sheet("images", "sheet.png")
#     pack_images_into_sheet("DFK Assests\\Export V8 (Rig-v0.1.8)\\Archer\\Bow Mastery\Bow mastery hero", "sheet.png")
