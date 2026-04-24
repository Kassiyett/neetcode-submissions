class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float("inf")
        max_profit = float("-inf")
        
        for p in prices:
            min_p = min(p, min_p)
            profit = p - min_p
            max_profit = max(profit, max_profit)
        return max_profit