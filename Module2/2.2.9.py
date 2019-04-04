import simplecrypt

with open("passwords.txt", "r") as pw:
    passwords = pw.read().split()
    print(passwords)

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

for password in passwords:
    try:
        info = simplecrypt.decrypt(password, encrypted)
        print(info.decode('utf8'))
    except:
        pass
