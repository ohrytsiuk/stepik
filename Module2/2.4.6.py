import os

tree = os.walk('main')
data = ""

for address, dirs, files in tree:
    for file in files:
        if file.split(".")[1] == "py":
            data = data + (address + '\n')
            print(address)
            break

with open("output.txt", "w") as file:
    file.write(data)

    # for d in dirs:
    #     new_dirs = os.walk(d)
    #     for i, j in new_dirs:
    #         print(i)
    #         print(j)
    #         # if file.split(".")[1] == "py":
    #         #     print(address + '/' + file)

# sorted(sorted(s), key=str.upper)