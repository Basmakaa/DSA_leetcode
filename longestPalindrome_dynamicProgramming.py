class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #intuition : 2 pointers but complexity is n^3
        #better Approach : dynamic programming, use two pointers technoque to expand until we're out of bound and the 2 pointers value is equal. update the max length each time, handle odd and even cases seperately 

        length =0
        result = ""
        for i in range(len(s)):
            #odd case
            l,r = i,i
            res = s[l]
            while l>=0 and r < len(s) and s[l]== s[r]:
                if r -l +1 > length:
                    result = s[l:r+1]
                    length = r-l +1
                l -= 1
                r += 1
            #even case
            l,r = i,i+1
            while l>=0 and r < len(s) and s[l]== s[r]:
                if r-l +1 > length:
                    result = s[l:r+1]
                    length = r-l +1
                l -= 1
                r += 1

        return result
            
        
