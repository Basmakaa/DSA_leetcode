class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(i, nums):
            if i == len(nums):
                return [[]]  # Base case

            resPerms = []
            perms = helper(i + 1, nums)
            unique_perms = set()

            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = list(p)
                    pCopy.insert(j, nums[i])
                    key = tuple(pCopy)
                    if key not in unique_perms:
                        resPerms.append(pCopy)
                        unique_perms.add(key)
            return resPerms

        nums.sort()
        return helper(0, nums)
