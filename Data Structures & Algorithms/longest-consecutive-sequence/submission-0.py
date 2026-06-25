class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        min_set = set()
        for num in nums:
            num_set.add(num)
        
        for num in nums:
            if num-1 in num_set:
                continue
            else:
                min_set.add(num)
        max_num =0
        for min in min_set:
            temp = 1
            while (min+1 in num_set):
                temp+=1
                min+=1
            max_num = max(temp,max_num)

        return max_num


        