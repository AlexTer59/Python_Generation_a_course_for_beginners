# Напишите программу, которая проверяет, что для заданного
# четырехзначного числа выполняется следующее соотношение: сумма первой
# и последней цифр равна разности второй и третьей цифр.
#
# Формат входных данных
# На вход программе подаётся одно целое положительное четырёхзначное число.
#
# Формат выходных данных
# Программа должна вывести «ДА», если соотношение выполняется, и
# «НЕТ» — если не выполняется.


num = int(input())
num_1 = num // 1000
num_2 = (num % 1000) // 100
num_3 = (num % 100) // 10
num_4 = num % 10
if (num_1 + num_4) == (num_2 - num_3):
    print('ДА')
else:
    print('НЕТ')
