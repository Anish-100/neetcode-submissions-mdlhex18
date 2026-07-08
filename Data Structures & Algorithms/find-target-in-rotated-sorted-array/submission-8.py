class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        l,r = 0, len(nums)-1
        while l <= r:
            print(l,r)
            mid = l + ((r-l)//2)
            if nums[mid] == target:
                index = mid
                break
            if nums[mid] < nums[l]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1
            elif nums[mid] >= nums[l]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid-1
                else:
                    l = mid +1

        return index