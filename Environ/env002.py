import os

while 1:
    # Принимаем имя переменной окружения
    key_value = input("Введите имя переменной окружения: ")
    print(os.environ.get(key_value))
# endwhile

