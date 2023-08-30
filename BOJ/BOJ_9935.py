from sys import stdin

word = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()

stack = []

for ch in word:
    stack.append(ch)
    if len(stack) >= len(bomb):
        # stack에서 bomb의 길이만큼 뽑아서 bomb과 같은지 확인
        if ''.join(stack[-len(bomb):]) == bomb:
            # 같으면 bomb 길이만큼 pop
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    # stack에 남아있는 문자들을 출력
    print(''.join(stack))
else:
    # stack이 비어있으면 FRULA 출력
    print('FRULA')