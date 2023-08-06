from sys import stdin

score = stdin.readline().rstrip()

if score == 'F':
    print(0.0)
else:
    arr = [4.0,3.0,2.0,1.0]
    answer = arr[ord(score[0])-65]
    if score[1] == '-':
        answer -= 0.3
    elif score[1] == '+':
        answer += 0.3
    print(answer)