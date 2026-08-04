class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_set = set()
        s1_chars = [0]*26
        for char in s1:
            s1_chars[ord(char)-97]+=1
            char_set.add(char)
        s2_chars = [0]*26
        l = 0
        for r in range(len(s2)) :
            char = s2[r]
            if char not in char_set:
                l = r+1
                s2_chars = [0]*26
                continue
            val = ord(char)-97
            s2_chars[val]+=1
            while l < r and s2_chars[val] > s1_chars[val]:
                s2_chars[ord(s2[l])-97]-=1
                l+=1
            if set(s2[l:r+1]) == char_set:
                len_c =0
                for char in char_set:
                    val = ord(char)-97
                    if s2_chars[val] == s1_chars[val]:
                        len_c +=1
                if len_c == len(char_set):
                    return True
        return False
                
            
