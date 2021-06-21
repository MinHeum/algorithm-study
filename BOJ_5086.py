from sys import stdin

while True:
    x, y = map(int,stdin.readline().split())
    
    if x == 0 and y == 0:
        break

    if y % x == 0:
        print('factor')
        continue

    if x % y == 0:
        print('multiple')
        continue

    print('neither')
