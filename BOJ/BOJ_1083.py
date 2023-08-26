from sys import stdin

N = int(stdin.readline().rstrip())
nums = list(map(int, stdin.readline().rstrip().split()))
S = int(stdin.readline().rstrip())

for i in range(N):
    max_val = nums[i]
    max_index = i
    for j in range(i + 1, min(N, i + S + 1)):
        if max_val < nums[j]:
            max_val = nums[j]
            max_index = j
    S -= max_index - i
    while max_index > i:
        nums[max_index] = nums[max_index - 1]
        max_index -= 1
    nums[i] = max_val

print(*nums)