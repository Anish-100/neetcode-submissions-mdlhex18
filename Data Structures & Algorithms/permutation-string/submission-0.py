# Time Complexity: O(n*m), n being len(s1), m = len(s2)
# Space Complexity: O(m)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        exp_freq = {}
        for i in s1:
            exp_freq[i] = 1 + exp_freq.get(i, 0)
        print(exp_freq)
        fixed_length = len(s1)
        l = 0
        obs_freq = {}
        if len(s2) < fixed_length:
            return False
        cur_len = 0
        for r in range(len(s2)):
            counter = 0
            if cur_len >= fixed_length:
                obs_freq[s2[l]] -=1
                l+=1
            obs_freq[s2[r]] = 1 + obs_freq.get(s2[r], 0)
            for key, val in obs_freq.items():
                if exp_freq.get(key, -1) == val:
                    counter+=1
            if counter == len(exp_freq):
                return True
        
            cur_len+=1
        return False
        
        
        