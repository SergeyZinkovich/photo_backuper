from datetime import datetime
import piexif
import os
import pythoncom
from win32com.propsys import propsys, pscon
from win32com.shell import shellcon


def change_photo_taken_date(filename: str, taken_date: datetime, timezone: str = '+10:00'):
    new_date = taken_date.strftime('%Y:%m:%d %H:%M:%S')

    exif_dict = piexif.load(filename)
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_dict['Exif'][piexif.ExifIFD.OffsetTime] = timezone

    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, filename)


def change_video_taken_date(filename: str, taken_date: datetime):
    properties = propsys.SHGetPropertyStoreFromParsingName(filename, None, shellcon.GPS_READWRITE,
                                                           propsys.IID_IPropertyStore)

    properties.SetValue(pscon.PKEY_Media_DateEncoded, propsys.PROPVARIANTType(taken_date, pythoncom.VT_DATE))
    properties.Commit()


def change_taken_date(filename: str, taken_date: datetime, change_access_time: bool = False,
                      set_taken_date_to_access_time: bool = True):
    if os.path.splitext(filename)[-1] in ['.jpg', '.JPG']:
        func = change_photo_taken_date
    if os.path.splitext(filename)[-1] in ['.mp4', '.MOV', '.3gp']:
        func = change_video_taken_date

    access_and_modification_time = (os.stat(filename).st_atime, os.stat(filename).st_mtime)

    func(filename, taken_date)

    if not change_access_time:
        os.utime(filename, access_and_modification_time)

    if set_taken_date_to_access_time:
        os.utime(filename, (taken_date.timestamp(), taken_date.timestamp()))


def change_taken_date_for_all(base_path: str, tree: dict, taken_date: datetime, change_access_time: bool = False,
                              set_taken_date_to_access_time: bool = True):
    for path, data in tree.items():
        for filename in data[1]:
            change_taken_date(os.path.join(base_path, path, filename), taken_date, change_access_time,
                              set_taken_date_to_access_time)
