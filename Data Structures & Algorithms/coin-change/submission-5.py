class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        coins_set = set(coins)
        def dfs(i, total):
            if i <0:
                return False
            elif i in cache:
                return cache[i]
            elif i == 0:
                return 0
            elif i in coins_set:
                return 1
            
            min_coins = float('inf')
            for coin in coins:
                val = dfs(i-coin, total+1)
                if val:
                    min_coins = min(val, min_coins)
            cache[i] = 1+ min_coins
            return cache[i]
        res = dfs(amount, 0)
        if res == float('inf'):
            return -1
        return res
