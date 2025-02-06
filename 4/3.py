n = int(input())
# Посчитать сумму цифр
ans = 0
while n > 0:
    d = n % 10
    ans += d
    n //= 10
print(ans)