def solution(jobs):
    answer = 0
    time = 0  # 현재 시간
    JOBS_LEN = len(jobs)
    jobs.sort(key=lambda x: x[1])  # 작업 소요시간 기준으로 정렬
    while jobs:  # 모든 jobs가 처리될 때까지 반복
        for i in range(len(jobs)):
            if jobs[i][0] <= time:  # 지금 시작 가능한 작업이면
                time += jobs[i][1]  # 작업 소요시간만큼 시간 증가
                answer += time - jobs[i][0]  # 요청부터 종료까지 걸린 시간
                jobs.pop(i)  # 해당 작업을 jobs에서 제거
                break
            if i == len(jobs) - 1:  # 시작 가능한 작업이 없을 때
                time += 1
    return answer // JOBS_LEN
