#!/usr/bin/env python3
"""
Simple test runner for the inflate_numbers project.

This script runs all tests and provides a clean summary.
Usage: python run_tests.py
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from test_inflate_numbers import run_tests

if __name__ == "__main__":
    print("Running all tests for inflate_numbers project...")
    print()
    exit_code = run_tests()
    sys.exit(exit_code)
