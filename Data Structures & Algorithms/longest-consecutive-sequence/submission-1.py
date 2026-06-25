class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest =0
        for num in nums:
            if num-1 not in num_set:
                temp = 1
                while (num+temp in num_set):
                    temp+=1
                longest = max(temp,longest)

        return longest


        