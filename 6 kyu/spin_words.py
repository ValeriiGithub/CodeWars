def spin_words(sentence):
    sentence = sentence.split(" ")
    res = []
    for word in sentence:
        if len(word) <= 4:
            res.append(word)
        else:
            res.append(word[::-1])

    return " ".join(res)