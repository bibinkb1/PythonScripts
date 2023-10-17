def read_file():
    file = open("/etc/passwd","r")
    for line in file:
        print(line, end="")
    file.close()

read_file()