def square_digits(num):
    num = str(num)
    res = ''
    for i in num:
        ans += str(int(i)**2)
    return int(res)
