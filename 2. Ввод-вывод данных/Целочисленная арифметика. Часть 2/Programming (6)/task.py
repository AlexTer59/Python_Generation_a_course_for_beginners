# Напишите программу, в которой рассчитывается сумма и произведение цифр
# положительного трёхзначного числа.
#
# Формат входных данных
# На вход программе подаётся положительное трёхзначное число.
#
# Формат выходных данных
# Программа должна вывести два числа с поясняющим текстом: сумма цифр
# и произведение цифр.


num = int(input())
print('Сумма цифр =', num // 100 + ((num % 100) // 10) + num % 10)
print('Произведение цифр =', (num // 100) * ((num % 100) // 10) * (num % 10))
