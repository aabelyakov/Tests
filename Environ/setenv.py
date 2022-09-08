import os
print 'setenv...',
print os.environ['USERNAME']                 # show current shell variable value

os.environ['USERNAME'] = 'Brian'             # runs os.putenv behind the scenes
os.system('python echoenv.py')

os.environ['USER'] = 'Arthur'                # changes passed to spawned programs
os.system('python echoenv.py')               # and linked-in C library modules

os.environ['USERNAME'] = raw_input('UserName')    
print os.popen('python echoenv.py').read() 
