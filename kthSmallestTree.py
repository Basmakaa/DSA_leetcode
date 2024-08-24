class Solution(object):
    def __init__(self):
        self.count = 0 
        self.result = None 
    
    def inorder(self, root, k) :
        if not root:
            return 

        self.inorder(root.left,k)

        self.count +=1 
        if self.count == k :
            self.result = root.val
            return 
        self.inorder(root.right, k)
        
    

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder(root,k)
        return self.result 
