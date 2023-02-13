import os


def remove_duplicates(my_list):
    return list(set(my_list))


def get_file_paths(dir_path):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            filePath = (os.path.join(root, file)).replace("../", "").split("\\")
            filePath = filePath[:-1][-1]
            file_paths.append(filePath)

    return remove_duplicates(file_paths[1:])


filePaths = get_file_paths("VFX flattened")
print(filePaths)