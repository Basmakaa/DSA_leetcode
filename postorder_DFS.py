class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def backtrack(root, result):
            if not root:
                return 
            for child in root.children:
                backtrack(child,result)

            result.append(root.val)
        
        backtrack(root,result)
        return result 
        
