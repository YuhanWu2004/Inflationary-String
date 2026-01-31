#!/usr/bin/env python3
"""
Example usage of the inflationary string operation.

This script demonstrates various use cases and patterns to help understand
how the inflate_string function works.

Run: python examples.py
"""

from inflate_numbers import inflate_string


def print_section(title):
    """Print a section header."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def print_example(description, input_text):
    """Print an example with input and output."""
    result = inflate_string(input_text)
    print(f"\n{description}")
    print(f"  Input:  '{input_text}'")
    print(f"  Output: '{result}'")


def main():
    """Run all examples."""
    
    print_section("INFLATIONARY STRING OPERATION - EXAMPLES")
    
    # Basic examples
    print_section("1. BASIC EXAMPLES")
    print_example(
        "Challenge example",
        "Anyone up for tennis?"
    )
    print_example(
        "Simple increment",
        "I have one apple"
    )
    print_example(
        "Zero to hero",
        "Zero to hero"
    )
    
    # Capitalization
    print_section("2. CAPITALIZATION PRESERVATION")
    print_example("Lowercase", "one two three")
    print_example("Title Case", "One Two Three")
    print_example("ALL CAPS", "ONE TWO THREE")
    print_example("Mixed case", "One TWO three")
    
    # Substring matching
    print_section("3. SUBSTRING MATCHING")
    print_example("Tennis (contains 'ten')", "tennis")
    print_example("Done (contains 'one')", "done")
    print_example("Money (contains 'one')", "money")
    print_example("Someone (contains 'one')", "someone")
    print_example("Atone (contains 'one')", "atone")
    
    # Multiple numbers
    print_section("4. MULTIPLE NUMBERS")
    print_example(
        "Sequential numbers",
        "First one, then two, then three!"
    )
    print_example(
        "Book reference",
        "Chapter one, section two, page three"
    )
    print_example(
        "Countdown",
        "three, two, one, blast off!"
    )
    
    # Teen numbers
    print_section("5. TEEN NUMBERS (SPECIAL CASES)")
    print_example("Thirteen (not three)", "thirteen")
    print_example("Fourteen", "fourteen")
    print_example("Nineteen (not nine)", "nineteen")
    
    # Tens
    print_section("6. MULTIPLES OF TEN")
    print_example("Twenty", "twenty")
    print_example("Fifty", "fifty")
    print_example("Ninety", "ninety")
    
    # Edge cases
    print_section("7. EDGE CASES")
    print_example("Empty string", "")
    print_example("No numbers", "Hello, world!")
    print_example("Repeated number", "one one one")
    print_example("With punctuation", "one! two? three.")
    
    # Real-world examples
    print_section("8. REAL-WORLD EXAMPLES")
    print_example(
        "Shopping list",
        "I need one apple, two oranges, and three bananas"
    )
    print_example(
        "Story fragment",
        "Once upon a time, there were three little pigs"
    )
    print_example(
        "Instructions",
        "Step one: mix ingredients. Step two: bake for ten minutes."
    )
    
    # What doesn't work (limitations)
    print_section("9. LIMITATIONS (NOT SUPPORTED)")
    print("\nThe following are NOT supported in the current implementation:")
    print_example(
        "Numeric digits (not supported)",
        "I have 5 apples and 10 oranges"
    )
    print_example(
        "Ordinals (not supported)",
        "First place, second place, third place"
    )
    print_example(
        "Compound numbers (treated separately)",
        "twenty-one items"
    )
    
    # Summary
    print("\n" + "=" * 70)
    print("NOTE:")
    print("  - The function performs SUBSTRING matching")
    print("  - 'tennis' contains 'ten', so it becomes 'elevennis'")
    print("  - Capitalization is preserved (lowercase, Title, UPPERCASE)")
    print("  - Longest matches are found first ('thirteen' not 'three')")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
