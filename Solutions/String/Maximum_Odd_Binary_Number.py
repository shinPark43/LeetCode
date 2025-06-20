class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        # binary string s
        # at least one '1'
        # rearrange -> max odd binary number 
        # !! it can have leading zero !! 
        # in binary, right most bit has to be '1' to become odd number
        char_list = list(s)
        char_list.sort(reverse=True)
        return "".join(char_list)[1:] + '1'
