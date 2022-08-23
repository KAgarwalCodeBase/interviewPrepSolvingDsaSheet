class Solution:
    def find_max_value(self, W, wt, val):
        n = len(wt)
        dp = [[0]*(W+1) for i in range(n+1)]
        for i in range(n+1):
            for j in range(W+1):
                if i==0 or j==0:
                    pass
                dp[i][j] = max(dp[i-1][j], val[i-1]+dp[i-1][j-wt[i-1]] if j>=wt[i-1] else 0)
        return dp[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
ans = Solution().find_max_value(W, wt, val)
print(ans)
    