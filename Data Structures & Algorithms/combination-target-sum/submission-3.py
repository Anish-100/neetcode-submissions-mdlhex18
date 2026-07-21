class Solution:
   # A bit more time efficient
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(s,path, total):
            if total == target:
                res.append(path[:])
                return 
            if total > target:
                return
            for i in range(s,len(nums)):
                m = 0
                while total < target:
                    path.append(nums[i])
                    total+=nums[i]
                    backtrack(i+1,path, total)
                    m+=1
                for n in range(m):
                    total-= path.pop()
        backtrack(0,[],0)
        return res
        