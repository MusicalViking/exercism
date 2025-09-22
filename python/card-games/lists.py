"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    if not hand:
        return 0.0

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    if not hand:
        return False

    average = card_average(hand)
    n = len(hand)

    # Check average of first and last
    first_last_avg = (hand[0] + hand[-1]) / 2

    if first_last_avg == average:
        return True

    # Check middle element for odd-length lists
    if n % 2 == 1:
        middle = hand[n // 2]
        if middle == average:
            return True

    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    if not hand:
        return True

    even_indexed = [hand[i] for i in range(0, len(hand), 2)]
    odd_indexed = [hand[i] for i in range(1, len(hand), 2)]

    if not even_indexed or not odd_indexed:
        return True

    even_avg = sum(even_indexed) / len(even_indexed)
    odd_avg = sum(odd_indexed) / len(odd_indexed)

    return even_avg == odd_avg


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if not hand:
        return hand

    result = hand.copy()
    if result[-1] == 11:
        result[-1] *= 2

    return result
