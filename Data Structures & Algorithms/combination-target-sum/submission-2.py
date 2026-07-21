class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(s,path):
            if sum(path) == target:
                res.append(path[:])
                return 
            if sum(path) > target:
                return
            for i in range(s,len(nums)):
                m = 0
                while sum(path) < target:
                    path.append(nums[i])
                    backtrack(i+1,path)
                    m+=1
                for n in range(m):
                    path.pop()
        backtrack(0,[])
        return res
        