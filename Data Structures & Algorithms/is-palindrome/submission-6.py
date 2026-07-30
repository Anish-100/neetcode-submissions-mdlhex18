

class Solution:

    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<r:
            while l < r and not s[l].isalnum():
                l+=1
            while r > l and not s[r].isalnum():
                r-=1
            if r < l or l >r:
                return False
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
    def alphaNum(self, c):
        return 'A'<=c<='Z' or  'a' <=c<='z' or '0'<=c<='9'
        