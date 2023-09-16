A, B, C = map(int, input().split())

toll = [0] * 101
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        toll[i] += 1

ans = 0

for i in range(1, 101):
    if toll[i] == 1:
        ans += A
    elif toll[i] == 2:
        ans += B * 2
    elif toll[i] == 3:
        ans += C * 3

print(ans)
