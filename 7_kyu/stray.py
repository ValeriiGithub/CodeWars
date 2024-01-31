def stray(arr):
    return [x for x in arr if arr.count(x) == 1][0]
