from sys import stdin

t = int(stdin.readline())
for _ in range(t):
	N, L = map(int, stdin.readline().split())
	риша = list(map(int,input().split()))
	Дима = list(map(int,input().split()))
	риша.sort()
	Дима.sort()
	if sum(риша[:L]) <= sum(Дима[L*-1:]):
		print('NO')
	else:
		print('YES')
