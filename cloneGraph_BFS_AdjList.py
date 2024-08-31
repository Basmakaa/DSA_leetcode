from collections import deque
"""
 Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        clone = {}
        queue = deque([node])
        clone[node] = Node(node.val)

        # we go over each element of the queue
        #BFS
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clone :
                    clone[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone[curr].neighbors.append(clone[neighbor])

        return clone[node]

