class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inorder = {i:0 for i in range(numCourses)}
        outorder = {i:[] for i in range(numCourses)}
        
        for cr, pre in prerequisites:
            inorder[cr]+=1
            outorder[pre].append(cr)
        q = deque()
        for cr in inorder.keys():
            if inorder[cr] == 0:
                q.append(cr)
        res = []
        while q:
            n = q.popleft()
            res.append(n)
            for v in outorder[n]:
                inorder[v]-=1
                if inorder[v] == 0:
                    q.append(v)
            outorder.pop(n)
            inorder.pop(n)
        if len(res) == numCourses:
            return res
        return []


        