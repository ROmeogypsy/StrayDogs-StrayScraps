import unittest
from unittest.mock import patch, mock_open, MagicMock
import sys
from pathlib import Path
from datetime import datetime

# Add the scripts directory to sys.path to import engine_sync
sys.path.append(str(Path(__file__).parent.parent / "scripts"))

import engine_sync

class TestUpdateCharacter(unittest.TestCase):

    @patch('engine_sync.find_character_file')
    def test_character_file_not_found(self, mock_find):
        """Test that update_character returns False if character file is not found."""
        mock_find.return_value = None
        result = engine_sync.update_character("Unknown Char", {}, "session_001")
        self.assertFalse(result)

    @patch('engine_sync.find_character_file')
    @patch('builtins.open', new_callable=mock_open, read_data="status: Alive\nlast_updated: 2023-01-01\ncanon_version: session_000\n## Current Status\nExisting status.")
    def test_update_status(self, mock_file, mock_find):
        """Test updating the status field."""
        mock_find.return_value = Path("dummy/path/char.md")

        changes = {'status': 'Deceased'}
        session_id = "session_001"

        result = engine_sync.update_character("Char Name", changes, session_id)

        self.assertTrue(result)

        # Check if file was opened for writing
        mock_file.assert_called_with(Path("dummy/path/char.md"), 'w', encoding='utf-8')

        # Get the written content
        handle = mock_file()
        written_content = handle.write.call_args[0][0]

        self.assertIn("status: Deceased", written_content)
        self.assertIn(f"canon_version: {session_id}", written_content)
        today = datetime.now().strftime('%Y-%m-%d')
        self.assertIn(f"last_updated: {today}", written_content)

    @patch('engine_sync.find_character_file')
    @patch('builtins.open', new_callable=mock_open, read_data="status: Alive\nlast_updated: 2023-01-01\ncanon_version: session_000\n## Current Status\nExisting status.")
    def test_update_note(self, mock_file, mock_find):
        """Test appending a note to the Current Status section."""
        mock_find.return_value = Path("dummy/path/char.md")

        changes = {'note': 'Something happened.'}
        session_id = "session_001"

        result = engine_sync.update_character("Char Name", changes, session_id)

        self.assertTrue(result)

        handle = mock_file()
        written_content = handle.write.call_args[0][0]

        expected_note = f"\n\n**Session {session_id}**: Something happened."
        self.assertIn(expected_note, written_content)

    @patch('engine_sync.find_character_file')
    @patch('builtins.open', new_callable=mock_open, read_data="status: Alive\nlast_updated: 2023-01-01\ncanon_version: session_000\n## Current Status\nExisting status.\n## Next Section")
    def test_update_note_with_next_section(self, mock_file, mock_find):
        """Test appending a note when there is a following section."""
        mock_find.return_value = Path("dummy/path/char.md")

        changes = {'note': 'Something happened.'}
        session_id = "session_001"

        result = engine_sync.update_character("Char Name", changes, session_id)

        self.assertTrue(result)

        handle = mock_file()
        written_content = handle.write.call_args[0][0]

        expected_note = f"Existing status.\n\n**Session {session_id}**: Something happened.\n## Next Section"
        self.assertIn(expected_note, written_content)

    @patch('engine_sync.find_character_file')
    @patch('builtins.open', side_effect=IOError("File permission denied"))
    def test_update_file_error(self, mock_file, mock_find):
        """Test handling of file I/O errors."""
        mock_find.return_value = Path("dummy/path/char.md")

        changes = {'status': 'Deceased'}
        session_id = "session_001"

        result = engine_sync.update_character("Char Name", changes, session_id)

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
