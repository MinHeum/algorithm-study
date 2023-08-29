class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0

        left = 0
        right = len(height)-1

        while left < right:
            # answer 갱신
            temp_width = right - left 
            temp_height = min(height[left], height[right])
            temp_area = temp_width * temp_height
            answer = max(answer, temp_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer