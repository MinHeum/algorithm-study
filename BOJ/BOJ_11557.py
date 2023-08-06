from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())
    dic = {}
    for __ in range(N):
        k, v = stdin.readline().split()
        dic[k] = int(v)

    print(max(dic, key=dic.get))
