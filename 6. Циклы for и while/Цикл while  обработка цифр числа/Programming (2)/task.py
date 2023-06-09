# Дано натуральное число n,(n≥10). Напишите программу, которая определяет
# его максимальную и минимальную цифры.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести максимальную и минимальную цифры введенного числа
# (с поясняющей надписью).


num = int(input())
max_digit = -1
min_digit = 10
while num != 0:
    last_digit = num % 10
    if last_digit > max_digit:
        max_digit = last_digit
    if last_digit < min_digit:
        min_digit = last_digit
    num = num // 10
print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)
