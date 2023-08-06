while True:
    lst = input().split(" ")
    if lst[0] == "0" and lst[1] == "0":
        break
    else:
        print(int(lst[0])+int(lst[1]))
