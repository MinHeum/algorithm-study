from sys import stdin
N, K = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()
print(arr[K-1])
