import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1], x[0]))  # 종료시각 기준으로 정렬, 종료시각이 같으면 시작시각 기준으로 정렬
end_time = 0
cnt = 0

for i in arr:
    # end_time을 갱신하면서 진행할 수 있는 회의를 센다. (종료시각 기준으로 정렬했음)
    if end_time <= i[0]:  # 종료시각이 시작시각보다 작거나 같으면 진행할 수 있음
        cnt += 1
        end_time = i[1]

print(cnt)
