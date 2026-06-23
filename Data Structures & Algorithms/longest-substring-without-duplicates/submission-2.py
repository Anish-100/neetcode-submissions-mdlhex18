class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        char_set = set()
        max_value = 1
        l = 0
        char_set.add(s[l])
        for r in range(1,len(s)):
            if s[r] in char_set:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l+=1
            char_set.add(s[r])
            max_value = max(max_value, len(char_set))
        return max_value
                


        