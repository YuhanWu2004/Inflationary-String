# Quick Start Guide

Get started with the Inflationary String Operation in 30 seconds!

## ⚡ Instant Testing

```bash
# Clone and test immediately
git clone https://github.com/yourusername/inflate-numbers.git
cd inflate-numbers

# Run all tests (should see 28 tests pass)
python run_test.py

# Try the interactive demo
python inflate_numbers.py

# See examples
python examples.py
```

## 🎯 Quick Test Commands

```bash
# Run all tests
python run_tests.py

# Run specific test file
python test_inflate_numbers.py

# Interactive mode
python inflate_numbers.py

# See all examples
python examples.py
```

## 💻 Quick Code Example

```python
from inflate_numbers import inflate_string

# Basic usage
print(inflate_string("Anyone up for tennis?"))
# Output: "Anytwo up for elevennis?"

# More examples
print(inflate_string("I have one apple"))    # → "I have two apple"
print(inflate_string("TEN items"))           # → "ELEVEN items"
print(inflate_string("Zero to hero"))        # → "One to hero"
```

## ✅ What to Expect

When you run `python run_tests.py`, you should see:

```
Running all tests for inflate_numbers project...

test_challenge_example ... ok
test_simple_numbers ... ok
test_all_caps ... ok
...
----------------------------------------------------------------------
Ran 28 tests in 0.005s

OK

======================================================================
Tests run: 28
Failures: 0
Errors: 0
Success rate: 100.0%
======================================================================
```

## 📁 Files You Need

Minimum files to run:
- `inflate_numbers.py` - Main code
- `number_mappings.py` - Number mappings
- `test_inflate_numbers.py` - Tests
- `run_tests.py` - Test runner

That's it! No dependencies, no setup, just Python 3.6+.

## 🚀 Next Steps

- Read [README.md](README.md) for full documentation
- Check [AI_USAGE.md](AI_USAGE.md) for AI collaboration details
- See [examples.py](examples.py) for comprehensive examples

## ❓ Troubleshooting

**Problem: `ModuleNotFoundError: No module named 'inflate_numbers'`**
- Solution: Make sure you're in the project directory
- Run: `cd inflate-numbers` first

**Problem: Tests fail**
- Check Python version: `python --version` (need 3.6+)
- Make sure all files are present

**Need help?** Open an issue on GitHub!

---

**Happy Testing!** 🎉
