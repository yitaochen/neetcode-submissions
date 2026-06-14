class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[py] > self.rank[px]:
            px, py = py, px
        self.parent[py] = px
        self.rank[x] += self.rank[y]

        return True 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n+1)
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        # n = len(edges)
        # indegree = [0] * (n + 1)
        # adj = [[] for _ in range(n + 1)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        #     indegree[u] += 1
        #     indegree[v] += 1

        # q = deque()
        # for i in range(1, n + 1):
        #     if indegree[i] == 1:
        #         q.append(i)

        # while q:
        #     node = q.popleft()
        #     indegree[node] -= 1
        #     for nei in adj[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 1:
        #             q.append(nei)

        # for u, v in reversed(edges):
        #     if indegree[u] == 2 and indegree[v] == 2:
        #         return [u, v]
        # return []