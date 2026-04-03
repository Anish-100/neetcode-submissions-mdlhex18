class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for i in strs:
            final+=i
            final+=('-[]}')
        return final
    def decode(self, s: str) -> List[str]:
        return s.split('-[]}')[:-1]
