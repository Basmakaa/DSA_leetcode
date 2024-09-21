class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        curr = []
        res = []
        if not digits:
            return []
        hashset = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]
    }

        def helper(i):
            if len(curr) == len(digits) :
                res.append("".join(curr))
                return 

            letters = hashset[int(digits[i])]
            for letter in letters:
                curr.append(letter)
                helper(i+1)
                curr.pop()


        helper(0)
        return res
        
