# На числовой прямой даны два отрезка: [a1;b1] и [a2;b2]. Напишите
# программу, которая находит их пересечение.
#
# Пересечением двух отрезков может быть:
#
# отрезок;
# точка;
# пустое множество.

# Формат входных данных
# На вход программе подаются 4 целых числа a1,b1,a2,b2, каждое на отдельной строке.
# Гарантируется, что a1<b1 и a2<b2.
#
# Формат выходных данных
# Программа должна вывести на экран границы отрезка, являющегося пересечением,
# либо общую точку, либо текст «пустое множество».


a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a1 <= a2 and b1 >= a2 and b2 >= b1:
    if a2 == b1:
        print(a2)
    elif b1 < a2:
        print('пустое множество')
    else:
        print(a2, b1)
elif a2 <= a1 and b2 >= a1 and b1 >= b2:
    if a1 == b2:
        print(a1)
    elif b2 < a1:
        print('пустое множество')
    else:
        print(a1, b2)
elif a2 <= a1 and b2 >= b1:
    if a1 == b1:
        print(a1)
    else:
        print(a1, b1)
elif a1 <= a2 and b1 >= b2:  # сделать сравнение длины
    if a2 == b2:
        print(a2)
    else:
        print(a2, b2)
else:
    print('пустое множество')
