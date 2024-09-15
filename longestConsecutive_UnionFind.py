class UnionFind(object):
    def __init__(self):
        self.par = {}
        self.rank = {} 

    def add(self, x):
        if x not in self.par:
            self.par[x] = x  # Each node starts as its own parent
            self.rank[x] = 1  # Each node starts with rank 1

    def search(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    def union(self,n1,n2) :
        p1, p2 = self.search(n1), self.search(n2)
        if p1 == p2:
            return False
        else:
            # Union by rank (attach smaller tree under larger tree)
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
                self.rank[p1] += self.rank[p2]  # Update size of the root
            else:
                self.par[p1] = p2
                self.rank[p2] += self.rank[p1]  # Update size of the root

            return True


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0

        uf = UnionFind()
        for num in nums:
            uf.add(num)
        for num in nums :
            if (num+1) in uf.par:
                uf.union(num, num+1)
        longest = 0
        for num in nums:
            p = uf.search(num)
            longest = max(longest, uf.rank[p])

        return longest
