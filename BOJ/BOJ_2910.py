from sys import stdin

N, C = map(int, stdin.readline().split())

nums = list(map(int, stdin.readline().split()))

dic = {}

for num in nums:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for num in range(len(dic)): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    for i in range(dic[num][1]): # dictionary의 value 만큼
        print(dic[num][0], end=' ') # dictoionary의 key 출력