class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # same backtracking as generating subsets 
        # but we can do some save by sorting and pruning

        ans = []
        cur = []
        candidates.sort()
        
        def dfs(i, total): 
            if total == target:
                ans.append(cur[:])
                return 
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i + 1, total)
        
        dfs(0, 0)

        return ans 