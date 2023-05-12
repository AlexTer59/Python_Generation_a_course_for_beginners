# Напишите функцию is_correct_bracket(text), которая принимает в качестве
# аргумента непустую строку text, состоящую из символов ( и ) и возвращает
# значение True если поступившая на вход строка является правильной скобочной
# последовательностью и False в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью называется строка,
# состоящая только из символов ( и ), где каждой открывающей скобке найдется
# парная закрывающая скобка (при этом каждая открывающая скобка должна быть левее
# соответствующей ей закрывающей скобки).
#


def is_correct_bracket(text):
    check_sum = 0
    if text[0] == '(' and text[len(text) - 1] == ')':
        for i in range(0, len(text)):
            if text[i] == '(':
                check_sum += 1
            else:
                check_sum -= 1
            if check_sum < 0:
                return False
        if check_sum == 0:
            # print(close_bracket, open_bracket)
            return True
        else:
            return False
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
