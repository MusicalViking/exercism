def is_armstrong_number(number):
    digits = str(number)
    number_digits = len(digits)
    total = sum(int(digit) ** number_digits for digit in digits)
    return total == number
