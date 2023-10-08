from sys import stdin
from collections import deque

darr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
year = 0


# 빙산 덩어리 개수 세기
def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + darr[i][0]
            ny = y + darr[i][1]
            # 범위 안에 있고
            if 0 <= nx < n and 0 <= ny < m:
                # 바다이면
                if not graph[nx][ny]:
                    sea += 1
                # 방문하지 않았으면
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
        # 바다의 개수 저장
        if sea > 0:
            seaList.append((x, y, sea))
    # 빙산 높이 감소
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1


n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

while ice:
    visited = [[False] * m for _ in range(n)]
    delete = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delete.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delete)))
    year += 1

if group < 2:
    print(0)
