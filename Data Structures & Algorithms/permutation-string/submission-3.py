class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_set = set()
        s1_chars = [0]*26
        for char in s1:
            s1_chars[ord(char)-97]+=1
            char_set.add(char)
        s2_chars = [0]*26
        l = 0
        curr = []
        for r in range(len(s2)) :
            char = s2[r]
            if char not in char_set:
                while l <=r:
                    s2_chars[ord(s2[l])-97] = 0
                    l+=1
                continue
            val = ord(char)-97
            s2_chars[val]+=1
            while l < r and s2_chars[val] > s1_chars[val]:
                s2_chars[ord(s2[l])-97]-=1
                l+=1
            if s2_chars == s1_chars:
                return True
        return False
                
            
