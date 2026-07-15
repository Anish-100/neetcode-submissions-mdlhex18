# TC : O(nlog(n))
# SC: O(n)

import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        hq.heapify(stones)
        while len(stones) > 1:
            x = - hq.heappop(stones)
            y = - hq.heappop(stones)
            if x == y:
                continue
            elif x < y:
                hq.heappush(stones, x-y)
            else:
                hq.heappush(stones, y-x)
        if not stones:
            return 0
        return -stones[0]