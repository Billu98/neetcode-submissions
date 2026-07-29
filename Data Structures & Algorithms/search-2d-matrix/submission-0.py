class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        for row in matrix:

            if target >= row[0] and target <= row[-1]:

                left = 0
                right = len(row) - 1

                while left <= right:

                    mid = (left + right) // 2

                    if row[mid] == target:
                        return True

                    elif row[mid] < target:
                        left = mid + 1

                    else:
                        right = mid - 1

        return False

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
print(Solution().searchMatrix(matrix, target))