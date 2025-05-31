#!/usr/bin/env python3

"""
Script to combine all chapters into the EPUB master document with proper formatting.
Python equivalent of combine-chapters.sh
"""

import os
import glob
import shutil
import sys

DEFAULT_TARGET_FILE = 'build/epub-master.md'

def find_chapter_file(chapter_num):
    """Find the chapter file for a given chapter number."""
    pattern = f"chapters/{chapter_num:02d}_*.md"
    matches = glob.glob(pattern)
    if matches:
        return matches[0]
    return None

def extract_chapter_content(filepath):
    """Extract chapter content starting from '# Chapter' line."""
    if not os.path.exists(filepath):
        return ""
    
    content_lines = []
    found_chapter_start = False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('# Chapter'):
                found_chapter_start = True
            if found_chapter_start:
                content_lines.append(line.rstrip())
    
    return '\n'.join(content_lines)

def main():
    # Start with the existing master document content
    target_file = DEFAULT_TARGET_FILE
    
    with open(target_file, 'w', encoding='utf-8') as f:
        # Add Part I with page break and proper formatting
        f.write('\n')
        f.write('\\newpage\n')
        f.write('\n')
        f.write('# Part I\n')
        f.write('\n')
        f.write('## The Rude Awakening\n')
        f.write('\n')
        
        # Process chapters 1-3 for Part I
        for i in [1, 2, 3]:
            chapter_file = find_chapter_file(i)
            if chapter_file:
                print(f"Adding Chapter {i}…")
                f.write('\\newpage\n')
                f.write('\n')
                chapter_content = extract_chapter_content(chapter_file)
                f.write(chapter_content)
                f.write('\n')
                f.write('\n')
        
        # Add Part II with page break and proper formatting
        f.write('\\newpage\n')
        f.write('\n')
        f.write('# Part II\n')
        f.write('\n')
        f.write('## Seeds of Rebellion\n')
        f.write('\n')
        
        # Process chapters 4-11 for Part II
        for i in [4, 5, 6, 7, 8, 9, 10, 11]:
            chapter_file = find_chapter_file(i)
            if chapter_file:
                print(f"Adding Chapter {i}…")
                f.write('\\newpage\n')
                f.write('\n')
                chapter_content = extract_chapter_content(chapter_file)
                f.write(chapter_content)
                f.write('\n')
                f.write('\n')
        
        # Add Part III with page break and proper formatting
        f.write('\\newpage\n')
        f.write('\n')
        f.write('# Part III\n')
        f.write('\n')
        f.write('## An Unlikely Saint\n')
        f.write('\n')
        
        # Process chapters 12-17 for Part III
        for i in [12, 13, 14, 15, 16, 17]:
            chapter_file = find_chapter_file(i)
            if chapter_file:
                print(f"Adding Chapter {i}…")
                f.write('\\newpage\n')
                f.write('\n')
                chapter_content = extract_chapter_content(chapter_file)
                f.write(chapter_content)
                f.write('\n')
                f.write('\n')
        
        # Add Part IV with page break and proper formatting
        f.write('\\newpage\n')
        f.write('\n')
        f.write('# Part IV\n')
        f.write('\n')
        f.write('## Forging a Free Nation\n')
        f.write('\n')
        
        # Process chapters 18-22 for Part IV
        for i in [18, 19, 20, 21, 22]:
            chapter_file = find_chapter_file(i)
            if chapter_file:
                print(f"Adding Chapter {i}…")
                f.write('\\newpage\n')
                f.write('\n')
                chapter_content = extract_chapter_content(chapter_file)
                f.write(chapter_content)
                f.write('\n')
                f.write('\n')
        
        # Add Part V with page break and proper formatting
        f.write('\\newpage\n')
        f.write('\n')
        f.write('# Part V\n')
        f.write('\n')
        f.write('## The War for Freedom\n')
        f.write('\n')
        
        # Process chapters 22-27 for Part V
        for i in [23, 24, 25, 26, 27]:
            chapter_file = find_chapter_file(i)
            if chapter_file:
                print(f"Adding Chapter {i}…")
                f.write('\\newpage\n')
                f.write('\n')
                chapter_content = extract_chapter_content(chapter_file)
                f.write(chapter_content)
                f.write('\n')
                f.write('\n')
    
    print("Master document created successfully with proper page breaks and part formatting!")

if __name__ == '__main__':
    main()
