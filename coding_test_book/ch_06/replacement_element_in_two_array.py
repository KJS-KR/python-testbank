a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

a.sort()
b.sort(reverse=True)

for i in range(3):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
