#!/usr/bin/env python3
"""
Inflationary String Operation

Finds English number words in strings and increments them by one.
Example: "Anyone up for tennis?" -> "Anytwo up for elevennis?"

This module provides efficient string inflation using optimized pattern matching.
"""

import re
from typing import Optional
from number_mappings import NUMBER_MAP, WORDS_BY_LENGTH


def inflate_string(text: str) -> str:
    """
    Find number words in a string and increment them by one.
    
    This function performs substring matching, so "tennis" becomes "elevennis"
    because it contains "ten".
    
    Args:
        text: The input string to process
        
    Returns:
        The string with all number words incremented by one
        
    Examples:
        >>> inflate_string("Anyone up for tennis?")
        'Anytwo up for elevennis?'
        
        >>> inflate_string("I have one apple")
        'I have two apple'
        
        >>> inflate_string("TEN items")
        'ELEVEN items'
    
    Algorithm:
        1. Filter patterns to only those that could fit in the text (optimization)
        2. Sort by length (longest first) to match "thirteen" before "three"
        3. Use regex to find and replace all matches in one pass
        4. Preserve original capitalization (lowercase, Title Case, ALL CAPS)
    
    Time Complexity: O(n) where n is the length of the text
    Space Complexity: O(n) for the output string
    """
    if not text:
        return text
    
    # Optimization: only check number words that could fit in the text
    text_len = len(text)
    valid_words = [word for word in WORDS_BY_LENGTH if len(word) <= text_len]
    
    if not valid_words:
        return text  # No patterns to match
    
    # Create regex pattern from valid words
    # Use re.escape to handle any special regex characters (though none exist in our words)
    pattern = '|'.join(re.escape(word) for word in valid_words)
    
    def replace_number(match):
        """Replace a matched number word with its incremented version."""
        matched_text = match.group(0)
        lower_match = matched_text.lower()
        
        # Look up the replacement
        replacement = NUMBER_MAP[lower_match]
        
        # Preserve original capitalization
        if matched_text.isupper():
            # All caps: TEN -> ELEVEN
            return replacement.upper()
        elif matched_text[0].isupper():
            # Title case: Ten -> Eleven
            return replacement.capitalize()
        else:
            # Lowercase: ten -> eleven
            return replacement
    
    # Perform the replacement (case-insensitive matching)
    result = re.sub(pattern, replace_number, text, flags=re.IGNORECASE)
    
    return result


def main():
    """
    Main function for interactive usage and quick testing.
    """
    print("=" * 70)
    print("INFLATIONARY STRING OPERATION")
    print("=" * 70)
    print()
    print("This program finds number words in text and increments them by one.")
    print("Example: 'Anyone up for tennis?' -> 'Anytwo up for elevennis?'")
    print()
    print("Quick Tests:")
    print("-" * 70)
    
    # Quick test cases
    test_cases = [
        "Anyone up for tennis?",
        "I have one apple",
        "TEN items",
        "Zero to hero",
    ]
    
    for test in test_cases:
        result = inflate_string(test)
        print(f"Input:  '{test}'")
        print(f"Output: '{result}'")
        print()
    
    # Interactive mode
    print("=" * 70)
    print("Interactive Mode - Enter text to inflate (Ctrl+C or Ctrl+D to exit)")
    print("=" * 70)
    print()
    
    try:
        while True:
            user_input = input("Enter text: ")
            if user_input.strip():
                result = inflate_string(user_input)
                print(f"Result: {result}")
                print()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGoodbye!")


if __name__ == "__main__":
    main()
