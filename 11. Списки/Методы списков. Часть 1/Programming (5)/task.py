# На вход программе подается натуральное число n≥2, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список, состоящий из
# сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из сумм соседних чисел.


n = int(input())
list = []
new_list = []
for i in range(n):
    num = str(input())
    list.append(num)
for k in range (len(list) - 1):
    new_num = int(list[k]) + int(list[k + 1])
    new_list.append(new_num)
print(new_list)

    
