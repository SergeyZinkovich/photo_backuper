from datetime import datetime
import piexif
import os


def change_taken_date(filename, date, change_access_time=False):
    access_and_modification_time = (os.stat(filename).st_atime, os.stat(filename).st_mtime)

    new_date = date.strftime('%Y:%m:%d %H:%M:%S')

    exif_dict = piexif.load(filename)
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_dict['Exif'][piexif.ExifIFD.OffsetTime] = '+10:00'
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, filename)

    if not change_access_time:
        os.utime(filename, access_and_modification_time)


def change_taken_date_for_all(base_path, tree, date, change_access_time=False):
    for path, data in tree.items():
        for filename in data[1]:
            change_taken_date(os.path.join(base_path, path, filename), date, change_access_time)
