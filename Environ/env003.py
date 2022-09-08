# Загрузка переменных окружения из файла .env.
# Он должен лежать в той же папке, в которой находится настоящая программа.

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
# endif

while 1:
    key_value = input("Введите имя переменной окружения: ")
    print(os.environ.get(key_value))
# endwhile