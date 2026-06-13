class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prefix min 
        MIN = prices[0]
        n = len(prices)
        ans = 0
        for i in range(1, n):
            ans = max(ans, prices[i] - MIN)
            MIN = min(MIN, prices[i])
        
        return ans 
