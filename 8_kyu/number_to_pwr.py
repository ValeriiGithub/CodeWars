def number_to_pwr(number, power):
    if power < 0:
        return 0  # Return False for negative powers

    elif power == 0:
        return 1

    result = 1
    for _ in range(power):
        result *= number
    return result
