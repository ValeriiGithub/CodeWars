"""
https://www.codewars.com/kata/55e529bf6c6497394a0000b5
"""

def combine(*args):
    result = []
    max_length = max(len(arr) for arr in args)

    for i in range(max_length):
        for arr in args:
            if i < len(arr):
                result.append(arr[i])

    return result
