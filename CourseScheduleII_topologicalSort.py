class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        #intuition : DFS and topological sort 
        adj = {}

        for i in range(0, numCourses) :
            adj[i] = []

        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visit = set()
        res = []
        path = set()

        def dfs(src):
            if src in visit :
                return True 
            if src in path:
                return False 
            path.add(src)
            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False
            path.remove(src)
            visit.add(src)
            res.append(src)
            return True 

            
        for i in range(0, numCourses) :
            if not dfs(i):
                return []
           
        return res 
        

        
