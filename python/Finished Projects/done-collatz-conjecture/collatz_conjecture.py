def steps(number):

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    new = number
    while new != 1:

        if new % 2 == 0:
            new = new // 2
        else:
            new = 3 * new + 1
        steps += 1
    return steps
