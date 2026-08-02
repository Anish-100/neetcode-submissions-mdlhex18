# TC: O(n*log(n))
import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x,y = points[i]
            heap.append((math.sqrt(x**2+y**2),x,y))
        hq.heapify(heap)
        res = []
        for i in range(k):
            _, x,y = hq.heappop(heap)
            res.append([x,y])
        return res

        