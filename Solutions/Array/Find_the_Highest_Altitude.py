class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_al = 0
        curr_al = 0

        for i in gain:
            curr_al += i
            if curr_al > max_al:
                max_al = curr_al
        return max_al
