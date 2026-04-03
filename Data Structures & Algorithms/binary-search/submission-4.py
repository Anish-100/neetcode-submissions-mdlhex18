class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min,max = 0,len(nums)-1
        while min <= max:
            mid = (min + max)//2
            result = nums[mid]
            if target == result:
                return mid
            elif target < result:
                max = mid-1
            elif target > result:
                min = mid+1
        return -1