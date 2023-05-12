# Напишите функцию print_digit_sum(), которая принимает
# одно целое число num и выводит на печать сумму его цифр.


def print_digit_sum(num):
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    print(res)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
