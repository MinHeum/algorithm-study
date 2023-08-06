
while True:
    try:
        n = int(input())
        num = 1
        addition = 10
        while num % n != 0:
            num += addition
            addition *= 10
        print(len(str(num)))

    except EOFError:
        break
