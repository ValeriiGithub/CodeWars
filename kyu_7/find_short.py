def find_short0(s):
    return min(len(x) for x in s.split())


def find_short1(s):
    return min(s.split(), key=len)


def find_short2(s):
    return min(map(len, s.split(' ')))


s = "bitcoin take over the world maybe who knows perhaps"

find_short0(s)
find_short1(s)
find_short2(s)
