
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxLen = 1
        freq_map = {s[0]:1}
        l = 0
        sub_len = 1
        most_freq = 1
        for r in range(1, len(s)):
            sub_len+=1
            if s[r] not in freq_map:
                freq_map[s[r]] = 1
            else:
                freq_map[s[r]] +=1
                most_freq = max(most_freq, freq_map[s[r]])
            while sub_len - most_freq > k :
                freq_map[s[l]]-=1
                l+=1
                sub_len-=1
            maxLen = max(sub_len, maxLen)
            
        return maxLen





        