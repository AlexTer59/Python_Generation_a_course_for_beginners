# Дополните приведенный код, используя списочное выражение так, чтобы получить новый список,
# содержащий строки исходного списка с удаленным первым символом.


keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [keywords[i][1::] for i in range(len(keywords))]

print(new_keywords)
