class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}

        for string in strs:
            value = ''.join(sorted(string))
            if value in freq_map:
                freq_map[value].append(string)
            else:
                freq_map[value] = [string]
        res = []
        for val in freq_map.values():
            res.append(val)
        return res





        