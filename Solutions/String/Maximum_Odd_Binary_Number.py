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

        list_chr = list(s)
        list_chr.sort(reverse=True)
        string_front = str("".join(list_chr))[1:]
        return string_front + '1'
