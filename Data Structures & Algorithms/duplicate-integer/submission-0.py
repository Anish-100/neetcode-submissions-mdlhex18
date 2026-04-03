class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_dict = {}
        for num in nums:
            if num in number_dict:
                return True
            number_dict[num] = True
        return False
        