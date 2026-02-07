import unittest
import tempfile
import shutil
from pathlib import Path
import sys
import os

# Ensure scripts can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.engine_sync import find_character_file

class TestFindCharacterFile(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.chars_dir = Path(self.test_dir)

        # Create dummy character files
        (self.chars_dir / "scraps_harper.md").touch()
        (self.chars_dir / "some_character.md").touch()

        # Create subdirectory and file in it
        subdir = self.chars_dir / "subdir"
        subdir.mkdir()
        (subdir / "other_char.md").touch()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_alias_lookup(self):
        # 'Scraps' should resolve to 'scraps_harper.md'
        result = find_character_file('Scraps', chars_dir=self.chars_dir)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, 'scraps_harper.md')

    def test_direct_match(self):
        # 'Some Character' should resolve to 'some_character.md'
        result = find_character_file('Some Character', chars_dir=self.chars_dir)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, 'some_character.md')

    def test_subdirectory_search(self):
        # 'Other Char' should resolve to 'subdir/other_char.md'
        result = find_character_file('Other Char', chars_dir=self.chars_dir)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, 'other_char.md')
        self.assertEqual(result.parent.name, 'subdir')

    def test_not_found(self):
        # 'Unknown' should return None
        result = find_character_file('Unknown', chars_dir=self.chars_dir)
        self.assertIsNone(result)

    def test_alias_not_found(self):
        # 'Big 9' is in alias map but file doesn't exist in our mock
        # Should return None (or warn, but returns None in code)
        result = find_character_file('Big 9', chars_dir=self.chars_dir)
        self.assertIsNone(result)

    def test_chars_dir_not_exists(self):
        # Should handle missing directory gracefully
        non_existent_dir = Path(self.test_dir) / "non_existent"
        result = find_character_file('Any', chars_dir=non_existent_dir)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
