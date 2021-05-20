import sys

S, T = [list(sys.stdin.readline().strip()) for _ in range(2)]

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1] # 문자열 뒤집기

if S == T:
    print(1)
else:
    print(0)