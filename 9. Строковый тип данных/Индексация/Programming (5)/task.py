# На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
#
# Формат входных данных
# На вход программе подается одна строка состоящая из цифр.
#
# Формат выходных данных
# Программа должна вывести сумму цифр данной строки.


str = input()
num = int(str)
sum = 0
for i in range(0, num + 1):
    last_digit = num % 10
    sum += last_digit
    num = num // 10
print(sum)
