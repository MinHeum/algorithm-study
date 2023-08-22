from sys import stdin

# N: 접시의 수, d: 초밥의 가짓수, k: 연속해서 먹는 접시의 수, c: 쿠폰 번호
N, d, k, c = map(int, stdin.readline().split())

# 초밥의 종류
sushi = [int(stdin.readline()) for _ in range(N)]

start = 0
end = k-1

kind = set()

while start < N:
    if end >= N:
        end -= N

    if end < start:
        temp = sushi[start:] + sushi[:end+1]
    else:
        temp = sushi[start:end+1]

    cases = set(temp)
  
    if c not in cases:
        cases.add(c)
    if len(kind) < len(cases):
        kind = cases
    
    start += 1
    end += 1

print(len(kind))