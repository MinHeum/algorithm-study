from sys import stdin

n = int(stdin.readline().rstrip())

# d: 마감일, p: 페이
arr = []

for _ in range(n):
    p, d = map(int, stdin.readline().rstrip().split())
    arr.append((d, p))

arr.sort(key=lambda x: -x[1])

maxDate = 10_000

plan = [0] * (maxDate + 1)

for d, p in arr:
    for i in range(d, 0, -1):
        if plan[i] == 0:
            plan[i] = p
            break
        
print(sum(plan))