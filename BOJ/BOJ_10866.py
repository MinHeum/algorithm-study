from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
deq = deque()

for i in range(N):
    S = stdin.readline().split()
    if len(S) == 1:
        # size, empty, front, back
        if S[0] == 'size':
            print(len(deq))

        if S[0] == 'empty':
            if len(deq) == 0:
                print(1)
            else:
                print(0)

        if S[0] == 'front':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq[0])

        if S[0] == 'back':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq[-1])

        if S[0] == 'pop_front':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq.popleft())

        if S[0] == 'pop_back':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq.pop())
    else: # len(S) == 2,
        # push_front X, push_back X, pop_front X, pop_back X
        command, value = S[0], S[1]
        if command == 'push_front':
            deq.appendleft(value)
        if command == 'push_back':
            deq.append(value)
