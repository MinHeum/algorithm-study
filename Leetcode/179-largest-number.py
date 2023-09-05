class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 1. 길이가 짧은 순서대로 정렬
        # 2. 사전 순서 역순으로 정렬
        # 3. 정렬된 숫자를 이어붙여서 리턴
        def compare(a, b):
            return int(b+a) - int(a+b)
        
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        return str(int(''.join(nums)))