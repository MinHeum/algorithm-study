# NOT SOLVED 런타임 에러 (IndexError)
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

count = [0] * 100
max_len = 0

sub_arr = []

for i in range(N): # i is index of pointing
    sub_arr.append(arr[i])
    count[arr[i]] += 1
    if count[arr[i]] > K:
        newstart = sub_arr.index(arr[i])+1
        for j in range(0, newstart):
            count[sub_arr[j]] -= 1
        sub_arr = sub_arr[newstart:]
        i = newstart

    if max_len < len(sub_arr):
        max_len = len(sub_arr)
    
print(max_len)
