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
phones = [
      {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
      {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
      {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def total_number_of_sales(product):
    summa = 0
    for var_sales in product:
        summa += var_sales
    return summa

def avg_number_of_sales(product):
    average = 0
    for var_sales in product:
        average += var_sales
    return average / len(product)

sum_phones = 0
for one_product in phones:
    product_sum = total_number_of_sales(one_product['items_sold'])
    print(f'Суммарное количество продаж для {one_product["product"]}: {product_sum}')
    sum_phones += product_sum

avg_phones = 0
for one_product in phones:
    product_avg = avg_number_of_sales(one_product['items_sold'])
    print(f'Среднее количество продаж для {one_product["product"]}: {round(product_avg)}')
    avg_phones += product_avg

print(f'Суммарное количество продаж всех товаров {sum_phones}')
print(f'Среднее количество продаж всех товаров {avg_phones/len(phones)}')


    
if __name__ == "__main__":
    sum_phones = 0
    for one_product in phones:
        product_sum = total_number_of_sales(one_product['items_sold'])
        print(f'Суммарное количество продаж для {one_product["product"]}: {product_sum}')
        sum_phones += product_sum
    print(f'Суммарное количество продаж всех товаров {sum_phones}')   
    
    avg_phones = 0
    for one_product in phones:
        product_avg = avg_number_of_sales(one_product['items_sold'])
        print(f'Среднее количество продаж для {one_product["product"]}: {round(product_avg)}')
        avg_phones += product_avg
    print(f'Среднее количество продаж всех товаров {avg_phones/len(phones)}')

    
