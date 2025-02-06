n = int(input())

c = 0
while c < n:
    print('С Новым годом!')
    c += 1
    if c == 4:
        break
else:
    print('Блок else')
print('Программа закончена')