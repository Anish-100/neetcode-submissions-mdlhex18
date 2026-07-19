# Approach
# Start at left end and for each new character added in substring, add it to the set
# Then go greedy until frequency_map of that runs out.
# If it runs out before, freq_map[i] == 0, return max_string_length
# Then keep popping out of the set of characters in the set and ensure their freq_map is 0 too
# If set is None and append string length to res


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        freq_map = {}
        for char in s:
            freq_map[char] = 1+ freq_map.get(char, 0)
        curr = set()
        cLen = 0
        for i, ch in enumerate(s):
            cLen+=1
            freq_map[ch]-=1
            curr.add(ch)
            if freq_map[ch] == 0:
                curr.remove(ch)
            if len(curr) == 0:
                res.append(cLen)
                cLen = 0
        return res