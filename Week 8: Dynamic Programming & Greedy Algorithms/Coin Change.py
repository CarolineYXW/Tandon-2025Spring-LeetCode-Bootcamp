class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort()
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            dp[i] = min((dp[i - c] for c in coins if i >= c), default=float('inf'))+1
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]