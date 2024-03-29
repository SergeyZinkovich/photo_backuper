from PIL import Image
import os


def images_equal(path1: str, path2: str):
    image1 = Image.open(path1)
    image2 = Image.open(path2)

    return list(image1.getdata()) == list(image2.getdata())


def duplicate_exists(base_path: str, folder_path: str, filename: str, paths: list):
    extension = os.path.splitext(filename)[-1]
    if extension not in ['.jpg', '.JPG', '.jpeg']:
        print(f'WARNING {os.path.join(base_path, folder_path, filename)} can\'t be checked by pixels')
        return False

    for path in paths:
        if path == folder_path:
            continue

        if images_equal(os.path.join(base_path, folder_path, filename), os.path.join(base_path, path, filename)):
            return True

    return False
