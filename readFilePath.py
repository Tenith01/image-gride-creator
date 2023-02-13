import os


def get_file_paths(dir_path):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            filePath = (os.path.join(root, file)).replace("../", "").split("\\")
            filePath = filePath[:-1][-1]
            file_paths.append(filePath)

    return file_paths[1:]


filePaths = get_file_paths("VFX flattened")
