class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # isn't this the same as combi sum ii?
        ans = []
        cur = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                ans.append(cur[:])
                return 
            
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()

            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i + 1)
        
        dfs(0)

        return ans 