def is_valid(isbn):
    # Remove dashes
    isbn = isbn.replace('-', '')

    # Check length
    if len(isbn) != 10:
        return False

    # Check for invalid characters
    for i, char in enumerate(isbn):
        if i == 9:  # Check digit position
            if char not in '0123456789X':
                return False
        else:  # Digits 1-9 positions
            if char not in '0123456789':
                return False

    # Calculate check digit
    total = 0
    for i, char in enumerate(isbn):
        if char == 'X':
            digit = 10
        else:
            digit = int(char)
        total += digit * (10 - i)

    return total % 11 == 0
