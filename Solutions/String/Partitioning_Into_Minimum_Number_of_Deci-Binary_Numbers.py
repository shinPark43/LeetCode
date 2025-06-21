class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        # Without any leading zeros, positive decimal integer
        set_of_digits = set(n)
        return int(max(set_of_digits))
