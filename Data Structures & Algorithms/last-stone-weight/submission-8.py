import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq.heapify_max(stones)
        while len(stones) > 1:
            y= hq.heappop_max(stones)
            x = hq.heappop_max(stones)
            if x < y:
                hq.heappush_max(stones, y-x)
        return stones[0] if stones else 0