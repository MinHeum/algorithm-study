import sys

T = int(sys.stdin.readline())
for _ in range(T):
    s = list(sys.stdin.readline().split())
    for i in s:
        news = ""
        for x in range(len(i)-1, -1, -1):
            news += i[x]
        print(news, end=" ")
    print()
