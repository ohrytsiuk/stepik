# s = "ababac"
# a = "c"
# b = "c"

# s = "aabbcc"
# a = "aa"
# b = "aaa"

s = "abab"
a = "ab"
b = "ba"

# print(s.replace(a, b, 0))
# print(s.replace(a, b, 1))
# print(s.replace(a, b, 2))
# print(s.replace(a, b, 3))
# print(s.replace(a, b, 4))

# s = input()
# a = input()
# b = input()

if a in b and a in s:
    print("Impossible")
else:
    i = 0
    new_str = s
    while a in new_str:
        if i > 1000:
            print("Impossible")
            break
        new_str = new_str.replace(a, b)
        i += 1
    else:
        print(i)
