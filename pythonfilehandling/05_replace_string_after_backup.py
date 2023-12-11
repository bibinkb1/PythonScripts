import re
import os

# specify the filepath and the strings to be searched and replaced
filepath = '/home/bibin/work/pythonscriptingexamples/pythonfilehandling/bibin.txt'
pattern = 'hello'
replacement = 'hi'

# open the file and read its contents
with open(filepath, 'r') as file:
    filedata = file.read()

# perform the search-and-replace
filedata = re.sub(pattern, replacement, filedata)

os.rename(filepath,filepath+'.bak')

# write the modified data back to the file
with open(filepath, 'w') as file:
    file.write(filedata)