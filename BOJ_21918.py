N, M = map(int, input().split())

lst = list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split())
    b = b - 1
    if a == 1:
        lst[b] = c
    else:
        if a == 2: # 켜져있는거 끄고 꺼져있는거 켜기
            for i in range(b,c):
                if lst[i] == 1:
                    lst[i] = 0
                else:
                    lst[i] = 1
        if a == 3: # 끄기
            for i in range(b,c):
                lst[i] = 0

        if a == 4: # 켜기
            for i in range(b,c):
                lst[i] = 1

print(*lst)
