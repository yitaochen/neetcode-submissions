class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {}
        adj = {}
        for a, b in prerequisites:
            if b not in adj:
                adj[b] = []
            adj[b].append(a)
            indegree[a] = indegree.get(a, 0) + 1

        dq = deque([])
        for i in range(numCourses):
            if i not in indegree:
                dq.append(i)
        
        while dq:
            cur = dq.popleft()
            numCourses -= 1
            if numCourses == 0:
                return True 
            if cur in adj:
                for nei in adj[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        dq.append(nei)
        
        return numCourses == 0