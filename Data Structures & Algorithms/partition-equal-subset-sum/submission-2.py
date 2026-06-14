class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # can be turned into combination sum -> TLE
        # but with memo it works 
        # the bottom-up version is actually 0/1 knapsack problem
        # no value / value is whether fit current W exactly
        # weight is num
        SUM = sum(nums)
        if SUM % 2:
            return False
        SUM //= 2
        n = len(nums)
        dp = [[False] * (SUM + 1) for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = True 
        
        for i in range(1, n + 1):
            for j in range(1, SUM+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][SUM]

        # SUM = sum(nums)
        # if SUM % 2:
        #     return False
        # SUM //= 2
        # n = len(nums)
        # memo = [[False] * (SUM + 1) for _ in range(n)]
        # def dfs(i, total):
        #     if total == SUM:
        #         return True
        #     if i >= len(nums) or total > SUM:
        #         return False
        #     if memo[i][total]:
        #         return True 
        #     memo[i][total] = dfs(i+1, total+nums[i]) or dfs(i+1, total)

        #     return memo[i][total]

        # return dfs(0, 0)

        