from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())
sensors = sorted(map(int, stdin.readline().split()))

if K >= N: # K >= N이면 센서를 다 끊어도 되므로 0 출력
    print(0)
else:
    distances = []
    for i in range(1, N): # 센서 사이의 거리를 구해서 리스트에 저장
        distances.append(sensors[i] - sensors[i-1])
    distances.sort() # 거리를 오름차순으로 정렬

    for _ in range(K-1): # 가장 긴 거리를 K-1번 끊음
        distances.pop()

    print(sum(distances)) # 남은 거리의 합 출력
