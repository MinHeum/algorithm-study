from sys import stdin

left = list(stdin.readline().rstrip())
right = []

N = int(stdin.readline())

for _ in range(N):
    command, *char = stdin.readline().rstrip().split(' ')

    # L: 커서를 왼쪽으로 한 칸 옮김
    if command == 'L':
        if len(left) == 0:
            continue
        right.append(left.pop())

    # D: 커서를 오른쪽으로 한 칸 옮김
    if command == 'D':
        if len(right) == 0:
            continue
        left.append(right.pop())

    # B: 커서 왼쪽에 있는 문자를 삭제
    if command == 'B':
        if len(left) == 0:
            continue
        left.pop()

    # P $: $라는 문자를 커서 왼쪽에 추가함
    if command == 'P':
        left.append(char[0])

left.extend(reversed(right))
print(''.join(left))