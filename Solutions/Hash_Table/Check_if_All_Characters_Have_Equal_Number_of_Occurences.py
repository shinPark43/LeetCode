class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_table = {}
        for ch in s:
            if ch not in char_table:
                char_table[ch] = 1
            else:
                char_table[ch] += 1
        limit = char_table[s[0]]
        for count in char_table.values():
            if count != limit:
                return False
        return True
