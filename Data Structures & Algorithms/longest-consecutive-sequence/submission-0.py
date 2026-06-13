class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash set
        # identify seq start by checking num - 1 in the set
        numSet = set(nums)
        ans = 0

        for num in numSet:
            if (num - 1) not in numSet:
                l = 1
                while num + l in numSet:
                    l += 1
                ans = max(ans, l)
        
        return ans 