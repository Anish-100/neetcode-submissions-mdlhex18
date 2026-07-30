# Plan:
# Start with left and right pointer
# Take the min of l,r
# Multiply that with distance
# Keep advancing r as long as container volume is increasing
# If lower than max_volume, keep advancing l

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        max_water = 0
        while l <r:
            curr = (r-l)*min(heights[r], heights[l])
            max_water = max(curr, max_water)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_water
        
        