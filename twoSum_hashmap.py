class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mymap = {}
        for i in range(0, len(nums)):
            if (target -nums[i]) not in mymap :
                mymap[nums[i]] = i
            else:
                return [ i , mymap[target-nums[i]]]

