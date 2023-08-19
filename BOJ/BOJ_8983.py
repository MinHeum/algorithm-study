from sys import stdin

M, N, L = map(int, stdin.readline().split())

shooter = list(map(int, stdin.readline().split()))

animal = []

for _ in range(N):
    animal.append(list(map(int, stdin.readline().split())))

answer = 0

for animal_x, animal_y in animal:
    for shooter_x in shooter:
        if abs(animal_x - shooter_x) + animal_y <= L:
            answer += 1
            break

print(answer)
