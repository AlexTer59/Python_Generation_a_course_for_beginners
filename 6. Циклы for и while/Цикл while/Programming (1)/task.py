# На вход программе подается последовательность слов, каждое слово на
# отдельной строке. Концом последовательности является слово «КОНЕЦ» или
# «конец» (большими или маленькими буквами, без кавычек). При этом сами слова
# «КОНЕЦ» и «конец» не входят в последовательность, лишь символизируя её окончание.
# Напишите программу, которая выводит члены данной последовательности.
#
# Формат входных данных
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести члены данной последовательности.


str = input()
while str != 'КОНЕЦ' and str != 'конец':
    print(str)
    str = input()
