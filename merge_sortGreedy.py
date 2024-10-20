
#intuition : sort +  compare end time of sorte list and end time of the merged list 
# Approach as the intuition 
#Complexity O(nlog(n)) 
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Sort the intervals based on the start times
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If merged is empty or there is no overlap, append the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is overlap, so merge the current interval with the previous one
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
