def duplicate_encode(s):
    # convert the string to lowercase
    s = s.lower()
    # create an empty dictionary
    freq = {}
    # loop through each character in the string
    for c in s:
        # if the character is already in the dictionary, increment its value by 1
        if c in freq:
            freq[c] += 1
        # otherwise, set its value to 1
        else:
            freq[c] = 1
    # create an empty string for the result
    result = ""
    # loop through each character in the string again
    for c in s:
        # if the character has a frequency of 1, append "(" to the result
        if freq[c] == 1:
            result += "("
        # otherwise, append ")" to the result
        else:
            result += ")"
    # return the result
    return result
