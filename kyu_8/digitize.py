def digitize(n):
    return [int(x) for x in str(n)[::-1]]

def digitize_2(n):
    return map(int, str(n)[::-1])

def digitize_3(n):
    return [int(x) for x in reversed(str(n))]
