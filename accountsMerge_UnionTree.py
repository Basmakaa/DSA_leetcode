class UnionFind():
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]

        return x

    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)

        if x == y:
            return False 

        if self.rank[x] > self.rank[y]:
            self.parents[parenty] = parentx
            self.rank[parentx] += self.rank[parenty]
        else:
            self.parents[parentx] = parenty
            self.rank[parenty] += self.rank[parentx]
 
        return True

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
        # 1. create a unionFind data structure for all emails
        # 2. create email to account number hashmap
        # 3. if emailNumber exists in hashmap already, then union 2 users together 

        uf = UnionFind(len(accounts))
        emailToNum = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in emailToNum:
                    emailToNum[email] = i
                else:
                    # merge 2 accounts together 
                    uf.union(emailToNum[email], i)


        emailGroups = {}

        for e, i in emailToNum.items(): # find every possible unique email
            leader = uf.find(i)
            if leader not in emailGroups:
                emailGroups[leader] = []

            emailGroups[leader].append(e)

        res = []
        for i, group in emailGroups.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroups[i]))

        return res
