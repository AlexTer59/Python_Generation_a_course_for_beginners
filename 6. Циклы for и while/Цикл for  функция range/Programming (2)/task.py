# Даны два целых числа m и n (m>n). Напишите программу, которая выводит
# все нечетные числа от m до n включительно в порядке убывания.
#
# Формат входных данных
# На вход программе подаются два целых числа m и n, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести числа в соответствии с условием задачи.


m, n = int(input()), int(input())
if m % 2 == 0:
    for i in range(m - 1, n - 1, -2):
        print(i)
else:
    for i in range(m, n - 1, -2):
        print(i)
