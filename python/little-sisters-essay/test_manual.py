#!/usr/bin/env python3

from string_methods import capitalize_title, check_sentence_ending, clean_up_spacing, replace_word_choice

# Test capitalize_title
print("Testing capitalize_title:")
print(f"  'canopy' -> '{capitalize_title('canopy')}'")
print(f"  'fish are cold blooded' -> '{capitalize_title('fish are cold blooded')}'")

# Test check_sentence_ending
print("\nTesting check_sentence_ending:")
print(f"  'Snails can sleep for 3 years.' -> {check_sentence_ending('Snails can sleep for 3 years.')}")
print(f"  'Fittonia are nice' -> {check_sentence_ending('Fittonia are nice')}")

# Test clean_up_spacing
print("\nTesting clean_up_spacing:")
print(f"  '  A rolling stone gathers no moss' -> '{clean_up_spacing('  A rolling stone gathers no moss')}'")
print(f"  '  Elephants can\\'t jump.  ' -> '{clean_up_spacing('  Elephants can\\'t jump.  ')}'")

# Test replace_word_choice
print("\nTesting replace_word_choice:")
print(f"  'Animals are cool.', 'cool', 'awesome' -> '{replace_word_choice('Animals are cool.', 'cool', 'awesome')}'")
print(f"  'Animals are cool.', 'small', 'tiny' -> '{replace_word_choice('Animals are cool.', 'small', 'tiny')}'")
