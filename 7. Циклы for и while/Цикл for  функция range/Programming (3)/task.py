# Даны два натуральных числа m и n (m≤n). Напишите программу, которая
# выводит все числа от m до n включительно удовлетворяющие хотя бы одному
# из условий:
#
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.

# Формат входных данных
# На вход программе подаются два натуральных числа m и n (m≤n), каждое на
# отдельной строке.
#
# Формат выходных данных
# Программа должна вывести числа в соответствии с условием задачи.
#
# Примечание. Если чисел удовлетворяющих условию нет, выводить ничего не надо.


m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)
