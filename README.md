# Paladin's Rise

An epic fantasy novel project featuring both English original and Japanese translation.

LLMs are used heavily via Cline throughout the process.

## Project Description

**Paladin's Rise** is a complete fantasy novel following Gond, a former soldier turned reluctant hero who discovers divine powers while fighting against slavery and corruption. The story spans 27 chapters across 5 parts, featuring themes of redemption, freedom, and unexpected heroism in a richly detailed fantasy world.

This project includes:
- **English Original**: Complete 27-chapter manuscript in `chapters/`
- **Japanese Translation**: LLM-assisted translation in `manuscript-ja/` with comprehensive quality assurance
- **Supporting Materials**: Character guides, world-building documentation, and translation resources

![Cover](images/cover.png)

## Using the Makefile

The project includes a Makefile for building and managing the EPUB version:

### Available Commands

```bash
# Build the EPUB (default target)
make

# Build and verify the EPUB
make test

# Show word count statistics
make word-count

# Combine all chapters into a master document
make master

# Clean build artifacts
make clean

# Show all available commands
make help
```

### Requirements

- **pandoc**: Required for EPUB generation
- **Python 3**: Required for utility scripts

## Installing Pandoc

Pandoc is required to build the EPUB version of the book. For installation instructions, visit:

**[Pandoc Installation Guide](https://pandoc.org/installing.html)**

The guide provides detailed instructions for all major operating systems (Windows, macOS, Linux).

## Project Structure

- `chapters/` - English manuscript chapters
- `manuscript-ja/` - Japanese translations with notes
- `cline_docs/` - Project documentation and guides
- `build/` - Generated files (EPUB output)
- `images/` - Cover art and maps
- `scripts/` - Utility scripts for word counting and file management

## Documentation

For detailed project information, see the `cline_docs/` directory:
- `projectRoadmap.md` - Project goals and progress
- `translationGuide.md` - Japanese translation methodology
- `authoringGuidelines.md` - Writing standards and style guide
