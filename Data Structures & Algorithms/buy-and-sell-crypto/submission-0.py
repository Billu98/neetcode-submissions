class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0          
        right = 1         

        maximumProfit = 0

        while right < len(prices):

            if prices[right] > prices[left]:

                profit = prices[right] - prices[left]

                maximumProfit = max(maximumProfit, profit)

            else:

                left = right

            right += 1

        return maximumProfit

prices = [10,1,5,6,7,1]
print(Solution().maxProfit(prices))