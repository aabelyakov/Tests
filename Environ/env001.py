import os

print("Переменные окружения системного интерпретатора (Ключ => Значение):")
# print(os.environ)
for key in os.environ:
    print(key, '=>', os.environ.get(key))
# endfor

print("\nЗначение переменной окружения HOME: ", os.environ['HOME'])

path = os.environ.get('PATH').replace(':', '\n')
print("\nПути из переменной окружения PATH: ")
print(path)

