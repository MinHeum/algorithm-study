import sys

T = int(sys.stdin.readline())

for _ in range(T):
    input = sys.stdin.readline()
    output = []
    i = int(input.split()[0])
    s = input.split()[1]
    output.append(s[:i-1])
    output.append(s[i:])
    print(''.join(output))
