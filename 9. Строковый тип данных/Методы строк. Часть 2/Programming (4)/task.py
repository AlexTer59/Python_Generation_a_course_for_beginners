# На вход программе подается строка текста. Напишите программу, которая
# проверяет, что строка заканчивается подстрокой .com или .ru.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести «YES» если введенная строка заканчивается подстрокой
# .com или .ru и «NO» в противном случае.


s = input()
if s.endswith('.com') or s.endswith('.ru'):
    print('YES')
else:
    print('NO')
