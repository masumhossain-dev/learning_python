file = open("read_files/names.txt", "r")
content = file.read()

print(content)

file.close()

with open("read_files/names.txt", "r") as file:
    content = file.read()

    print(content)