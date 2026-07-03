class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(start):
            if sum(path) == target:
                result.append(path[:])

            for i in range(start, len(nums)):
                if sum(path)<= target :
                    path.append(nums[i])
                    backtrack(i)
                    path.pop()
        backtrack(0)
        return result