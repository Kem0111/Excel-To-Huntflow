import os
import tempfile
import unittest
from src.utils.file_search import find_file_in_directory


class TestFindFileInDirectory(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_find_file_in_directory(self):
        # Arrange
        file_prefix = 'test'
        file_name = f'{file_prefix}_file.txt'
        file_path = os.path.join(self.temp_dir.name, file_name)

        with open(file_path, 'w') as f:
            f.write('Test content')

        # Act
        result = find_file_in_directory(self.temp_dir.name, file_prefix)

        # Assert
        self.assertEqual(result, file_path)

    def test_find_file_in_directory_no_file(self):
        # Arrange
        file_prefix = 'non_existent'

        # Act
        result = find_file_in_directory(self.temp_dir.name, file_prefix)

        # Assert
        self.assertIsNone(result)
