"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = {}
        def clone(old, node):
            visited[node.val] = node
            if old is None:
                return None
            for n in old.neighbors:
                if n.val in visited:
                    node.neighbors.append(visited[n.val])
                else:
                    new_n = Node(n.val)
                    visited[new_n.val] = new_n
                    node.neighbors.append(visited[n.val])
                    clone(n, new_n)
            return node
        return clone(node, Node(node.val))