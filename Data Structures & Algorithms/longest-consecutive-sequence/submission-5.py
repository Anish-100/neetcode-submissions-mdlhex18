class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsSet = set()
        for val in nums:
            numsSet.add(val)
        max_value = 0
        for val in nums:
            if val not in numsSet:
                continue
            curr = 1
            while val+1 in numsSet:
                val+=1
                curr+=1
            max_value = max(curr, max_value)
        return max_value

        