from sys import platform

# windows implementation disabled
if platform == "win32" and False:
    from video_metadata_setter.video_metadata_setter_windows import *
else:
    from video_metadata_setter.video_metadata_setter_crossplatform import *
