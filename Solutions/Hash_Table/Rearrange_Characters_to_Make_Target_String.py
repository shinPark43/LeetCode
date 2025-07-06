class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        #1 Check and count available target letter in string s.
        #2 Count the number of character needed for creating a one new string.

        letter_table ={}
        target_table={}
        for ch in s:
            if ch not in letter_table:
                letter_table[ch] = 1
            else:
                letter_table[ch] += 1
        max_num = 100
        for ch in target:
            if ch not in target_table:
                target_table[ch] = 1
            else:
                target_table[ch] += 1
        for ch in target:
            # If letter in target does not exist in letter table, return 0
            if ch not in letter_table:
                return 0
            result = letter_table[ch] // target_table[ch]
            if result < max_num:
                max_num = result
        return max_num
