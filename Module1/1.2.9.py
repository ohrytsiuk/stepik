objects = [1, 2, 1, 2, 3]

ans = 0
unique = []
for obj in objects:  # доступная переменная objects
    if obj not in unique:
        unique.append(obj)
        ans += 1

print(ans)
