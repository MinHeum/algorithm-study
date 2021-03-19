T = int(input())
for _ in range(T):
    a = map(str, input().split())
    a = list(a)
    res = float(a.pop(0))
    for i in a:
        if i == "@":
            res *= 3
        elif i == "%":
            res += 5
        elif i == "#":
            res -= 7
    print('%.2f' % res)