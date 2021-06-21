from sys import stdin
from math import ceil

N = int(stdin.readline().rstrip())
arr = list(map(int,stdin.readline().split()))
B, C = map(int,stdin.readline().split())

count = N

for i in range(len(arr)):
    arr[i] -= B
    if arr[i] > 0:
        count += ceil(arr[i] / C)

print(count)
