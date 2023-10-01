from sys import stdin
from collections import deque
import copy


N, M = map(int, stdin.readline().split())
board = []
darr = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    q = deque()
    copied = copy.deepcopy(board)

    for i in range(N):
        for j in range(M):
            if copied[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in darr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and copied[nx][ny] == 0:
                copied[nx][ny] = 2
                q.append((nx, ny))

    global answer
    cnt = 0

    for i in range(N):
        cnt += copied[i].count(0)

    answer = max(answer, cnt)

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(cnt + 1)
                board[i][j] = 0

for _ in range(N):
    board.append(list(map(int, stdin.readline().split())))

answer = 0
make_wall(0)
print(answer)