# TC: O(n*k)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        temp = deque()
        curr = 0
        for i in range(len(nums)):
            temp.append(nums[i])
            curr +=1
            if curr == k:
                res.append(max(temp))
                temp.popleft()
                curr-=1
        return res
