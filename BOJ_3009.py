from sys import stdin

arr = []
for _ in range(3):
    arr.append(list(map(int,stdin.readline().split())))

answerX = set([])
answerY = set([])

for i in arr:
    if i[0] in answerX:
        answerX.remove(i[0])
    else:
        answerX.add(i[0])
    if i[1] in answerY:
        answerY.remove(i[1])
    else:
        answerY.add(i[1])

print('{} {}'.format(answerX.pop(), answerY.pop()))
