class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # bottom up solution
        dp = [amount + 1] * (amount + 1)
        # to get 0 coins the amount of coins we need is 0
        dp[0] = 0

        # for each amount in the array
        for a in range(1, amount + 1):
            # check each coin
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1