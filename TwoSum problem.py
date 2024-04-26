class Solution(object):
    # It returns index of elem in given array arr
    # l: left r: right
    def binarySearch(self, arr, l, r, elem):
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == elem:
                return mid
            if elem > arr[mid]:
                l = mid + 1
            if elem < arr[mid]:
                r = mid - 1
        return None

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        size = len(nums)
        # check if list has a minimum of 2 elements
        if size < 2:
            return []

        sorted_nums = sorted(nums) #sort list and create new one for Binary search 
        i = 0
        while i < size:
            elem1 = sorted_nums[i] # value of first element
            binarysearch = self.binarySearch(sorted_nums, i + 1, size - 1, target - elem1) # look for second element if it exists using the binary search method so elem2= target - elem1
            if binarysearch is not None: # second element exists
                elem2 = sorted_nums[binarysearch] # binarySearch returns the index of the element 
                result.append(nums.index(elem1))
                result.append(nums.index(elem2) if elem1 != elem2 else nums.index(elem2, nums.index(elem1) + 1)) # add index of the element on the unsorted original list
                # if elem1 == elem2, we should look for index od the second occurrance of elem1 

                return result
            else: # solution doesn't exist move to next element on the list
                i += 1

        return []
            



