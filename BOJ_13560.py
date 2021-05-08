import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
answer = 1
arr = [0]+arr

sum = 0
for i in range (1, N+1):
    sum += arr[i]
    if sum < (i * (i-1)) // 2:
        answer = -1
if sum != n * (n+1) // 2

print(answer)
