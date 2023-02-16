import os
import unittest
import shutil
from src import file_processor


class TestEmptyDirsDeletion(unittest.TestCase):
    RESOURCES_TEST_DIR = './tests_resources/file_processor_resources/test'
    RESOURCES_ANS_DIR = './tests_resources/file_processor_resources/correct'

    def setUp(self) -> None:
        def create_file(path):
            f = open(path, 'w')
            f.close()

        shutil.rmtree(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1'), ignore_errors=True)
        shutil.rmtree(os.path.join(self.RESOURCES_ANS_DIR, 'test_dir_1'), ignore_errors=True)

        # Test tree
        os.makedirs(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1'))
        os.makedirs(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1', 'test_dir_2'))
        os.makedirs(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1', 'test_dir_3'))
        os.makedirs(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1', 'test_dir_4'))

        os.makedirs(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1', 'test_dir_2', 'test_dir_5'))
        os.makedirs(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1', 'test_dir_2', 'test_dir_6'))
        create_file(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1', 'test_dir_2', 'test_file_1.txt'))

        create_file(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1', 'test_dir_3', 'test_file_2.txt'))
        create_file(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1', 'test_dir_3', 'test_file_3.txt'))

        # Correct tree
        os.makedirs(os.path.join(self.RESOURCES_ANS_DIR, 'test_dir_1'))
        os.makedirs(os.path.join(self.RESOURCES_ANS_DIR, 'test_dir_1', 'test_dir_2'))
        os.makedirs(os.path.join(self.RESOURCES_ANS_DIR, 'test_dir_1', 'test_dir_3'))

        create_file(os.path.join(self.RESOURCES_ANS_DIR, 'test_dir_1', 'test_dir_2', 'test_file_1.txt'))

        create_file(os.path.join(self.RESOURCES_ANS_DIR, 'test_dir_1', 'test_dir_3', 'test_file_2.txt'))
        create_file(os.path.join(self.RESOURCES_ANS_DIR, 'test_dir_1', 'test_dir_3', 'test_file_3.txt'))

    def tearDown(self) -> None:
        shutil.rmtree(os.path.join(self.RESOURCES_TEST_DIR, 'test_dir_1'))
        shutil.rmtree(os.path.join(self.RESOURCES_ANS_DIR, 'test_dir_1'))

    def test_dis_deletion(self):
        """
        Tests delete_empty_dirs
        """
        file_processor.delete_empty_dirs(self.RESOURCES_TEST_DIR)

        test_tree = file_processor.get_tree(self.RESOURCES_TEST_DIR)
        correct_tree = file_processor.get_tree(self.RESOURCES_ANS_DIR)

        self.assertEqual(test_tree, correct_tree)


if __name__ == "__main__":
    unittest.main()
