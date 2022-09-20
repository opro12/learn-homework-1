"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
from audioop import avg


phones = [
      {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
      {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
      {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

if __name__ == "__main__":
    total_sum = 0
    count_phone = 0
    for phone in phones:
        phone_sum = sum(phone['items_sold'])
        print(f'Суммарное количество продаж для {phone["product"]}: {phone_sum}')
        avg_count = phone_sum/len(phone['items_sold'])
        print(f'Среднее количество продаж для {phone["product"]}: {round(avg_count)}') 
        total_sum += phone_sum
        count_phone = count_phone + len(phone['items_sold'])
        
    print(f'Суммарное количество продаж всех товаров {total_sum}')

    total_avg = total_sum/count_phone
    print(f'Среднее количество продаж всех товаров {total_avg}')

    
