def is_pangram(sentence):
    # Convert to lowercase and keep only letters
    letters = [char.lower() for char in sentence if char.isalpha()]
    # Use set to get unique letters
    unique_letters = set(letters)
    # Check if we have all 26 letters
    return len(unique_letters) == 26
