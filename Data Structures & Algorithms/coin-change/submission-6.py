class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i):
            if i == 0:
                return 0
            if i in cache:
                return cache[i]
            min_coins = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    min_coins = min(1+dfs(i-coin), min_coins)
            cache[i] = min_coins
            return cache[i]
        res = dfs(amount)
        if res == float('inf'):
            return -1
        return res
