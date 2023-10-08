from sys import stdin


gears = [list(stdin.readline().rstrip()) for _ in range(4)]

k = int(stdin.readline())
for _ in range(k):
    num, dir = map(int, stdin.readline().split())
    num -= 1
    dirs = [0] * 4
    dirs[num] = dir

    # 왼쪽 톱니바퀴
    for i in range(num - 1, -1, -1):
        if gears[i][2] != gears[i + 1][6]:
            dirs[i] = -dirs[i + 1]
        else:
            break

    # 오른쪽 톱니바퀴
    for i in range(num + 1, 4):
        if gears[i - 1][2] != gears[i][6]:
            dirs[i] = -dirs[i - 1]
        else:
            break

    # 회전
    for i in range(4):
        if dirs[i] == 1:
            gears[i].insert(0, gears[i].pop())
        elif dirs[i] == -1:
            gears[i].append(gears[i].pop(0))

ans = 0
for i in range(4):
    if gears[i][0] == "1":
        ans += 2**i

print(ans)
