from sys import stdin

N, M, K = map(int,stdin.readline().split())

while K > 0:
    if N > 2 * M:
        N -= 1
    else:
        M -= 1
    K -= 1

if N <= 1 or M == 0:
    print(0)
else:
    print(min(N//2, M))
