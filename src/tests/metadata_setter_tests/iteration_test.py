import unittest
import shutil
from src import metadata_setter
from datetime import datetime
from main import get_tree, get_paths


class TestMetadataSetter(unittest.TestCase):
    RESOURCES_DIR = './tests_resources/metadata_setter_resources'
    RESOURCES_TEMP_DIR = RESOURCES_DIR + '_temp'

    def _create_resources_dir_copy(self):
        shutil.copytree(self.RESOURCES_DIR, self.RESOURCES_TEMP_DIR)

    def _remove_resources_dir_copy(self):
        shutil.rmtree(self.RESOURCES_TEMP_DIR)

    def test_change_date_for_all(self):
        """
        Tests that change_taken_date_for_all dont raise any exception
        """
        self._create_resources_dir_copy()

        tree = get_tree(self.RESOURCES_TEMP_DIR)
        paths = get_paths(self.RESOURCES_TEMP_DIR, tree)

        new_date = datetime(2015, 8, 7, 15, 13, 2)
        metadata_setter.change_taken_date_for_all(paths, new_date)

        self._remove_resources_dir_copy()


if __name__ == "__main__":
    unittest.main()
