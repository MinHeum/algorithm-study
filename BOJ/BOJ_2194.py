from sys import stdin
from collections import deque

N, M, A, B, K = map(int, stdin.readline().split())

# 지도
maze = [[0 for _ in range(M)] for _ in range(N)]

# 방문 여부
visited = [[0 for _ in range(M)] for _ in range(N)]

# 장애물
for _ in range(K):
    x, y = map(int, stdin.readline().split())
    maze[x - 1][y - 1] = 1

# 시작점
start = list(map(int, stdin.readline().split()))
start[0] -= 1
start[1] -= 1

# 도착점
end = list(map(int, stdin.readline().split()))
end[0] -= 1
end[1] -= 1

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
q = deque()
q.append(start)
visited[start[0]][start[1]] = 1

while q:
    x, y = q.popleft()

    if x == end[0] and y == end[1]:
        print(visited[x][y] - 1)
        exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx + A - 1 >= N or ny + B - 1 >= M:
            continue

        if visited[nx][ny] == 0:
            is_obstacle = False

            for j in range(A):
                for k in range(B):
                    if maze[nx + j][ny + k] == 1:
                        is_obstacle = True
                        break
                if is_obstacle:
                    break
            else:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

print(-1)
