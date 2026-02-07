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
REPO_ROOT = Path(__file__).parent.parent  # Assumes script is in scripts/
TAGS_FILE = REPO_ROOT / "meta" / "tags.md"
TAG_VARIATIONS_FILE = REPO_ROOT / "meta" / "tag_variations.md"

try:
    from colors import Colors
except ImportError:
    from scripts.colors import Colors

def load_valid_tags() -> Set[str]:
    """Load all valid tags from tags.md and tag_variations.md"""
    valid_tags = set()

    # Load canonical tags
    if TAGS_FILE.exists():
        with open(TAGS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            # Find all #Tags in the file
            tags = re.findall(r'(?:^|\s)(#\w+)', content)
            valid_tags.update(tags)
            print(f"{Colors.BLUE}Loaded {len(tags)} canonical tags from tags.md{Colors.RESET}")
    else:
        print(f"{Colors.RED}ERROR: {TAGS_FILE} not found!{Colors.RESET}")
        return set()

    # Load tag variations
    if TAG_VARIATIONS_FILE.exists():
        with open(TAG_VARIATIONS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            variations = re.findall(r'(?:^|\s)(#\w+)', content)
            valid_tags.update(variations)
            print(f"{Colors.BLUE}Loaded {len(variations)} tag variations from tag_variations.md{Colors.RESET}")
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
            yaml_tags = set(re.findall(r'(?:^|\s)(#\w+)', yaml_content))

        # Also find inline tags in content (after frontmatter)
        body_content = content
        if yaml_match:
            body_content = content[yaml_match.end():]
        inline_tags = set(re.findall(r'(?:^|\s)(#\w+)', body_content))

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
