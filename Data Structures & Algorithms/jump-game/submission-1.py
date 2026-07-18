class Solution:
    def canJump(self, nums: List[int]) -> bool:
        remainingJumps = 0
        jumps = 0
        for i in range(len(nums)-1):
            print(remainingJumps, nums[i])
            if remainingJumps ==0 and nums[i] == 0:
                return False
            elif nums[i] > remainingJumps:
                remainingJumps = nums[i]
            remainingJumps-=1
        return True

        