#!/bin/bash

# Script to combine all chapters into the EPUB master document with proper formatting

# Start with the existing master document content
cp epub-master.md temp-master.md

# Add Part I with page break and proper formatting
echo "" >> temp-master.md
echo "\\newpage" >> temp-master.md
echo "" >> temp-master.md
echo "# Part I" >> temp-master.md
echo "" >> temp-master.md
echo "## The Rude Awakening" >> temp-master.md
echo "" >> temp-master.md

for i in {1..3}; do
    chapter_file="manuscript/chapter-$(printf "%02d" $i).md"
    if [ -f "$chapter_file" ]; then
        echo "Adding Chapter $i..."
        echo "\\newpage" >> temp-master.md
        echo "" >> temp-master.md
        # Extract just the chapter content (skip the title and part header)
        sed -n '/^### Chapter/,$p' "$chapter_file" >> temp-master.md
        echo "" >> temp-master.md
    fi
done

# Add Part II with page break and proper formatting
echo "\\newpage" >> temp-master.md
echo "" >> temp-master.md
echo "# Part II" >> temp-master.md
echo "" >> temp-master.md
echo "## Seeds of Rebellion" >> temp-master.md
echo "" >> temp-master.md

for i in {4..10}; do
    chapter_file="manuscript/chapter-$(printf "%02d" $i).md"
    if [ -f "$chapter_file" ]; then
        echo "Adding Chapter $i..."
        echo "\\newpage" >> temp-master.md
        echo "" >> temp-master.md
        # Extract just the chapter content (skip the title and part header)
        sed -n '/^### Chapter/,$p' "$chapter_file" >> temp-master.md
        echo "" >> temp-master.md
    fi
done

# Add Part III with page break and proper formatting
echo "\\newpage" >> temp-master.md
echo "" >> temp-master.md
echo "# Part III" >> temp-master.md
echo "" >> temp-master.md
echo "## An Unlikely Saint" >> temp-master.md
echo "" >> temp-master.md

for i in {11..16}; do
    chapter_file="manuscript/chapter-$(printf "%02d" $i).md"
    if [ -f "$chapter_file" ]; then
        echo "Adding Chapter $i..."
        echo "\\newpage" >> temp-master.md
        echo "" >> temp-master.md
        # Extract just the chapter content (skip the title and part header)
        sed -n '/^### Chapter/,$p' "$chapter_file" >> temp-master.md
        echo "" >> temp-master.md
    fi
done

# Add Part IV with page break and proper formatting
echo "\\newpage" >> temp-master.md
echo "" >> temp-master.md
echo "# Part IV" >> temp-master.md
echo "" >> temp-master.md
echo "## Forging a Free Nation" >> temp-master.md
echo "" >> temp-master.md

for i in {17..21}; do
    chapter_file="manuscript/chapter-$(printf "%02d" $i).md"
    if [ -f "$chapter_file" ]; then
        echo "Adding Chapter $i..."
        echo "\\newpage" >> temp-master.md
        echo "" >> temp-master.md
        # Extract just the chapter content (skip the title and part header)
        sed -n '/^### Chapter/,$p' "$chapter_file" >> temp-master.md
        echo "" >> temp-master.md
    fi
done

# Add Part V with page break and proper formatting
echo "\\newpage" >> temp-master.md
echo "" >> temp-master.md
echo "# Part V" >> temp-master.md
echo "" >> temp-master.md
echo "## The War for Freedom" >> temp-master.md
echo "" >> temp-master.md

for i in {22..25}; do
    chapter_file="manuscript/chapter-$(printf "%02d" $i).md"
    if [ -f "$chapter_file" ]; then
        echo "Adding Chapter $i..."
        echo "\\newpage" >> temp-master.md
        echo "" >> temp-master.md
        # Extract just the chapter content (skip the title and part header)
        sed -n '/^### Chapter/,$p' "$chapter_file" >> temp-master.md
        echo "" >> temp-master.md
    fi
done

# Add maps as appendices with page breaks
echo "\\newpage" >> temp-master.md
echo "" >> temp-master.md
echo "# Appendix A: Maps" >> temp-master.md
echo "" >> temp-master.md
echo "## Slavers Coast Map" >> temp-master.md
echo "" >> temp-master.md
echo "![Slavers Coast Map](assets/slavers-coast-map.png)" >> temp-master.md
echo "" >> temp-master.md
echo "\\newpage" >> temp-master.md
echo "" >> temp-master.md
echo "## Southern Continent Map" >> temp-master.md
echo "" >> temp-master.md
echo "![Southern Continent Map](assets/southern-continent-map.png)" >> temp-master.md
echo "" >> temp-master.md

# Replace the original master document
mv temp-master.md epub-master.md

echo "Master document created successfully with proper page breaks and part formatting!"
