import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort(key = lambda x: (x[1], x[0]))
end_time = 0
cnt = 0
for i in arr:
    if end_time <= i[0]:
        cnt += 1
        end_time = i[1]

print(cnt)
