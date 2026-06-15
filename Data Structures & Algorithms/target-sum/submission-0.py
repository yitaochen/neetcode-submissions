class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # top-down dp
        self.ans = 0
        def dfs(i, total):

            if i == len(nums):
                if total == target:
                    self.ans += 1
                return 
            
            dfs(i+1, total-nums[i])
            dfs(i+1, total+nums[i])
        
        dfs(0, 0)

        return self.ans

