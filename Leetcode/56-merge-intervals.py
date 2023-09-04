class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # start 기준으로 정렬
        answer = []
        for interval in intervals:
            # answer가 비어있거나, answer의 마지막 interval의 end가 현재 interval의 start보다 작으면
            if not answer or answer[-1][1] < interval[0]:
                answer.append(interval)
                
            # answer의 마지막 interval의 end를 현재 interval의 end와 비교하여 더 큰 값으로 갱신
            else:
                answer[-1][1] = max(answer[-1][1], interval[1])
        return answer