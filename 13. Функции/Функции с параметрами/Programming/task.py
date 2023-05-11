# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
#
# Примечание. Гарантируется, что основание треугольника – нечетное число.


def draw_triangle(fill, base):
    for i in range(base // 2 + 2):
        print(fill * i)
    for i in range(base // 2, 0, -1):
        print(fill * i)


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
