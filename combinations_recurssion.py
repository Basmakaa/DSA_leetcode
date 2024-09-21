class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        #intuition: recurssion
        # include

        curr = []
        res= []

        def helper(i) :
            # len of curr subset is k
            if len(curr) == k :
                res.append(list(curr))
                return

            if i > n :
                return 

            #include element
            curr.append(i)
            helper(i+1)
            curr.pop()
            helper(i+1)

        helper(1)
        return res

        
       
