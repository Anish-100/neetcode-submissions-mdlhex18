class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [0]*length
        right = [0]*length
        final = [0]*length
        for i in range(length):
            if i == 0:
                left[i] = 1
            elif i == 1:
                left[i] = nums[i-1]
            else:
                left[i] = nums[i-1]*left[i-1]
        
        for i in range(length-1,-1,-1):
            if i == length-1:
                right[i] = 1
            elif i == length-2:
              right[i] = nums[i+1]
            else:
                right[i] = nums[i+1]*right[i+1]
        for i in range(len(nums)):
            final[i] = left[i]*right[i]
        return final

        