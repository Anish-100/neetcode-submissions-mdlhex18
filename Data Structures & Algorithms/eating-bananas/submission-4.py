
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_sum(mid):
            numSum = 0
            for p in piles:
                numSum+= math.ceil(p/mid)
            return numSum
        l,r = 1, max(piles)
        res= float('inf')
        while l <=r:
            mid = l + (r-l)//2
            num_sum = calc_sum(mid)
            if num_sum > h:
                l = mid+1
            elif num_sum <= h:
                r = mid-1
                res= mid

        return res
        