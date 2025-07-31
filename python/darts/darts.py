def score(x, y):

    distance = x * x + y * y

    if distance <= 1**2:
        return 10
    elif distance <= 5**2:
        return 5
    elif distance <= 10**2:
        return 1
    else:
        return 0
