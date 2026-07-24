class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        lenN= len(nums)
        def backtrack(length,visited):
            if length == lenN:
                res.append(path.copy())
            if length > lenN:
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                path.append(nums[i])
                visited.add(i)
                backtrack(length+1, visited)
                path.pop()
                visited.remove(i)
        backtrack(0, set())
        return res
        