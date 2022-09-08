import os
print('setenv...')
os.environ['USERNAME'] = input('Введите UserName: ')
# show current shell variable value
print(os.environ['USERNAME'])

# runs os.putenv behind the scenes
os.environ['USERNAME'] = 'Brian'
os.system('python echoenv.py')

# changes passed to spawned programs
os.environ['USER'] = 'Arthur'

# and linked-in C library modules
os.system('python echoenv.py')

os.environ['USERNAME'] = input('Введите UserName: ')
print(os.popen('python echoenv.py').read())
