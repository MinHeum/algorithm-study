from sys import stdin

arr = [[0] * 101 for _ in range(0, 101)]
squares = []
for _ in range(4):
    squares.append(list(map(int,stdin.readline().split())))

for i in squares:
    for x in range(i[0], i[2]):
        for y in range(i[1], i[3]):
            arr[x][y] = 1

answer = 0

for i in range(1, 101):
    for j in range(1, 101):
        answer += arr[i][j]

print(answer)
