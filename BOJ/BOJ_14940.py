from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

visited = [[False] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 시작점 설정
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i, j

# bfs
q = deque()
q.append((start_x, start_y))
visited[start_x][start_y] = True

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue

        if graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=" ")
        elif graph[i][j] == 2:
            print(0, end=" ")
        else:
            print(graph[i][j] - 2, end=" ")
    print()
