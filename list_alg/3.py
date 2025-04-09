import random
n = 4
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# сумма элементов
ans = 0
for i in range(n):
    ans += a[i]

print(ans)
print(sum(a))