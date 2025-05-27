## Current Objective
Reorganize the "Paladin's Rise" novel files to match the recommended ebook publishing format structure.

## Context
The user has requested a complete reorganization of the project files to follow standard ebook publishing conventions. This involves:
- Creating new directory structure (chapters/, images/, build/)
- Renaming all 27 chapter files with descriptive names and zero-padded numbering
- Creating metadata.yml with integrated blurb content
- Moving support files to appropriate locations
- Creating basic epub.css stylesheet

## Target Structure
```
paladin/
├── build/                 # generated files
├── chapters/
│   ├── 01_mark-of-betrayal.md
│   ├── 02_breaking-chains.md
│   └── … (through 27_epilogue.md)
├── images/
│   ├── cover.jpg
│   ├── map_world.png
│   └── other images
├── metadata.yml
└── epub.css
```

## Next Steps
1. Create new directory structure (chapters/, build/)
2. Rename assets/ to images/
3. Move and rename all 27 chapter files with descriptive names
4. Create metadata.yml with blurb content integrated
5. Move synopsis.md to cline_docs/
6. Move epub-master.md to build/
7. Create basic epub.css
8. Delete manuscript/blurb.md (content moved to metadata.yml)
9. Update documentation to reflect new structure
