import sys

# f(A)는 A의 모든 약수의 합.
# g(A) = Sum( f(1) ... f(A) )

N = int(sys.stdin.readline())

def fun(N):
    res = 0
    for i in range(1,N+1):
        res += int(N/i)*i
    return res

print(fun(N))

