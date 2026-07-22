class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicates = []
        for value in nums:
            if value in seen:
                duplicates.append(value)
            else:
                seen.add(value)
        if duplicates:
            return True
        else:
            return False

nums = [1, 2, 3, 4]
result = Solution().hasDuplicate(nums)
print(result)