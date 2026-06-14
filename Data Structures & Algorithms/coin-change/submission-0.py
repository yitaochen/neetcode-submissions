class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp on amount
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(amount+1):
            tmp = float("inf")
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] >= 0:
                    tmp = min(tmp, dp[i - coin] + 1)
            if tmp < float("inf"):
                dp[i] = tmp 

        return dp[-1] 