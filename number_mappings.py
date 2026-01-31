"""
Number word mappings for inflationary string operations.

This module contains mappings from number words to their incremented versions in range one to one hundred.
Organized for efficient lookup and easy maintenance.
"""

# Primary mapping: number word -> next number word
NUMBER_MAP = {
    'zero': 'one',
    'one': 'two',
    'two': 'three',
    'three': 'four',
    'four': 'five',
    'five': 'six',
    'six': 'seven',
    'seven': 'eight',
    'eight': 'nine',
    'nine': 'ten',
    'ten': 'eleven',
    'eleven': 'twelve',
    'twelve': 'thirteen',
    'thirteen': 'fourteen',
    'fourteen': 'fifteen',
    'fifteen': 'sixteen',
    'sixteen': 'seventeen',
    'seventeen': 'eighteen',
    'eighteen': 'nineteen',
    'nineteen': 'twenty',
    'twenty': 'twentyone',
    "twentynine": "thirty",
    'thirty': 'thirtyone',
    "thirtynine": "forty",
    'forty': 'fortyone',
    "fortynine": "fifty",
    'fifty': 'fiftyone',
    "fiftynine": "sixty",
    'sixty': 'sixtyone',
    "sixtynine": "seventy",
    'seventy': 'seventyone',
    "seventynine": "eighty",
    'eighty': 'eightyone',
    "eightynine": "ninety",
    'ninety': 'ninetyone',
    "ninetynine": "onehundred",
}

# Pre-computed: words sorted by length (longest first)
# This ensures we match "thirteen" before "three"
WORDS_BY_LENGTH = sorted(NUMBER_MAP.keys(), key=len, reverse=True)

# Maximum length of any number word (for optimization)
MAX_NUMBER_WORD_LENGTH = max(len(word) for word in NUMBER_MAP.keys())
