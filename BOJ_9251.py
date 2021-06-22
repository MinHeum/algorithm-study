from sys import stdin

A = stdin.readline().rstrip()
B = stdin.readline().rstrip()

LCS = [[0] * (len(B)+1) for i in range(len(A)+1)]
answer = 0
for i in range(len(A)+1):
    for j in range(len(B)+1):
        if i == 0 or j == 0:
            LCS[i][j] = 0 # to avoid index out of range Error
        elif A[i-1] == B[j-1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
            if answer < LCS[i][j]:
                answer = LCS[i][j]
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(answer)
