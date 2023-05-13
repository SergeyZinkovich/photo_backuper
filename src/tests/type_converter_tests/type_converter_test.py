import os
import unittest
import shutil
from src.executor import type_converter_executor


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
        type_converter_executor.convert_all_to_jpeg(self.RESOURCES_TEMP_DIR)

        paths = os.listdir(self.RESOURCES_TEMP_DIR)
        for i in paths:
            self.assertNotEqual(os.path.splitext(i)[1], '.webp')
        self.assertEqual(len(paths), 3)

    def test_change_alias_extension_for_all(self):
        """
        Tests change_alias_extension_to_jpeg
        """
        type_converter_executor.convert_all_to_jpeg(self.RESOURCES_TEMP_DIR)
        type_converter_executor.change_all_alias_extensions_to_jpeg(self.RESOURCES_TEMP_DIR)

        paths = os.listdir(self.RESOURCES_TEMP_DIR)
        for i in paths:
            self.assertNotEqual(os.path.splitext(i)[1], 'webp')
            self.assertNotEqual(os.path.splitext(i)[1], 'JPG')
        self.assertEqual(len(paths), 3)


if __name__ == "__main__":
    unittest.main()
