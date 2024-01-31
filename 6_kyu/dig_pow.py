def dig_pow(n, p):
    # Convert n to string to easily access its digits
    n_str = str(n)

    # Calculate the sum of the digits of n raised to consecutive powers starting from p
    total = sum(int(n_str[i]) ** (p + i) for i in range(len(n_str)))

    # Check if total is a multiple of n
    if total % n == 0:
        return total // n
    else:
        return -1
   