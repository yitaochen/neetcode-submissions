class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix suffix product if division not allowed
        # can be further optimized to O(1) space O(n) time 
        prefix = 1
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            ans[i] = prefix 
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans 