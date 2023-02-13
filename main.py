from readFilePath import get_file_paths
from spriteCreator import pack_images_into_sheet

filePaths = get_file_paths("VFX flattened")

for filePath in filePaths:
    print(filePath)
    if __name__ == "__main__":
        # pack_images_into_sheet("images", "sheet.png")
        pack_images_into_sheet("VFX flattened\\" + str(filePath), "VFX flattened Sprite heets\\" + str(filePath)+".png")
