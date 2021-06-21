from sys import stdin

n = int(stdin.readline().rstrip())
a, b = 100, 100
for _ in range(n):
    dice1, dice2 = map(int,stdin.readline().split())
    if dice1 > dice2:
        b -= dice1
    elif dice1 == dice2:
        continue
    else:
        a-= dice2

print(a)
print(b)
