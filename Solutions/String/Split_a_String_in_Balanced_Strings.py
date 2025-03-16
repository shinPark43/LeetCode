class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        R_count = 0
        L_count = 0

        for i in range(len(s)):
            if s[i] == 'R':
                R_count += 1
            elif s[i] == 'L':
                L_count += 1
            if R_count == L_count:
                count += 1
                R_count = 0
                L_count = 0
        return count