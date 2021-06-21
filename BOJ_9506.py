from sys import stdin

def fun(N):
    answer = []
    for i in range(1,N+1):
        if N % i == 0:
            answer.append(i)
    answer.sort()
    return answer[:-1]

while True:
    N = int(stdin.readline().rstrip())
    if N == -1:
        break
    s = fun(N)
    if N == sum(s):
        answer = ''
        answer += str(N)
        answer += ' = '
        for i in s:
            answer += str(i)
            answer += ' + '
        print(answer[:-3])
    else:
        print('{} is NOT perfect.'.format(N))
