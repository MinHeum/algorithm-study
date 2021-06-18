from sys import stdin

N, M = map(int, stdin.readline().split())
pokedex = {}
pokelst = []


for i in range(N):
    s = stdin.readline().rstrip()
    pokedex[s] = i+1
    pokelst.append(s)

for _ in range(M):
    question = stdin.readline().rstrip()
    if question.isalpha():
        print(pokedex[question])
    else:
        print(pokelst[int(question)-1])
