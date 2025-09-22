#!/usr/bin/env python3

from lists import (
    get_rounds,
    concatenate_rounds,
    list_contains_round,
    card_average,
    approx_average_is_average,
    average_even_is_average_odd,
    maybe_double_last
)

# Test all functions
print("Testing Card Games Functions:")
print()

# Test get_rounds
print("1. get_rounds:")
test_cases = [0, 1, 10, 27]
for case in test_cases:
    result = get_rounds(case)
    print(f"   get_rounds({case}) -> {result}")
print()

# Test concatenate_rounds
print("2. concatenate_rounds:")
test_cases = [([1], [2]), ([], []), ([1, 2, 3], [4, 5, 6])]
for case1, case2 in test_cases:
    result = concatenate_rounds(case1, case2)
    print(f"   concatenate_rounds({case1}, {case2}) -> {result}")
print()

# Test list_contains_round
print("3. list_contains_round:")
test_cases = [([1, 2, 3], 1), ([1, 2, 3], 4), ([], 1)]
for rounds, number in test_cases:
    result = list_contains_round(rounds, number)
    print(f"   list_contains_round({rounds}, {number}) -> {result}")
print()

# Test card_average
print("4. card_average:")
test_cases = [[1], [5, 6, 7], [1, 2, 3, 4], [1, 10, 100]]
for hand in test_cases:
    result = card_average(hand)
    print(f"   card_average({hand}) -> {result}")
print()

# Test approx_average_is_average
print("5. approx_average_is_average:")
test_cases = [[1, 2, 3], [2, 3, 4], [0, 1, 5], [3, 6, 9, 12, 150]]
for hand in test_cases:
    result = approx_average_is_average(hand)
    print(f"   approx_average_is_average({hand}) -> {result}")
print()

# Test average_even_is_average_odd
print("6. average_even_is_average_odd:")
test_cases = [[5, 6, 8], [1, 2, 3, 4], [1, 2, 3], [5, 6, 7]]
for hand in test_cases:
    result = average_even_is_average_odd(hand)
    print(f"   average_even_is_average_odd({hand}) -> {result}")
print()

# Test maybe_double_last
print("7. maybe_double_last:")
test_cases = [[1, 2, 11], [5, 9, 11], [5, 9, 10], [1, 2, 3]]
for hand in test_cases:
    result = maybe_double_last(hand)
    print(f"   maybe_double_last({hand}) -> {result}")

print()
print("All tests completed!")
