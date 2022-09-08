import os
print("Ключи и значения переменных окружения интерпретатора PYTHON:")
# print(os.environ)
for key in os.environ:
    print(key, '=>', os.environ[key])
# endfor

print("\nЗначение переменной окружения HOME: ", os.environ['HOME'])
path = os.environ['PATH'].replace(':', '\n')
print("\nПути из переменной окружения PATH: ")
print(path)

