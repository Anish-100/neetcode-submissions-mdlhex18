import math
import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x,y in points:
            val = math.sqrt(x**2 + y**2)
            hq.heappush(min_heap, (val,x,y))
        res = []
        for _ in range(k):
            val,x,y = hq.heappop(min_heap)
            res.append([x,y])
        return res



        