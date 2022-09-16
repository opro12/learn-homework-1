"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


from cmath import phase


def hello_user():
    while True:
        phrase = input('Как дела? ')
        if phrase == 'Хорошо':
          break
        else:
          continue
          #print('Неправильный ответ')
    return phrase  

    
if __name__ == "__main__":
    hello_user()
