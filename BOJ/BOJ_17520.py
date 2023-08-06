n = int(input())

mod = 16769023

res = 2
x = int((n-1)/2+1)

while x > 1:
    res *= 2
    res %= mod
    x -= 1

print(res % mod)
