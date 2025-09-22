#!/usr/bin/env python3

from isbn_verifier import is_valid

# Test cases from the test file
test_cases = [
    ("3-598-21508-8", True),      # valid
    ("3-598-21508-9", False),     # invalid check digit
    ("3-598-21507-X", True),      # valid with X
    ("3-598-21507-A", False),     # invalid check digit
    ("3598215088", True),         # no dashes
    ("359821507X", True),         # no dashes with X
    ("359821507", False),         # too short
    ("", False),                  # empty
]

print("Testing ISBN verifier:")
for isbn, expected in test_cases:
    result = is_valid(isbn)
    status = "PASS" if result == expected else "FAIL"
    print(f"  '{isbn}' -> {result} ({status})")
