# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()

# for line in open("data.txt", "r"):
#     print(line)

# file = open("data.txt", "r")
# # line = file.readline()
# lines = file.readlines()
# print(lines)
# file.close()

# context manager
# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

with open("data.txt", "r+") as file:
    data = file.read()
    print(data)
    file.write("New data added")
    print(file.read())