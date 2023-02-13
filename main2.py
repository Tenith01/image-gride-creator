import os
import math
import numpy as np
import cv2

def get_images(dir_path):
    images = []
    for filename in os.listdir(dir_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = cv2.imread(os.path.join(dir_path, filename))
            images.append(image)
    return images

def create_sprite_sheet(images, sprite_sheet_size=(1024,1024)):
    # Create an empty sprite sheet
    max_width = 0
    total_height = 0
    for image in images:
        max_width = max(max_width, image.shape[1])
        total_height += image.shape[0]
    sprite_sheet = np.zeros((total_height, max_width, 3), np.uint8)

    # Copy the images onto the sprite sheet
    y = 0
    for image in images:
        h, w = image.shape[:2]
        x1 = 0
        y1 = y
        x2 = x1 + w
        y2 = y1 + h
        sprite_sheet[y1:y2, x1:x2] = image
        y += h

    return sprite_sheet

if __name__ == "__main__":
    # Load all images from the "images" directory
    images = get_images("images")

    # Create the sprite sheet
    sprite_sheet = create_sprite_sheet(images)

    # Save the sprite sheet as a PNG image
    cv2.imwrite("sprite_sheet.png", sprite_sheet)