class SegmentTree(object):
    def __init__(self,total,L,R):
        self.sum = total 
        self.left = None
        self.right = None
        self.L = L 
        self.R = R
    @staticmethod
    def build(nums,L,R):
        if L == R:
            return SegmentTree(nums[L],L,R)
        M= (L+R) //2
        root = SegmentTree(0, L, R)
        root.left = root.build(nums, L, M)
        root.right =root.build(nums, M+1, R)
        root.sum = root.left.sum + root.right.sum 
        return root
    def update(self, index, val):
        if self.L == self.R :
            self.sum = val 
            return 
        M= (self.L + self.R) //2 
        if index > M :
            self.right.update(index,val)
        else:
            self.left.update(index,val)
        self.sum = self.left.sum + self.right.sum
    def sumRange(self,L,R):
        if self.L == L and self.R == R:
            return self.sum 
        M = (self.L + self.R) //2
        if L > M :
            return self.right.sumRange(L, R)
        if R<= M :
            return self.left.sumRange(L, R)
        else:
            return self.left.sumRange(L, M) + self.right.sumRange(M+1, R)




class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sg = SegmentTree(nums,0, len(nums)-1)
        self.sg = SegmentTree.build(nums, 0, len(nums)-1)
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """

        self.sg.update(index,val)
        return

        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.sg.sumRange(left,right)
        

