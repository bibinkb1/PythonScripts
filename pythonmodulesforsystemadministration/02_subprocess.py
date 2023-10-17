import subprocess
# run a command and wait for it to complete
subprocess.run(['ls', '-l']) # runs the command 'ls -l'
# run a command and get the output
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print(result.stdout)