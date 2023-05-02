import os
import unittest
import shutil
from src import type_converter
from main import get_tree, get_paths


class TestTypeConverter(unittest.TestCase):
    RESOURCES_DIR = './tests_resources/type_converter_resources'
    RESOURCES_TEMP_DIR = RESOURCES_DIR + '_temp'

    def setUp(self) -> None:
        shutil.copytree(self.RESOURCES_DIR, self.RESOURCES_TEMP_DIR)

    def tearDown(self) -> None:
        shutil.rmtree(self.RESOURCES_TEMP_DIR)

    def test_convert_all_to_jpeg(self):
        """
        Tests that convert_all_to_jpeg converts webp (not binary check) and file count has no changes
        """
        tree = get_tree(self.RESOURCES_TEMP_DIR)
        paths = get_paths(self.RESOURCES_TEMP_DIR, tree)

        type_converter.convert_all_to_jpeg(paths)

        paths = os.listdir(self.RESOURCES_TEMP_DIR)
        for i in paths:
            self.assertNotEqual(os.path.splitext(i)[1], '.webp')
        self.assertEqual(len(paths), 3)

    def test_change_alias_extension_for_all(self):
        """
        Tests change_alias_extension_to_jpeg
        """
        tree = get_tree(self.RESOURCES_TEMP_DIR)
        paths = get_paths(self.RESOURCES_TEMP_DIR, tree)

        type_converter.convert_all_to_jpeg(paths)
        type_converter.change_all_alias_extensions_to_jpeg(paths)

        paths = os.listdir(self.RESOURCES_TEMP_DIR)
        for i in paths:
            self.assertNotEqual(os.path.splitext(i)[1], 'webp')
            self.assertNotEqual(os.path.splitext(i)[1], 'JPG')
        self.assertEqual(len(paths), 3)


if __name__ == "__main__":
    unittest.main()
