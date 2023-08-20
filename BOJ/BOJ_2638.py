from sys import stdin
from collections import deque

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, stdin.readline().split())
visited = [[False] * M for _ in range(N)]
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
answer = 0


def outSide():
    q = deque()
    out_visited = [[False] * M for _ in range(N)]
    q.append((0, 0))
    out_visited[0][0] = True
    board[0][0] = -1
    while q:
        y, x = q.popleft()
        for dy, dx in delta:
            ny = dy + y
            nx = dx + x
            if 0 > ny or ny >= N or 0 > nx or nx >= M:
                continue
            if board[ny][nx] == 1 or out_visited[ny][nx]:
                continue
            q.append((ny, nx))
            board[ny][nx] = -1
            out_visited[ny][nx] = True
    return


# 치즈가 다 녹았는지 확인하는 함수
def is_melted():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                return False
    return True


while not is_melted():
    outSide()
    check = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt = 0  # 바깥 공기와 닿은 칸의 수
                for dy, dx in delta:
                    ny = dy + i
                    nx = dx + j
                    if 0 > ny or ny >= N or 0 > nx or nx >= M:
                        continue
                    if board[ny][nx] == -1:
                        cnt += 1
                if cnt >= 2:
                    check.append([i, j])
    for y, x in check:
        board[y][x] = 0
    answer += 1


print(answer)
