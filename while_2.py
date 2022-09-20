"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

answers = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "На Python?": "Ага", 
                          "А долго еще?": "Незнаю, всё зависит от программиста"}


def ask_user(question):
    while True: 
        question = input('Задай вопрос кожаный! ')
        if question in answers:
            print(answers[question])
            break
        else:
            continue


if __name__ == "__main__":
    ask_user(answers)
