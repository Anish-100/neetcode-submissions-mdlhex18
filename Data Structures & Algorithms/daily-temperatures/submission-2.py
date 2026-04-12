class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append(i)
                continue
            elif temperatures[i]> temperatures[stack[-1]]:
                while temperatures[stack[-1]] < temperatures[i]:
                    result[stack.pop()] = i - stack[-1]
                    if len(stack)==0:
                        break
            stack.append(i)          
        for j in stack:
            result[j] = 0
        return result



            