

with open("dataset_24465_4.txt", "r") as f1:
    data = f1.read().split()

data.reverse()

with open("fileout.txt", "w+") as f2:
    for s in data:
        f2.write(s + "\n")
