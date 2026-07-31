class MinStack:

    def __init__(self):
        self.stack =  []
        self.curr_len = -1
        self.overall_min = float('inf')
        self.min_map = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curr_len+=1
        self.overall_min = min(self.overall_min,val)
        self.min_map[self.curr_len] = self.overall_min
        
    def pop(self) -> None:
        self.min_map.pop(self.curr_len)
        self.curr_len-=1
        if self.curr_len >=0:
            self.overall_min = self.min_map[self.curr_len]
        else:
            self.overall_min = float('inf')
        return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
        
    def getMin(self) -> int:
        return self.min_map[self.curr_len]

        
