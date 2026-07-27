class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maximum = 0

        while left < right:

            width = right - left

            currentHeight = min(heights[left], heights[right])

            area = width * currentHeight

            maximum = max(maximum, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maximum

height = [1,7,2,5,4,7,3,6]
print(Solution().maxArea(height))