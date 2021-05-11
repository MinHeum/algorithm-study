import sys
n, m = map(int, sys.stdin.readline().split())
if n > m:
    temp = n
    n = m
    m = temp
arr = []
for i in range(n+1, m):
    arr.append(i)
print(len(arr))
if len(arr) != 0:
    print(*arr)