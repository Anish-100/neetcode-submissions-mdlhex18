class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        in_degree = {i:0 for i in range(numCourses)}
        for cr, prereq in prerequisites:
            adj[prereq].append(cr)
            in_degree[cr]+=1
        q = deque([])
        for key, val in in_degree.items():
            if not val:
                q.append(key)
        res = []
        while q:
            n = q.popleft()
            res.append(n)
            for v in adj[n]:
                in_degree[v]-=1
                if in_degree[v] == 0:
                    q.append(v)
            in_degree.pop(n)
            adj.pop(n)
        if len(res) == numCourses:
            return res
        return []

        

        