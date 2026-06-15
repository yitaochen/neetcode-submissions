class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp on amount
        # how to guarantee distinct
        # dp(i, a) means the number of ways total up to a starting from i-th coin onward
        # it is a multi-set problem
        # k0 copies of coin 0, k1 copies of coin 1, ... give a unique combination 
        # dp = [0] * (amount + 1)
        # dp[0] = 1
        # for c in coins:
        #     for a in range(c, amount+1):
        #         dp[a] += dp[a-c]
        
        # return dp[-1]

        # write the top-down dp (recursion + memo) solution having the multi-set view
        coins.sort()
        n = len(coins)
        memo = [[-1] * (amount + 1) for _ in range(n + 1)]

        def dfs(i, a):
            if a == 0:
                return 1
            if i >= n:
                return 0 
            if memo[i][a] != -1:
                return memo[i][a]
            
            tmp = 0
            if a >= coins[i]:
                tmp = dfs(i+1, a)
                tmp += dfs(i, a - coins[i])

            memo[i][a] = tmp

            return memo[i][a]

        return dfs(0, amount)

        # bottom-up dp solution 
        # n = len(coins)
        # coins.sort()
        # dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # for i in range(n + 1):
        #     dp[i][0] = 1 

        # for i in range(n - 1, -1, -1):
        #     for a in range(1, amount + 1):
        #         if coins[i] <= a:
        #             dp[i][a] = dp[i+1][a]
        #             dp[i][a] += dp[i][a-coins[i]]
        
        # return dp[0][amount]