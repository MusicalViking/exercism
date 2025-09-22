#!/usr/bin/env python3

from rotational_cipher import rotate

# Test cases from the test file
test_cases = [
    ("a", 0, "a"),
    ("a", 1, "b"),
    ("a", 26, "a"),
    ("m", 13, "z"),
    ("n", 13, "a"),
    ("OMG", 5, "TRL"),
    ("O M G", 5, "T R L"),
    ("Testing 1 2 3 testing", 4, "Xiwxmrk 1 2 3 xiwxmrk"),
    ("Let's eat, Grandma!", 21, "Gzo'n zvo, Bmviyhv!"),
    ("The quick brown fox jumps over the lazy dog.", 13, "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."),
]

print("Testing Rotational Cipher:")
all_passed = True
for text, key, expected in test_cases:
    result = rotate(text, key)
    passed = result == expected
    status = "PASS" if passed else "FAIL"
    print(f"  rotate('{text}', {key}) -> '{result}' ({status})")
    if not passed:
        all_passed = False

print(f"\nOverall: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
