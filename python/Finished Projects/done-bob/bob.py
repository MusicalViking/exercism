def response(hey_bob):
    statement = hey_bob.strip()

    if not statement:
        return "Fine. Be that way!"

    is_question = statement.endswith("?")
    is_yelling = statement.isupper() and any(char.isalpha() for char in statement)

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."
