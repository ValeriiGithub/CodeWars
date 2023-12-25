def remove_smallest(numbers):
    if numbers:
        res = numbers.copy()
        res.pop(res.index(min(res)))
        return res
    else:
        return []