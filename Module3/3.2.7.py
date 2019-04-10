s = "abababa"
t = "aba"

numbers = []

for i in range(len(s)):
    pos = s.find(t, i)
    if pos == -1:
        break
    else:
        numbers.append(pos)

print(len(set(numbers)))