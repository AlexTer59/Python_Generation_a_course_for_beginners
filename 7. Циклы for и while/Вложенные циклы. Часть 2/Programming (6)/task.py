# На вход программе подается два натуральных числа a и b (a<b). Напишите
# программу, которая находит все простые числа от a до b включительно.
#
# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести все простые числа от a до b включительно, каждое
# на отдельной строке.
#
# Примечание. Число 1 простым не является.


a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    for j in range (1, b + 1):
        if i % j == 0:
            counter += 1
    if counter == 2:
        print(i)
    counter = 0
          