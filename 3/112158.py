a, b, c = map(int, input().split())

if a == b:
    if a > c:
        print('A C')
    elif a == c:
        print(0)
    else:
        print('C')
elif b > a:
    if b > c:
        print('B')
    elif b == c:
        print('B C')
    elif c > b:
        print('C')
elif a > b:
    if a > c:
        print('A')
    elif a == b:
        print('A B')
    elif c > a:
        print('C')