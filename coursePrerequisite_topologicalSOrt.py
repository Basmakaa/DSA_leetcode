class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # DFS + Topological sort 

        adj = {}
        visit = set()
        path = set()
        res= True
        for i in range(0, numCourses ):
            adj[i] = []
        for src, dst in prerequisites :
            adj[src].append(dst)

        def dfs(src, adj, visit ) :
            if src in visit :
                return True
            if src in path:
                return False
            path.add(src)
            
            for neighbor in adj[src]:
                if not dfs(neighbor, adj,visit):
                    return False
            visit.add(src)
            path.remove(src)
            return True
            
        for i in range(0, numCourses):
            if not dfs(i,adj, visit):
                return False
        
        return True 

