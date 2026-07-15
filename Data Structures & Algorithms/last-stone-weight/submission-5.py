# TC : O(nlog(n))
# SC: O(n)

import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        hq.heapify(stones)
        while len(stones) > 1:
            x = - hq.heappop(stones)
            y = - stones[0]
            if x == y:
                hq.heappop(stones)
            elif x < y:
                hq.heappushpop(stones, x-y)
                continue
            else:
                hq.heappop(stones)
                hq.heappush(stones, y-x)
        if not stones:
            return 0
        return -stones[0]