class Solution:
    def isValid(self, s: str) -> bool:
        close_stack = []
        ref = {'{':'}','(':')','[':']'}
        for char in s:
            print(close_stack)
            if char in ref:
                close_stack.append(ref[char])
            else:
                if len(close_stack) == 0:
                    return False
                if not (char == close_stack[-1]):
                    return False
                close_stack.pop()
        if len(close_stack)!=0:
            return False
        return True
                

        