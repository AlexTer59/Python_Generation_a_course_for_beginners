# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает список из символов всех строк,
# а затем выводит его.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n строк,
# каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список состоящий из символов всех введенных строк.
#
# Примечание. В результирующем списке могут содержаться одинаковые символы.


n = int(input())
list = []
for i in range(n):
    list.extend(input())
print(list)
