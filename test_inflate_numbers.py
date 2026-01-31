#!/usr/bin/env python3
"""
Unit tests for the inflationary string operation.

Run tests:
    python test_inflate_numbers.py
    python -m pytest test_inflate_numbers.py  (if pytest installed)
    python run_tests.py  (runs all tests with coverage)
"""

import unittest
from inflate_numbers import inflate_string


class TestBasicFunctionality(unittest.TestCase):
    """Test basic number inflation functionality."""
    
    def test_challenge_example(self):
        """Test the main example from the problem statement."""
        self.assertEqual(
            inflate_string("Anyone up for tennis?"),
            "Anytwo up for elevennis?"
        )
    
    def test_simple_numbers(self):
        """Test simple single number replacements."""
        self.assertEqual(inflate_string("one"), "two")
        self.assertEqual(inflate_string("ten"), "eleven")
        self.assertEqual(inflate_string("nineteen"), "twenty")
        self.assertEqual(inflate_string("zero"), "one")
    
    def test_multiple_numbers(self):
        """Test strings with multiple number words."""
        self.assertEqual(
            inflate_string("one two three"),
            "two three four"
        )
        self.assertEqual(
            inflate_string("First one, then two, then three!"),
            "First two, then three, then four!"
        )
    
    def test_empty_string(self):
        """Test empty string input."""
        self.assertEqual(inflate_string(""), "")
    
    def test_no_numbers(self):
        """Test strings with no number words."""
        self.assertEqual(
            inflate_string("Hello world!"),
            "Hello world!"
        )
        self.assertEqual(
            inflate_string("The quick brown fox"),
            "The quick brown fox"
        )


class TestCapitalization(unittest.TestCase):
    """Test capitalization preservation."""
    
    def test_lowercase(self):
        """Test lowercase number words."""
        self.assertEqual(inflate_string("one apple"), "two apple")
        self.assertEqual(inflate_string("ten items"), "eleven items")
    
    def test_title_case(self):
        """Test title case number words."""
        self.assertEqual(inflate_string("One apple"), "Two apple")
        self.assertEqual(inflate_string("Ten items"), "Eleven items")
    
    def test_all_caps(self):
        """Test all caps number words."""
        self.assertEqual(inflate_string("ONE APPLE"), "TWO APPLE")
        self.assertEqual(inflate_string("TEN ITEMS"), "ELEVEN ITEMS")
    
    def test_mixed_case_sentence(self):
        """Test a sentence with mixed capitalization."""
        self.assertEqual(
            inflate_string("One, Two, THREE"),
            "Two, Three, FOUR"
        )


class TestSubstringMatching(unittest.TestCase):
    """Test substring matching behavior."""
    
    def test_tennis_example(self):
        """Test the classic 'tennis' example."""
        self.assertEqual(inflate_string("tennis"), "elevennis")
    
    def test_embedded_one(self):
        """Test 'one' embedded in various words."""
        self.assertEqual(inflate_string("done"), "dtwo")
        self.assertEqual(inflate_string("money"), "mtwoy")
        self.assertEqual(inflate_string("someone"), "sometwo")
        self.assertEqual(inflate_string("anyone"), "anytwo")
    
    def test_embedded_other_numbers(self):
        """Test other numbers embedded in words."""
        self.assertEqual(inflate_string("atone"), "attwo")
        self.assertEqual(inflate_string("ozone"), "oztwo")


class TestOverlappingPatterns(unittest.TestCase):
    """Test that longest matches are found first."""
    
    def test_thirteen_not_three(self):
        """Test that 'thirteen' matches as a whole, not 'three'."""
        self.assertEqual(inflate_string("thirteen"), "fourteen")
        # Should NOT become "fourteenteen"
        self.assertNotEqual(inflate_string("thirteen"), "fourteenteen")
    
    def test_nineteen_not_nine(self):
        """Test that 'nineteen' matches as a whole, not 'nine'."""
        self.assertEqual(inflate_string("nineteen"), "twenty")
        # Should NOT become "twelveteenteen" or similar
        self.assertNotEqual(inflate_string("nineteen"), "twelveteenteen")
    
    def test_all_teens(self):
        """Test all teen numbers."""
        teens = [
            ("thirteen", "fourteen"),
            ("fourteen", "fifteen"),
            ("fifteen", "sixteen"),
            ("sixteen", "seventeen"),
            ("seventeen", "eighteen"),
            ("eighteen", "nineteen"),
        ]
        for input_word, expected in teens:
            with self.subTest(input=input_word):
                self.assertEqual(inflate_string(input_word), expected)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def test_repeated_numbers(self):
        """Test the same number appearing multiple times."""
        self.assertEqual(
            inflate_string("one one one"),
            "two two two"
        )
    
    def test_number_at_start(self):
        """Test number at the beginning of string."""
        self.assertEqual(inflate_string("one apple"), "two apple")
    
    def test_number_at_end(self):
        """Test number at the end of string."""
        self.assertEqual(inflate_string("I have one"), "I have two")
    
    def test_only_number(self):
        """Test string that is only a number word."""
        self.assertEqual(inflate_string("seven"), "eight")
    
    def test_punctuation(self):
        """Test that punctuation doesn't interfere."""
        self.assertEqual(
            inflate_string("one! two? three."),
            "two! three? four."
        )
        self.assertEqual(
            inflate_string("one, two, three"),
            "two, three, four"
        )
    
    def test_whitespace_preservation(self):
        """Test that whitespace is preserved."""
        self.assertEqual(
            inflate_string("one  two   three"),
            "two  three   four"
        )
    
    def test_newlines_and_tabs(self):
        """Test handling of newlines and tabs."""
        self.assertEqual(
            inflate_string("one\ntwo\tthree"),
            "two\nthree\tfour"
        )


class TestNumberRange(unittest.TestCase):
    """Test the full range of supported numbers."""
    
    def test_zero_through_nine(self):
        """Test single digit number words."""
        numbers = [
            ("zero", "one"),
            ("one", "two"),
            ("two", "three"),
            ("three", "four"),
            ("four", "five"),
            ("five", "six"),
            ("six", "seven"),
            ("seven", "eight"),
            ("eight", "nine"),
            ("nine", "ten"),
        ]
        for input_word, expected in numbers:
            with self.subTest(input=input_word):
                self.assertEqual(inflate_string(input_word), expected)
    
    def test_ten_through_twenty(self):
        """Test numbers from ten to twenty."""
        numbers = [
            ("ten", "eleven"),
            ("eleven", "twelve"),
            ("twelve", "thirteen"),
            ("thirteen", "fourteen"),
            ("fourteen", "fifteen"),
            ("fifteen", "sixteen"),
            ("sixteen", "seventeen"),
            ("seventeen", "eighteen"),
            ("eighteen", "nineteen"),
            ("nineteen", "twenty"),
        ]
        for input_word, expected in numbers:
            with self.subTest(input=input_word):
                self.assertEqual(inflate_string(input_word), expected)
    
    def test_tens(self):
        """Test multiples of ten."""
        tens = [
            ("twenty", "twentyone"),
            ("thirty", "thirtyone"),
            ("forty", "fortyone"),
            ("fifty", "fiftyone"),
            ("sixty", "sixtyone"),
            ("seventy", "seventyone"),
            ("eighty", "eightyone"),
            ("ninety", "ninetyone"),
        ]
        for input_word, expected in tens:
            with self.subTest(input=input_word):
                self.assertEqual(inflate_string(input_word), expected)


class TestRealWorldExamples(unittest.TestCase):
    """Test realistic usage examples."""
    
    def test_sentence_with_context(self):
        """Test realistic sentences."""
        self.assertEqual(
            inflate_string("I have one apple and two oranges"),
            "I have two apple and three oranges"
        )
    
    def test_story_fragment(self):
        """Test a story-like text."""
        self.assertEqual(
            inflate_string("Once upon a time, there were three little pigs"),
            "Once upon a time, there were four little pigs"
        )
    
    def test_countdown(self):
        """Test a countdown sequence."""
        self.assertEqual(
            inflate_string("three, two, one, blast off!"),
            "four, three, two, blast off!"
        )


def run_tests():
    """
    Run all tests and return exit code.
    Returns 0 if all tests pass, 1 if any fail.
    """
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestBasicFunctionality,
        TestCapitalization,
        TestSubstringMatching,
        TestOverlappingPatterns,
        TestEdgeCases,
        TestNumberRange,
        TestRealWorldExamples,
    ]
    
    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {(result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100:.1f}%")
    print("=" * 70)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    exit(run_tests())
