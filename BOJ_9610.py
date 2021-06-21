from sys import stdin

n = int(stdin.readline().rstrip())
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0

for _ in range(n):
    x, y = map(int,stdin.readline().split())
    if x == 0 or y == 0:
        axis += 1
        continue
    
    if x > 0:
        if y > 0:
            q1 += 1
        else:
            q4 += 1
    else:
        if y > 0:
            q2 += 1
        else:
            q3 += 1
print("Q1: "+str(q1))
print("Q2: "+str(q2))
print("Q3: "+str(q3))
print("Q4: "+str(q4))
print("AXIS: "+str(axis))
