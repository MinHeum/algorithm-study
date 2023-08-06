from sys import stdin

N = int(stdin.readline().rstrip())

for _ in range(N):
    r, e, c = map(int,stdin.readline().split())
    if r > (e - c):
        print('do not advertise')
    elif r == (e - c):
        print('does not matter')
    else:
        print('advertise')
