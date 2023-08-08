from sys import stdin

n = int(stdin.readline())
lst = list(map(int,stdin.readline().split()))
target = int(stdin.readline())

lst = sorted(lst)

left = 0
right = n - 1

answer = 0

while left != right:
    s = lst[left] + lst[right]
    if s == target:
        answer += 1
        left += 1
    else:
        if s < target:
            left += 1
        else:
            right -= 1
print(answer)