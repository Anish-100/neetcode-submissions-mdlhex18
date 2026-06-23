class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit,l, profit = 0,0,0
        for r in range(1,len(prices)):
            while l < r and prices[l] >= prices[r]:
                l+=1
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit) 
        return max_profit

        