class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        jumpsMade = 0
        max_idx = 0
        max_val = 0
        while r < len(nums)-1:
            for i in range(l,r+1):
                if i + nums[i] > max_val:
                    max_val = i + nums[i]
                    max_idx = i
            l = max_idx
            r = max_idx+ nums[max_idx]
            jumpsMade+=1
        return jumpsMade


        
        