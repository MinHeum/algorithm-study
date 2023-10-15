from sys import stdin
from copy import deepcopy

DIRECTION = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]],
}

darr = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, M = map(int, stdin.readline().split())

office = []

for _ in range(N):
    office.append(list(map(int, stdin.readline().split())))

cctvs = []  # cctv의 위치와 번호를 저장

for i in range(N):
    for j in range(M):
        if office[i][j] != 0 and office[i][j] != 6:
            cctvs.append((i, j, office[i][j]))  # cctv의 위치와 번호를 저장


def set_watched_area(office, direction, x, y):
    for d in direction:
        dx, dy = darr[d]
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < M and office[nx][ny] != 6:
            if office[nx][ny] == 0:
                office[nx][ny] = "#"
            nx += dx
            ny += dy


def dfs(office, cctvs, idx):  # idx번째 cctv를 감시 방향을 정하고, 다음 cctv를 감시 방향을 정함
    if idx == len(cctvs):  # 모든 cctv의 감시 방향을 정했으면 사각지대의 개수를 세고 리턴
        cnt = 0  # 사각지대의 개수
        for i in range(N):
            for j in range(M):
                if office[i][j] == 0:
                    cnt += 1
        return cnt

    answer = N * M  # 사각지대의 최솟값을 저장

    x, y, cctv = cctvs[idx]  # idx번째 cctv의 위치와 번호를 가져옴

    for direction in DIRECTION[cctv]:  # cctv의 번호에 따라 감시할 수 있는 방향을 가져옴
        tmp = deepcopy(office)  # deepcopy
        set_watched_area(tmp, direction, x, y)  # cctv가 감시할 수 있는 방향으로 감시 영역을 표시
        answer = min(answer, dfs(tmp, cctvs, idx + 1))  # 다음 cctv를 감시 방향을 정함

    return answer


print(dfs(office, cctvs, 0))
