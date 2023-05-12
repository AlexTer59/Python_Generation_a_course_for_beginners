# Интернет магазин осуществляет экспресс доставку для своих товаров по
# цене 1000 рублей за первый товар и 120 рублей за каждый последующий товар.
# Напишите функцию get_shipping_cost(quantity), которая принимает в качестве
# аргумента натуральное число quantity – количество товаров в заказе и возвращает
# стоимость доставки.


def get_shipping_cost(quantity):
    if quantity == 1:
        cost = 1000
    elif quantity > 1:
        cost = 1000 + 120 * (quantity - 1)
    else:
        return False
    return cost


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))
