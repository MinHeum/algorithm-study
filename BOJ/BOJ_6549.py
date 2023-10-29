from sys import stdin
from collections import deque

while True:
    inputs = list(map(int, stdin.readline().split()))

    if inputs[0] == 0:  # 0을 입력받으면 종료
        break

    N = inputs[0]  # 입력받을 수의 개수
    heights = inputs[1:]  # 높이

    stack = deque()
    answer = 0

    for i in range(N):
        # 스택이 비어있지 않고, 스택의 마지막 인덱스의 값이 현재 인덱스의 값보다 크면
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]  # 스택의 마지막 인덱스의 값을 높이로 설정
            width = i  # 현재 인덱스가 너비

            if stack:
                width = i - stack[-1] - 1  # 스택이 비어있지 않으면, 현재 인덱스에서 스택의 마지막 인덱스를 뺀 값이 너비

            answer = max(answer, width * height)  # 최대값 갱신

        stack.append(i)

    while stack:  # 스택이 빌 때까지
        height = heights[stack.pop()]  # 스택의 마지막 인덱스의 값을 높이로 설정
        width = N  # 너비

        if stack:  # 스택이 비어있지 않으면
            width = N - stack[-1] - 1  # 스택의 마지막 인덱스를 뺀 값이 너비

        answer = max(answer, width * height)  # 최대값 갱신

    print(answer)
