class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        total = 0
        for i in range(10):
            rode_idx = str(i)
            if 'R' + rode_idx in rings and 'G' + rode_idx in rings and 'B' + rode_idx in rings:
                total += 1
        return total 
