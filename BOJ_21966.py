from sys import stdin

N = int(stdin.readline())
S = stdin.readline().strip()

if len(S) <= 25:
    print(S)
else:
    if len(S[12:-12].split('.')) <= 1 :
        print(S[:11]+"..."+S[-11:])
    else:
        print(S[:9]+"......"+S[-10:])
