from PIL import Image
import os
from pillow_heif import register_heif_opener
import moviepy.editor as moviepy

register_heif_opener()


def webp_to_jpeg(path: str):
    image = Image.open(path)

    image.convert('RGB')
    image.save(os.path.splitext(path)[0] + '.jpeg', 'jpeg')
    os.remove(image.filename)


def heic_to_jpeg(path: str):
    image = Image.open(path)

    image.convert('RGB')
    image.save(os.path.splitext(path)[0] + '.jpeg', 'jpeg')
    os.remove(image.filename)


def mov_to_mp4(path: str):
    clip = moviepy.VideoFileClip(path)
    clip.write_videofile(os.path.splitext(path)[0] + '.mp4')
    os.remove(path)


def change_alias_extension_to_jpeg(path: str):
    os.rename(
        os.path.join(path),
        os.path.splitext(path)[0] + '.jpeg'
    )


def convert_all(paths: list):
    for path in paths:
        if os.path.splitext(path)[1] == '.webp':
            webp_to_jpeg(path)
        elif os.path.splitext(path)[1] == '.HEIC':
            heic_to_jpeg(path)
        elif os.path.splitext(path)[1] in ['.mov', '.MOV']:
            mov_to_mp4(path)


def change_all_alias_extensions_to_jpeg(paths: list):
    for path in paths:
        if os.path.splitext(path)[1] in ['.JPG', '.jpg']:
            change_alias_extension_to_jpeg(path)
