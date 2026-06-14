class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # sol 2 iteration 
        ans = [[]]

        for num in nums:
            ans += [subset + [num] for subset in ans]

        return ans 
        # # sol 1 backtracking 
        # ans = []
        # subset = []

        # def dfs(i):
        #     if i >= len(nums):
        #         ans.append(subset[:])
        #         return 
        #     subset.append(nums[i])
        #     dfs(i+1)
        #     subset.pop()
        #     dfs(i+1)
        
        # dfs(0)

        # return ans 