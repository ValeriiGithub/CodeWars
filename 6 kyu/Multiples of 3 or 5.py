def solution(number):
    # Check if the number is negative
    if number < 0:
        return 0

    # Initialize the sum
    sum_multiples = 0

    # Iterate through numbers below the input
    for i in range(number):
        # Check if the current number is a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i

    return sum_multiples
