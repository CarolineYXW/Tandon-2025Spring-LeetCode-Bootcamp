class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        aim = sum(nums)
        if aim % 2 != 0:
            return False
        else:
            aim = aim // 2
        dp = [[False]*(aim+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(n):
            for j in range(aim+1):
                dp[i+1][j] = dp[i][j] or (j >= nums[i-1] and dp[i][j-nums[i-1]])
        return dp[n][aim]