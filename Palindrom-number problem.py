class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        result = False 
        if x<0 :
            return False
        mystr = str(x) # convert to string 
        size = len(mystr)
        i = 0
        while i < size :
            if mystr[i] != mystr[size -1 - i] :
                return False
            i+=1 
            result = True


        return result 
        
