import os

# specify the filepath and the strings to be searched and replaced
filepath = '/home/bibin/work/pythonscriptingexamples/pythonfilehandling/bibin.txt'
old_string = 'hello'
new_string = 'hi'

# open the file and read its contents
with open(filepath, 'r') as file:
    filedata = file.read()

# replace the old string with the new string
filedata = filedata.replace(old_string, new_string)

# write the modified data back to the file
with open(filepath, 'w') as file:
    file.write(filedata)