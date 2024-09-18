class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        # Build the prefix sum matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (matrix[i - 1][j - 1] 
                                     + self.prefix[i - 1][j] 
                                     + self.prefix[i][j - 1] 
                                     - self.prefix[i - 1][j - 1])
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (self.prefix[row2 + 1][col2 + 1]
                - self.prefix[row1][col2 + 1]
                - self.prefix[row2 + 1][col1]
                + self.prefix[row1][col1])
