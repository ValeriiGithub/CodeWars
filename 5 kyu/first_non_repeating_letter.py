def first_non_repeating_letter(s):
    # Convert the string to lowercase for case-insensitive comparison
    s_lower = s.lower()

    for char in s:
        if s_lower.count(char.lower()) == 1:
            return char

    return ''


print(first_non_repeating_letter('sTreSS'))
