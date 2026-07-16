class Solution:
   
# Incorrect solution, but I cannot figure this out. I know I am close   
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_map = {}
        res =[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in num_map:
                    num_map[nums[i]] = set()
            for j in range(i+1,len(nums)):
                if nums[j] not in num_map:
                    num_map[nums[j]] = set()
                nSum = -(nums[i] + nums[j])
                if nSum in num_map and i not in num_map[nSum] and j not in num_map[nSum]:
                    res.append([nums[i],nums[j], nSum])
                num_map[nums[j]].add(j)
            num_map[nums[i]].add(i) 
        return res



        