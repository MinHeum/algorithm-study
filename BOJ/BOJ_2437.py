from sys import stdin

N = int(stdin.readline().rstrip())
arr = list(map(int,stdin.readline().split()))

arr.sort()
num = 1

for i in range(N):
    if num < arr[i]:
        break
    num += arr[i]
print(num)
