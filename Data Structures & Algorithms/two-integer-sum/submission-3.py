class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverse_nums = {}
        for i in range(len(nums)):
            reverse_nums[target-nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in reverse_nums:
                j = reverse_nums[nums[i]]
                if i !=j:
                    return [i,j]
        