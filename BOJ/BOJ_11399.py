from sys import stdin

N = int(stdin.readline().rstrip())
lst = list(map(int, stdin.readline().split()))

lst.sort()

cumulative_sum = 0
continuous_sum = 0

for i in lst:
    continuous_sum += i
    cumulative_sum += continuous_sum

print(cumulative_sum)
