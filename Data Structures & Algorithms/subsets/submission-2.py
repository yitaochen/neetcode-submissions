class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking 
        # there is a universal dfs solution 
        # the recursive part depends on when I need to make a decision 
        ans = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                ans.append(subset[:])
                return 
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)

        return ans 