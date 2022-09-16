"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def string_checking(string1, string2):
    if type(string1) != str or type(string2) != str:
      return '0'
    if string1 == string2:
      return '1'
    if len(string1) > len(string2):
      return '2'
    if string2 == 'learn':
      return '3'

temp_var = int(4)
print(string_checking('temp_var', temp_var))
print(string_checking('test', 'test'))
print(string_checking('testtest', 'test'))
print(string_checking('test', 'learn'))
        
if __name__ == "__main__":
    string_checking()
