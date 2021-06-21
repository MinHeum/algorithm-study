from sys import stdin

N = int(stdin.readline().rstrip())
arr = [[0] * 101 for _ in range(0, 101)]
data = []
for _ in range(N):
    data.append(list(map(int,stdin.readline().split())))
cnt = 1
for i in data:
    for w in range(i[0], i[0] + i[2]):
        for h in range(i[1], i[1] + i[3]):
            arr[w][h] = cnt
    
    cnt+=1
answer = [0] * N
question = 1
for q in range(0, N):
    for i in range(0,101):
        for j in range(0,101):
            if question == arr[i][j]:
                answer[q] += 1
    question += 1
    
for a in answer:
    print(a)
