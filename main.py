import math
import os
from PIL import Image


def load_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        try:
            image = Image.open(os.path.join(directory, filename))
            images.append(image)
        except Exception as e:
            print("Failed to load image:", filename)
            print("Error:", e)
    return images


def create_image_sheet(images, sheet_width, sheet_height):
    n = len(images)
    print(n)
    rows = math.ceil(math.sqrt(n))
    # cols = math.ceil(n / rows)
    cols = math.ceil(rows)
    cell_width = sheet_width // cols
    cell_height = sheet_height // rows
    sheet = Image.new("RGBA", (sheet_width, sheet_height), (255, 255, 255, 0))
    for i, image in enumerate(images):
        x = (i % cols) * cell_width
        y = (i // cols) * cell_height
        image = image.resize((cell_width, cell_height), Image.ANTIALIAS)
        sheet.paste(image, (x, y))
    return sheet


def save_image_sheet(sheet, filename):
    sheet.save(filename, "PNG")


def pack_images_into_sheet(directory, sheet_filename):
    images = load_images_from_directory(directory)
    widths, heights = zip(*(i.size for i in images))
    max_width, max_height = max(widths), max(heights)
    sheet_width = max_width * len(images)
    sheet_height = max_height * len(images)
    sheet = create_image_sheet(images, sheet_width, sheet_height)
    save_image_sheet(sheet, sheet_filename)


if __name__ == "__main__":
    pack_images_into_sheet("images", "sheet.png")
