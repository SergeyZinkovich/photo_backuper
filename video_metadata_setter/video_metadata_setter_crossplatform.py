import struct
from datetime import datetime

ATOM_HEADER_SIZE = 8
# Difference between Unix epoch and QuickTime epoch, in seconds
EPOCH_ADJUSTER = 2082844800


def get_video_taken_date(filename: str):
    f = open(filename, "rb+")
    date = _read_video_binary(f).strftime("%Y:%m:%d %H:%M:%S")
    f.close()

    return date


def change_video_taken_date(filename: str, new_date: datetime):
    f = open(filename, "rb+")

    _read_video_binary(f)

    f.seek(-4, 1)
    f.write(struct.pack(">I", int(new_date.timestamp() + EPOCH_ADJUSTER)))

    f.close()


def _read_video_binary(filestream):
    while True:
        atom_header = filestream.read(ATOM_HEADER_SIZE)
        if atom_header[4:8] == b'moov':
            break
        atom_size = struct.unpack(">I", atom_header[0:4])[0]
        filestream.seek(atom_size - 8, 1)

    atom_header = filestream.read(ATOM_HEADER_SIZE)
    if atom_header[4:8] == b'cmov':
        raise Exception("moov atom is compressed")
    elif atom_header[4:8] != b'mvhd':
        raise Exception("expected to find 'mvhd' header")
    else:
        filestream.seek(4, 1)
        creation_date = struct.unpack(">I", filestream.read(4))[0]

        if creation_date == 0:
            return None

        return datetime.fromtimestamp(creation_date - EPOCH_ADJUSTER)
