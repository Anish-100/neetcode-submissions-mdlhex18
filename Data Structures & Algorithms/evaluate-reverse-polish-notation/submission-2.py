class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+','-','*','/'}
        stack = []
        for i in tokens:
            if i in operators:
                result = self.do_operation(i,stack[-2],stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(i)
        return int(stack[0])


    def do_operation(self,operation,lval,rval):
        lval,rval = int(lval),int(rval)
        if operation == '+':
            return lval+rval
        elif operation == '-':
            return lval - rval
        elif operation == '*':
            return lval * rval
        elif operation == '/':
            return int(lval/rval)