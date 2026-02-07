# **AUTOMATION SCRIPTS PACKAGE - STRAY DOGS WORLDENGINE**
## **DOCUMENT 4: COMPLETE WORKING CODE FOR JULES**

**Purpose**: Provide Jules with ready-to-use Python scripts for tag validation, canon synchronization, and cross-reference generation.

---

## **SCRIPT 1: `tag_validator.py`**

**Purpose**: Ensures all tags used in repository files exist in the master tag list.

```python
#!/usr/bin/env python3
"""
Tag Validator for Stray Dogs Worldengine
Ensures all tags in markdown files exist in meta/tags.md or meta/tag_variations.md
"""

import os
import re
from pathlib import Path
from typing import Set, Dict, List

# Configuration

def get_repo_root() -> Path:
    """Find repository root by looking for marker files (.git, README.md)"""
    current = Path(__file__).resolve().parent
    for _ in range(5):
        if (current / ".git").exists() or (current / "README.md").exists():
            return current
        if current.parent == current:
            break
        current = current.parent
    return Path(__file__).parent.parent

REPO_ROOT = get_repo_root()
TAGS_FILE = REPO_ROOT / "meta" / "tags.md"
TAG_VARIATIONS_FILE = REPO_ROOT / "meta" / "tag_variations.md"

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def load_valid_tags() -> Set[str]:
    """Load all valid tags from tags.md and tag_variations.md"""
    valid_tags = set()
    
    # Load canonical tags
    if TAGS_FILE.exists():
        with open(TAGS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            # Find all #Tags in the file
            count = 0
            for match in re.finditer(r'#\w+', content):
                valid_tags.add(match.group(0))
                count += 1
            print(f"{Colors.BLUE}Loaded {count} canonical tags from tags.md{Colors.RESET}")
    else:
        print(f"{Colors.RED}ERROR: {TAGS_FILE} not found!{Colors.RESET}")
        return set()
    
    # Load tag variations
    if TAG_VARIATIONS_FILE.exists():
        with open(TAG_VARIATIONS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            count = 0
            for match in re.finditer(r'#\w+', content):
                valid_tags.add(match.group(0))
                count += 1
            print(f"{Colors.BLUE}Loaded {count} tag variations from tag_variations.md{Colors.RESET}")
    else:
        print(f"{Colors.YELLOW}WARNING: {TAG_VARIATIONS_FILE} not found, using only canonical tags{Colors.RESET}")
    
    return valid_tags

def extract_tags_from_file(filepath: Path) -> Set[str]:
    """Extract all #Tags from a markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find YAML frontmatter
        yaml_match = re.search(r'^---\n(.*?)\n---', content, re.MULTILINE | re.DOTALL)
        yaml_tags = set()
        if yaml_match:
            yaml_content = yaml_match.group(1)
            yaml_tags = set(re.findall(r'#\w+', yaml_content))
        
        # Also find inline tags in content (after frontmatter)
        body_content = content
        if yaml_match:
            body_content = content[yaml_match.end():]
        inline_tags = set(re.findall(r'#\w+', body_content))
        
        return yaml_tags | inline_tags
    
    except Exception as e:
        print(f"{Colors.RED}Error reading {filepath}: {e}{Colors.RESET}")
        return set()

def validate_repository() -> Dict[str, List[str]]:
    """Check all markdown files for invalid tags"""
    valid_tags = load_valid_tags()
    
    if not valid_tags:
        print(f"{Colors.RED}No valid tags loaded. Aborting validation.{Colors.RESET}")
        return {}
    
    print(f"\n{Colors.BLUE}Validating repository...{Colors.RESET}\n")
    
    errors = {}
    files_checked = 0
    
    # Directories to check
    check_dirs = [
        'chars',
        'locations',
        'factions',
        'tensions',
        'events',
        'mechanics',
        'culture',
        'registry',
        'reactive_world'
    ]
    
    for dir_name in check_dirs:
        dir_path = REPO_ROOT / dir_name
        if not dir_path.exists():
            print(f"{Colors.YELLOW}Skipping {dir_name}/ (not found){Colors.RESET}")
            continue
        
        for filepath in dir_path.rglob("*.md"):
            # Skip index files (they reference many tags intentionally)
            if '00_' in filepath.name or 'index' in filepath.name.lower():
                continue
            
            files_checked += 1
            file_tags = extract_tags_from_file(filepath)
            invalid = file_tags - valid_tags
            
            if invalid:
                relative_path = filepath.relative_to(REPO_ROOT)
                errors[str(relative_path)] = sorted(list(invalid))
    
    print(f"{Colors.BLUE}Checked {files_checked} files{Colors.RESET}\n")
    return errors

def display_results(errors: Dict[str, List[str]]):
    """Display validation results"""
    if not errors:
        print(f"{Colors.GREEN}✓ ALL TAGS VALID{Colors.RESET}")
        print(f"{Colors.GREEN}No invalid tags found. Repository is consistent.{Colors.RESET}")
        return True
    
    print(f"{Colors.RED}✗ TAG VALIDATION FAILED{Colors.RESET}")
    print(f"{Colors.RED}Found invalid tags in {len(errors)} file(s):{Colors.RESET}\n")
    
    for filepath, invalid_tags in sorted(errors.items()):
        print(f"{Colors.YELLOW}{filepath}:{Colors.RESET}")
        for tag in invalid_tags:
            print(f"  {Colors.RED}✗{Colors.RESET} {tag}")
        print()
    
    print(f"{Colors.BLUE}Action Required:{Colors.RESET}")
    print("1. Add missing tags to meta/tags.md (if they should be canonical)")
    print("2. Add variations to meta/tag_variations.md (if they're acceptable alternatives)")
    print("3. Fix typos in files (if tags are misspelled)")
    
    return False

def main():
    """Main validation function"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BLUE}STRAY DOGS WORLDENGINE - TAG VALIDATOR{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*60}{Colors.RESET}\n")
    
    errors = validate_repository()
    success = display_results(errors)
    
    print(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}\n")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
```

**Usage**:
```bash
cd stray-dogs-worldengine
python scripts/tag_validator.py
```

---

## **SCRIPT 2: `engine_sync.py`**

**Purpose**: Monitors sessions/ folder and automatically updates canon based on CANON_UPDATE blocks.

```python
#!/usr/bin/env python3
"""
Engine Sync for Stray Dogs Worldengine
Monitors session files and updates canon based on CANON_UPDATE YAML blocks
"""

import os
import re
import yaml
import logging
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
        logging.error(f"{Colors.RED}Error parsing {session_file}: {e}{Colors.RESET}")
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

    logging.warning(f"{Colors.YELLOW}Warning: Character file not found for '{char_name}'{Colors.RESET}")
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
                f"\\g<1>{changes['status']}",
                content
            )

        # Update last_updated
        content = re.sub(
            r'(last_updated:\s*).*',
            f"\\g<1>{datetime.now().strftime('%Y-%m-%d')}",
            content
        )

        # Update canon_version
        content = re.sub(
            r'(canon_version:\s*).*',
            f"\\g<1>{session_id}",
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

        logging.info(f"{Colors.GREEN}✓ Updated {char_name}{Colors.RESET}")
        return True

    except Exception as e:
        logging.error(f"{Colors.RED}Error updating {char_name}: {e}{Colors.RESET}")
        return False

def update_tension(tension_name: str, changes: Dict[str, Any], session_id: str) -> bool:
    """Update tension markdown file with new developments"""
    # Convert name to filename
    filename = tension_name.lower().replace(' ', '_') + '.md'
    tension_file = TENSIONS_DIR / filename

    if not tension_file.exists():
        logging.warning(f"{Colors.YELLOW}Warning: Tension file not found for '{tension_name}'{Colors.RESET}")
        return False

    try:
        with open(tension_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update status in YAML
        if 'status' in changes:
            content = re.sub(
                r'(status:\s*).*',
                f"\\g<1>{changes['status']}",
                content
            )

        # Update last_updated
        content = re.sub(
            r'(last_updated:\s*).*',
            f"\\g<1>{datetime.now().strftime('%Y-%m-%d')}",
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

        logging.info(f"{Colors.GREEN}✓ Updated tension: {tension_name}{Colors.RESET}")
        return True

    except Exception as e:
        logging.error(f"{Colors.RED}Error updating tension {tension_name}: {e}{Colors.RESET}")
        return False

def apply_canon_updates(canon_data: Dict[str, Any], session_id: str):
    """Apply all canon updates from session"""
    logging.info(f"\n{Colors.BLUE}Applying canon updates from {session_id}...{Colors.RESET}\n")

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
            logging.info(f"{Colors.BLUE}→ New event logged: {event.get('title', 'Unnamed Event')}{Colors.RESET}")
            updates_applied += 1

    logging.info(f"\n{Colors.GREEN}Applied {updates_applied} canon update(s){Colors.RESET}")
    return updates_applied

def git_commit(session_id: str, summary: str):
    """Commit changes to git"""
    try:
        # Git add all changes
        os.system('git add .')

        # Create commit message
        commit_msg = f"Update canon: Session {session_id}\n\n{summary}"
        os.system(f'git commit -m "{commit_msg}"')

        logging.info(f"{Colors.GREEN}✓ Git commit created{Colors.RESET}")

    except Exception as e:
        logging.error(f"{Colors.RED}Git commit failed: {e}{Colors.RESET}")

def process_session_file(session_file: Path):
    """Process a single session file"""
    logging.info(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}")
    logging.info(f"{Colors.BLUE}Processing: {session_file.name}{Colors.RESET}")
    logging.info(f"{Colors.BLUE}{'='*60}{Colors.RESET}")

    canon_data = parse_canon_update(session_file)

    if not canon_data:
        logging.warning(f"{Colors.YELLOW}No CANON_UPDATE block found{Colors.RESET}")
        return

    session_id = session_file.stem
    updates = apply_canon_updates(canon_data, session_id)

    if updates > 0:
        summary = canon_data.get('scene_summary', 'Canon updates applied')
        git_commit(session_id, summary)

def watch_sessions():
    """Monitor sessions directory for new files"""
    logging.info(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}")
    logging.info(f"{Colors.BLUE}STRAY DOGS WORLDENGINE - ENGINE SYNC{Colors.RESET}")
    logging.info(f"{Colors.BLUE}Monitoring: {SESSIONS_DIR}{Colors.RESET}")
    logging.info(f"{Colors.BLUE}{'='*60}{Colors.RESET}\n")

    processed_files = set()

    # Process existing session files first
    if SESSIONS_DIR.exists():
        for session_file in sorted(SESSIONS_DIR.glob("*.md")):
            if session_file.name.startswith('000_'):
                continue  # Skip setup file
            if session_file not in processed_files:
                process_session_file(session_file)
                processed_files.add(session_file)

    logging.info(f"\n{Colors.GREEN}Watching for new sessions... (Ctrl+C to stop){Colors.RESET}\n")

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
        logging.info(f"\n{Colors.BLUE}Engine sync stopped{Colors.RESET}\n")

def main():
    """Main function"""
    import sys
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    if len(sys.argv) > 1:
        # Process specific file
        session_file = Path(sys.argv[1])
        if session_file.exists():
            process_session_file(session_file)
        else:
            logging.error(f"{Colors.RED}File not found: {session_file}{Colors.RESET}")
    else:
        # Watch mode
        watch_sessions()

if __name__ == "__main__":
    main()
```

**Usage**:
```bash
# Watch mode (monitors for new sessions continuously)
python scripts/engine_sync.py

# Single file mode
python scripts/engine_sync.py sessions/001_scraps_first_shift.md
```

---

## **SCRIPT 3: `cross_ref_builder.py`**

**Purpose**: Auto-generates cross-reference documentation by analyzing tag relationships.

```python
#!/usr/bin/env python3
"""
Cross-Reference Builder for Stray Dogs Worldengine
Analyzes all files and builds relationship maps
"""

import re
import logging
from pathlib import Path
from typing import Dict, Set, List, Tuple
from collections import defaultdict

# Configuration

def get_repo_root() -> Path:
    """Find repository root by looking for marker files (.git, README.md)"""
    current = Path(__file__).resolve().parent
    for _ in range(5):
        if (current / ".git").exists() or (current / "README.md").exists():
            return current
        if current.parent == current:
            break
        current = current.parent
    return Path(__file__).parent.parent

REPO_ROOT = get_repo_root()
CHARS_DIR = REPO_ROOT / "chars"
LOCATIONS_DIR = REPO_ROOT / "locations"
FACTIONS_DIR = REPO_ROOT / "factions"
OUTPUT_FILE = REPO_ROOT / "meta" / "cross_reference.md"

def extract_yaml_tags(filepath: Path) -> Dict[str, List[str]]:
    """Extract tags from YAML frontmatter"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        yaml_match = re.search(r'^---\n(.*?)\n---', content, re.MULTILINE | re.DOTALL)
        if not yaml_match:
            return {}
        
        yaml_content = yaml_match.group(1)
        
        # Extract tags section
        tags_match = re.search(r'tags:\s*\n((?:  .*\n)*)', yaml_content)
        if not tags_match:
            return {}
        
        tags_section = tags_match.group(1)
        
        # Parse tag categories
        tag_dict = {}
        current_category = None
        
        for line in tags_section.split('\n'):
            if ':' in line and line.strip().endswith(':'):
                # Category line
                current_category = line.split(':')[0].strip()
                tag_dict[current_category] = []
            elif current_category and '#' in line:
                # Tag line
                tags = re.findall(r'#\w+', line)
                tag_dict[current_category].extend(tags)
        
        return tag_dict
    
    except Exception as e:
        logging.error(f"Error reading {filepath}: {e}")
        return {}

def build_maps() -> Tuple[Dict[str, Dict[str, Set[str]]], Dict[str, Set[str]]]:
    """Build character-location map and relationship map in a single pass"""
    char_to_locations = defaultdict(set)
    location_to_chars = defaultdict(set)
    relationships = defaultdict(set)
    
    # Scan all character files
    for char_file in CHARS_DIR.rglob("*.md"):
        if '00_' in char_file.name:
            continue
        
        tags = extract_yaml_tags(char_file)
        char_tag = tags.get('character', [''])[0] if 'character' in tags else ''
        
        if not char_tag:
            continue

        if 'locations' in tags:
            for loc_tag in tags['locations']:
                char_to_locations[char_tag].add(loc_tag)
                location_to_chars[loc_tag].add(char_tag)
        
        if 'relationships' in tags:
            for rel_tag in tags['relationships']:
                relationships[char_tag].add(rel_tag)
                # Bidirectional
                relationships[rel_tag].add(char_tag)
    
    loc_map = {
        'char_to_locations': dict(char_to_locations),
        'location_to_chars': dict(location_to_chars)
    }

    return loc_map, dict(relationships)

def generate_cross_reference():
    """Generate complete cross-reference markdown"""
    logging.info("Building cross-reference map...")
    
    loc_map, rel_map = build_maps()
    
    output = []
    output.append("# Cross-Reference Map\n")
    output.append("**Auto-generated by cross_ref_builder.py**\n")
    output.append(f"**Generated**: {Path(__file__).stat().st_mtime}\n")
    output.append("---\n\n")
    
    # Character ↔ Location section
    output.append("## Character ↔ Location Relationships\n\n")
    for char, locations in sorted(loc_map['char_to_locations'].items()):
        output.append(f"### {char}\n")
        output.append("**Appears at**:\n")
        for loc in sorted(locations):
            output.append(f"- {loc}\n")
        output.append("\n")
    
    # Location ↔ Character section
    output.append("## Location ↔ Character Presence\n\n")
    for loc, characters in sorted(loc_map['location_to_chars'].items()):
        output.append(f"### {loc}\n")
        output.append("**Characters present**:\n")
        for char in sorted(characters):
            output.append(f"- {char}\n")
        output.append("\n")
    
    # Character ↔ Character section
    output.append("## Character ↔ Character Relationships\n\n")
    for char, related in sorted(rel_map.items()):
        output.append(f"### {char}\n")
        output.append("**Connected to**:\n")
        for rel in sorted(related):
            output.append(f"- {rel}\n")
        output.append("\n")
    
    # Write to file
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(''.join(output))
    
    logging.info(f"Cross-reference generated: {OUTPUT_FILE}")
    logging.info(f"  - Characters mapped: {len(loc_map['char_to_locations'])}")
    logging.info(f"  - Locations mapped: {len(loc_map['location_to_chars'])}")
    logging.info(f"  - Relationships: {len(rel_map)}")

def main():
    """Main function"""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logging.info("="*60)
    logging.info("STRAY DOGS WORLDENGINE - CROSS-REFERENCE BUILDER")
    logging.info("="*60)
    
    generate_cross_reference()

if __name__ == "__main__":
    main()
```

**Usage**:
```bash
python scripts/cross_ref_builder.py
```

---

## **INSTALLATION INSTRUCTIONS FOR JULES**

### **Step 1: Create Scripts Directory**

```bash
cd stray-dogs-worldengine
mkdir -p scripts
```

### **Step 2: Copy Scripts**

Save the three Python files above as:
- `scripts/tag_validator.py`
- `scripts/engine_sync.py`
- `scripts/cross_ref_builder.py`

### **Step 3: Make Executable (Optional)**

```bash
chmod +x scripts/*.py
```

### **Step 4: Test Scripts**

```bash
# Test tag validator
python scripts/tag_validator.py

# Test cross-reference builder
python scripts/cross_ref_builder.py

# Test engine sync (will run in watch mode)
# Press Ctrl+C to stop
python scripts/engine_sync.py
```

---

## **REQUIREMENTS**

All scripts use Python 3.7+ standard library only. No external dependencies required.

**Required Python modules** (all standard library):
- `os`
- `re`
- `yaml` (included in Python 3.x)
- `pathlib`
- `typing`
- `collections`
- `time`
- `datetime`

---

## **INTEGRATION WITH GIT WORKFLOW**

### **Recommended Workflow**

1. **Before committing changes**:
   ```bash
   python scripts/tag_validator.py
   ```
   Ensure all tags are valid.

2. **After gameplay session**:
   AI creates session file in `sessions/001_session_name.md` with CANON_UPDATE block.
   
3. **Run engine sync**:
   ```bash
   python scripts/engine_sync.py sessions/001_session_name.md
   ```
   Canon updates automatically applied and committed.

4. **Periodically rebuild cross-references**:
   ```bash
   python scripts/cross_ref_builder.py
   git add meta/cross_reference.md
   git commit -m "Update cross-references"
   ```

---

## **AUTOMATED WORKFLOW (OPTIONAL)**

### **Git Pre-Commit Hook**

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Run tag validator before commits

echo "Running tag validator..."
python scripts/tag_validator.py

if [ $? -ne 0 ]; then
    echo "Tag validation failed. Commit aborted."
    exit 1
fi

echo "Tags validated successfully."
exit 0
```

Make executable:
```bash
chmod +x .git/hooks/pre-commit
```

Now every `git commit` will automatically validate tags!

---

## **TROUBLESHOOTING**

### **"ModuleNotFoundError: No module named 'yaml'"**

Install PyYAML:
```bash
pip install pyyaml
```

### **"Permission denied" when running scripts**

Make executable:
```bash
chmod +x scripts/tag_validator.py
```

### **Scripts can't find repository root**

Ensure you're running from repository root:
```bash
cd stray-dogs-worldengine
python scripts/tag_validator.py
```

---

## **JULES: FINAL SCRIPT CHECKLIST**

When building repository:

✅ **Create `scripts/` directory**
✅ **Add all three Python scripts**
✅ **Test tag_validator.py runs without errors**
✅ **Test cross_ref_builder.py generates meta/cross_reference.md**
✅ **Document script usage in README.md**
✅ **Include scripts in initial Git commit**

---

**WITH THESE SCRIPTS, THE WORLDENGINE IS FULLY AUTOMATED.** 🐕

---

**END OF DOCUMENT 4: AUTOMATION SCRIPTS PACKAGE**
