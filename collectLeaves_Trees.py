# Helper function to collect the leaf nodes
        def collectLeaves(node):
            if not node:
                return []
            # If it's a leaf node, return its value
            if not node.left and not node.right:
                return [node.val]
            
            # Otherwise, traverse both left and right subtrees
            return collectLeaves(node.left) + collectLeaves(node.right)
        
        # Collect the leaves for both trees
        leaves1 = collectLeaves(root1)
        leaves2 = collectLeaves(root2)
        
        # Compare the two lists of leaves
        return leaves1 == leaves2
