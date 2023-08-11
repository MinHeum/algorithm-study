class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lst = [0, 0, 0]
        for i in nums:
            lst[i] += 1
        for idx in range(len(nums)):
            if lst[0] != 0:
                nums[idx] = 0
                lst[0] -= 1
            elif lst[1] != 0:
                nums[idx] = 1
                lst[1] -= 1
            else:
                nums[idx] = 2
                lst[2] -= 1
