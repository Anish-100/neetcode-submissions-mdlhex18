class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total = 0
        max_i = 0
        i = 0
        while i < len(gas):
            if gas[i] - cost[i] > 0:
                max_i = i
                while i < len(gas) and gas[i] - cost[i] >= 0 :
                    total+= gas[i] - cost[i]
                    i+=1
            else:
                total+= gas[i] - cost[i]
                i+=1
        print(total)
        if total < 0:
            return -1
        return max_i

        