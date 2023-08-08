import sys
lst = []
for _ in range(5):
    lst.append(int(sys.stdin.readline().rstrip()))

summary = sum(lst)
avg = summary / 5
median = sorted(lst)[2]

print("%0.0f" %avg)
print(median)