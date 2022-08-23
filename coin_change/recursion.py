class Solution:
    def no_of_ways_to_get_coin_change(self, S, coins, ind):
        if S==0:
            return 1
        if S<0:
            return 0
        if ind>=len(coins):
            return 0
        mul = 0
        ans = 0 
        while coins[ind]*mul <= S:
            ans += self.no_of_ways_to_get_coin_change(S-coins[ind]*mul, coins, ind+1)
            mul +=1
        return ans


S = int(input())
coins = list(map(int, input().split()))
ans = Solution().no_of_ways_to_get_coin_change(S, coins, 0)
print('total number of unique ways to change the coin: ', ans)

