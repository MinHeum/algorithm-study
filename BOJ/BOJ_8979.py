from sys import stdin

N, K = map(int, stdin.readline().split())

medals = []

for _ in range(N):
    medals.append(list(map(int, stdin.readline().split())))

# 금메달, 은메달, 동메달 순으로 정렬
medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# K번째 국가의 인덱스를 찾는다.
for i in range(N):
    if medals[i][0] == K:
        k = i
        break

for i in range(N):
    if medals[i][1:] == medals[k][1:]:
        print(i + 1)
        break
