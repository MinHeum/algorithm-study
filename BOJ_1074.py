import sys

N, r, c = map(int, sys.stdin.readline().split())

def z_fun(N,r,c):
    sq = 2**N
    sq_half = int(sq/2)
    quarter = sq_half * sq_half

    # print("N:",N,"r:",r,"c:",c,"Quartar:",quarter,"sq_half:",sq_half)

    if N == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        else:
            return 3

    if r < sq_half and c < sq_half:    # 1
        return z_fun(N-1, r, c)
    elif r < sq_half and c >= sq_half: # 2
        return ((quarter) + z_fun(N-1, r, c % sq_half))
    elif r >= sq_half and c < sq_half: # 3
        return ((2 * quarter) + z_fun(N-1, r % sq_half, c))
    else:                              # 4
        return ((3 * quarter) + z_fun(N-1, r % sq_half, c % sq_half))

print(z_fun(N,r,c)) 