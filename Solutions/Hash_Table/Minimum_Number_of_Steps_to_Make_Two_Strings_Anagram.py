class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_char_count_dict = {}

        for char in s:
            if char not in s_char_count_dict:
                s_char_count_dict[char] = 1
            else:
                s_char_count_dict[char] += 1

        total = 0
        for char in t:
            if char in s_char_count_dict and s_char_count_dict[char] > 0:
                s_char_count_dict[char] -= 1
            else:
                total += 1
        return total
