class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        min_val = 10000
        while l <= r:
            mid = (l+r)//2
            min_val = min(nums[mid], min_val)
            if nums[mid] < nums[l]:
                r = mid -1
            else:
                if nums[r] < nums[l]:
                    l = mid +1
                else:
                    r = mid -1
        return min_val
        