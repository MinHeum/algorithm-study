lst = list(map(int, input().split(" ")))
lst.sort()
if lst[0] == lst[1]:
    if lst[1] == lst[2]:
        print(10000 + lst[2]*1000)
    else:
        print(1000 + lst[1]*100)
else:
    if lst[1] == lst[2]:
        print(1000 + lst[1]*100)
    else:
        print(lst[2]*100)