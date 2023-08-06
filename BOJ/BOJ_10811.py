import sys
N, M = map(int, sys.stdin.readline().split())
lst = [i for i in range(1,N+1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    lst = lst[:s-1] + lst[s-1:e][::-1] + lst[e:]
print (*lst, sep=' ')
