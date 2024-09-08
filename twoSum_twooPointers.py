class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        #Intuition : Two pointers 

        #Approach : we compare the sum of the two pointers values, if the sum is greater than target we decrease the right pointer, if sum is less than target we increase th value of the pointer 

        #Implementation :

        L= 0 
        R= len(numbers) -1 
        while L != R:
            if numbers[L] + numbers[R] < target :
                L+=1
            elif numbers[L] + numbers[R] > target :
                R-=1 
            else:
                return [L+1]+[R+1]
        
