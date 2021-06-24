from sys import stdin

A, B = map(int,stdin.readline().split())
C, D = map(int,stdin.readline().split())

results = []

for i in range(0,4):
    results.append([i, A/C + B/D])
    A, B, C, D = C, A, D ,B

results.sort(key=lambda x: x[1])

print(results[-1][0])
