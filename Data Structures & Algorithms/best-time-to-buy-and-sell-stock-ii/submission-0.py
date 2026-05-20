class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        temp_profit = 0
        for r in range(len(prices)):
            temp = prices[r] - prices[l]
            if temp < 0 or temp < temp_profit:
                l = r
                profit += temp_profit
                temp_profit = 0
            else:
                temp_profit = temp
        
        profit += temp_profit
        return profit