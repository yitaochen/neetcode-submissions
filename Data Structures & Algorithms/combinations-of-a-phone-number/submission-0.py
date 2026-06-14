class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mp = {'2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y', 'z'],
        }
        ans = []
        cur = []
        def dfs(i):
            if i == len(digits):
                ans.append("".join(cur[:]))
                return
            for cand in mp[digits[i]]:
                cur.append(cand)
                dfs(i+1)
                cur.pop()
        
        dfs(0)

        return ans 