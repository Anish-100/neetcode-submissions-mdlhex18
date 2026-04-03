class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums)-1
        while min <= max:
            mid = (min + max)//2
            result = nums[mid]
            if target < result:
                max = mid-1
            elif target > result:
                min = mid+1
            elif target == result:
                return mid
        return -1