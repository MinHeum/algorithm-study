from sys import stdin
from itertools import combinations


while True:
  line = stdin.readline().rstrip()
  if line == '0':
    break

  k, *S = map(int, line.split())
  for comb in combinations(S, 6):
    print(' '.join(map(str, comb)))

  print() # 빈줄
