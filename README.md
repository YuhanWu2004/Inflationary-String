# Inflationary String Operation

A Python program that finds English number words in strings and increments them by one.

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)

## 📋 Problem Statement

Given a string containing English number words (like "one", "ten", "nineteen"), find all occurrences and increment them by one:
- "one" → "two"
- "ten" → "eleven"  
- "tennis" (contains "ten") → "elevennis"

**Example:** 
```
Input:  "Anyone up for tennis?"
Output: "Anytwo up for elevennis?"
```

This is a solution to the AGI Coding Mini-Challenge.

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No external dependencies (uses only standard library)

### Installation

```bash
# Clone the repository
git clone https://github.com/YuhanWu2004/inflate-numbers.git
cd inflate-numbers
```

### Running the Program

```bash
# Interactive mode with quick tests
python inflate_numbers.py

# See examples
python examples.py

# Run all tests
python run_tests.py

# Or run tests directly
python test_inflate_numbers.py
```

### Using as a Module

```python
from inflate_numbers import inflate_string

result = inflate_string("Anyone up for tennis?")
print(result)  # Output: "Anytwo up for elevennis?"
```

## 📁 Project Structure

```
inflate-numbers/
├── inflate_numbers.py      # Main implementation
├── number_mappings.py      # Number word mappings (separate file)
├── test_inflate_numbers.py # Comprehensive test suite
├── run_tests.py            # Simple test runner
├── examples.py             # Usage examples
├── README.md               # This file
├── AI_USAGE.md            # Documentation of AI assistance
├── requirements.txt        # Dependencies (empty - uses stdlib)
└── .gitignore             # Git ignore rules
```

## 🎯 Features

✅ **Substring Matching**: Finds number words even within other words  
✅ **Capitalization Preservation**: Maintains lowercase, Title Case, and ALL CAPS  
✅ **Optimized Performance**: O(n) time complexity with smart pattern filtering  
✅ **Comprehensive Tests**: 40+ test cases covering edge cases  

## 💡 Algorithm Design

### Core Approach

The solution uses **regex-based pattern matching** with optimized lookup:

1. **Separate mapping file** (`number_mappings.py` only include number text from 1-100)
2. **Length-based optimization**: Only checks patterns that fit in the text
3. **Longest-match-first**: Ensures "thirteen" matches before "three"
4. **Single-pass processing**: O(n) time complexity

### Why This Approach?

**Pros:**
- ✅ Efficient single-pass solution
- ✅ Handles overlapping patterns correctly
- ✅ Natural support for case-insensitive matching
- ✅ Optimized to skip impossible patterns

**Trade-offs:**
- Limited to predefined number mappings (0-90)
- Substring matching may modify words unexpectedly
- Does not support numeric digits (123 → 124)

### Optimization Details

```python
# Instead of checking ALL patterns for short strings:
# Old: Check all patterns for "hi" (2 chars) ❌
# New: Only check patterns of length ≤ 2 ✅

text_len = len(text)
valid_words = [word for word in ALL_WORDS if len(word) <= text_len]
```

This optimization improves performance especially for short strings.

## 🧪 Testing

### Run All Tests

```bash
# Using the test runner (recommended)
python run_test.py

# Or directly
python test_inflate_numbers.py
```

### Test Coverage

The test suite includes **40+ test cases** covering:

- ✅ Basic functionality
- ✅ Capitalization (lowercase, Title Case, ALL CAPS)
- ✅ Substring matching behavior
- ✅ Overlapping patterns (thirteen vs. three)
- ✅ Edge cases (empty strings, no numbers, punctuation)

**All tests passing ✓**

### Example Test Output

```
test_challenge_example ... ok
test_simple_numbers ... ok
test_all_caps ... ok
test_tennis_example ... ok
test_thirteen_not_three ... ok
...
----------------------------------------------------------------------
Ran 42 tests in 0.005s

OK
```

## 📖 Usage Examples

### Basic Usage

```python
from inflate_numbers import inflate_string

# Simple example
inflate_string("I have one apple")
# → "I have two apple"

# Challenge example
inflate_string("Anyone up for tennis?")
# → "Anytwo up for elevennis?"

# Capitalization preserved
inflate_string("TEN items")
# → "ELEVEN items"
```

### Advanced Examples

```python
# Multiple numbers
inflate_string("one, two, three")
# → "two, three, four"

# Substring matching
inflate_string("done")  # contains "one"
# → "dtwo"

# Overlapping patterns handled correctly
inflate_string("thirteen")  # not "three"
# → "fourteen"
```

See `examples.py` for more detailed examples.

## 🔧 Design Decisions

### 1. Separate Mapping File

**Why:** Maintainability and single responsibility principle
```python
# number_mappings.py - only covers mapping for one to one hundred
NUMBER_MAP = {
    'one': 'two',
    'ten': 'eleven',
    # ... easily extensible
}
```

### 2. Longest-Match-First

**Why:** Prevents incorrect partial matches
```python
# "thirteen" should match as whole word, not "three"
WORDS_BY_LENGTH = sorted(NUMBER_MAP.keys(), key=len, reverse=True)
```

### 3. Optimization by Length

**Why:** Don't check patterns that can't possibly match
```python
# For "hi" (2 chars), skip checking "thirteen" (8 chars)
valid_words = [w for w in WORDS if len(w) <= len(text)]
```

### 4. Case Preservation

**Why:** Natural-looking output
```python
if matched_text.isupper():
    return replacement.upper()  # TEN → ELEVEN
elif matched_text[0].isupper():
    return replacement.capitalize()  # Ten → Eleven
else:
    return replacement  # ten → eleven
```

## 📊 Algorithm Analysis

### Time Complexity
- **O(n)** where n = length of input text
- The optimization reduces the constant factor significantly
- Regex engine processes the string in a single pass

### Space Complexity
- **O(n)** for the output string
- **O(1)** for the number mapping (fixed size)

### Performance Characteristics
- Fast for short strings (optimization eliminates long patterns)
- Efficient for long strings (single regex pass)
- Scalable to large texts

## ⚠️ Known Limitations

### 1. Substring Matching Side Effects
```python
inflate_string("done")      # → "dtwo" (contains "one")
inflate_string("money")     # → "mtwoy" (contains "one")
inflate_string("lonely")    # → "ltwoly" (contains "one")
```
This is **intentional** based on the "tennis" example, but may be unexpected.

### 2. Limited Number Range
- Supports: 0-100 (zero through one hundred)
- Does NOT support: 91+, compound numbers, ordinals

```python
inflate_string("ninety")       # ✅ → "ninetyone"
inflate_string("one hundred")  # ❌ No mapping
inflate_string("twenty-one")   # ❌ Treated as separate words
```

### 3. No Digit Support
```python
inflate_string("I have 5 apples")  # ❌ → "I have 5 apples" (unchanged)
```

### 4. No Ordinal Support
```python
inflate_string("first place")  # ❌ → "first place" (unchanged)
```

## 🚀 Future Improvements

If given more time, here are potential enhancements:

### 1. Configuration Options
```python
inflate_string(text, 
               match_substrings=True,    # Current behavior
               match_digits=False,        # NEW: Support "5" → "6"
               match_ordinals=False)      # NEW: Support "first" → "second"
```

### 2. Word Boundary Mode
```python
# Option to avoid "done" → "dtwo"
inflate_string("done", word_boundaries=True)  
# → "done" (unchanged, only matches whole words)
```

### 3. Extended Number Support
- Compound numbers: "twenty-one" → "twenty-two"
- Large numbers: "one hundred" → "one hundred one"
- Ordinals: "first" → "second"

### 4. Using NLP Libraries
```python
# Use word2number + num2words for unlimited range
from word2number import w2n
import num2words

# Could support ANY number
inflate_string("nine hundred ninety-nine")
# → "one thousand"
```

### 5. Performance Enhancements
- Trie data structure for even faster lookups
- Compiled regex patterns (cached)
- Parallel processing for very large texts

## 📝 AI Usage

This solution was developed with AI assistance (ChatGPT, Claude). For complete documentation of the AI collaboration process, see [AI_USAGE.md](AI_USAGE.md).

## 🙏 Acknowledgments

- Anthropic and ChatGPT for the coding challenge
- Python community for excellent documentation
- Everyone who reviews this code

---

**Ready to test?** Run `python run_tests.py` to see all 40+ tests pass! ✅
