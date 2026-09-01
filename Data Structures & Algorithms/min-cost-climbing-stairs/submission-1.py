class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        prev_1, prev_2 = 0,0

        for i in range(2,len(cost)+1):
            tmp = prev_1
            prev_1 = min(prev_1 + cost[i-1], prev_2 + cost[i-2])
            prev_2 = tmp
        return prev_1
        