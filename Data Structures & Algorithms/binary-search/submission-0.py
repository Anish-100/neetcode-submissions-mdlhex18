class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums)-1
        while min <= max:
            mid = (min + max)//2
            print(mid)
            if target < nums[mid]:
                max = mid-1
            elif target > nums[mid]:
                min = mid+1
            elif target == nums[mid]:
                return mid
        return -1