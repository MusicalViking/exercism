def translate(text):
    def is_vowel(ch):
        return ch in "aeiou"

    def translate_words(words):
        if words.startswith(
            (
                "a",
                "e",
                "i",
                "o",
                "xr",
                "yt",
            )
        ):
            return words + "ay"

        if words.startswith("qu"):
            return words[2:] + "quay"

        if "qu" in words:
            index = words.find("qu")
            if all(not is_vowel(c) for c in words[:index]):
                return words[index + 2 :] + words[: index + 2] + "ay"

        for i, ch in enumerate(words):
            if is_vowel(ch):
                return words[i:] + words[:i] + "ay"

        if "y" in words[1:] and all(
            not is_vowel(ch) for ch in words[: words.find("y")]
        ):
            index = words.find("y", 1)
            return words[index:] + words[:index] + "ay"

        return words + "ay"

    return " ".join(translate_words(w) for w in text.split())
