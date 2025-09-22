def is_isogram(string):
    # Convert to lowercase
    string = string.lower()

    # Filter out non-letter characters except spaces and hyphens
    letters = []
    for char in string:
        if char.isalpha():
            letters.append(char)

    # Check if all letters are unique
    return len(letters) == len(set(letters))
