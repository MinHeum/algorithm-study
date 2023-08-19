from sys import stdin
from collections import deque
from itertools import permutations

# 첫 째 줄부터 25째 줄까지 각 줄에 5개의 정수가 주어진다.
# 0은 들어갈 수 없는 칸, 1은 들어갈 수 있는칸

plates = []
for _ in range(5):
    plate = []
    for _ in range(5):
        plate.append(list(map(int, stdin.readline().split())))
    plates.append(plate)

# 5개의 판을 쌓는 순서를 정한다.
# 5개의 판을 쌓는 순서는 5! = 120가지이다.
# 각 핀당 회전할 수 있는 경우의 수는 4가지이다.
# 따라서 총 경우의 수는 120 * 4^5 = 307,200가지이다.

# 회전시킨 판을 return하는 함수


def rotate_plate(plate, direction):
    if direction == 0:
        return plate
    elif direction == 1:
        new_plate = []
        for i in range(5):
            new_plate.append([])
            for j in range(5):
                new_plate[i].append(plate[4-j][i])
        return new_plate
    elif direction == 2:
        new_plate = []
        for i in range(5):
            new_plate.append([])
            for j in range(5):
                new_plate[i].append(plate[4-i][4-j])
        return new_plate
    elif direction == 3:
        new_plate = []
        for i in range(5):
            new_plate.append([])
            for j in range(5):
                new_plate[i].append(plate[j][4-i])
        return new_plate


# plates[0][0][0]또는 plates[4][4][4]가 0이면 False를 return하는 함수
def is_valid_plates(plates):
    if plates[0][0][0] == 0 or plates[4][4][4] == 0:
        return False
    else:
        return True

# plates[0][0][0]에서 plates[4][4][4]까지 가는 최소 이동 횟수를 BFS탐색


def bfs(plates):
    # 5개의 판을 쌓는 순서를 정한다.
    orders = list(permutations([0, 1, 2, 3, 4], 5))

    # 0,1,2,3,4 와 4,3,2,1,0 은 같은 판이므로 중복을 제거한다.
    orders = list(set(orders))

    is_all_invalid = True
    answer = 1e9

    # 5개의 판들을 각각 회전시킨다.
    # 첫 번째 판은 i 번 회전, 두 번째 판은 j 번 회전, ... 다섯 번째 판은 m 번 회전
    for order in orders:
        for rotate_i in range(4):
            for rotate_j in range(4):
                for rotate_k in range(4):
                    for rotate_l in range(4):
                        for rotate_m in range(4):
                            min_move = 1e9
                            is_valid = True
                            new_plates = []
                            new_plates.append(
                                rotate_plate(plates[order[0]], rotate_i))
                            new_plates.append(
                                rotate_plate(plates[order[1]], rotate_j))
                            new_plates.append(
                                rotate_plate(plates[order[2]], rotate_k))
                            new_plates.append(
                                rotate_plate(plates[order[3]], rotate_l))
                            new_plates.append(
                                rotate_plate(plates[order[4]], rotate_m))

                            # 회전시킨 판이 유효한 판인지 확인한다.
                            if is_valid_plates(new_plates) == False:
                                continue

                            # 회전시킨 판이 유효한 판이라면 BFS탐색을 통해 최소 이동 횟수를 구한다.
                            queue = deque()
                            # 3차원 5x5x5 visted 배열
                            visited = [
                                [[False for _ in range(5)] for _ in range(5)] for _ in range(5)]
                            # 시작점은 방문했다고 표시한다.
                            visited[0][0][0] = True
                            # 3차원 delta 배열
                            delta = [[0, 0, 1], [0, 0, -1], [0, 1, 0],
                                     [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
                            # (x, y, z, move) 형태로 queue에 넣는다.
                            queue.append((0, 0, 0, 0))
                            while queue:
                                cur = queue.popleft()

                                # 조기탈출
                                if cur[3] >= min_move:
                                    continue

                                # 현재 위치가 목적지라면 최소 이동 횟수를 비교하여 min_move 를 갱신
                                if cur[0] == 4 and cur[1] == 4 and cur[2] == 4:
                                    min_move = min(min_move, cur[3])
                                    break

                                # 현재 위치에서 갈 수 있는 위치를 탐색한다.
                                for i in range(6):
                                    dx = cur[0] + delta[i][0]
                                    dy = cur[1] + delta[i][1]
                                    dz = cur[2] + delta[i][2]

                                    # 갈 수 있는 위치가 유효한 위치인지 확인한다.
                                    if dx < 0 or dx >= 5 or dy < 0 or dy >= 5 or dz < 0 or dz >= 5:
                                        continue

                                    # 갈 수 있는 위치가 방문한 적이 있는 위치인지 확인한다.
                                    if visited[dx][dy][dz] == True:
                                        continue

                                    # 갈 수 있는 위치가 0인지 확인한다.
                                    if new_plates[dx][dy][dz] == 0:
                                        continue

                                    # 갈 수 있는 위치가 유효한 위치라면 방문했다고 표시하고 queue에 넣는다.
                                    visited[dx][dy][dz] = True
                                    queue.append((dx, dy, dz, cur[3] + 1))
                            if min_move == 12:
                                return 12

                            # 최소 이동 횟수를 비교하여 answer를 갱신한다.
                            if min_move < answer :
                                answer = min_move
                            
    if answer == 1e9:
        return -1
    else:
        return answer


print(bfs(plates))
