from sys import stdin

n = int(stdin.readline().rstrip())
arr = []

for _ in range(n):
    x, y = list(map(int,stdin.readline().split()))
    arr.append((x, y))

arr.sort()

def get_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solution(l, r):
    if l == r:
        return float('inf')
    
    m = (l + r) // 2
    min_dist = min(solution(l, m), solution(m+1, r))
    target = []

    for i in range(m, l - 1, -1):
        if (arr[i][0] - arr[m][0]) ** 2 < min_dist:
            target.append(arr[i])
        else:
            break
    
    for i in range(m+1, r+1, 1):
        if(arr[i][0] - arr[m][0]) ** 2 < min_dist:
            target.append(arr[i])
        else:
            break
    
    target.sort(key=lambda x: x[1]) # y를 기준으로 정렬

    for i in range(len(target) - 1):
        for j in range(i + 1, len(target)):
            if (target[i][1] - target[j][1]) ** 2 < min_dist:
                dist = get_dist(target[i], target[j])
                min_dist = min(min_dist, dist)
            else:
                break
    return min_dist

if len(arr) != len(set(arr)):
    print('0')
else:
    print(solution(0, len(arr)-1))