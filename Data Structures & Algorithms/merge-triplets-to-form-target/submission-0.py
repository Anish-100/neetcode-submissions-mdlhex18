class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        curr = [0,0,0]
        for trip in triplets:
            if trip[0] > target[0] or trip[2] > target[2] or trip[1] > target[1]:
                continue
            if max(trip[0], curr[0]) == target[0] or max(trip[1], curr[1]) == target[1] or max(trip[2], curr[2]) == target[2]:
                for i,val in enumerate(curr):
                    curr[i] = max(trip[i], val)
        if curr == target:
            return True
        return False
