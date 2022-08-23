class Solution:
    def no_of_ways_to_get_coin_change(self, S, coins):
        #t.c -  O(m*S)
        #s.c -  O(m*S)
        m = len(coins)
        dp = [[0]*(S+1) for i in range(m)]
        for i in range(m):
            for j in range(S+1):
                x = dp[i][j-coins[i]] if j>=coins[i] else 0
                y = dp[i-1][j] if i>0 else 0  
                dp[i][j] = x+y if j>0 else 1
        return dp[-1][-1]

    def no_of_ways_to_get_coin_change_2(self, S, coins):
        #t.c -  O(m*S)
        #s.c -  O(S)
        table = [0]*(S+1)
        table[0] = 1
        for coin in coins:
            for j in range(coin, S+1):
                table[j] += table[j - coin]
        return table[-1]


S = int(input())
coins = list(map(int, input().split()))
# ans = Solution().no_of_ways_to_get_coin_change(S, coins)
ans = Solution().no_of_ways_to_get_coin_change_2(S, coins)
print('total number of unique ways to change the coin: ', ans)

