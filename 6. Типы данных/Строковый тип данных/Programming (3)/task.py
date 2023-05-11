# Даны названия трех городов. Напишите программу, которая определяет самое короткое
# и самое длинное название города.
#
# Формат входных данных
# На вход программе подаётся названия трех городов, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на
# отдельной строке.
#
# Примечание. Гарантируется, что длины названий всех трех городов различны.


city1, city2, city3 = input(), input(), input()
len_city1 = len(city1)
len_city2 = len(city2)
len_city3 = len(city3)

if len_city1 < len_city2:
    if len_city1 < len_city3:
        print(city1)
    else:
        print(city3)
elif len_city2 < len_city3:
    print(city2)
else:
    print(city3)

if len_city1 > len_city2:
    if len_city1 > len_city3:
        print(city1)
    else:
        print(city3)
elif len_city2 > len_city3:
    print(city2)
else:
    print(city3)
