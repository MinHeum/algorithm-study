import sys

def gcd (m, n):
    if(n == 0):
        return m
    else:
        return gcd(n, m % n)
t = int(sys.stdin.readline())

for _ in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    answer = 0
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            answer += gcd(arr[i], arr[j])
    print(answer)