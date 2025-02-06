# Является ли число простым
n = int(input())

d = 2 # кандидат в делители
while d < n:
    if n % d == 0:
        print('no')
        break
    d += 1
else:
    print('yes')
