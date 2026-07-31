class MinStack:

    def __init__(self):
        self.stack =  []
        self.overall_min = float('inf')

    def push(self, val: int) -> None:
        self.overall_min = min(self.overall_min,val)
        self.stack.append((val, self.overall_min))
        
    def pop(self) -> None:
        val, minimum = self.stack.pop()
        if self.overall_min == minimum:
            if self.stack:
                self.overall_min = self.stack[-1][1]
            else:
                self.overall_min = float('inf')
        return val
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]

        
