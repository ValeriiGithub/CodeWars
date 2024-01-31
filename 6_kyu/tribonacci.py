def tribonacci(signature, n):
    # Initialize the sequence with the signature
    sequence = signature[:n]

    # Generate the rest of the sequence
    while len(sequence) < n:
        sequence.append(sum(sequence[-3:]))

    return sequence

print(tribonacci([1, 1, 1], 10))  # Output: [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([0, 0, 1], 10))  # Output: [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]

"""
1. `def tribonacci(signature, n):` - Это определение функции с именем `tribonacci`, которая принимает два аргумента: 
`signature` (начальные три числа последовательности) и `n` (количество чисел, которые нужно сгенерировать).

2. `sequence = signature[:n]` - Здесь создается новый список `sequence`, который начинается с первых `n` чисел 
из `signature`. Если `n` меньше длины `signature`, то `sequence` будет содержать только первые `n` чисел `signature`.

3. `while len(sequence) < n:` - Это цикл, который продолжается до тех пор, пока длина `sequence` меньше `n`. 
Цель этого цикла - заполнить `sequence` до `n` чисел.

4. `sequence.append(sum(sequence[-3:]))` - В каждой итерации цикла к `sequence` добавляется сумма последних 
трех чисел `sequence`. Это и есть основная логика последовательности Трибоначчи: каждое следующее число является 
суммой трех предыдущих.

5. `return sequence` - Когда `sequence` достигает `n` чисел, цикл завершается и `sequence` возвращается 
как результат функции.

Надеюсь, это объяснение помогло! Если у вас есть еще вопросы, не стесняйтесь задавать. 😊
"""