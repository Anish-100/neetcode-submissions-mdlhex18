# approach
# Keep a left and a right stack and * stack
# for every left push it in 
# For every * push that in
# When right is hit, starting popping from left.
# If there is a left or right left, keep matching with *
# IF there are any in l or r left, return False
# Else return True

class Solution:
    def checkValidString(self, s: str) -> bool:
        lStk = []
        starStk = []
        for i, c in enumerate(s):
            if c == '*':
                starStk.append((c,i))
            elif c == '(':
                lStk.append((c,i))
            elif c == ')' and lStk:
                lStk.pop()
            elif c == ')' and starStk:
                starStk.pop()
            else:
                return False
        while lStk:
            if starStk and starStk[-1][1] > lStk[-1][1]:
                starStk.pop()
            else:
                return False
            lStk.pop()
        return True

        