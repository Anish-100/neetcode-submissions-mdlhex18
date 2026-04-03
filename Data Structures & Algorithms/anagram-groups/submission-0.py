
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = {}
        for string in strs:
            key = tuple(sorted(string))
            if key in final_dict:
                final_dict[key].append(string)
            else:
                final_dict[key] = [string]
        final_list = []
        for value in final_dict.values():
            final_list.append(value)
        return final_list