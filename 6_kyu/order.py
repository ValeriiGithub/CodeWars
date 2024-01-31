def order(sentence):
    if not sentence:
        return ""

    words = sentence.split()
    sorted_words = sorted(words, key=lambda word: sorted(word))

    return " ".join(sorted_words)


print(order("is2 Thi1s T4est 3a"))  # Outputs: "Thi1s is2 3a T4est"
print(order("4of Fo1r pe6ople g3ood th5e the2"))  # Outputs: "Fo1r the2 g3ood 4of th5e pe6ople"
print(order(""))  # Outputs: ""
