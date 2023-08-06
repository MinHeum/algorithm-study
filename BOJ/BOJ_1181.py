from sys import stdin

N = int(stdin.readline().rstrip())

lst = []

for _ in range(N):
    lst.append(stdin.readline().rstrip())

s = set(lst)
lst = list(s)

lst.sort(key=lambda x : (len(x), x))

for i in lst:
    print(i)
