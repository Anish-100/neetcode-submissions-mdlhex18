class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum_stack)== 0 or val <= self.minimum_stack[-1]:
            self.minimum_stack.append(val)
        
    def pop(self) -> None:
        if self.minimum_stack[-1] == self.stack[-1]:
            self.minimum_stack.pop(-1) 
        self.stack.pop(-1)
                   
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum_stack[-1]

        
