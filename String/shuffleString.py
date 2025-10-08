def restoreString(s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
        s = [v for v in s]
        c = {}

        for i in range(len(s)):
            c[indices[i]] = s[i]

        sorted_c = dict(sorted(c.items()))

        res = ""

        for v in sorted_c.values():
            res += v

        return res

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))