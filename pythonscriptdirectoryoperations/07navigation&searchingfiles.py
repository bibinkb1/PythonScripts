import os
print(os.getcwd()) 
os.system('ls -l')
output = os.popen('ls -l').read()