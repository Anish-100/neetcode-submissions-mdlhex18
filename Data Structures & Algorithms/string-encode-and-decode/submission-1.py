class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for a in strs:
            res+=a
            res+="å"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        tmp = ''
        for n in s:
            if n == 'å':
                res.append(tmp)
                tmp = ''
            else:
                tmp+=n
        return res