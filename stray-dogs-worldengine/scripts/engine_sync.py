#!/usr/bin/env python3
"""
Engine Sync for Stray Dogs Worldengine
Monitors session files and updates canon based on CANON_UPDATE YAML blocks
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional
import time

# Configuration
REPO_ROOT = Path(__file__).parent.parent
SESSIONS_DIR = REPO_ROOT / "sessions"
CHARS_DIR = REPO_ROOT / "chars"
TENSIONS_DIR = REPO_ROOT / "tensions"
EVENTS_DIR = REPO_ROOT / "events"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def parse_canon_update(session_file: Path) -> Optional[Dict[str, Any]]:
    """Extract CANON_UPDATE YAML block from session file"""
    try:
        with open(session_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find CANON_UPDATE or canon_update YAML block
        # Pattern: ```yaml\ncanon_update: or CANON_UPDATE:
        pattern = r'```yaml\s*(?:canon_update|CANON_UPDATE)[:]*\s*\n(.*?)\n```'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

        if not match:
            # Try alternative format (just yaml block with canon_update key)
            pattern2 = r'```yaml\s*\n(.*?canon_update.*?)\n```'
            match = re.search(pattern2, content, re.DOTALL | re.IGNORECASE)

        if not match:
            return None

        yaml_content = match.group(1)
        canon_data = yaml.safe_load(yaml_content)

        # If it's wrapped in canon_update key, unwrap it
        if isinstance(canon_data, dict) and 'canon_update' in canon_data:
            canon_data = canon_data['canon_update']

        return canon_data

    except Exception as e:
        print(f"{Colors.RED}Error parsing {session_file}: {e}{Colors.RESET}")
        return None

def find_character_file(char_name: str) -> Optional[Path]:
    """Search for character file by name (handles aliases)"""
    # Common aliases
    alias_map = {
        'Scraps': 'scraps_harper.md',
        'Harper': 'scraps_harper.md',
        'Big 9': 'big_9.md',
        'Big Nine': 'big_9.md',
        'Chew-toy': 'chew_toy.md',
        'Chewtoy': 'chew_toy.md',
        'K-9': 'k9_kian_nines.md',
        'K9': 'k9_kian_nines.md',
        'Kian': 'k9_kian_nines.md',
        'Z-Artist': 'zed_kidd.md',
        'ZArtist': 'zed_kidd.md',
        'Zed Kidd': 'zed_kidd.md',
    }

    # Check alias map first
    if char_name in alias_map:
        filename = alias_map[char_name]
    else:
        # Convert to snake_case filename
        filename = char_name.lower().replace(' ', '_').replace('-', '_') + '.md'

    # Search all character subdirectories
    for subdir in CHARS_DIR.iterdir():
        if subdir.is_dir():
            filepath = subdir / filename
            if filepath.exists():
                return filepath

    # Try direct in chars/
    filepath = CHARS_DIR / filename
    if filepath.exists():
        return filepath

    print(f"{Colors.YELLOW}Warning: Character file not found for '{char_name}'{Colors.RESET}")
    return None

def update_character(char_name: str, changes: Dict[str, Any], session_id: str) -> bool:
    """Update character markdown file with new status/changes"""
    char_file = find_character_file(char_name)
    if not char_file:
        return False

    try:
        with open(char_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update YAML frontmatter
        if 'status' in changes:
            content = re.sub(
                r'(status:\s*).*',
                f"\\1{changes['status']}",
                content
            )

        # Update last_updated
        content = re.sub(
            r'(last_updated:\s*).*',
            f"\\1{datetime.now().strftime('%Y-%m-%d')}",
            content
        )

        # Update canon_version
        content = re.sub(
            r'(canon_version:\s*).*',
            f"\\1{session_id}",
            content
        )

        # Append to Current Status section if note provided
        if 'note' in changes:
            # Find Current Status section
            status_pattern = r'(## Current Status.*?)(\n## |\Z)'

            def add_note(match):
                section = match.group(1)
                next_section = match.group(2)
                note = f"\n\n**Session {session_id}**: {changes['note']}"
                return section + note + next_section

            content = re.sub(status_pattern, add_note, content, flags=re.DOTALL)

        # Write updated content
        with open(char_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"{Colors.GREEN}✓ Updated {char_name}{Colors.RESET}")
        return True

    except Exception as e:
        print(f"{Colors.RED}Error updating {char_name}: {e}{Colors.RESET}")
        return False

def update_tension(tension_name: str, changes: Dict[str, Any], session_id: str) -> bool:
    """Update tension markdown file with new developments"""
    # Convert name to filename
    filename = tension_name.lower().replace(' ', '_') + '.md'
    tension_file = TENSIONS_DIR / filename

    if not tension_file.exists():
        print(f"{Colors.YELLOW}Warning: Tension file not found for '{tension_name}'{Colors.RESET}")
        return False

    try:
        with open(tension_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update status in YAML
        if 'status' in changes:
            content = re.sub(
                r'(status:\s*).*',
                f"\\1{changes['status']}",
                content
            )

        # Update last_updated
        content = re.sub(
            r'(last_updated:\s*).*',
            f"\\1{datetime.now().strftime('%Y-%m-%d')}",
            content
        )

        # Append development to Recent Developments section
        if 'development' in changes:
            dev_pattern = r'(## Recent Developments.*?)(\n## |\Z)'

            def add_development(match):
                section = match.group(1)
                next_section = match.group(2)
                dev = f"\n\n**Session {session_id}**: {changes['development']}"
                return section + dev + next_section

            content = re.sub(dev_pattern, add_development, content, flags=re.DOTALL)

        with open(tension_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"{Colors.GREEN}✓ Updated tension: {tension_name}{Colors.RESET}")
        return True

    except Exception as e:
        print(f"{Colors.RED}Error updating tension {tension_name}: {e}{Colors.RESET}")
        return False

def apply_canon_updates(canon_data: Dict[str, Any], session_id: str):
    """Apply all canon updates from session"""
    print(f"\n{Colors.BLUE}Applying canon updates from {session_id}...{Colors.RESET}\n")

    updates_applied = 0

    # Update characters
    if 'characters' in canon_data:
        for char_name, changes in canon_data['characters'].items():
            if update_character(char_name, changes, session_id):
                updates_applied += 1

    # Update tensions
    if 'tensions' in canon_data:
        for tension_name, changes in canon_data['tensions'].items():
            if update_tension(tension_name, changes, session_id):
                updates_applied += 1

    # Create new events if specified
    if 'new_events' in canon_data:
        for event in canon_data['new_events']:
            # This would create new event files - simplified for now
            print(f"{Colors.BLUE}→ New event logged: {event.get('title', 'Unnamed Event')}{Colors.RESET}")
            updates_applied += 1

    print(f"\n{Colors.GREEN}Applied {updates_applied} canon update(s){Colors.RESET}")
    return updates_applied

def git_commit(session_id: str, summary: str):
    """Commit changes to git"""
    try:
        # Git add all changes
        os.system('git add .')

        # Create commit message
        commit_msg = f"Update canon: Session {session_id}\n\n{summary}"
        os.system(f'git commit -m "{commit_msg}"')

        print(f"{Colors.GREEN}✓ Git commit created{Colors.RESET}")

    except Exception as e:
        print(f"{Colors.RED}Git commit failed: {e}{Colors.RESET}")

def process_session_file(session_file: Path):
    """Process a single session file"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BLUE}Processing: {session_file.name}{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*60}{Colors.RESET}")

    canon_data = parse_canon_update(session_file)

    if not canon_data:
        print(f"{Colors.YELLOW}No CANON_UPDATE block found{Colors.RESET}")
        return

    session_id = session_file.stem
    updates = apply_canon_updates(canon_data, session_id)

    if updates > 0:
        summary = canon_data.get('scene_summary', 'Canon updates applied')
        git_commit(session_id, summary)

def watch_sessions():
    """Monitor sessions directory for new files"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BLUE}STRAY DOGS WORLDENGINE - ENGINE SYNC{Colors.RESET}")
    print(f"{Colors.BLUE}Monitoring: {SESSIONS_DIR}{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*60}{Colors.RESET}\n")

    processed_files = set()

    # Process existing session files first
    if SESSIONS_DIR.exists():
        for session_file in sorted(SESSIONS_DIR.glob("*.md")):
            if session_file.name.startswith('000_'):
                continue  # Skip setup file
            if session_file not in processed_files:
                process_session_file(session_file)
                processed_files.add(session_file)

    print(f"\n{Colors.GREEN}Watching for new sessions... (Ctrl+C to stop){Colors.RESET}\n")

    # Watch for new files
    try:
        while True:
            time.sleep(5)  # Check every 5 seconds

            if not SESSIONS_DIR.exists():
                continue

            for session_file in SESSIONS_DIR.glob("*.md"):
                if session_file.name.startswith('000_'):
                    continue
                if session_file not in processed_files:
                    process_session_file(session_file)
                    processed_files.add(session_file)

    except KeyboardInterrupt:
        print(f"\n{Colors.BLUE}Engine sync stopped{Colors.RESET}\n")

def main():
    """Main function"""
    import sys

    if len(sys.argv) > 1:
        # Process specific file
        session_file = Path(sys.argv[1])
        if session_file.exists():
            process_session_file(session_file)
        else:
            print(f"{Colors.RED}File not found: {session_file}{Colors.RESET}")
    else:
        # Watch mode
        watch_sessions()

if __name__ == "__main__":
    main()
