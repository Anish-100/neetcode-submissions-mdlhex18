class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key_map = {'(':')','[':']','{':'}'}

        stack = []

        for b in s:
            if b in key_map:
                stack.append(b)
            else:
                if not stack:
                    return False
                if key_map[stack[-1]] == b:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True



        