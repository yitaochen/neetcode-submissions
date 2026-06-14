class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        cur = []

        def dfs(i, seen):
            if i == len(nums):
                ans.append(cur[:])
                return
            
            for j in range(len(nums)):
                if not seen[j]:
                    cur.append(nums[j])
                    seen[j] = 1
                    dfs(i + 1, seen)
                    cur.pop()
                    seen[j] = 0
        
        dfs(0, [0] * len(nums))

        return ans 