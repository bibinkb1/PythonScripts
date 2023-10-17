import paramiko
# create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# connect to a remote host
client.connect('192.168.15.46', username='test', password='test')
# run a command
stdin, stdout, stderr = client.exec_command('cat /etc/passwd')
print(stdout.read())
# close the connection
client.close()