from sys import stdin

target = int(stdin.readline())
N = int(stdin.readline())
broken_buttons = list(stdin.readline().split())

cur = 100  # 현재 보고있는 채널은 100번
answer = abs(target - cur)  # 현재 보고있는 채널에서 +, -로만 이동하는 경우


for i in range(1000000):
    for j in range(len(str(i))):
        if str(i)[j] in broken_buttons:  # 고장난 버튼이면
            break
        elif j == len(str(i)) - 1:  # 고장난 버튼이 아님
            answer = min(answer, abs(target - i) + len(str(i)))

print(answer)
