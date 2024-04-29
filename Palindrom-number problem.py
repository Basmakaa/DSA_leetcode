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


#Solution without converting to string 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        result = False 
        if x<0 :
            return False
        if x<10 and x>-1 :
            return True
        mylist = []
        while x :
            #derive the number so we get each single difit without converting to string 
            x, digit = divmod(x, 10)
            mylist.append(digit)
        print(mylist)
        i = 0
        size = len(mylist)
        while i<size :
            if mylist[i] != mylist[size -1 - i] :
                return False
            i+=1 
            result = True
        return result 
        
        
