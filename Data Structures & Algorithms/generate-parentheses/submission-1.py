class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def backtrack(open_count, close_count):
            if open_count + close_count == 2*n:
                res.append(''.join(curr))
                return
            if open_count + close_count > 2*n:
                return 
            if open_count <n:
                curr.append('(')
                backtrack(open_count+1, close_count)
                curr.pop()
            if close_count <n and open_count > 0 and open_count > close_count:
                curr.append(')')
                backtrack(open_count,close_count+1)
                curr.pop()

        backtrack(0,0)
        return res

        
    