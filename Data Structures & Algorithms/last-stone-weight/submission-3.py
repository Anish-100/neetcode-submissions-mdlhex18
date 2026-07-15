# TC : O(n^2log(n))
# SC: O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        if len(stones) == 1:
            return stones[0]
        
        while len(stones) > 1:
            x = stones[-1]
            y = stones[-2]
            print(x,y)
            if x == y:
                stones.pop()
            elif x < y:
                stones[-2] = y-x
            else:
                stones[-2] = x-y
            stones.pop()
            stones.sort()
        if not stones:
            return 0
        return stones[0]