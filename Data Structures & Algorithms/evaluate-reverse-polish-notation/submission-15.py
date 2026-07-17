

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        key_map = {'+':add, '-':sub, '*': mul, '/': div}
        i = 0
        while i < len(tokens):
            while tokens[i] not in key_map:
                stack.append(tokens[i])
                i+=1
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append((key_map[tokens[i]](num2, num1)))
            i+=1
        return stack[0]
def add(x,y):
    return (x+y)
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return int(x/y)

    