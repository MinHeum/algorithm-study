from sys import stdin

N, K = map(int, stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
arr_diff = []

for i in range(len(arr)-1):
    arr_diff.append(arr[i+1] - arr[i])

arr_diff.sort()

for i in range(K-1):
    arr_diff.pop()

print(sum(arr_diff))