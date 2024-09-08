class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        #Intuition 2 pointers 
        #Approach convert to lowercase + remove all non-alpha charcaters then use 2 pointers and shrink the window and compare each two elements until L=R

        L= 0
        R= len(s)-1 
        if len(s) ==1 :
            return True
        while L <= R:
            
            # check if character is alphanumeric 
            if not s[L].isalnum():
                L+=1
                continue

            if not s[R].isalnum():
                R-=1
                continue

            left = s[L].lower()
            right = s[R].lower()
            if left != right:
                return False 
            R-=1
            L+=1
        return True 
            

           
