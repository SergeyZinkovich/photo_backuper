from PIL import Image
import os


def webp_to_jpeg(path):
    image = Image.open(path)

    image.convert('RGB')
    image.save('.'.join(path.split('.')[:-1]) + '.jpeg', 'jpeg')
    os.remove(image.filename)


def convert_all_to_jpeg(paths):
    for path in paths:
        if path.split('.')[1] == 'webp':
            webp_to_jpeg(path)
