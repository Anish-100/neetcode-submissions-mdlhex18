class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        res = 0
        speedMap = {}
        for i in range(len(position)): 
            speedMap[position[i]] = speed[i]
        position.sort()
        for i in range(len(position)):
            stack.append ((target  - position[i])/speedMap[position[i]])
        while stack:
            num = stack.pop()
            while stack and num >= stack[-1]:
                num = max(num, stack.pop())
            res+=1
        return res
            