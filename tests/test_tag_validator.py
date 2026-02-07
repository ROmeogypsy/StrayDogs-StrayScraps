import unittest
from unittest.mock import patch, mock_open
import sys
import os
from pathlib import Path

# Add scripts directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

import tag_validator

class TestLoadValidTags(unittest.TestCase):

    @patch('pathlib.Path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_load_valid_tags_success(self, mock_file, mock_exists):
        # Both files exist
        mock_exists.side_effect = [True, True]

        # Mock file content
        # We need to handle open() being called with different files
        # The mock_open will return the same mock object by default, but we can change read_data?
        # No, mock_open is tricky with multiple files. Better to use side_effect on the mock_file object itself?

        def open_side_effect(filename, *args, **kwargs):
            if str(filename) == str(tag_validator.TAGS_FILE):
                return mock_open(read_data="#Tag1 #Tag2").return_value
            elif str(filename) == str(tag_validator.TAG_VARIATIONS_FILE):
                return mock_open(read_data="#Tag1Var #Tag3").return_value
            return mock_open(read_data="").return_value

        mock_file.side_effect = open_side_effect

        # Run function
        tags = tag_validator.load_valid_tags()

        # Verify
        expected = {"#Tag1", "#Tag2", "#Tag1Var", "#Tag3"}
        self.assertEqual(tags, expected)

    @patch('pathlib.Path.exists')
    def test_load_valid_tags_missing_tags_file(self, mock_exists):
        # TAGS_FILE missing
        mock_exists.side_effect = [False]

        # Run function
        tags = tag_validator.load_valid_tags()

        # Verify
        self.assertEqual(tags, set())

    @patch('pathlib.Path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data="#Tag1")
    def test_load_valid_tags_missing_variations_file(self, mock_file, mock_exists):
        # TAGS_FILE exists, TAG_VARIATIONS_FILE missing
        mock_exists.side_effect = [True, False]

        # Run function
        tags = tag_validator.load_valid_tags()

        # Verify
        self.assertEqual(tags, {"#Tag1"})

if __name__ == '__main__':
    unittest.main()
