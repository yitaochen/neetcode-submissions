class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mn = 0
        S = 0
        ans = float("-inf")
        for num in nums:
            S += num
            ans = max(ans, S - mn)
            mn = min(mn, S)

        
        return ans