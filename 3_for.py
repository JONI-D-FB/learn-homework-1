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

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    total = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
     ]
    
    def count_sum_person(sku_sum_product):
       sku_sell=0
       for sku_sum in sku_sum_product:
          sku_sell += sku_sum
          summm = sku_sell
       return summm
    
      
    def average_count_sum_person(av_sku_sum_product):
       sku_sell=0
       for sku_sum in av_sku_sum_product:
          sku_sell += sku_sum
          av_sku_sell = sku_sell/len(av_sku_sum_product)
       return av_sku_sell

    middle_sku_sell = 0
    each_sku_sell = 0
    for phone in total:
       sku_sum_sell = count_sum_person(phone['items_sold'])
       av_sku_sum_sell = average_count_sum_person(phone['items_sold'])
       print(f"суммарное количество продаж для товара {phone['product']} : {sku_sum_sell}")
       print(f"Среднее колличество продаж для товара {phone['product']}' : {av_sku_sum_sell}")
       each_sku_sell += sku_sum_sell
       middle_sku_sell +=  av_sku_sum_sell
       print(f"Суммарное количество продаж всех товаров: {each_sku_sell}")
       print(f"Среднее количество продаж всех товаров: {middle_sku_sell}")

if __name__ == "__main__":
    main()
   

