class Solution:
    def rob(self, nums: List[int]) -> int:
        # because both house 0 and house n - 1 can't be both present in the answer
        # it is ok to check house 0 to n - 2 and house 1 to n - 1
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0] ,nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]