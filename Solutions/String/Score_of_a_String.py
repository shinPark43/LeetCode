class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        total = 0
        for i in range(1, n):
            total += abs(ord(s[i - 1]) - ord(s[i]))
        return total
