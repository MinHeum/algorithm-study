import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    command, *val = sys.stdin.readline().rstrip().split()
    if command == 'push':
        stack.append(val[0])
    if command == 'pop':
        print(stack.pop() if stack else -1)
    if command == 'size':
        print(len(stack))
    if command == 'empty':
        print( 1 if len(stack) == 0 else 0)
    if command == 'top':
        print( stack[-1] if stack else -1)