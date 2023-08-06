N = int(input())

q = 2

if N != 1:
    while N > 1:
        while N % q == 0:
            print(q)
            N = int(N/q)
        q += 1
