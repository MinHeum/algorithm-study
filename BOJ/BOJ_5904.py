N = int(input())


def moo(length, mid, N):
    if N <= 3:
        return "moo"[N-1]

    left = (length - mid) // 2

    if N <= left:  # N이 왼쪽에 있으면
        return moo(left, mid - 1, N)

    if N > left + mid:  # N이 오른쪽에 있으면
        return moo(left, mid - 1, N - left - mid)

    # N이 중간에 있으면
    if N - left == 1:
        return "m"
    else:
        return "o"


length = 3  # m o o 니까 3부터 시작
n = 0
while length < N:
    n += 1
    # S(k)는 S(k-1)과 o가 k+2개인 수열 "m o ... o" 와 S(k-1)
    length = 2 * length + n + 3

print(moo(length, n+3, N))
