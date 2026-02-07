import sys
import os
import pytest
from pathlib import Path
import yaml

# Add scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts'))

from engine_sync import parse_canon_update

def test_parse_canon_update_valid_with_key(tmp_path):
    """Test parsing a valid canon update with 'canon_update' key."""
    content = """
Some text before the block.

```yaml
canon_update:
  scene_summary: "Test summary"
  characters:
    foo:
      status: "bar"
```

Some text after.
"""
    file_path = tmp_path / "test_session_1.md"
    file_path.write_text(content, encoding="utf-8")

    result = parse_canon_update(file_path)
    assert result is not None
    assert result['scene_summary'] == "Test summary"
    assert result['characters']['foo']['status'] == "bar"

def test_parse_canon_update_valid_without_key_in_yaml(tmp_path):
    """Test parsing a valid canon update where canon_update is mentioned in comment/text but not a root key."""
    # Pattern2 matches if "canon_update" string is present.
    # Pattern1 fails because it doesn't start with canon_update.
    content = """
```yaml
scene_summary: "Test summary"
# This is a canon_update
characters:
  foo:
    status: "bar"
```
"""
    file_path = tmp_path / "test_session_2.md"
    file_path.write_text(content, encoding="utf-8")

    result = parse_canon_update(file_path)
    assert result is not None
    assert result['scene_summary'] == "Test summary"
    # It returns the whole dict because 'canon_update' key is missing.

def test_parse_canon_update_mixed_case(tmp_path):
    """Test parsing with mixed case CANON_UPDATE."""
    content = """
```yaml
CANON_UPDATE:
  scene_summary: "Upper case test"
```
"""
    file_path = tmp_path / "test_session_3.md"
    file_path.write_text(content, encoding="utf-8")

    result = parse_canon_update(file_path)
    assert result is not None
    # Verify behavior: returns unwrapped dict because regex 1 matches and strips CANON_UPDATE
    assert 'scene_summary' in result
    assert result['scene_summary'] == "Upper case test"

def test_parse_canon_update_nested_canon_update(tmp_path):
    """Test parsing where canon_update is nested among other keys."""
    content = """
```yaml
other_key: value
canon_update:
  scene_summary: "Nested test"
```
"""
    file_path = tmp_path / "test_session_mixed.md"
    file_path.write_text(content, encoding="utf-8")

    result = parse_canon_update(file_path)
    assert result is not None
    # Should unwrap and return only contents of canon_update
    assert 'scene_summary' in result
    assert result['scene_summary'] == "Nested test"
    assert 'other_key' not in result

def test_parse_canon_update_invalid_yaml(tmp_path):
    """Test parsing invalid YAML."""
    content = """
```yaml
canon_update:
  [Invalid YAML]
  : -
```
"""
    file_path = tmp_path / "test_session_4.md"
    file_path.write_text(content, encoding="utf-8")

    result = parse_canon_update(file_path)
    assert result is None

def test_parse_canon_update_no_yaml(tmp_path):
    """Test file with no YAML block."""
    content = "Just some text."
    file_path = tmp_path / "test_session_5.md"
    file_path.write_text(content, encoding="utf-8")

    result = parse_canon_update(file_path)
    assert result is None

def test_parse_canon_update_file_not_found(tmp_path):
    """Test file not found."""
    file_path = tmp_path / "non_existent.md"
    result = parse_canon_update(file_path)
    assert result is None

def test_parse_canon_update_empty_file(tmp_path):
    """Test empty file."""
    file_path = tmp_path / "empty.md"
    file_path.touch()
    result = parse_canon_update(file_path)
    assert result is None
