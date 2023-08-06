from sys import stdin
from collections import deque

N, M = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))

answer = 0
neg = [ i * -1 for i in arr if i < 0]
pos = [ i for i in arr if i > 0]

neg.sort(reverse=True)
pos.sort(reverse=True)

neg = deque(neg)
pos = deque(pos)

# 가장 큰 값을 찾기 전에 pos, 혹은 neg 중에 원소가 없는 경우에는 따로 처리를 해준다.
if len(neg) == 0:
    answer += pos[0]
    for _ in range(M):
        if len(pos) != 0:
            pos.popleft()
elif len(pos) == 0:
    answer += neg[0]
    for _ in range(M):
        if len(neg) != 0:
            neg.popleft()
# 가장 큰 값의 거리는 한번만 더해야 하므로 먼저 계산한다
else:
    if neg[0] > pos[0]:
        answer += neg[0]
        for _ in range(M):
            if len(neg) > 0:
                neg.popleft()
    else :
        answer += pos[0]
        for _ in range(M):
            if len(pos) > 0:
                pos.popleft()

while len(neg) > 0:
    answer += neg[0] * 2
    for _ in range(M):
        if len(neg) > 0:
            neg.popleft()

while len(pos) > 0:
    answer += pos[0] * 2
    for _ in range(M):
        if len(pos) > 0:
            pos.popleft()

print(answer)
