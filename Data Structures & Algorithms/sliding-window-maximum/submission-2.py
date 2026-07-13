# TC: O(n*k)
# SC: O(n)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <=k:
            return [max(nums)]
        res = []
        min_nums = deque()
        l = 0
        for r in range(0, len(nums)):
            min_nums.append(nums[r])
            if r-l +1  < k:
                continue
            if r-l + 1 > k:
                l+=1
                min_nums.popleft()
            res.append(max(min_nums))
        return res



        