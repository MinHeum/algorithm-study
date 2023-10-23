from sys import stdin

N, K = map(int, stdin.readline().split())

coins = []

for _ in range(N):
    coins.append(int(stdin.readline()))

answer = 0

for coin in coins[::-1]:
    if K == 0:
        break
    answer += K // coin  # K를 coin으로 나눈 몫을 answer에 더함
    K %= coin  # K를 coin으로 나눈 나머지로 갱신

print(answer)
