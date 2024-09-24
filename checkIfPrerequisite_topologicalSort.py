class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Adjacency list
        adj = {i: [] for i in range(numCourses)}

        # Build the graph (adjacency list)
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        # Store results of whether a course is reachable from another
        reach = [[False] * numCourses for _ in range(numCourses)]
        
        # DFS to check if course `end` is reachable from course `start`
        def dfs(start, end, visited):
            if start == end:
                return True
            visited.add(start)
            for neighbor in adj[start]:
                if neighbor not in visited:
                    if dfs(neighbor, end, visited):
                        return True
            return False

        # For each query, run DFS to check if `uj` is a prerequisite of `vj`
        result = []
        for uj, vj in queries:
            if reach[uj][vj] or dfs(uj, vj, set()):
                reach[uj][vj] = True
                result.append(True)
            else:
                result.append(False)
        
        return result
