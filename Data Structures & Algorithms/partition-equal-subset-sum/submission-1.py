class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # can be turned into combination sum -> TLE
        # but with memo it works (basically lru cache)
        SUM = sum(nums)
        if SUM % 2:
            return False
        SUM //= 2
        n = len(nums)
        memo = [[False] * (SUM + 1) for _ in range(n)]
        def dfs(i, total):
            if total == SUM:
                return True
            if i >= len(nums) or total > SUM:
                return False
            if memo[i][total]:
                return True 
            memo[i][total] = dfs(i+1, total+nums[i]) or dfs(i+1, total)

            return memo[i][total]

        return dfs(0, 0)

        