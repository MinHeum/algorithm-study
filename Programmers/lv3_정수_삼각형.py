TRI = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	

def solution(triangle):
    answer = 0
    dp = [[0] * len(i) for i in triangle]
    dp[0][0] = triangle[0][0]
    
    for height in range(1, len(triangle)):
        for idx, el in enumerate(dp[height]):
            if idx == 0:
                dp[height][idx] = dp[height-1][0] + triangle[height][0]
            elif idx == len(dp[height])-1:
                dp[height][idx] = dp[height-1][-1] + triangle[height][-1]
            else:
                dp[height][idx] = max(dp[height-1][idx-1], dp[height-1][idx]) + triangle[height][idx]
    answer = max(dp[len(dp)-1])
    return answer

print(solution(TRI))