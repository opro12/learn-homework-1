"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  try:
      while True:
          phrase = input('Как дела? ')
          if phrase == 'Хорошо':
              break
          else:
            continue
  except KeyboardInterrupt:
      print('Пока')
          #print('Неправильный ответ')
  return phrase
    
if __name__ == "__main__":
    hello_user()
