class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        exp_freq = {}
        for i in s1:
            exp_freq[i] = 1 + exp_freq.get(i, 1)
        fixed_length = len(s1)
        l = 0
        counter = 0
        obs_freq = {}
        if len(s2) < fixed_length:
            return False
        cur_len = 0
        for r in range(len(s2)):
            print(s2[l:r+1])
            if cur_len >= fixed_length:
                obs_freq[s2[l]] -=1
                l+=1
                obs_freq[s2[l]] = 1 + obs_freq.get(s2[l], 1)
                if obs_freq[s2[l]] == obs_freq.get(s2[l], 0):
                    counter+=1
            obs_freq[s2[r]] = 1 + obs_freq.get(s2[r], 1)
            if obs_freq[s2[r]] == obs_freq.get(s2[r], 0):
                    counter+=1
            print(counter)
            if sorted(s2[l:r+1]) == sorted(s1):
                return True
            cur_len+=1
        return False
        
        
        