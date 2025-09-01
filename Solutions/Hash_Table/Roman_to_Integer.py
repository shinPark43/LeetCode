class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numeral = {'I':1, 
                         'V':5, 
                         'X':10,
                         'L':50,
                         'C':100,
                         'D':500,
                         'M':1000}
        total = 0
        for i in range(len(s)):
            if i != len(s) - 1 and roman_numeral[s[i]] < roman_numeral[s[i+1]]:
                total -= roman_numeral[s[i]]
            else:
                total += roman_numeral[s[i]]
        return total
