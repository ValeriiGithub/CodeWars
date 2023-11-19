def remov_nb(n):
    total_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    result = []

    for a in range(1, n + 1):
        b = (total_sum - a) // (a + 1)  # Calculate b based on the given condition
        if 1 <= b <= n and a * b == total_sum - a - b:
            result.append((a, b))

    return result
