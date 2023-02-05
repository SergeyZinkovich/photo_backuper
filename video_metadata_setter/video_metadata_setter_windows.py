from datetime import datetime
import pythoncom
from win32com.propsys import propsys, pscon
from win32com.shell import shellcon


def get_video_taken_date(filename: str):
    properties = propsys.SHGetPropertyStoreFromParsingName(filename, None, shellcon.GPS_READWRITE,
                                                           propsys.IID_IPropertyStore)

    if properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue():
        properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()

    return None


def change_video_taken_date(filename: str, taken_date: datetime):
    properties = propsys.SHGetPropertyStoreFromParsingName(filename, None, shellcon.GPS_READWRITE,
                                                           propsys.IID_IPropertyStore)

    properties.SetValue(pscon.PKEY_Media_DateEncoded, propsys.PROPVARIANTType(taken_date, pythoncom.VT_DATE))
    properties.Commit()
