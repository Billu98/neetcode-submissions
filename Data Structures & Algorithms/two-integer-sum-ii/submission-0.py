class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            
            current = numbers[left] + numbers[right]
            
            if current == target:
                return [left + 1, right + 1]
            
            elif current < target:
                left += 1
                
            else:
                right -= 1

numbers = [1,2,3,4]
target = 3
print(Solution().twoSum(numbers, target))