# Understand
# Given a string, find the substring where if you make k replacements,
# you can get a string of only a single character
# Plan
# We start a sliding window which expands until max_freq - k < 0:
# If that is the case, we shrink it and update max_freq until the 
# most common element - k >= 0 
# return max_freq = max(freq, max_freq)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0 :
            return 0
        if len(s) == 1:
            return 1
        l = 0
        max_len = 0
        most_freq = 0
        curr = ""
        freq_map = {s[l]:1}
        curr_max = s[l]
        for r in range(1, len(s)):
            curr_len = (r - l) + 1
            freq_map[s[r]] = 1+ freq_map.get(s[r],0)
            most_freq = max(most_freq, freq_map[s[r]])

            if curr_len - most_freq > k:
                freq_map[s[l]]-=1
                l+=1
                curr_len-=1
            
            max_len = max(max_len,curr_len)

            print(most_freq, l ,r)
            print(freq_map)
        return max_len

        