class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(start):
            if start <=2:
                cache[start] = start
                return start
            if start in cache:
                return cache[start]
            val =  dfs(start-1) + dfs(start-2)
            cache[start] =val
            return val
        return dfs(n)