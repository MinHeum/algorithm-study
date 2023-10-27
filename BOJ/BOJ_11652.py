import sys

N = int(sys.stdin.readline())
dic = {}

for i in range(N):
    num = int(sys.stdin.readline())
    if num in dic.keys():
        dic[num] += 1
    else:
        dic[num] = 1

res = sorted(dic.items(), key=lambda x: (-x[1], x[0]))  # 내림차순 정렬

print(res[0][0])
