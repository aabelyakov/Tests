import os

# Определяем имя файла из переменной окружения PYTHONSTARTUP
filename = os.environ.get('PYTHONSTARTUP')

if filename and os.path.isfile(filename):
    os.execl(filename, "")
# endif
