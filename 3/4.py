n = int(input())
a = n % 4 == 0
b = n % 100 == 0
c = n % 400 == 0

if a and not b or c:
    print('YES')
else:
    print('NO')