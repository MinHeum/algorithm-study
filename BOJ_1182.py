from itertools import combinations
from sys import stdin

N, S = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
answer = 0

for i in range(1, N+1):
    subsequence = combinations(lst, i)
    for tu in subsequence:
        if sum(tu) == S:
            answer += 1

print(answer)
