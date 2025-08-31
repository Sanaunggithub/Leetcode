def countGoodSubstrings(s):
        """
        :type s: str
        :rtype: int
        """
        window = []
        left = 0
        count = 0

        for right in range(len(s)):
            if right - left + 1 >= 3:
                window.remove(s[left])
                left += 1
                     
            if s[right] in window:
                  
            window.append(s[right])

        print(window)
        return count


s = "aababcabc"

print(countGoodSubstrings(s))