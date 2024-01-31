// Импортируем пакет strings для работы со строками
import "strings"

// Определяем функцию initials, которая принимает строку name и возвращает строку с инициалами
func AbbrevName(name string) string{
  // Разделяем строку name на две подстроки по пробелу и сохраняем результат в слайс words
  words := strings.Split(name, " ")
  // Получаем первый символ первого слова в верхнем регистре и сохраняем его в переменную first
  first := strings.ToUpper(string(words[0][0]))
  // Получаем первый символ второго слова в верхнем регистре и сохраняем его в переменную second
  second := strings.ToUpper(string(words[1][0]))
  // Соединяем first, "." и second в одну строку и возвращаем ее из функции
  return first + "." + second
}
