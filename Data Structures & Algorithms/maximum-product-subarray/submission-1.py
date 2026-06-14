class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane style 
        # put num itself in min max computation for restart
        MIN, MAX = 1, 1
        # MIN, MAX are running products
        # ans is the global max, just naming thing
        ans = float("-inf")
        for num in nums:
            tmp = MAX * num 
            MAX = max(num, tmp, MIN*num)
            MIN = min(num, tmp, MIN*num)
            ans = max(ans, MAX)
        
        return ans 
