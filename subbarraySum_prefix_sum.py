class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = {0:1}
        curr_sum = 0
        count = 0 

        for n in nums :
            curr_sum += n 

            if (curr_sum - k) in prefix_sum :
                count += prefix_sum[curr_sum -k]

            if curr_sum in prefix_sum :
                prefix_sum[curr_sum] +=1 
            else:
                prefix_sum[curr_sum] = 1

        return count 
