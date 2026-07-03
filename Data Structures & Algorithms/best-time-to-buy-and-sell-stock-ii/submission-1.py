class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        sell = 0
        for r in range(len(prices)):
            temp = prices[r] - prices[l]
            if temp <= 0:
                l = r
            else:
                sell += temp
                l = r 
            max_profit = max(max_profit , sell)
        
        return max_profit
                