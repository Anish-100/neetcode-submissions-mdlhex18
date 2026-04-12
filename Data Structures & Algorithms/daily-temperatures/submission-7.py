class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            #Removed the if condition and incorporated the rest of the code within this loop
            while stack and  temperatures[stack[-1]] < temperatures[i]:
                popped = stack.pop()
                result[popped] = i - popped
                if len(stack)==0:
                    break
            stack.append(i)    
        # Removing iterating to 0 as it is defaulted to that.       
        return result



            