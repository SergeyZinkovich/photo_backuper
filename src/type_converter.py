from PIL import Image
import os


def webp_to_jpeg(path: str):
    image = Image.open(path)

    image.convert('RGB')
    image.save(os.path.splitext(path)[0] + '.jpeg', 'jpeg')
    os.remove(image.filename)


def change_alias_extension_to_jpeg(path: str):
    os.rename(
        os.path.join(path),
        os.path.splitext(path)[0] + '.jpeg'
    )


def convert_all_to_jpeg(paths: list):
    for path in paths:
        if os.path.splitext(path)[1] == '.webp':
            webp_to_jpeg(path)


def change_all_alias_extensions_to_jpeg(paths: list):
    for path in paths:
        if os.path.splitext(path)[1] in ['.JPG', '.jpg']:
            change_alias_extension_to_jpeg(path)
