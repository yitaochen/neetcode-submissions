class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP works better
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[-1]

        # # Naive DFS TLE
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0 
        #     return max(dfs(i+1), dfs(i+2) + nums[i])
        
        # return dfs(0)