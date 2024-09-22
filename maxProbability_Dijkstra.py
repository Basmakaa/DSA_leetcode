class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """

        #Inuition Dijkstra 

        adj = {}
        
        for i in range(0, n) :
            adj[i] = []
    
        for i in range(len(edges)):
            s, d = edges[i]
            adj[s].append([d, succProb[i]])
            adj[d].append([s, succProb[i]])


        shortest = {}
        minheap = [[-1.00000, start_node]]

        while minheap :
            w1, n1 = heapq.heappop(minheap)
            w1 = - w1

            if n1 in shortest :
                continue 
            shortest[n1] = w1

            

            if n1 == end_node :
                return w1
                
            
            for n2, w2 in adj[n1] :
                if n2 not in shortest :
                    heapq.heappush(minheap, [-w1*w2, n2])

        return 0.00000


