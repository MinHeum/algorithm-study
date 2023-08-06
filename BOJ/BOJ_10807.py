N = int(input())
arr = list(map(int, input().split()))
target = int(input())

count = 0
for i in arr:
    if i == target:
        count += 1
print(count)