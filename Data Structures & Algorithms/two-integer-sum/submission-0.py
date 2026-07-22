class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for key, value in enumerate(nums):
            needed = target - value
            if needed in seen:
                return [seen[needed], key]
            else:
                seen[value] = key

nums = [1, 4, 7, 8]
target = 12

print(Solution().twoSum(nums, target))