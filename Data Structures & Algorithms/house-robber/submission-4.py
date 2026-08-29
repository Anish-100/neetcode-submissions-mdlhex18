class Solution:
    def rob(self, nums: List[int]) -> int:
        len_n = len(nums)
        cache = [-1]*len_n
        def dfs(i):
            if i >= len_n:
                return 0
            elif cache[i] != -1:
                return cache[i]
            cache[i] = max(dfs(i+2) + nums[i], dfs(i+1))
            return cache[i]
        return dfs(0)
        