import os
import unittest
import video_metadata_setter
from datetime import datetime, timezone
import shutil


class TestVideoMetadataSetter(unittest.TestCase):
    MP4_FILE_EXAMPLE = './tests_resources/metadata_setter_resources/mp4_example_1.mp4'

    def test_getter(self):
        taken_date = video_metadata_setter.get_video_taken_date(self.MP4_FILE_EXAMPLE)

        correct_date = datetime(2015, 8, 7, 9, 13, 2, tzinfo=timezone.utc).astimezone().strftime('%Y:%m:%d %H:%M:%S')
        self.assertEqual(taken_date, correct_date, f'Should be {correct_date}')

    def test_setter(self):
        # Check original date
        taken_date = video_metadata_setter.get_video_taken_date(self.MP4_FILE_EXAMPLE)

        correct_date = datetime(2015, 8, 7, 9, 13, 2, tzinfo=timezone.utc).astimezone().strftime('%Y:%m:%d %H:%M:%S')
        self.assertEqual(taken_date, correct_date, f'Should be {correct_date}')

        # Set new date
        new_date = datetime(2022, 4, 4, 2, 2, 2)
        video_metadata_setter.change_video_taken_date(self.MP4_FILE_EXAMPLE, new_date)

        # Check changed date
        taken_date = video_metadata_setter.get_video_taken_date(self.MP4_FILE_EXAMPLE)
        correct_date = new_date.strftime('%Y:%m:%d %H:%M:%S')
        self.assertEqual(taken_date, correct_date, f'Should be {correct_date}')

        # Set back original date
        new_date = datetime(2015, 8, 7, 15, 13, 2)
        video_metadata_setter.change_video_taken_date(self.MP4_FILE_EXAMPLE, new_date)

        # Check current date equal original
        taken_date = video_metadata_setter.get_video_taken_date(self.MP4_FILE_EXAMPLE)
        correct_date = new_date.strftime('%Y:%m:%d %H:%M:%S')
        self.assertEqual(taken_date, correct_date, f'Should be {correct_date}')

    def test_binary_integrity(self):
        f = open(self.MP4_FILE_EXAMPLE, 'rb')
        original_binary = f.read()
        f.close()

        def check_binary():
            f = open(self.MP4_FILE_EXAMPLE, 'rb')
            new_binary = f.read()
            f.close()

            self.assertEqual(original_binary, new_binary, f'Binary damaged')

        video_metadata_setter.get_video_taken_date(self.MP4_FILE_EXAMPLE)

        check_binary()

        new_date = datetime(2015, 8, 7, 15, 13, 2)
        video_metadata_setter.change_video_taken_date(self.MP4_FILE_EXAMPLE, new_date)

        check_binary()

        new_date = datetime(2010, 1, 2, 3, 4, 5)
        video_metadata_setter.change_video_taken_date(self.MP4_FILE_EXAMPLE, new_date)
        new_date = datetime(2015, 8, 7, 15, 13, 2)
        video_metadata_setter.change_video_taken_date(self.MP4_FILE_EXAMPLE, new_date)

        check_binary()

    def test_setter_for_empty_taken_date(self):
        # Create file copy
        mp4_temp_file_example = '.'.join(self.MP4_FILE_EXAMPLE.split('.')[:-1]) \
                                + '_temp.' \
                                + self.MP4_FILE_EXAMPLE.split('.')[-1]
        shutil.copy(self.MP4_FILE_EXAMPLE, mp4_temp_file_example)

        # Set taken date
        new_date = datetime(2015, 8, 7, 15, 13, 2)
        video_metadata_setter.change_video_taken_date(mp4_temp_file_example, new_date)

        # Check new date
        taken_date = video_metadata_setter.get_video_taken_date(mp4_temp_file_example)
        correct_date = new_date.strftime('%Y:%m:%d %H:%M:%S')
        self.assertEqual(taken_date, correct_date, f'Should be {correct_date}')

        # Delete temp file
        os.remove(mp4_temp_file_example)


if __name__ == '__main__':
    unittest.main()
