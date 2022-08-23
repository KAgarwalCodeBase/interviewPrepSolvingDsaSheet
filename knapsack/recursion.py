class Solution:
    def find_max_value(self, W, wt, val):
        def find(W, n):
            if n==0:
                return 0
            x = val[n-1] + find(W-wt[n-1], n-1) if W>=wt[n-1] else 0
            y = find(W, n-1)
            return max(x,y)
        return find(W, len(val))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
ans = Solution().find_max_value(W, wt, val)
print(ans)
    