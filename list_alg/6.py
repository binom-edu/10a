import random
n = 10
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# количество пар соседних элементов одного знака
cnt = 0
for i in range(n - 1):
    x, y = a[i], a[i + 1]
    if x * y > 0:
        cnt += 1
print(cnt)