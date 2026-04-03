class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s    = sorted(s)
        t = sorted(t)
        i=0
        j=0
        if len(s) != len(t):
            return False
            
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                return False
            i+=1
            j+=1
        if i != j:
            return False
        return True

        