from sys import stdin

K, N = map(int, stdin.readline().split())

lines = []
for _ in range(K):
    lines.append(int(stdin.readline()))

start = 1
end = max(lines)

# 이분 탐색
while start <= end:
    mid = (start + end) // 2

    count = 0
    for line in lines:
        count += line // mid

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)