import random
n = 4
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# среднее арифметическое положительных элементов
cnt = 0
summ = 0
for i in range(n):
    if a[i] > 0:
        cnt += 1
        summ += a[i]
print(summ / cnt)