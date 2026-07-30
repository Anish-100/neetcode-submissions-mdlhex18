class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        max_freq = float('-inf')
        for val in nums:
            if val in freq_map:
                freq_map[val] +=1
            else:
                freq_map[val] = 1
            max_freq = max(freq_map[val],max_freq)
        buckets = [[]for x in range(max_freq+1)]
        for val, freq in freq_map.items():
            buckets[freq].append(val)
        res= []
        for i in range(len(buckets)-1,-1,-1):
            if len(res)==k:
                break
            if buckets[i]:
                res.extend(buckets[i])
        return res
        
            

        