class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]

            if j < n:
                res[i] = j - i
        return res
        # # monotic stack 
        # stack = []
        # ans = [0] * len(temperatures)
        # for i, t in enumerate(temperatures):
        #     while stack and temperatures[stack[-1]] < t:
        #         ans[stack[-1]] = i - stack[-1] 
        #         stack.pop() 
        #     stack.append(i)
        
        # return ans 
