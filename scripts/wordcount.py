"""
Calculates word count stats for the book.
"""

import glob 

PAGE_LEN = 400

filenames = glob.glob('manuscript/chapter-*.md')

minmax = dict(
    shortest=(filenames[0], 1_000_000),
    longest=(filenames[0], 0),
)

print(f'Found {len(filenames)} chapters')
total_words = 0
for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as fp:
        content = fp.read()
        words = content.split()
        word_count = len(words)
        # update minmax
        if word_count < minmax['shortest'][1]:
            minmax['shortest'] = (filename, word_count)
        if word_count > minmax['longest'][1]:
            minmax['longest'] = (filename, word_count)
        total_words += word_count
        print(f'{filename}: {word_count} words')

print(f'Total words in book: {total_words}')
print(f'Total pages in book: {total_words // PAGE_LEN + 1}')
print(f'Average words per chpater: {total_words / len(filenames):.2f}')
print(f'Shortest chapter: {minmax["shortest"][0]} ({minmax["shortest"][1]} words)')
print(f'Longest chapter: {minmax["longest"][0]} ({minmax["longest"][1]} words)')