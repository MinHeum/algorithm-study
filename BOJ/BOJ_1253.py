from sys import stdin

N = int(stdin.readline().rstrip())

# 수를 입력받아 arr에 저장
arr = list(map(int, stdin.readline().rstrip().split()))

# 수를 오름차순으로 정렬
arr.sort()

# 정답을 저장할 변수
answer = 0

for idx, num in enumerate(arr):
    # 투포인터 사용 ^_^
    start = 0
    end = N - 1

    while start < end:
        temp = arr[start] + arr[end]

        # temp가 num과 같다면
        if temp == num:
            if start == idx:
                start += 1
            elif end == idx:
                end -= 1
            else:
                answer += 1
                break
            
        # temp가 num보다 크다면
        elif temp > num:
            end -= 1

        # temp가 num보다 작다면
        else:
            start += 1

print(answer)
