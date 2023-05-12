# Напишите функцию convert_to_python_case(text), которая принимает в
# качестве аргумента строку в «верблюжьем регистре» и преобразует его в
# «змеиный регистр».


def convert_to_python_case(text):
    for i in range(len(text)):
        if text[i].isupper():
            text = text.replace(text[i], '_' + text[i].lower())
    return text[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
