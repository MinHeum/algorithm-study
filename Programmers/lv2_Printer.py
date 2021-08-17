from collections import deque

priorities = map(int, input().split())
location = int(input())

answer = 0
d = deque([(i,v) for i, v in enumerate(priorities)])

while len(d):
    chk = d.popleft()
    if chk[1] < max(d[1]):
        d.append(chk)
    else:
        answer += 1
        if chk[0] == location:
            break
    
print(answer)