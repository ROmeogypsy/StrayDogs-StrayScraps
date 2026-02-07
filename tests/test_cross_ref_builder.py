import unittest
from pathlib import Path
import sys
import os
import tempfile
import shutil

# Add scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import cross_ref_builder

class TestCrossReferenceBuilderIntegration(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.chars_dir = Path(self.test_dir) / "chars"
        self.chars_dir.mkdir()

        # Monkeypatch CHARS_DIR in the module
        self.original_chars_dir = cross_ref_builder.CHARS_DIR
        cross_ref_builder.CHARS_DIR = self.chars_dir

        # Register cleanup
        self.addCleanup(shutil.rmtree, self.test_dir)
        self.addCleanup(self.restore_chars_dir)

    def restore_chars_dir(self):
        cross_ref_builder.CHARS_DIR = self.original_chars_dir

    def create_char_file(self, filename, content):
        p = self.chars_dir / filename
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)

    def test_bidirectional_relationship(self):
        """Test that relationships are bidirectional"""
        self.create_char_file("char1.md", """---
tags:
  character:
    - #Char1
  relationships:
    - #Char2
---
# Char 1
""")
        self.create_char_file("char2.md", """---
tags:
  character:
    - #Char2
  relationships:
    - #Char3
---
# Char 2
""")

        result = cross_ref_builder.build_relationship_map()

        # Char1 -> Char2 implies Char2 -> Char1
        self.assertIn('#Char1', result)
        self.assertIn('#Char2', result['#Char1'])
        self.assertIn('#Char2', result)
        self.assertIn('#Char1', result['#Char2'])

        # Char2 -> Char3 implies Char3 -> Char2
        self.assertIn('#Char3', result['#Char2'])
        self.assertIn('#Char3', result)
        self.assertIn('#Char2', result['#Char3'])

    def test_ignore_files(self):
        """Test that files starting with 00_ are ignored"""
        self.create_char_file("00_index.md", """---
tags:
  character:
    - #IgnoredChar
  relationships:
    - #Char1
---
""")
        self.create_char_file("char1.md", """---
tags:
  character:
    - #Char1
---
""")

        result = cross_ref_builder.build_relationship_map()

        self.assertNotIn('#IgnoredChar', result)

        if '#Char1' in result:
             self.assertNotIn('#IgnoredChar', result['#Char1'])

    def test_missing_tags(self):
        """Test handling of files with missing tags"""
        # File with no character tag
        self.create_char_file("no_char_tag.md", """---
tags:
  relationships:
    - #Char1
---
""")
        # File with character tag but no relationships
        self.create_char_file("isolated.md", """---
tags:
  character:
    - #Isolated
---
""")

        result = cross_ref_builder.build_relationship_map()

        # Isolated char -> no 'relationships' key -> skipped loop
        self.assertNotIn('#Isolated', result)

        # Verify result is empty as no valid relationships exist
        self.assertEqual(len(result), 0)

    def test_multiple_relationships(self):
        """Test a character with multiple relationships"""
        self.create_char_file("poly.md", """---
tags:
  character:
    - #Poly
  relationships:
    - #Char1
    - #Char2
---
""")

        result = cross_ref_builder.build_relationship_map()

        self.assertIn('#Poly', result)
        self.assertIn('#Char1', result['#Poly'])
        self.assertIn('#Char2', result['#Poly'])

        # Check reverse
        self.assertIn('#Poly', result['#Char1'])
        self.assertIn('#Poly', result['#Char2'])

if __name__ == '__main__':
    unittest.main()
