def valid_braces(string):
    brackets_counter = {}
    for bracket in string:
        brackets_counter[bracket] = brackets_counter.get(bracket, 0) + 1
    print(brackets_counter)

    return None

valid_braces("(({[[]])))")
