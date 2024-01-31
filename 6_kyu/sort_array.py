def sort_array(array):
    # Extract odd numbers and sort them in ascending order
    sorted_odds = sorted(x for x in array if x % 2 != 0)

    # Replace the odd numbers in the original array with the sorted ones
    for i in range(len(array)):
        if array[i] % 2 != 0:
            array[i] = sorted_odds.pop(0)

    return array


print(sort_array([7, 1]))  # Output: [1, 7]
print(sort_array([5, 8, 6, 3, 4]))  # Output: [3, 8, 6, 5, 4]
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # Output: [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

"""
Конечно, я с удовольствием объясню, как работает этот код на Python:

1. `def sort_array(array):` - Это определение функции с именем `sort_array`, которая принимает один аргумент: `array` (массив чисел).

2. `sorted_odds = sorted(x for x in array if x % 2 != 0)` - Здесь создается новый список `sorted_odds`, который содержит все нечетные числа из `array`, отсортированные в порядке возрастания. Это достигается с помощью генератора списка, который выбирает только те числа `x` из `array`, которые являются нечетными (`x % 2 != 0`), и функции `sorted()`, которая сортирует эти числа.

3. `for i in range(len(array)):` - Это цикл, который проходит по каждому индексу `i` в `array`.

4. `if array[i] % 2 != 0:` - Это условное выражение, которое проверяет, является ли текущее число `array[i]` нечетным.

5. `array[i] = sorted_odds.pop(0)` - Если `array[i]` является нечетным, то оно заменяется на наименьшее оставшееся нечетное число из `sorted_odds` (которое затем удаляется из `sorted_odds`).

6. `return array` - Когда все нечетные числа в `array` заменены на отсортированные нечетные числа, `array` возвращается как результат функции.

Надеюсь, это объяснение помогло! Если у вас есть еще вопросы, не стесняйтесь задавать. 😊
"""