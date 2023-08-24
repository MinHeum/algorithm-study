from sys import stdin
from collections import deque

# 보물 지도의 크기 입력받기

# N: 세로 크기
# M: 가로 크기

N, M = map(int, stdin.readline().rstrip().split())

# 보물 지도 입력받기
map = [list(stdin.readline().rstrip()) for _ in range(N)]

# 상하좌우
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 정답을 저장할 변수
answer = 0

# 모든 육지에 대해 BFS를 수행하며 가장 먼 거리를 찾는다.
for i in range(N):
    for j in range(M):
        # 육지라면
        if map[i][j] == 'L':
            # 방문 여부를 저장할 리스트
            visited = [[False] * M for _ in range(N)]

            q = deque()
            q.append((i, j, 0))
            visited[i][j] = True

            # BFS
            while q:
                x, y, dist = q.popleft()

                # 현재 위치에서 상하좌우를 탐색한다.
                for dx, dy in delta:
                    nx = x + dx
                    ny = y + dy

                    # 지도를 벗어나지 않는다면
                    if 0 <= nx < N and 0 <= ny < M:
                        # 방문하지 않았고, 육지라면
                        if not visited[nx][ny] and map[nx][ny] == 'L':
                            visited[nx][ny] = True
                            q.append((nx, ny, dist + 1))
                            answer = max(answer, dist + 1)

print(answer)
