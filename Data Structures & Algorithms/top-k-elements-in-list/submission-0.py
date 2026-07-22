class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        # Step 1: Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Sort by frequency (largest first)
        sortedItems = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Step 3: Collect first k numbers
        result = []

        for i in range(k):
            result.append(sortedItems[i][0])

        return result