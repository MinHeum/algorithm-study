import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hq = []
        heapq.heapify(hq)
        
        for i in range(min(len(nums1), k)):
            # 힙에 (nums1[i]+nums2[0], nums1[i], nums2[0], 0)을 넣는다.
            heapq.heappush(hq, (nums1[i]+nums2[0], nums1[i], nums2[0], 0))

        answer = []
        while k > 0 and hq:
            # 힙에서 가장 작은 원소를 뽑는다. 
            _, n1, n2, idx = heapq.heappop(hq)
            answer.append((n1, n2))

            # nums2의 다음 원소를 힙에 넣는다.
            if idx + 1 < len(nums2):
                # n1은 고정시키고 nums2의 다음 원소를 힙에 넣는다.
                # n1 + nums2[idx+1]은 다음 원소를 힙에 넣었을 때의 합
                # idx+1은 nums2의 다음 원소의 인덱스
                heapq.heappush(hq, (n1+nums2[idx+1], n1, nums2[idx+1], idx+1))
            k -= 1
                
        return answer