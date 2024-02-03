from collections import Counter

def only_duplicates(str):
  # Создаем счетчик, который подсчитывает, сколько раз каждый символ встречается в строке
  counter = Counter(str)
  # Создаем пустую строку, в которую будем добавлять только дублирующиеся символы
  result = ""
  # Проходим по строке и проверяем, встречается ли символ больше одного раза
  for char in str:
    if counter[char] > 1:
      # Если да, то добавляем его в результат
      result += char
  # Возвращаем результат
  return result
  