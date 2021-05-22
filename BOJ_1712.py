from sys import stdin

A, B, C = map(float, stdin.readline().split())

if C-B <= 0: print(-1)
else:
    print(int(A / (C-B))+1)
