import random
import PIL
from PIL import Image, ImageDraw, ImageFont


def generate_image(width, height, text, font, font_size, text_color, background_color, border_width, border_color):
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font, font_size)
    text_width, text_height = draw.textsize(text, font)
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    draw.text((x, y), text, font=font, fill=text_color)
    border_width_half = int(border_width / 2)
    image = image.crop((border_width_half, border_width_half, width - border_width_half, height - border_width_half))
    border = Image.new("RGB", (width, height), border_color)
    border.paste(image, (border_width_half, border_width_half))
    return border


def save_image(image, filename):
    image.save(filename, "PNG")


if __name__ == "__main__":
    width = 500
    height = 500
    font = "arial.ttf"
    font_size = 100
    text_color = (0, 0, 0)
    border_width = 50
    for i in range(16):
        background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        text = str(i)
        image = generate_image(width, height, text, font, font_size, text_color, background_color, border_width,
                               border_color)
        filename = "images/image_{}.png".format(i)
        save_image(image, filename)
