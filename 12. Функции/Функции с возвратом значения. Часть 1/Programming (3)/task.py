# Напишите функцию number_of_factors(num), принимающую в качестве
# аргумента число и возвращающую количество делителей данного числа.
#
# Примечание 1. Используйте уже реализованную функцию get_factors(num)
# из предыдущей задачи


def number_of_factors(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result += 1
    return result


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
