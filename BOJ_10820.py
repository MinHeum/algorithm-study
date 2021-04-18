while True:
    try:
        s = input()
    except EOFError:
        break
    uppercase, lowercase, numbers, spaces = 0, 0, 0, 0
    for i in s:
        ch = ord(i)
        if ch >= 65 and ch <= 90:
            uppercase += 1
        elif ch >= 97 and ch <= 122:
            lowercase += 1
        elif ch >= 48 and ch <= 57:
            numbers += 1
        elif ch == 32:
            spaces += 1
    print("{} {} {} {}".format(lowercase,uppercase,numbers,spaces))

