from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]

# 방문 여부를 저장하는 삼차원 배열
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


# 상하좌우
darr = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for dx, dy in darr:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아닌 경우
                if board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))

                # 벽인 경우
                if z == 0 and board[nx][ny] == 1 and visited[nx][ny][z + 1] == 0:
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
                    q.append((nx, ny, z + 1))

    return -1


print(bfs())
