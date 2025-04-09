import random
n = 10
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# минимальное значение
ans = 10 ** 12
for i in range(n):
    if a[i] < ans:
        ans = a[i]
print(ans)
print(min(a))