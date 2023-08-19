from sys import stdin

M, N, L = map(int, stdin.readline().split())

shooter = list(map(int, stdin.readline().split()))

# 이분탐색을 위한 정렬
shooter.sort()

animal = []

# 동물의 위치를 입력받음
for _ in range(N):
    animal.append(list(map(int, stdin.readline().split())))

# 사냥 가능한 동물의 수
answer = 0

# 동물의 위치를 기준으로 이분탐색
for x, y in animal:
    # 동물의 y 좌표가 사정거리가 넘어가면 사냥 불가능
    if y > L:
        continue

    # 각 동물별로 사정거리를 만족하는 사대의 x좌표를 찾음
    start = x + y - L
    end = x - y + L

    # 이분탐색
    left = 0
    right = M - 1

    while left <= right:
        mid = (left + right) // 2
        if shooter[mid] >= start and shooter[mid] <= end:
            answer += 1
            break
        elif shooter[mid] < start:
            left = mid + 1
        else:
            right = mid - 1

print(answer)
