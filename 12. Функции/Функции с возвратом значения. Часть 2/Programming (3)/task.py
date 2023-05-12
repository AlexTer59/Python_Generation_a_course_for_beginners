# Напишите функцию is_password_good(password), которая принимает
# в качестве аргумента строковое значение пароля password и возвращает
# значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
#
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.


def is_password_good(password):
    totaldigit, totalupper, totallower = 0, 0, 0
    if len(password) < 8:
        return False
    for i in range(len(password)):
        if password[i].isupper():
            totalupper += 1
        if password[i].isdigit():
            totaldigit += 1
        if password[i].islower():
            totallower += 1
    if totaldigit != 0 and totalupper != 0 and totallower != 0:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
