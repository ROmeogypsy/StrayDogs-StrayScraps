import unittest
from unittest.mock import MagicMock, patch, mock_open
import sys
from pathlib import Path
import re

# Add repo root to path so we can import scripts
repo_root = Path(__file__).parent.parent
sys.path.append(str(repo_root))

from scripts.engine_sync import update_tension, update_character

class TestEngineSync(unittest.TestCase):
    def setUp(self):
        # Mock TENSIONS_DIR to avoid filesystem access
        self.tensions_dir_patcher = patch('scripts.engine_sync.TENSIONS_DIR')
        self.mock_tensions_dir = self.tensions_dir_patcher.start()

        # Sample markdown content for a tension file
        self.sample_content = """---
title: Scraps Integration
status: active
last_updated: 2026-02-01
canon_version: 001
---

# Scraps Integration

## Overview
Scraps is trying to fit in.

## Recent Developments
**Session 001**: Scraps joined the Dogs.
"""

    def tearDown(self):
        self.tensions_dir_patcher.stop()

    def test_update_tension_status(self):
        """Test updating the status of a tension."""
        tension_name = "Scraps Integration"
        changes = {"status": "resolved"}
        session_id = "002"

        # Mock file existence
        mock_file_path = self.mock_tensions_dir / "scraps_integration.md"
        mock_file_path.exists.return_value = True

        # Mock file opening and reading/writing
        m = mock_open(read_data=self.sample_content)
        with patch('builtins.open', m):
            result = update_tension(tension_name, changes, session_id)

            self.assertTrue(result)

            # Verify file was written
            m().write.assert_called()

            # Get the written content. Note: write might be called multiple times or once with full content.
            # In update_tension, it reads all, replaces, writes all.
            written_content = m().write.call_args[0][0]

            # Verify status update
            self.assertIn("status: resolved", written_content)
            # Verify last_updated update (we check if it changed, not exact date)
            self.assertNotIn("last_updated: 2026-02-01", written_content)
            self.assertRegex(written_content, r"last_updated: \d{4}-\d{2}-\d{2}")

    def test_update_tension_development(self):
        """Test appending a development to a tension."""
        tension_name = "Scraps Integration"
        changes = {"development": "Scraps proved her worth."}
        session_id = "002"

        mock_file_path = self.mock_tensions_dir / "scraps_integration.md"
        mock_file_path.exists.return_value = True

        m = mock_open(read_data=self.sample_content)
        with patch('builtins.open', m):
            result = update_tension(tension_name, changes, session_id)

            self.assertTrue(result)

            written_content = m().write.call_args[0][0]

            # Verify development appended
            expected_dev = "**Session 002**: Scraps proved her worth."
            self.assertIn(expected_dev, written_content)
            # Verify it's under Recent Developments
            self.assertIn("## Recent Developments", written_content)

    def test_update_tension_file_not_found(self):
        """Test handling when tension file does not exist."""
        tension_name = "Nonexistent Tension"
        changes = {"status": "resolved"}
        session_id = "002"

        # Setup mock behavior for path joining
        mock_file_path = MagicMock()
        mock_file_path.exists.return_value = False
        self.mock_tensions_dir.__truediv__.return_value = mock_file_path

        # We also need to patch print so we don't spam stdout
        with patch('builtins.print') as mock_print:
            result = update_tension(tension_name, changes, session_id)

            self.assertFalse(result)
            mock_print.assert_called()
            args, _ = mock_print.call_args
            self.assertIn("Warning: Tension file not found", args[0])

    def test_update_tension_exception(self):
        """Test handling of exceptions during update."""
        tension_name = "Scraps Integration"
        changes = {"status": "resolved"}
        session_id = "002"

        mock_file_path = self.mock_tensions_dir / "scraps_integration.md"
        mock_file_path.exists.return_value = True

        # Mock open to raise exception
        with patch('builtins.open', side_effect=PermissionError("Permission denied")):
            with patch('builtins.print') as mock_print:
                result = update_tension(tension_name, changes, session_id)

                self.assertFalse(result)
                mock_print.assert_called()
                args, _ = mock_print.call_args
                self.assertIn("Error updating tension", args[0])

    def test_update_character_success(self):
        """Test updating a character works and doesn't have regex replacement issues."""
        char_name = "Stray"
        changes = {"status": "Alive"} # last_updated is handled internally by function
        session_id = "002"

        # Mock find_character_file
        with patch('scripts.engine_sync.find_character_file') as mock_find:
            mock_path = MagicMock()
            mock_find.return_value = mock_path

            sample_char_content = """---
name: Stray
status: Unknown
last_updated: 2020-01-01
canon_version: 000
---
"""
            m = mock_open(read_data=sample_char_content)
            with patch('builtins.open', m):
                result = update_character(char_name, changes, session_id)
                self.assertTrue(result)

                written = m().write.call_args[0][0]
                self.assertIn("status: Alive", written)
                # Verify replacement of last_updated worked correctly (no P issue)
                self.assertRegex(written, r"last_updated: \d{4}-\d{2}-\d{2}")
                # Verify canon_version
                self.assertIn("canon_version: 002", written)

if __name__ == '__main__':
    unittest.main()
