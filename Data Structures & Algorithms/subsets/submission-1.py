class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(s,path):
            res.append(path[:])
            for i in range(s,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res


        