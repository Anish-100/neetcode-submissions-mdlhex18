class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_nums = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff_nums.get(diff) is not None:
                return[diff_nums[diff],i]
            diff_nums[nums[i]] = i
        