#!/usr/bin/env python3

"""
General-purpose script to combine all chapter files in a supplied directory into a single output.
- Excludes files matching "*notes.md"
- Sorts files by filename
- Outputs combined content to stdout

Usage:
    python scripts/create_master.py [directory]

If no directory is supplied, defaults to "chapters/"
"""

import sys
import os
import glob

def get_chapter_files(directory):
    # Get all .md files, excluding *notes.md
    pattern = os.path.join(directory, "*.md")
    all_files = glob.glob(pattern)
    files = [f for f in all_files if not f.endswith("notes.md")]
    return sorted(files)

def main():
    if len(sys.argv) > 2:
        print("Usage: python scripts/create_master.py [directory]", file=sys.stderr)
        sys.exit(1)
    directory = sys.argv[1] if len(sys.argv) == 2 else "chapters"
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.", file=sys.stderr)
        sys.exit(1)
    files = get_chapter_files(directory)
    if not files:
        print(f"No chapter files found in '{directory}'.", file=sys.stderr)
        sys.exit(1)
    for idx, filepath in enumerate(files):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().rstrip()
            print(content, end="\n\n" if idx < len(files) - 1 else "\n")

if __name__ == "__main__":
    main()
