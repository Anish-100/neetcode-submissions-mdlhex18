class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        path = []
        def backtrack(start, total):
            if total > target:
                return
            if total == target:
                res.append(path.copy())
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, total+candidates[i])
                path.pop()
        backtrack(0,0)
        return res