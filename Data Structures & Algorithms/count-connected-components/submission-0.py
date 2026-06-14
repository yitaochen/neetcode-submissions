class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [0] * n 
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            if visited[node]:
                return 
            visited[node] = 1
            if node in adj:
                for nei in adj[node]:
                    dfs(nei)
            
        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)
        
        return ans 