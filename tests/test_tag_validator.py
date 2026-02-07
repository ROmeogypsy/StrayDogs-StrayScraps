import unittest
from unittest.mock import patch, mock_open
from pathlib import Path
import sys
import os

# Ensure scripts dir is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.tag_validator import extract_tags_from_file

class TestExtractTags(unittest.TestCase):
    def test_yaml_tags(self):
        content = """---
tags:
  - #Tag1
  - #Tag2
---
"""
        with patch("builtins.open", mock_open(read_data=content)):
            tags = extract_tags_from_file(Path("dummy.md"))
            self.assertEqual(tags, {"#Tag1", "#Tag2"})

    def test_inline_tags(self):
        content = """
# Title
This is a #Tag3.
Another #Tag4?
"""
        with patch("builtins.open", mock_open(read_data=content)):
            tags = extract_tags_from_file(Path("dummy.md"))
            self.assertEqual(tags, {"#Tag3", "#Tag4"})

    def test_mixed_tags(self):
        content = """---
tags:
  - #Tag1
---
Some #Tag2 here.
"""
        with patch("builtins.open", mock_open(read_data=content)):
            tags = extract_tags_from_file(Path("dummy.md"))
            self.assertEqual(tags, {"#Tag1", "#Tag2"})

    def test_no_tags(self):
        content = "Just some text."
        with patch("builtins.open", mock_open(read_data=content)):
            tags = extract_tags_from_file(Path("dummy.md"))
            self.assertEqual(tags, set())

    def test_punctuation(self):
        content = "Tags: #Tag1, #Tag2. And #Tag3!"
        with patch("builtins.open", mock_open(read_data=content)):
            tags = extract_tags_from_file(Path("dummy.md"))
            self.assertEqual(tags, {"#Tag1", "#Tag2", "#Tag3"})

    def test_code_blocks_and_urls(self):
        # This test ensures we DON'T extract invalid tags like hex codes or anchors
        content = """
Check this link: [Link](#anchor).
Color:#fff.
Code block:
```python
# comment
color = "#abc"
```
"""
        with patch("builtins.open", mock_open(read_data=content)):
            tags = extract_tags_from_file(Path("dummy.md"))
            # With current implementation, these will likely be extracted.
            # I want to assert they are NOT extracted once fixed.
            unexpected_tags = {"#anchor", "#fff", "#abc", "#comment"}
            found_tags = tags.intersection(unexpected_tags)
            self.assertEqual(found_tags, set(), f"Found unexpected tags: {found_tags}")

    def test_read_error(self):
        with patch("builtins.open", side_effect=IOError("File not found")):
            # Mock print to suppress output
            with patch("builtins.print") as mock_print:
                tags = extract_tags_from_file(Path("dummy.md"))
                self.assertEqual(tags, set())
                mock_print.assert_called()

if __name__ == "__main__":
    unittest.main()
