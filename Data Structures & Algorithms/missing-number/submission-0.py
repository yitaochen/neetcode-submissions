class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = sum([i for i in range(len(nums)+1)])
        for num in nums:
            ans -= num
        return ans 