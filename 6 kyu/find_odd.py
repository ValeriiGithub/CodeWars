def find_odd(arr):
    # create an empty dictionary
    freq = {}
    # loop through each integer in the array
    for n in arr:
        # if the integer is already in the dictionary, increment its value by 1
        if n in freq:
            freq[n] += 1
        # otherwise, set its value to 1
        else:
            freq[n] = 1
    # loop through the dictionary
    for k, v in freq.items():
        # if the value is odd, return the key
        if v % 2 != 0:
            return k
    # if no odd frequency is found, return None
    return None


# test the function with some examples
print(find_odd([7]))  # 7
print(find_odd([0]))  # 0
print(find_odd([1, 1, 2]))  # 2
print(find_odd([0, 1, 0, 1, 0]))  # 0
print(find_odd([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))  # 4
