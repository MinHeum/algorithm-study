from sys import stdin

# N * M의 배열
N, M, R = map(int, stdin.readline().split())

# 배열 입력
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

modified_arr = []

# 배열을 겉에서부터 안으로 나누기
for i in range(min(N, M) // 2):
    temp = []
    for j in range(i, M - i - 1):
        temp.append(arr[i][j])
    for j in range(i, N - i - 1):
        temp.append(arr[j][M - i - 1])
    for j in range(M - i - 1, i, -1):
        temp.append(arr[N - i - 1][j])
    for j in range(N - i - 1, i, -1):
        temp.append(arr[j][i])
    modified_arr.append(temp)


# r만큼 회전시키는 함수
def rotate(sub_arr, r):
    r %= len(sub_arr)
    return sub_arr[r:] + sub_arr[:r]


# 회전시키고 다시 배열에 넣기
for i in range(min(N, M) // 2):
    modified_arr[i] = rotate(modified_arr[i], R)

# 배열에 다시 넣기
for i in range(min(N, M) // 2):
    idx = 0
    for j in range(i, M - i - 1):
        arr[i][j] = modified_arr[i][idx]
        idx += 1
    for j in range(i, N - i - 1):
        arr[j][M - i - 1] = modified_arr[i][idx]
        idx += 1
    for j in range(M - i - 1, i, -1):
        arr[N - i - 1][j] = modified_arr[i][idx]
        idx += 1
    for j in range(N - i - 1, i, -1):
        arr[j][i] = modified_arr[i][idx]
        idx += 1  

# 배열 출력
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()
