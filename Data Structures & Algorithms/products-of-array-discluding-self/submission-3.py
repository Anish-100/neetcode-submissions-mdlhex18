class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        dsc = []
        asc = []
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                dsc.append(1)
            else:
                dsc.append(nums[i+1]*dsc[-1])
        sum = 1
        for i in range(len(nums)):
            print(sum,dsc[-(i+1)] )
            asc.append(sum*dsc[-(i+1)])
            sum*=nums[i]
        return asc
        