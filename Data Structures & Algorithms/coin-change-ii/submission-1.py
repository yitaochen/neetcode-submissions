class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp on amount
        # how to guarantee distinct
        # dp(i, a) means the number of ways total up to a starting from i-th coin onward
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for a in range(c, amount+1):
                dp[a] += dp[a-c]
        
        return dp[-1]
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