class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0 
        r = len(heights)-1
        max_volume = 0
        while l < r:
            volume = (r-l)*min(heights[l],heights[r])
            if volume  > max_volume:
                max_volume = volume 
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_volume