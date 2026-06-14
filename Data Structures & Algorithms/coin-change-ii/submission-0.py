class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp on amount
        # how to guarantee distinct
        # dp(i, a) means the number of ways total up to a starting from i-th coin onward
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1 

        for i in range(n - 1, -1, -1):
            for a in range(1, amount + 1):
                if coins[i] <= a:
                    dp[i][a] = dp[i+1][a]
                    dp[i][a] += dp[i][a-coins[i]]
        
        return dp[0][amount]