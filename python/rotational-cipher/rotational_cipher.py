def rotate(text, key):
    result = []

    for char in text:
        if char.islower():
            # Handle lowercase letters
            shifted = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result.append(shifted)
        elif char.isupper():
            # Handle uppercase letters
            shifted = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            result.append(shifted)
        else:
            # Leave non-letters unchanged
            result.append(char)

    return ''.join(result)
