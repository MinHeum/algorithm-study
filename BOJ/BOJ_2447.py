from sys import stdin


N = int(stdin.readline().rstrip())

def star(n):
  if n == 1:
    return ['*']
  # (3 9 27 81 ...)
  else:
    prev = star(n // 3)
    result = []
    for row in prev:
      # 이전 row * 3
      result.append(row * 3)
    for row in prev:
      # 이전 row, 빈공간, 이전 row
      result.append(row + ' ' * (n // 3) + row)
    for row in prev:
      # 이전 row * 3
      result.append(row * 3)
    return result
  
for row in star(N):
  print(row)

