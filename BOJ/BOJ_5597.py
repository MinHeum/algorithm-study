arr = [0] * 30
for i in range(0,28):
    arr[int(input())-1] = 1

for i in range(0,30):
    if arr[i] == 0:
        print(i+1)
