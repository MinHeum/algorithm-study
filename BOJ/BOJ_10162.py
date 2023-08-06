# A = 5 min, B = 1 min, C = 10 sec

T = int(input())
res = [0,0,0]

if T % 10 != 0:
    print("-1")
else:
    while T>0:
        if T >= 300:
            T -= 300
            res[0] += 1
            continue
        if T >= 60:
            T -= 60
            res[1] += 1
            continue
        T -= 10
        res[2] += 1
        continue
    print(res[0],res[1],res[2])