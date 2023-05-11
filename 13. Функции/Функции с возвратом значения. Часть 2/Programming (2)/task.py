# Напишите функцию get_next_prime(num), которая принимает в качестве
# аргумента натуральное число num и возвращает первое простое число большее
# числа num.
#
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.


def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter > 2 or counter == 1:
        return False
    else:
        return True


def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
