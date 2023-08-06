from sys import stdin
import itertools

def fun(a, b):
    score = 0
    for i in range(4):
        if a[i] != b[i]:
            score += 1
    return score

def calc(a):
    score = 0
    score += fun(a[0],a[1])
    score += fun(a[0],a[2])
    score += fun(a[1],a[2])
    return score

T = int(stdin.readline().rstrip())

for _ in range(T):
    answer = 0
    N = int(stdin.readline().rstrip())
    arr = list(stdin.readline().split())
    score_arr = []
    if N > 32:
        print(answer)
    else:
        for i in itertools.combinations(arr, 3):
            score_arr.append(calc(i))
        score_arr.sort()
        print(score_arr[0])
