import math
import os
import re

from PIL import Image


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
    print("row :", rows)
    cols = math.ceil(rows)
    print("cols :", cols)

    print("cell_width :", cell_width)
    print("cell_height", cell_height)

    sheet_width = cell_width * cols
    sheet_height = cell_height * rows

    sheet = Image.new("RGBA", (sheet_width, sheet_height), (255, 255, 255, 0))
    for i, image in enumerate(images):
        x = (i % cols) * cell_width
        y = (i // cols) * cell_height
        print(x, y)
        image = image.resize((cell_width, cell_height), Image.ANTIALIAS)
        sheet.paste(image, (x, y))
    return sheet


def save_image_sheet(sheet, filename):
    sheet.save(filename, "PNG")


def pack_images_into_sheet(directory, sheet_filename):
    images = load_images_from_directory(directory)
    widths, heights = zip(*(i.size for i in images))
    max_width, max_height = max(widths), max(heights)

    sheet = create_image_sheet(images, max_width, max_height)
    save_image_sheet(sheet, sheet_filename)


if __name__ == "__main__":
    # pack_images_into_sheet("images", "sheet.png")
    pack_images_into_sheet("DFK Assests\\Export V8 (Rig-v0.1.8)\\Archer\\Bow Mastery\Bow mastery hero", "sheet.png")
