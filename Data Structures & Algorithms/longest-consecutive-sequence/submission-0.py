class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numbers = set(nums)

        longest = 0

        for num in numbers:

            if num - 1 not in numbers:

                length = 1

                while num + length in numbers:
                    length += 1

                longest = max(longest, length)

        return longest
            
nums = [2,20,4,10,3,4,5]
print(Solution().longestConsecutive(nums))