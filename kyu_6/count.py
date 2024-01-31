def count(s):
    res = {}
    for ch in s:
        res[ch] = res.get(ch, 0) + 1
    return res