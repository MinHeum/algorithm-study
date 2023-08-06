T = int(input())
for _ in range(T):
    y, k = 0, 0
    for __ in range(9):
        n = input().split(" ")
        y += int(n[0])
        k += int(n[1])
    if y > k:
        print("Yonsei")
    elif y < k:
        print("Korea")
    else:
        print("Draw")
