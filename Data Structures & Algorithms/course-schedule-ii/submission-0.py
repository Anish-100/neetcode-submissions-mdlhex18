class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        in_degree = {i:[] for i in range(numCourses)}
        for cr, prereq in prerequisites:
            adj[prereq].append(cr)
            in_degree[cr].append(prereq)
        q = deque([])
        for key, val in in_degree.items():
            if val == []:
                q.append(key)
        res = []
        print(q)
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                res.append(n)
                for v in adj[n]:
                    if v in in_degree:
                        in_degree[v].remove(n)
                        if in_degree[v] == []:
                            q.append(v)
                in_degree.pop(n)
                adj.pop(n)

        if len(res) == numCourses:
            return res
        return []

        

        