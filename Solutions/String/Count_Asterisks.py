class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        string_list = s.split("|")
        total = 0

        for i in range(0, len(string_list), 2):
            total += string_list[i].count('*')
        return total